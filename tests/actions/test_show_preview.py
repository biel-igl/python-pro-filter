from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview(capsys):
    context = {"all_files": [], "all_dirs": []}

    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"

    context2 = {
        "all_files": [
            "src/__init__.py",
            "src/app/init.py",
            "src/utils/__init__.py",
            "src/dev/code.py",
            "src/temp/temp.txt",
            "src/trybe/main.js",
        ],
        "all_dirs": [
            "src",
            "src/app",
            "src/utils",
            "src/dev",
            "src/temp",
            "src/trybe",
        ],
    }

    show_preview(context2)
    captured = capsys.readouterr()
    assert (
        captured.out == "Found 6 files and 6 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app/init.py',"
        " 'src/utils/__init__.py', 'src/dev/code.py', 'src/temp/temp.txt']\n"
        "First 5 directories: ['src',"
        " 'src/app', 'src/utils', 'src/dev', 'src/temp']\n"
    )
