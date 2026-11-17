# 🌐 IP Ping Tester (Concurrent Ping Sweep CLI)

A cross-platform Command-Line Interface (CLI) tool built in Python to test network connectivity for single or multiple IP addresses concurrently. Designed for quick infrastructure diagnostics and network health checks.

## 🚀 Features

* **Concurrent Execution:** Uses `concurrent.futures.ThreadPoolExecutor` to ping multiple hosts simultaneously, drastically reducing execution time compared to sequential checks.
* **Cross-Platform Support:** Automatically detects the operating system (`Windows` vs. `Linux/macOS`) via `platform.system()` and adapts the native `ping` command flags and output encoding accordingly.
* **Accurate Windows Detection:** Parses command output (`TTL` verification) to prevent false positives caused by Windows `ping` returning exit code `0` on host unreachable/timeout scenarios.
* **Input Validation:** Built-in IPv4 format validator ensuring all octets are valid integers between `0` and `255` before executing system commands.
* **Interactive CLI Menu:** Clean terminal interface allowing users to switch between single-host checks and batch IP sweeps.

## 🛠️ Technologies Used

* **Python 3.10+** (uses structural pattern matching `match/case`)
* Standard Libraries only (no external dependencies required):
  * `subprocess`
  * `concurrent.futures`
  * `platform`
