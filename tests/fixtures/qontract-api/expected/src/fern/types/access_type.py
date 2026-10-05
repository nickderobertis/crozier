

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessType(enum.StrEnum):
    """
    Keycloak client type.
    """

    CONFIDENTIAL = "confidential"
    PUBLIC = "public"
    BEARER_ONLY = "bearer-only"

    def visit(
        self,
        confidential: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
        bearer_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccessType.CONFIDENTIAL:
            return confidential()
        if self is AccessType.PUBLIC:
            return public()
        if self is AccessType.BEARER_ONLY:
            return bearer_only()
