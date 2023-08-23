from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_not_exist(capsys):
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File 'Trybe_logo.png' does not exist\n"


def test_show_details_exist(tmp_path, capsys):
    file_path = tmp_path / "trybe.pdf"
    with open(file_path, "w") as file:
        file.write("Fake File")

    context = {"base_path": str(file_path)}
    show_details(context)
    captured = capsys.readouterr()
    assert (
        captured.out == "File name: trybe.pdf\n"
        "File size in bytes: 9\n"
        "File type: file\n"
        "File extension: .pdf\n"
        "Last modified date: 2023-08-23\n"
    )


def test_show_details_no_extension(tmp_path, capsys):
    file_path = tmp_path / "trybe"
    with open(file_path, "w") as file:
        file.write("Fake File")

    context = {"base_path": str(file_path)}
    show_details(context)
    captured = capsys.readouterr()
    assert (
        captured.out == "File name: trybe\n"
        "File size in bytes: 9\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-08-23\n"
    )
