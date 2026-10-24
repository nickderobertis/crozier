

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DomainObject(enum.StrEnum):
    """
    Object type identifier
    """

    DOMAIN = "domain"

    def visit(self, domain: typing.Callable[[], T_Result]) -> T_Result:
        if self is DomainObject.DOMAIN:
            return domain()
