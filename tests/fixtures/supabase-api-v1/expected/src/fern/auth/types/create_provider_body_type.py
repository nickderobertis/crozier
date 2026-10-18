

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateProviderBodyType(enum.StrEnum):
    """
    What type of provider will be created
    """

    SAML = "saml"

    def visit(self, saml: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateProviderBodyType.SAML:
            return saml()
