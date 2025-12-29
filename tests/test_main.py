import unittest
import tempfile
import shutil
from pathlib import Path
from init_python_package.main import run_initializer

class TestInitializer(unittest.TestCase):
    def test_initializer_creates_structure(self):
        tmpdir = tempfile.mkdtemp()
        try:
            target = Path(tmpdir) / "my_test_package"
            run_initializer(target)

            # Assert key files exist
            self.assertTrue((target / "README.md").exists())
            self.assertTrue((target / "LICENSE").exists())
            self.assertTrue((target / "pyproject.toml").exists())
        finally:
            shutil.rmtree(tmpdir)



# import unittest
# import tempfile
# import shutil
# from pathlib import Path
# from init_python_package.main import main
#
# class TestInitializer(unittest.TestCase):
#     def test_main_scaffolds_package(self):
#         tmpdir = tempfile.mkdtemp()
#         try:
#             # Simulate user input: patch input() to return tmpdir
#             import builtins
#             original_input = builtins.input
#             builtins.input = lambda _: tmpdir
#
#             # Run initializer
#             main()
#
#             # Check that key files were created
#             self.assertTrue((Path(tmpdir) / "README.md").exists())
#             self.assertTrue((Path(tmpdir) / "LICENSE").exists())
#             self.assertTrue((Path(tmpdir) / "pyproject.toml").exists())
#
#         finally:
#             builtins.input = original_input
#             shutil.rmtree(tmpdir)
#
#
#
# # import unittest
# # from init_python_package.main import hello_world
# #
# # class TestMain(unittest.TestCase):
# #     def test_hello_world(self):
# #         self.assertEqual(hello_world(), "Hello, world!")
# #
# # if __name__ == "__main__":
# #     unittest.main()
