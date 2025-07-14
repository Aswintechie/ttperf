# Contributing to ttperf

Thank you for your interest in contributing to ttperf! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/Aswintechie/ttperf.git
   cd ttperf
   ```

2. **Set up development environment**
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt  # If available
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🔧 Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep lines under 88 characters when possible

### Testing
- Write tests for new features
- Ensure existing tests pass
- Test with different Python versions if possible

### Documentation
- Update README.md for new features
- Add examples for new functionality
- Update CHANGELOG.md with your changes

## 📝 Pull Request Process

1. **Update documentation**
   - Update README.md if needed
   - Add entry to CHANGELOG.md
   - Update version in pyproject.toml if needed

2. **Ensure code quality**
   - Run tests: `python -m pytest`
   - Check code style: `flake8 ttperf.py`
   - Fix any linting issues

3. **Submit Pull Request**
   - Use a clear, descriptive title
   - Provide detailed description of changes
   - Reference any related issues
   - Include screenshots if applicable

## 🐛 Bug Reports

When reporting bugs, please include:
- Python version
- Operating system
- TT-Metal version
- Complete error message
- Steps to reproduce
- Expected vs actual behavior

## 💡 Feature Requests

For feature requests, please:
- Describe the feature clearly
- Explain the use case
- Provide examples if possible
- Consider backward compatibility

## 🏷️ Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to docs
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed

## 🎯 Areas for Contribution

- **Performance improvements**: Optimize CSV parsing
- **Error handling**: Better error messages
- **Features**: New output formats, metrics
- **Testing**: Increase test coverage
- **Documentation**: Examples, tutorials
- **CLI**: Better argument parsing, help text

## 📞 Getting Help

- Create an issue for bugs or questions
- Check existing issues before creating new ones
- Be patient and respectful

## 🌟 Recognition

Contributors will be recognized in:
- README.md contributors section
- CHANGELOG.md for their contributions
- GitHub contributors page

Thank you for contributing to ttperf! 🚀 