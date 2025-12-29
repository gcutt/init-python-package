from pathlib import Path

README_TEXT = """# init-python-package
A lightweight initializer for Python packages, designed to scaffold reproducible, transparent, and user-friendly repositories.

## Features
- Generates a complete PyPI-ready package structure
- Includes `README.md`, `LICENSE`, and `pyproject.toml`
- IDE-neutral `.gitignore` for clean collaboration
- Modular design for optional flows and diagnostics
- Emphasis on reproducibility, auditability, and onboarding clarity

## Installation
Clone the repository and run the initializer:

```bash example: 
git clone https://github.com/your-username/init-py-pkg.git
cd init-py-pkg
```

where ~/path/to/my_new_package is the full path to the package. 

This will generate, e.g.:
- `my_new_package/`
  - `__init__.py`
  - `README.md`
  - `LICENSE`
  - `pyproject.toml`
  - `.gitignore`
  - `/tools`
  - `/test`
  - `/scripts`
  - `/notebooks`
  - `/data`
      
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