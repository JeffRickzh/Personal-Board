#!/bin/bash
# Sequential runner for all 4 members to avoid API rate limiting
# Each member runs one at a time with concurrency 1

cd "$(dirname "$0")"

echo "========================================="
echo "  Dataset Curation - Sequential Runner"
echo "========================================="
echo ""

for member in munger buffett paul_graham russell; do
    echo "[$(date '+%H:%M:%S')] Starting: $member"
    echo "-----------------------------------------"
    python3 dataset_curator.py --member "$member" --concurrency 1
    echo "[$(date '+%H:%M:%S')] Completed: $member"
    echo ""
    # Brief pause between members
    sleep 5
done

echo "========================================="
echo "  ALL MEMBERS COMPLETED"
echo "========================================="
echo ""
echo "Dataset files:"
for member in munger buffett paul_graham russell; do
    f="${member}_qa_dataset.jsonl"
    if [ -f "$f" ]; then
        count=$(wc -l < "$f")
        echo "  $f: $count QA pairs"
    fi
done
