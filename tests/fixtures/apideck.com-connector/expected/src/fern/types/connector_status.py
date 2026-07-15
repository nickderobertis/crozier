

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorStatus(str, enum.Enum):
    """
    Status of the connector. Connectors with status live or beta are callable.
    """

    LIVE = "live"
    BETA = "beta"
    DEVELOPMENT = "development"
    CONSIDERING = "considering"

    def visit(
        self,
        live: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        development: typing.Callable[[], T_Result],
        considering: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectorStatus.LIVE:
            return live()
        if self is ConnectorStatus.BETA:
            return beta()
        if self is ConnectorStatus.DEVELOPMENT:
            return development()
        if self is ConnectorStatus.CONSIDERING:
            return considering()
