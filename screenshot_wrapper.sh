#!/bin/bash

# Directory to monitor for new screenshots
SCREENSHOT_DIR="$HOME/Pictures/Screenshots"

# Function to process new screenshots
process_screenshot() {
    local screenshot_path="$1"
    echo "New screenshot detected: $screenshot_path"
    olca --screenshot "$screenshot_path"
}

# Monitor the directory for new screenshots
inotifywait -m -e create --format "%w%f" "$SCREENSHOT_DIR" | while read new_screenshot; do
    process_screenshot "$new_screenshot"
done
