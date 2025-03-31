import pytest

from src.decorators import log


def test_log_decorator_no_filename(capsys):
    @log()
    def test_func(x, y):
        return x + y

    test_func(2, 3)
    captured = capsys.readouterr()
    assert "test_func ok" in captured.out


def test_log_decorator_with_filename(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=log_file)
    def test_func(x, y):
        return x + y

    test_func(2, 3)
    with open(log_file, "r") as f:
        log_content = f.read()
    assert "test_func ok" in log_content


def test_log_decorator_error_no_filename(capsys):
    @log()
    def test_func(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(1, 0)

    captured = capsys.readouterr()
    assert "test_func error: ZeroDivisionError" in captured.out


def test_log_decorator_error_with_filename(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=log_file)
    def test_func(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(1, 0)

    with open(log_file, "r") as f:
        log_content = f.read()
    assert "test_func error: ZeroDivisionError" in log_content
