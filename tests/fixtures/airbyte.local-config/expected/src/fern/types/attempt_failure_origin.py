

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AttemptFailureOrigin(str, enum.Enum):
    """
    Indicates where the error originated. If not set, the origin of error is not well known.
    """

    SOURCE = "source"
    DESTINATION = "destination"
    REPLICATION = "replication"
    PERSISTENCE = "persistence"
    NORMALIZATION = "normalization"
    DBT = "dbt"
    AIRBYTE_PLATFORM = "airbyte_platform"
    UNKNOWN = "unknown"

    def visit(
        self,
        source: typing.Callable[[], T_Result],
        destination: typing.Callable[[], T_Result],
        replication: typing.Callable[[], T_Result],
        persistence: typing.Callable[[], T_Result],
        normalization: typing.Callable[[], T_Result],
        dbt: typing.Callable[[], T_Result],
        airbyte_platform: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AttemptFailureOrigin.SOURCE:
            return source()
        if self is AttemptFailureOrigin.DESTINATION:
            return destination()
        if self is AttemptFailureOrigin.REPLICATION:
            return replication()
        if self is AttemptFailureOrigin.PERSISTENCE:
            return persistence()
        if self is AttemptFailureOrigin.NORMALIZATION:
            return normalization()
        if self is AttemptFailureOrigin.DBT:
            return dbt()
        if self is AttemptFailureOrigin.AIRBYTE_PLATFORM:
            return airbyte_platform()
        if self is AttemptFailureOrigin.UNKNOWN:
            return unknown()
