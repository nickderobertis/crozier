

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArtifactState(enum.StrEnum):
    """
    Describes the state of an artifact or artifact version.  The following states
    are possible:

    * ENABLED
    * DISABLED
    * DEPRECATED
    """

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    DEPRECATED = "DEPRECATED"

    def visit(
        self,
        enabled: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ArtifactState.ENABLED:
            return enabled()
        if self is ArtifactState.DISABLED:
            return disabled()
        if self is ArtifactState.DEPRECATED:
            return deprecated()
