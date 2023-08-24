import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_not_duplicate_files(tmp_path, capsys):
    file_path = tmp_path / "trybe.pdf"
    file_path.write_text("Fake File")
    file_path2 = tmp_path / "trybe2.pdf"
    file_path2.write_text("Fake File de novo")

    context = {"all_files": [str(file_path), str(file_path2)]}

    assert find_duplicate_files(context) == []


def test_find_duplicate_files(tmp_path, capsys):
    file_path = tmp_path / "trybe.pdf"
    file_path.write_text("Fake File")

    context = {"all_files": [str(file_path), str(file_path)]}

    assert find_duplicate_files(context) == [(
        str(file_path),
        str(file_path),
    )]


def test_find_duplicate_files_not_exist():
    context = {
        "all_files": [
            ".gitignore",
            "src/app.py",
            "src/utils/__init__.py",
        ]
    }

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
