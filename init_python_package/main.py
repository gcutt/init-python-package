import os
from pathlib import Path

FOLDERS = ["data", "notebooks", "scripts", "tests"]

REQUIREMENTS = """# Project dependencies
pathlib
#numpy
#pandas
#python-dateutil
#pytz
#scipy
#fastapi
#uvicorn
"""

GITIGNORE = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
.venv/
env/
venv/

# Distribution / packaging
build/
dist/
*.egg-info/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Logs
*.log

# OS files
.DS_Store
Thumbs.db
"""

BASH_SCRIPT = """#!/bin/bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
"""

BAT_SCRIPT = """@echo off
python3.12 -m venv .venv
call .venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
"""

INIT_PY = """\"\"\"Top-level package for {pkgname}.\"\"\""""

PACKAGE_MAIN = """def hello_world():
    \"\"\"Example function to demonstrate project structure.\"\"\" 
    return "Hello, world!"

def main():
    message = hello_world()
    print(message)

if __name__ == "__main__":
    main()
"""

TEST_SCRIPT = """import unittest
from {pkgname}.main import hello_world

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
"""

PYPROJECT = """[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{pkgname}"
version = "0.1.0"
description = "A Python package scaffold"
authors = [{{ name = "Your Name" }}]
readme = "README.md"
dependencies = []
"""

# Simplified README template
README = """# {pkgname}

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

## Contributing
Contributions are welcome! Please open issues or submit pull requests to improve usability, diagnostics, or documentation clarity.

## Author

This project was created and is maintained by **George Cutter**.  
George is a systems thinker and open‑source advocate, focused on building reproducible, transparent, and user‑empowering scientific workflows. His work emphasizes modularity, auditability, and contributor onboarding clarity.

## Disclaimer

- This software is provided **“as is”**, without warranty of any kind, express or implied.  
- The author assumes **no responsibility** for errors, omissions, or outcomes resulting from the use of this code.  
- Users are encouraged to validate results independently and adapt workflows to their own requirements.  
- Contributions are welcome, but all contributors agree that their input will be licensed under the same terms as the project.  
- This project is intended for **educational and research purposes**. It should not be used as a substitute for professional advice in regulated domains (e.g., medical, legal, financial).

## License

This project is licensed under the **Apache License 2.0**.  
You may use, modify, and distribute this software under the terms of the Apache License.  
See the [LICENSE](LICENSE) file for the full text.

### License Compatibility Note

- Contributions are accepted under the same license.  
- The license includes explicit **patent rights protection**, ensuring contributors grant users rights to any patents necessarily infringed by their contributions.  
- Redistribution and derivative works are permitted, provided that the Apache 2.0 terms are followed.  
- Apache 2.0 is permissive, allowing integration with both open‑source and proprietary projects, while maintaining strong safeguards against patent litigation.
"""

def main():
    project_path_input = input("Enter the full path where you want to create the new package: ").strip()
    project_root = Path(project_path_input)

    project_root.mkdir(parents=True, exist_ok=False)
    print(f"Initializing package in: {project_root.resolve()}")

    pkgname = project_root.name.replace("-", "_")

    for folder in FOLDERS:
        path = project_root / folder
        path.mkdir(exist_ok=True)
        print(f"Created folder: {path}")

    pkg_path = project_root / pkgname
    pkg_path.mkdir(exist_ok=True)
    print(f"Created package folder: {pkg_path}")

    (pkg_path / "__init__.py").write_text(INIT_PY.format(pkgname=pkgname))
    (pkg_path / "main.py").write_text(PACKAGE_MAIN)

    (project_root / "tests" / "test_main.py").write_text(TEST_SCRIPT.format(pkgname=pkgname))

    (project_root / "requirements.txt").write_text(REQUIREMENTS)
    (project_root / ".gitignore").write_text(GITIGNORE)
    (project_root / "pyproject.toml").write_text(PYPROJECT.format(pkgname=pkgname))
    (project_root / "README.md").write_text(README.format(pkgname=pkgname))

    (project_root / "setup_env.sh").write_text(BASH_SCRIPT)
    os.chmod(project_root / "setup_env.sh", 0o755)
    (project_root / "setup_env.bat").write_text(BAT_SCRIPT)

    print("✅ Package initialized successfully!")

if __name__ == "__main__":
    main()