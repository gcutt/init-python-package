from pathlib import Path

FOLDERS = ["data", "notebooks", "scripts", "tests"]

def scaffold_structure(project_root: Path, pkgname: str):
    """
    Create the base project folders and package directory.
    """
    for folder in FOLDERS:
        (project_root / folder).mkdir(exist_ok=True)
        print(f"Created folder: {project_root / folder}")

    pkg_path = project_root / pkgname
    pkg_path.mkdir(exist_ok=True)
    print(f"Created package folder: {pkg_path}")