#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="/home/neotix/Documents/SOPs/neural-motion"
RCLONE="$PROJECT_DIR/.sync-tools/unpacked/rclone-v1.75.0-linux-amd64/rclone"
CONFIG="$PROJECT_DIR/.sync-tools/rclone.conf"
DRIVE_FOLDER_ID="1LM5RBeCHvwCemxa062YAsR_AJqkM4dsP"

while IFS= read -r -d '' source_file; do
  relative_path="${source_file#"$PROJECT_DIR"/}"
  relative_dir="$(dirname -- "$relative_path")"
  filename="$(basename -- "$relative_path")"

  if [[ "$filename" == *.* && "$filename" != .* ]]; then
    extension=".${filename##*.}"
    stem="${filename%.*}"
  else
    extension=""
    stem="$filename"
  fi

  if [[ "$stem" != *_updated ]]; then
    stem="${stem}_updated"
  fi

  drive_filename="${stem}${extension}"
  if [[ "$relative_dir" == "." ]]; then
    drive_path="$drive_filename"
  else
    drive_path="$relative_dir/$drive_filename"
  fi

  "$RCLONE" \
    --config "$CONFIG" \
    copyto "$source_file" "sop-drive:$drive_path" \
    --drive-root-folder-id "$DRIVE_FOLDER_ID" \
    --log-file "$PROJECT_DIR/.sync-tools/sync.log" \
    --log-level INFO
done < <(
  find "$PROJECT_DIR" \
    -type d -name '.*' -prune -o \
    -type f ! -name '.DS_Store' -print0
)
