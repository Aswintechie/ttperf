# ttperf/cli.py

import sys
import subprocess
import re
import pandas as pd
from pathlib import Path


def extract_csv_path(output: str) -> str:
    match = re.search(r"OPs csv generated at: (.+?\.csv)", output)
    if not match:
        print("❌ CSV path not found in output.")
        sys.exit(1)
    return match.group(1)


def get_device_kernel_duration(csv_path: str) -> float:
    df = pd.read_csv(csv_path)
    if "DEVICE KERNEL DURATION [ns]" not in df.columns:
        print("❌ 'DEVICE KERNEL DURATION [ns]' column not found.")
        sys.exit(1)
    return df["DEVICE KERNEL DURATION [ns]"].sum()


def parse_args(argv):
    # Default values
    name = None
    test_cmd = None

    for arg in argv:
        if arg.endswith(".py") or "::" in arg or Path(arg).exists():
            test_cmd = arg
        elif arg.lower() == "pytest":
            continue
        else:
            name = arg

    if not test_cmd:
        print("❌ Test file/path not found in arguments.")
        sys.exit(1)

    return name, test_cmd


def build_profile_command(name, test_cmd):
    name_arg = f"-n {name}" if name else ""
    return f"./tt_metal/tools/profiler/profile_this.py {name_arg} -c \"pytest {test_cmd}\""


def main():
    if len(sys.argv) < 2:
        print("Usage: ttperf [name] [pytest] <test_path>")
        sys.exit(1)

    name, test_cmd = parse_args(sys.argv[1:])
    profile_cmd = build_profile_command(name, test_cmd)

    print(f"▶️ Running: {profile_cmd}\n")

    process = subprocess.Popen(
        profile_cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1,
    )

    output_lines = []
    try:
        for line in process.stdout:
            print(line, end="")  # Real-time output
            output_lines.append(line)
    except KeyboardInterrupt:
        process.terminate()
        print("❌ Aborted.")
        sys.exit(1)

    process.wait()

    # Combine all output for post-analysis
    full_output = "".join(output_lines)

    # Extract CSV path and duration
    csv_path = extract_csv_path(full_output)
    print(f"\n📁 Found CSV path: {csv_path}")

    duration = get_device_kernel_duration(csv_path)
    print(f"\n⏱️ DEVICE KERNEL DURATION [ns] total: {duration:.2f} ns")


if __name__ == "__main__":
    main()