# 0xDSI-CET (C Engine)

C implementation of Complete Event Trend Detection (CET) with Databricks/Spark integration via Python ctypes bridge.

## Production Components Included
- Native C engine: DSL, graph, M-CET/T-CET/H-CET executors, sliding windows, graphlet optimizer.
- Shared library build (`liboxdsi_cet.so`) + static library for tests.
- Python FFI bridge (`bindings/python/bridge.py`) with typed wrappers.
- Databricks Structured Streaming notebook using distributed `mapPartitions` + `foreachBatch` + Delta MERGE.
- Unit tests for parser, traversal, graphlets, planning, and cache primitives.

## Build & Test
```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

## Deployment Notes
- Build shared library on cluster init and place in path used by `CETBridge`.
- Ensure Delta tables `cet_events`, `cet_complete_trends`, and `cet_metrics` exist.
