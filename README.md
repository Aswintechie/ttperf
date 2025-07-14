# 🚀 ttperf - TT-Metal Performance Profiler

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-0.1.2-orange.svg)
[![GitHub issues](https://img.shields.io/github/issues/Aswintechie/ttperf)](https://github.com/Aswintechie/ttperf/issues)
[![GitHub stars](https://img.shields.io/github/stars/Aswintechie/ttperf)](https://github.com/Aswintechie/ttperf/stargazers)

**A streamlined CLI tool for profiling Tenstorrent's TT-Metal tests and extracting device kernel performance metrics**

</div>

## ✨ Features

- 🔍 **Automated Profiling**: Seamlessly runs Tenstorrent's TT-Metal profiler with pytest
- 📊 **CSV Analysis**: Automatically extracts and parses performance CSV files
- ⚡ **Real-time Output**: Shows profiling progress in real-time
- 📈 **Performance Metrics**: Calculates total DEVICE KERNEL DURATION
- 🎯 **Simple CLI**: Easy-to-use command-line interface
- 🛠️ **Flexible**: Supports named profiles and various test paths

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI (recommended)
pip install ttperf
```

**Or install from source:**

```bash
# Clone the repository
git clone https://github.com/Aswintechie/ttperf.git
cd ttperf

# Install the package
pip install -e .
```

### Basic Usage

```bash
# Run profiling on a specific test
ttperf test_performance.py

# Run with a custom profile name
ttperf my_profile pytest test_performance.py

# Run on a specific test method
ttperf tests/test_ops.py::test_matmul
```

## 📋 Usage Examples

### Simple Test Profiling
```bash
ttperf test_conv.py
```

### Named Profile
```bash
ttperf conv_benchmark pytest test_conv.py
```

### Specific Test Method
```bash
ttperf tests/ops/test_matmul.py::test_basic_matmul
```

### Output Example
```
▶️ Running: ./tt_metal/tools/profiler/profile_this.py -n conv_benchmark -c "pytest test_conv.py"

... (profiling output) ...

📁 Found CSV path: /path/to/profile_results.csv
⏱️ DEVICE KERNEL DURATION [ns] total: 1234567.89 ns
```

## 🛠️ How It Works

1. **Command Parsing**: Analyzes input arguments to determine profile name and test path
2. **Profile Execution**: Runs the Tenstorrent's TT-Metal profiler with the specified test
3. **Output Monitoring**: Streams profiling output in real-time
4. **CSV Extraction**: Parses the output to find the generated CSV file path
5. **Performance Analysis**: Reads the CSV and calculates total device kernel duration

## 📊 Performance Metrics

The tool extracts the following key metrics:

- **DEVICE KERNEL DURATION [ns]**: Total time spent in device kernels
- **CSV Path**: Location of the detailed profiling results
- **Real-time Progress**: Live output during profiling

## 🔧 Requirements

- Python 3.8+
- pandas
- Tenstorrent's TT-Metal development environment
- pytest

## 📁 Project Structure

```
ttperf/
├── ttperf.py          # Main CLI implementation
├── pyproject.toml     # Project configuration
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is an independent utility that interfaces with Tenstorrent's TT-Metal profiling tools. It is not affiliated with or endorsed by Tenstorrent Inc. The tool serves as a convenience wrapper around existing TT-Metal profiling infrastructure.

## 🐛 Issues

If you encounter any issues, please [create an issue](https://github.com/Aswintechie/ttperf/issues) on GitHub.

## 👨‍💻 Author

**Aswin Z**
- GitHub: [@Aswintechie](https://github.com/Aswintechie)
- Portfolio: [aswinlocal.in](https://aswinlocal.in)

## 🌟 Acknowledgments

- Tenstorrent's TT-Metal development team for the profiling tools
- Python community for excellent libraries like pandas

---

<div align="center">
Made with ❤️ for the Tenstorrent TT-Metal community
</div> 