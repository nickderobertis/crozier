

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkType(enum.StrEnum):
    TERMS_OF_USE = "terms_of_use"
    PRIVACY_POLICY = "privacy_policy"
    RETURN_POLICY = "return_policy"

    def visit(
        self,
        terms_of_use: typing.Callable[[], T_Result],
        privacy_policy: typing.Callable[[], T_Result],
        return_policy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LinkType.TERMS_OF_USE:
            return terms_of_use()
        if self is LinkType.PRIVACY_POLICY:
            return privacy_policy()
        if self is LinkType.RETURN_POLICY:
            return return_policy()
