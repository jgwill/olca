# Quick Start

This example shows how to run `olca` with tracing and streaming.

1. Copy `olca.yml`:
   ```bash
   cp ../../olca.yml.sample olca.yml
   ```
   (If you don't have a sample config, run `olca init`.)

2. Run the assistant:
   ```bash
   olca -T --stream updates
   ```

Use `-H` for human-in-the-loop mode.
