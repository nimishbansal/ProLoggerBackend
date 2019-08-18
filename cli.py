import click
import subprocess

import sys

import os

node_server_path = "/home/nimish/"


@click.command()
@click.argument('command', default="ls")
def hello(command):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo("hi")


if __name__ == '__main__':
    hello()
