import os
from pathlib import Path

APACHE_HEADER = """# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""

TOOLS_SCRIPTS = {
    "lint.sh": """#!/bin/bash
pre-commit run --all-files
""",
    "diagnostics.py": """def run_diagnostics():
    print("Running basic diagnostics...")
"""
}

LICENSE_CONFIG = """{
  "header": "Apache-2.0",
  "files": ["*.py"],
  "enforce": true
}
"""

CHECK_APACHE = """import sys, pathlib

HEADER = \"\"\"# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.\"\"\"

def check_file(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    if HEADER not in text:
        print(f"Missing Apache header in {path}")
        return False
    return True

def main():
    root = pathlib.Path(".")
    py_files = list(root.rglob("*.py"))
    ok = True
    for f in py_files:
        if not check_file(f):
            ok = False
    if not ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
"""


from pathlib import Path

def write_tools(project_root: Path, pkgname: str) -> None:
    """
    Create a 'tools' directory inside the generated package.

    Args:
        project_root (Path): The root directory where the new package scaffold is being created.
        pkgname (str): The name of the package directory under project_root
                       (e.g. 'my_test_package'), where 'tools' will be placed.

    Returns:
        None
    """
    tools_dir = project_root / pkgname / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)

    # Example: write helper files
    (tools_dir / "lint.sh").write_text("#!/bin/bash\nflake8 ..\n")
    (tools_dir / "diagnostics.py").write_text(
        "def run_diagnostics():\n    print('Diagnostics running...')\n"
    )
    (tools_dir / "check_apache_header.py").write_text(
        "def check_header(file_path):\n    print(f'Checking header in {file_path}')\n"
    )
    (tools_dir / "license_config.json").write_text('{"license": "Apache-2.0"}')






## old
# def write_tools(project_root: Path):
#     """
#     Create the tools folder and populate with utility scripts.
#     """
#     tools_path = project_root / "tools"
#     tools_path.mkdir(exist_ok=True)
#
#     # Write simple tools
#     for fname, content in TOOLS_SCRIPTS.items():
#         fpath = tools_path / fname
#         fpath.write_text(content, encoding="utf-8")
#         if fname.endswith(".sh"):
#             os.chmod(fpath, 0o755)
#         print(f"Created tool: {fpath}")
#
#     # Write check_apache_header.py
#     (tools_path / "check_apache_header.py").write_text(APACHE_HEADER + "\n" + CHECK_APACHE, encoding="utf-8")
#     print(f"Created tool: {tools_path / 'check_apache_header.py'}")
#
#     # Write license_config.json
#     (tools_path / "license_config.json").write_text(LICENSE_CONFIG, encoding="utf-8")
#     print(f"Created tool: {tools_path / 'license_config.json'}")
