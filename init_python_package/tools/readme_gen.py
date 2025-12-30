from pathlib import Path

README_TEXT = """# init-python-package

Minimal, distribution-ready Python package scaffolding.  
Generate projects that are instantly installable with pip and publishable to PyPI.

init-python-package helps you bootstrap Python projects with a ready-to-publish structure:
- Editable install support (`pip install -e .`)
- PyPI-compliant metadata (`pyproject.toml`, SPDX license, README)
- Preconfigured tests, scripts, and notebooks

## Features
- Generates a complete PyPI-ready package structure
- Includes `README.md`, `LICENSE`, and `pyproject.toml`
- IDE-neutral `.gitignore` for clean collaboration
- Modular design for optional flows and diagnostics
- Emphasis on reproducibility, auditability, and onboarding clarity

## Installation

Clone the repository and set up your environment:

```bash
git clone https://github.com/your-username/init-python-package.git
cd init-python-package
./setup_env.sh        # or setup_env.bat on Windows
pip install -e .
```

Alternatively, users can manually create and activate a virtual environment if they prefer.

## 📦 Usage

After installation, you can run the scaffolder in two ways:

### 1. Command Line (CLI)
Run directly from your terminal:

```bash
init-python-package my_new_package
```

where `my_new_package` is the full path to the package. 


- Creates a new package at the given path (`my_new_package`).
- If you omit the path, the tool runs in **interactive mode** and prompts you for the package location.

### 2. Interactive Mode (default)
Simply run:

```bash
init-python-package
```

You’ll be prompted to enter the full path for your new package.

### 3. From an IDE
You can also run the CLI entry point from your IDE’s integrated terminal (e.g. VS Code, PyCharm).  
Open the terminal inside your project workspace and run the same commands as above.

---

This creates a new folder with a complete Python package structure, including:
- Metadata (`pyproject.toml`, `README.md`, `LICENSE`)
- Importable package directory (`my_new_package/`)
- CLI entry point (`my_new_package/main.py`)
- Test scaffolding (`tests/`)
- Supporting folders (`scripts/`, `notebooks/`, `data/`)


## 🗂️ Generated Package Structure

<pre><code>```
my_new_package/
├── my_new_package/           # Importable Python package
│   ├── __init__.py           # Includes dynamic version
│   ├── main.py               # CLI entry point
│   └── tools/                # Helper modules
├── tests/                    # pytest-ready test folder
├── scripts/                  # Example scripts
├── notebooks/                # Example notebooks
├── data/                     # Data folder
├── README.md                 # PyPI-ready long description
├── LICENSE                   # Apache-2.0 license
├── pyproject.toml            # Build metadata
├── .gitignore
├── requirements.txt
├── setup_env.bat / .sh       # Optional environment setup
```
</code></pre>


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


def write_readme_md(project_root: Path, pkgname: str) -> None:
    content = README_TEXT.format(pkgname=pkgname)
    readme_path = project_root / "README.md"
    readme_path.write_text(content, encoding="utf-8")
    print(f"Created README.md at {readme_path}")