import csv
import os

from typing import List

from clients.models import Client


class ClientService:
    """
    Client service class.
    """

    # Type definitions
    _table_name: str    

    def __init__(self, table_name: str) -> None:
        """Initializes the client service."""

        self._table_name = table_name
        self._storage_path = os.path.join(os.path.dirname(__file__), '..', self._table_name)

    def create_client(self, client: Client):
        """Creates a client.
        
        Time Complexity: O(1)

        Args:
            client (Client): The client to be created.
        """

        with open(self._storage_path, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self) -> List[dict]:
        """Shows the list of clients.
        
        Time Complexity: O(n)
        """

        with open(self._storage_path, 'r') as f:
            schema = Client.schema()

            reader = csv.DictReader(f, fieldnames=schema)

            return list(reader)

    def _save_to_disk(self, clients: List[dict]):
        """Saves the clients to the disk.
        
        Time Complexity: O(n)

        Args:
            clients (List[dict]): The clients to be saved.
        """

        tmp_path = self._storage_path + '.tmp'

        with open(tmp_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        if os.path.exists(self._storage_path):
            os.remove(self._storage_path)

        os.rename(tmp_path, self._storage_path)

    def update_client(self, updated_client: Client, clients: List[dict] = None):
        """Updates a client.
        
        Time Complexity: O(n)

        Args:
            updated_client (Client): The client to be updated.
        """

        if clients is None:
            clients = self.list_clients()

        updated_clients: List[dict] = []

        client: dict
        for client in clients:
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)


    def delete_client(self, client_uid: str, clients: List[dict] = None):
        """Deletes a client.
        
        Time Complexity: O(n)

        Args:
            client_uid (str): The client's UID.
        """

        if clients is None:
            clients = self.list_clients()

        updated_clients: List[dict] = []

        client: dict
        for client in clients:
            if client['uid'] != client_uid:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)
