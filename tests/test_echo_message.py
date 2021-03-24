from click.testing import CliRunner
from blur_python_example.cli import echo_message


def test_echo_default_message():
    runner = CliRunner()
    result = runner.invoke(echo_message, [])
    assert result.exit_code == 0
    assert result.output == "Hello World!\n"


def test_echo_custom_message():
    runner = CliRunner()
    result = runner.invoke(echo_message, ["--message", "Good Morning!"])
    assert result.exit_code == 0
    assert result.output == "Good Morning!\n"


def test_echo_multiple_messages():
    runner = CliRunner()
    result = runner.invoke(echo_message, ["--count", 2])
    assert result.exit_code == 0
    assert result.output == "Hello World!\nHello World!\n"


def test_echo_multiple_custom_messages():
    runner = CliRunner()
    result = runner.invoke(echo_message, ["--count", 3, "--message", "Good Afternoon!"])
    assert result.exit_code == 0
    assert result.output == "Good Afternoon!\nGood Afternoon!\nGood Afternoon!\n"
