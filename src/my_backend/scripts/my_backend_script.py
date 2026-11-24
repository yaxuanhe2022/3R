"""CLI script for the my_backend package. This will be called on the command line"""

import click

from my_backend.my_backend import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def my_backend_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
