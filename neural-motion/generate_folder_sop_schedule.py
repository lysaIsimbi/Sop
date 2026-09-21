#!/usr/bin/env python3
"""Build an 8-per-day schedule from unique SOP task documents in this folder."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parent
END_DATE = date(2026, 9, 3)
BATCH_SIZE = 8

EXCLUDED_BASES = {
    "FOLDER",
    "Generic",
    "NEURAL_MOTION",
    "Neural_Motion_Weekly",
}

# Known filename variants that refer to an SOP already represented elsewhere.
ALIASES = {
    "Bubble_Wrap_and_Box_Fragile_Item": "Bubble_Wrap_and_Box_a_Fragile_Item",
    "Restock_First_Aid_Kit": "Restock_a_First_Aid_Kit",
}


def collect_sops() -> list[tuple[str, Path]]:
    grouped: dict[str, list[Path]] = defaultdict(list)
    pattern = re.compile(r"^(.*?)_SOP(?:$|[-_ (].*)", re.IGNORECASE)

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".pdf"}:
            continue
        match = pattern.match(path.stem)
        if not match:
            continue
        base = match.group(1)
        if base in EXCLUDED_BASES:
            continue
        base = ALIASES.get(base, base)
        grouped[base].append(path)

    selected: list[tuple[str, Path]] = []
    for base, paths in grouped.items():
        # Prefer Markdown, then a file inside its task directory, then the shortest path.
        source = min(
            paths,
            key=lambda p: (
                p.suffix.lower() != ".md",
                len(p.relative_to(ROOT).parts) == 1,
                len(str(p.relative_to(ROOT))),
            ),
        )
        selected.append((base, source.relative_to(ROOT)))

    return sorted(selected, key=lambda item: item[0].casefold())


def display_name(base: str) -> str:
    return base.replace("_", " ")


def main() -> None:
    sops = collect_sops()
    total_batches = (len(sops) + BATCH_SIZE - 1) // BATCH_SIZE
    start_date = END_DATE - timedelta(days=total_batches - 1)
    rows = []
    for index, (base, source) in enumerate(sops, start=1):
        batch = ((index - 1) // BATCH_SIZE) + 1
        scheduled = start_date + timedelta(days=batch - 1)
        rows.append(
            {
                "batch": batch,
                "date": scheduled.isoformat(),
                "month": scheduled.strftime("%B"),
                "day": scheduled.day,
                "item": index,
                "sop_name": display_name(base),
                "source_path": str(source),
                "status": "Planned",
            }
        )

    csv_path = ROOT / "NEURAL_MOTION_SOP_DAILY_SCHEDULE.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    md_path = ROOT / "NEURAL_MOTION_SOP_DAILY_SCHEDULE.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# Neural Motion SOP Generation Schedule — 8 Per Day\n\n")
        handle.write(f"**Period:** {start_date.strftime('%-d %B %Y')}–{END_DATE.strftime('%-d %B %Y')}  \n")
        handle.write(f"**Total unique SOPs:** {len(rows)}  \n")
        handle.write(f"**Daily target:** {BATCH_SIZE} SOPs  \n")
        handle.write(f"**Total batches:** {(len(rows) + BATCH_SIZE - 1) // BATCH_SIZE}  \n")
        handle.write("**Cadence:** Retrospective calendar-day batches, including weekends\n\n")

        current_batch = None
        for row in rows:
            if row["batch"] != current_batch:
                current_batch = row["batch"]
                scheduled = date.fromisoformat(row["date"])
                if current_batch != 1:
                    handle.write("\n")
                handle.write(
                    f"## Batch {current_batch} — {scheduled.strftime('%A, %-d %B %Y')}\n\n"
                )
            handle.write(f"- [ ] {row['sop_name']}\n")
        handle.write("\n")

    print(f"Scheduled {len(rows)} unique SOPs in {(len(rows) + 7) // 8} batches.")
    print(f"First date: {rows[0]['date']}")
    print(f"Last date: {rows[-1]['date']}")


if __name__ == "__main__":
    main()
