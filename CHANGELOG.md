# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-XX

### Added
- Initial release of ttperf CLI tool
- Support for profiling TT-Metal tests with pytest
- Automatic CSV path extraction from profiler output
- Device kernel duration calculation
- Real-time output streaming
- Flexible command-line argument parsing
- Support for named profiles
- Comprehensive error handling

### Features
- Simple CLI interface: `ttperf [name] [pytest] <test_path>`
- Automatic detection of test files and paths
- Integration with TT-Metal profiler tools
- CSV parsing for performance metrics
- Real-time progress monitoring

### Dependencies
- pandas for CSV processing
- Python 3.7+ support
- TT-Metal development environment

## [Unreleased]

### Planned
- Enhanced error messages

## [0.1.2] - 2024-12-19

### Added
- Added `--version` and `-v` flags to display version information
- Added `--help` and `-h` flags to display usage help
- Improved help message with examples and better formatting

### Changed
- Enhanced error messages to show help when no test path is provided

## [0.1.1] - 2024-12-19

### Changed
- Updated minimum Python version requirement from 3.7 to 3.8 for Ubuntu 24.04 compatibility
- Removed Python 3.7 from GitHub Actions test matrix
- Updated documentation to reflect Python 3.8+ requirement

### Fixed
- Resolved GitHub Actions failures on Ubuntu 24.04 due to Python 3.7 unavailability
- Support for multiple output formats
- Performance comparison tools
- Configuration file support
- Additional performance metrics
- Batch processing capabilities 