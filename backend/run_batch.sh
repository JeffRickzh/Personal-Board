#!/bin/bash
# Run 2 batches of 2 processes each, concurrency 2 per process
# Batch 1: Munger + Buffett
# Batch 2: Paul Graham + Russell

cd "$(dirname "$0")"
export PYTHONUNBUFFERED=1

echo "=== Batch 1: Munger + Buffett ==="
python3 dataset_curator.py --member munger --concurrency 2 2>&1 &
PID1=$!
python3 dataset_curator.py --member buffett --concurrency 2 2>&1 &
PID2=$!
wait $PID1 $PID2
echo "=== Batch 1 complete ==="

echo ""
echo "=== Batch 2: Paul Graham + Russell ==="
python3 dataset_curator.py --member paul_graham --concurrency 2 2>&1 &
PID3=$!
python3 dataset_curator.py --member russell --concurrency 2 2>&1 &
PID4=$!
wait $PID3 $PID4
echo "=== Batch 2 complete ==="

echo ""
echo "=== ALL DONE ==="
for f in munger buffett paul_graham russell; do
    count=$(wc -l < "${f}_qa_dataset.jsonl" 2>/dev/null || echo 0)
    echo "  ${f}: $count QA pairs"
done
