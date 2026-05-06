#!/usr/bin/env bash
set -euo pipefail
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
python benchmarks/harness.py > /tmp/cet_bench.txt
cat /tmp/cet_bench.txt
