# Network Traffic Analyzer

**“If it moves on the network — it gets logged.”**

## Overview

**Network Traffic Analyzer** is a real-time packet sniffer and logger developed by **5H4MMZ**, built entirely in Python using the Scapy library. Designed with simplicity and precision in mind, this tool captures essential network packet metadata, displays it in real-time via the terminal, and logs it to a CSV file for further analysis.

Whether you're studying cybersecurity, analyzing traffic for educational purposes, or preparing to build a more advanced monitoring system, this tool provides a solid foundation.

## Features

* **Real-Time Packet Sniffing**
  Captures live packets from a specified network interface using Scapy.

* **Accurate Packet Parsing**
  Extracts useful metadata:

  * Source and Destination IPs
  * Source and Destination Ports
  * Protocol Type (TCP/UDP/Other)
  * Packet Length

* **CSV Logging**
  Logs every captured packet into `traffic_log.csv`, complete with timestamps in ISO 8601 format.

* **Terminal Output**
  Prints each packet’s details to the console in real-time, allowing for quick visibility and debugging.

## Project Structure

```text
.
├── README.md             # Project documentation
├── main.py               # Entry point: Launches the sniffer
├── requirements.txt      # Python dependencies
└── analyzer/
    ├── sniffer.py        # Scapy-based sniffing logic
    ├── parser.py         # Packet parsing and extraction
    └── logger.py         # CSV logging functionality
```

## Installation

Install the required Python dependencies using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
scapy
pandas
```

Make sure you're using Python 3.x on a Unix-like system (e.g. Linux, Pop!\_OS, Kali). Some functionality — like packet sniffing — may not work as expected on Windows without additional configuration.

## Usage

To run the program:

```bash
sudo python3 main.py [interface]
```

**Example:**

```bash
sudo python3 main.py wlo1
```

If no interface is provided, the program defaults to `wlo1`. You can change this in `main.py` to match your system configuration (e.g., `eth0`, `enpXsY`, etc.).

> **Note:** Root privileges are required to capture raw network traffic.

## Output

Captured packet data is logged into the `traffic_log.csv` file. Each entry contains:

* Timestamp (ISO 8601)
* Source IP
* Destination IP
* Protocol
* Source Port
* Destination Port
* Packet Length

## Why This Project Stands Out

This analyzer was purpose-built — not cloned — with real-world use in mind. It’s tailored to work on Unix-like systems (such as **Pop!\_OS**) and is optimised for wireless interfaces. It supports your learning journey into traffic inspection and network monitoring.

It also serves as a foundational layer for more complex projects, such as:

* Intrusion Detection Systems (IDS)
* Visual traffic dashboards
* Machine learning pipelines

## Future Enhancements

* Protocol-level filtering (e.g., HTTP, DNS)
* Web dashboard for real-time visualisation (Flask + React)
* Machine learning integration for anomaly detection
* Persistent storage via SQLite or MongoDB

## Credits

Developed by **therealshammz**

Crafted using Python, Scapy, and hands-on experience in network security.
