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

INIT_PY = "\"\"\"Top-level package for {pkgname}.\"\"\""

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

def write_py_with_header(path: Path, content: str):
    """
    Write a Python file with the Apache 2.0 header prepended.
    """
    path.write_text(APACHE_HEADER + "\n" + content, encoding="utf-8")
    print(f"Created Python file with Apache header: {path}")

def write_python_files_with_header(project_root: Path, pkgname: str):
    """
    Generate __init__.py, main.py, test_main.py, and starter files in scripts/notebooks
    with the Apache 2.0 header automatically included.
    """
    pkg_path = project_root / pkgname
    tests_path = project_root / "tests"
    scripts_path = project_root / "scripts"
    notebooks_path = project_root / "notebooks"

    # Core package files
    write_py_with_header(pkg_path / "__init__.py", INIT_PY.format(pkgname=pkgname))
    write_py_with_header(pkg_path / "main.py", PACKAGE_MAIN)

    # Tests
    write_py_with_header(tests_path / "test_main.py", TEST_SCRIPT.format(pkgname=pkgname))

    # Starter files in scripts/ and notebooks/
    write_py_with_header(scripts_path / "example_script.py", "print('Example script')")
    write_py_with_header(notebooks_path / "example_notebook.py", "print('Example notebook scaffold')")