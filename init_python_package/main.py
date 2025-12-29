from pathlib import Path
from tools.scaffold import scaffold_structure
from tools.tools import write_tools
from tools.metadata import write_metadata
from tools.headers import write_python_files_with_header


def run_initializer(project_root: Path):
    """
    Perform the full package scaffolding in the given project_root.
    Expects project_root to NOT already exist.
    """
    project_root.mkdir(parents=True, exist_ok=False)

    pkgname = project_root.name.replace("-", "_")

    scaffold_structure(project_root, pkgname)
    write_tools(project_root)
    write_metadata(project_root, pkgname)
    write_python_files_with_header(project_root, pkgname)

    print(f"✅ Package '{pkgname}' initialized successfully at {project_root}")


def main():
    """
    CLI entry point: prompt user for a path and run the initializer.
    """
    project_path_input = input(
        "Enter the full path where you want to create the new package: "
    ).strip()
    project_root = Path(project_path_input)
    run_initializer(project_root)


if __name__ == "__main__":
    main()









# from pathlib import Path
# from tools.scaffold import scaffold_structure
# from tools.tools import write_tools
# from tools.metadata import write_metadata
# from tools.headers import write_python_files_with_header
#
# def main():
#     project_path_input = input("Enter the full path where you want to create the new package: ").strip()
#     project_root = Path(project_path_input)
#     project_root.mkdir(parents=True, exist_ok=False)
#
#     pkgname = project_root.name.replace("-", "_")
#
#     scaffold_structure(project_root, pkgname)
#     write_tools(project_root)
#     write_metadata(project_root, pkgname)
#     write_python_files_with_header(project_root, pkgname)
#
#     print("✅ Package initialized successfully!")
#
# if __name__ == "__main__":
#     main()