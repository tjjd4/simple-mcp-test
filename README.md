# Simple MCP Client

This project provides a simple MCP (Multi-Client Protocol) implementation that demonstrates basic client-server communication capabilities.

## Prerequisites

- Python 3.12+
- Python package manager (e.g., `uv`) # suggestion

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tjjd4/simple-mcp-test.git
cd simple-mcp-test
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv # using python and pip
uv venv  # using uv

source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
uv run pip install -r pyproject.toml # using uv
```

## Running the Simple MCP Client

The simple MCP implementation can be tested using the `test_simple_mcp.py` script. This script demonstrates basic functionality including `call_tool()`, `read_resource()`, etc.

To run the test script:

```bash
# Run the test script
export PYTHONPATH=$(pwd)
python scripts/test_simple_mcp.py
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request