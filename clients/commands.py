import click

from typing import List
from tabulate import tabulate  # type: ignore

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manages the clients lifecycle."""
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name.')
@click.option('-c', '--company', type=str, prompt=True, help='The client company.')
@click.option('-e', '--email', type=str, prompt=True, help='The client email.')
@click.option('-p', '--position', type=str, prompt=True, help='The client position.')
@click.pass_context
def create(ctx: click.Context, name: str, company: str, email: str, position: str):
    """Creates a new client.

    Time Complexity: O(1)
    
    """
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx: click.Context):
    """List all clients.

    Time Complexity: O(n)
    """
    
    client_service = ClientService(ctx.obj['clients_table'])

    table_data: List[List[str]] = []

    client: dict
    for client in client_service.list_clients():

        table_data.append([
            client['name'],
            client['company'],
            client['email'],
            client['position'],
            client['uid'],
        ])

    table = tabulate(
        table_data,
        headers=Client.schema(),
    )
    print(table)


def _update_client_flow(client) -> Client:
    """Updates a client.

    Time Complexity: O(1)

    Returns:
        Client: The updated client.
    """

    click.echo('Leave empty if you do not want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.option('-u', '--uid', type=str, prompt=True, help='The client UID.')
@click.pass_context
def update(ctx: click.Context, uid: str):
    """Updates a client.

    Time Complexity: O(n)
    """

    client_service = ClientService(ctx.obj['clients_table'])

    clients = client_service.list_clients()

    client = None

    c: dict
    for c in clients:
        if c['uid'] == uid:
            client = Client.from_dict(c)
            break
    
    if client is None:
        click.echo('Client not found')
        return
    
    _update_client_flow(client)
    client_service.update_client(client, clients)

@clients.command()
@click.option('-u', '--uid', type=str, prompt=True, help='The client UID.')
@click.pass_context
def delete(ctx: click.Context, uid: str):
    """Deletes a client.

    Time Complexity: O(n)
    """
    
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()
    
    found: bool = False
    c: dict
    for c in clients:
        if c['uid'] == uid:
            found = True
            break

    if not found:
        click.echo('Client not found')
        return

    client_service.delete_client(uid, clients)


all = clients
