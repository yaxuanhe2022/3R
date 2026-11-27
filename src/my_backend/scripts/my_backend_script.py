"""CLI script for the my_backend package."""

import click

from my_backend.my_backend import descriptive_stats, hello_world


@click.command()
@click.option("--message", help="Type a message to say")
@click.option("--numbers", help="Comma-separated numbers")
@click.version_option()
def my_backend_cli(message, numbers):
    """A simple descriptive statistics tool."""
    if numbers is not None:
        try:
            data = [float(x) for x in numbers.split(",")]
            result = descriptive_stats(data)
        except ValueError as e:
            raise click.ClickException(str(e)) from e

        for key, value in result.items():
            if key == "Count":
                click.echo(f"{key}: {value}")
            else:
                click.echo(f"{key}: {value:.2f}")
    else:
        if message is None:
            message = click.prompt("message")
        click.echo(hello_world(message))
