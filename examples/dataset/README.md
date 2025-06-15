# Datasets

Manage Langfuse datasets via `olca fuse`.

```bash
# list existing datasets
olca fuse datasets list

# create a dataset named demo
olca fuse datasets create demo

# add a run
olca fuse datasets add-run demo <run_id>
```

`olca fuse` forwards directly to `coaia fuse`, so all FuseWill features are available.
