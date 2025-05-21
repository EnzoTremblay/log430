import pytest
from app import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

def test_main_output_format(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"
