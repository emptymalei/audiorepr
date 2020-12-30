import os
import sys
import pandas as pd

import click
from loguru import logger
from audiorepr import audiolize

# determine current working directory
__CWD__ = os.getcwd()


@click.group(invoke_without_command=True)
@click.pass_context
def audiorepr(ctx):
    """
    audiorepr is the root command line command
    """
    if ctx.invoked_subcommand is None:
        click.echo("Hello {}".format(os.environ.get("USER", "")))
        click.echo("Welcome to audiorepr.")
    else:
        click.echo("Loading Service: %s" % ctx.invoked_subcommand)

@audiorepr.command()
def help():
    """
    How to use command line tool of audiorepr
    """

    click.echo(
        "The audiorepr command creates audio files out of a tabular data file.\n"
        "`audiorepr help` shows this message.\n"
        "`audiorepr create` command is the core command to create audio."
    )

@audiorepr.command()
@click.option(
    '-d', '--data',
    type=str,
    prompt=f"Please specify your data file\n"
    f"Your current working directory is {__CWD__}\n"
    f"Use absolute path or path relative to {__CWD__}.\n"
)
@click.option(
    '-t', '--target',
    type=click.Path(),
    prompt=f"Please specify your output file\n"
    f"Your current working directory is {__CWD__}\n"
    f"Use absolute path or path relative to {__CWD__}.\n"
    f"URL is also possible."
)
@click.option(
    '-c', '--column',
    multiple=True, default=None
)
def create(data, target, column):
    """
    creates audio from data file
    """

    click.echo(
        f"Using {data} as data source."
    )
    if column is not None:
        column = list(column)
        click.echo(
            f"Using columns:\n{column}"
        )

    df = pd.read_csv(data)
    click.echo(
        f"Data loaded"
    )
    audiolize.audiolizer(df, target=target, pitch_columns=column)
    click.echo(
        f"Audio file has been saved as {target}"
    )



if __name__ == "__main__":

    pass
