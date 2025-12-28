# init-python-package
A lightweight initializer for Python packages, designed to scaffold reproducible, transparent, and user-friendly repositories.

## Features
- Generates a complete PyPI-ready package structure
- Includes `README.md`, `LICENSE`, and `pyproject.toml`
- IDE-neutral `.gitignore` for clean collaboration
- Modular design for optional flows and diagnostics
- Emphasis on reproducibility, auditability, and onboarding clarity

## Installation
Clone the repository and run the initializer:

```bash
git clone https://github.com/your-username/init-py-pkg.git
cd init-py-pkg
```

## Usage
Run the initializer to scaffold a new package, e.g.:

```bash
python init_pkg.py ~/path/to/my_new_package 
```

where ~/path/to/my_new_package is the full path to the package. 


This will generate:
- `my_new_package/`
  - `__init__.py`
  - `README.md`
  - `LICENSE`
  - `pyproject.toml`
  - `.gitignore`

## License
Distributed under the GPL-3 License. See `LICENSE` for details.

## Contributing
Contributions are welcome! Please open issues or submit pull requests to improve usability, diagnostics, or documentation clarity.
