import click


@click.command()
@click.option("--count", default=1, help="Number of times to print message.")
@click.option("--message", default="Hello World!", help="Message to print.")
def echo_message(count, message):
    for _ in range(count):
        click.echo(message)


if __name__ == "__main__":  # pragma: no cover
    echo_message()
