from typing import List
from uuid import uuid4


class Client:
    """Represents a client."""

    # Typing definitions
    name: str
    company: str
    email: str
    position: str
    _uid: str

    def __init__(self,
                 name: str,
                 company: str,
                 email: str,
                 position: str,
                 uid = None):
        """Initializes a client."""

        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self._uid = uid or self._generate_uid()

    @property
    def uid(self) -> str:
        """Returns the unique identifier of the client.
        
        Prevents the uid from being modified.
        """
        return self._uid

    def _generate_uid(self) -> str:
        """Generates a unique identifier for the client."""
        return uuid4().hex

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the client."""

        return {
            'name': self.name,
            'company': self.company,
            'email': self.email,
            'position': self.position,
            'uid': self.uid
        }

    @staticmethod
    def from_dict(client_dict: dict) -> 'Client':
        """Creates a client from a dictionary."""

        return Client(
            client_dict['name'],
            client_dict['company'],
            client_dict['email'],
            client_dict['position'],
            client_dict['uid']
        )

    @staticmethod
    def schema() -> List[str]:
        return ['name', 'company', 'email', 'position', 'uid']
