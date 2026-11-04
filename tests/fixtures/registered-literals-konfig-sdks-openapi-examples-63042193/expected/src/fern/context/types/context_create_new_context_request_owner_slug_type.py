

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContextCreateNewContextRequestOwnerSlugType(enum.StrEnum):
    """
    The type of owner. Defaults to "organization". Accounts are only used as context owners in server and must be specified by an id instead of a slug.
    """

    ORGANIZATION = "organization"

    def visit(self, organization: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContextCreateNewContextRequestOwnerSlugType.ORGANIZATION:
            return organization()
