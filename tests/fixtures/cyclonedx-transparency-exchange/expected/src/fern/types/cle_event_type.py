

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CleEventType(enum.StrEnum):
    """
    The type of CLE lifecycle event
    """

    RELEASED = "released"
    END_OF_DEVELOPMENT = "endOfDevelopment"
    END_OF_SUPPORT = "endOfSupport"
    END_OF_LIFE = "endOfLife"
    END_OF_DISTRIBUTION = "endOfDistribution"
    END_OF_MARKETING = "endOfMarketing"
    SUPERSEDED_BY = "supersededBy"
    COMPONENT_RENAMED = "componentRenamed"
    WITHDRAWN = "withdrawn"

    def visit(
        self,
        released: typing.Callable[[], T_Result],
        end_of_development: typing.Callable[[], T_Result],
        end_of_support: typing.Callable[[], T_Result],
        end_of_life: typing.Callable[[], T_Result],
        end_of_distribution: typing.Callable[[], T_Result],
        end_of_marketing: typing.Callable[[], T_Result],
        superseded_by: typing.Callable[[], T_Result],
        component_renamed: typing.Callable[[], T_Result],
        withdrawn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CleEventType.RELEASED:
            return released()
        if self is CleEventType.END_OF_DEVELOPMENT:
            return end_of_development()
        if self is CleEventType.END_OF_SUPPORT:
            return end_of_support()
        if self is CleEventType.END_OF_LIFE:
            return end_of_life()
        if self is CleEventType.END_OF_DISTRIBUTION:
            return end_of_distribution()
        if self is CleEventType.END_OF_MARKETING:
            return end_of_marketing()
        if self is CleEventType.SUPERSEDED_BY:
            return superseded_by()
        if self is CleEventType.COMPONENT_RENAMED:
            return component_renamed()
        if self is CleEventType.WITHDRAWN:
            return withdrawn()
