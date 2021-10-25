import click

from clients import commands as client_commands

CLIENTS_TABLE = '.clients.csv'


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """
    A command line interface for Platzi ventas.
    """

    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


# Register commands
cli.add_command(client_commands.all)
