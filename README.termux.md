# Running oLCa on Termux

This guide explains how to install and run the `olca` package on Android devices via [Termux](https://termux.dev).

## Prerequisites
- **Termux** from F‑Droid
- `pkg install git python clang` for the base toolchain
- Python 3.11 is recommended for best compatibility

## Installation
Clone the repository and use the helper script:

```bash
pkg install python git clang
git clone https://github.com/jgwill/olca.git
cd olca
./termux-install.sh
```

The script installs dependencies using a minimal requirements file that avoids heavy gRPC packages and then installs `olca` in editable mode. If you skip the script, run:
```bash
pip install -r requirements.txt && pip install -e .
```
to provide the necessary modules.

## Usage
After installation you can run:

```bash
olca --help
```

Some optional tracing features require `langfuse`, which depends on `grpcio`. These are disabled by default on Termux. If you later need tracing, consider installing a prebuilt `grpcio` wheel manually.
After installing `grpcio`, you can add tracing support with:
```bash
pip install 'olca[tracing]'
```

