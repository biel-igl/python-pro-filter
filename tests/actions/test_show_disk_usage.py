from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage_anything(capsys):
    context = {"all_files": []}

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage(tmp_path, capsys):
    file_path = tmp_path / "trybe.pdf"
    file_path.write_text("Fake File")
    file_path2 = tmp_path / "trybe2.pdf"
    file_path2.write_text("Fake File de novo")

    context = {"all_files": [str(file_path), str(file_path2)]}

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "'/tmp/pytest-of-biel/pytest-...st_show_disk_usage0/trybe2.pdf':"
        "        17 (65%)\n'/tmp/pytest-of-biel/pytest-"
        "...est_show_disk_usage0/trybe.pdf':"
        "        9 (34%)\nTotal size: 26\n"
    )
