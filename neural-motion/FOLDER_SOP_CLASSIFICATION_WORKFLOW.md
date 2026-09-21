# Folder-Based SOP Classification Workflow

## Source of truth

Use the SOP documents present in this folder. Do not use `neural-motion-linear-tasks.csv` to select
or classify work.

Each unique `*_SOP.md` file is one SOP. Sort paths in case-sensitive lexical order and classify the
next 8 unprocessed files per working day. PDFs and visual aids belonging to the same SOP are not
separate records.

## Recorded fields

- **Environment:** Tabletop or In-situ, based on the workspace described by the SOP.
- **Cell type:** the SOP's explicit `cell_type` value. If that field is absent, infer it from explicit
  arm-use instructions and mark the source as `inferred from SOP text`.
- **Parked side:** the SOP's explicit value, or `none` when the SOP explicitly uses both arms.
- **Evidence:** the metadata or decisive instruction supporting the classification.
- **Status:** `Classified` when the document is clear; `Needs review` when it is ambiguous.

Results are recorded in `folder_sop_classifications.csv`.

## Daily batch rule

1. List unique Markdown SOPs from the folder in case-sensitive lexical path order.
2. Exclude every source path already present in the results CSV.
3. Take the first 8 remaining paths.
4. Read each SOP and record its environment and cell configuration.
5. Do not count duplicate PDFs, root-level PDF copies, images, or steps-and-violations documents.

## Batch 1 — 2026-09-04

- SOPs classified: 8
- Environment: 8 Tabletop
- Cell type: 8 Bimanual
- Needs review: 0
