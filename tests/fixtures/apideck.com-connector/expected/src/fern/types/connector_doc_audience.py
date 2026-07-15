

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorDocAudience(str, enum.Enum):
    """
    Audience for the doc.
    """

    APPLICATION_OWNER = "application_owner"
    CONSUMER = "consumer"

    def visit(
        self, application_owner: typing.Callable[[], T_Result], consumer: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ConnectorDocAudience.APPLICATION_OWNER:
            return application_owner()
        if self is ConnectorDocAudience.CONSUMER:
            return consumer()
