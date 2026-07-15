

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorOauthCredentialsSource(str, enum.Enum):
    """
    Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.
    """

    INTEGRATION = "integration"
    CONNECTION = "connection"

    def visit(self, integration: typing.Callable[[], T_Result], connection: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectorOauthCredentialsSource.INTEGRATION:
            return integration()
        if self is ConnectorOauthCredentialsSource.CONNECTION:
            return connection()
