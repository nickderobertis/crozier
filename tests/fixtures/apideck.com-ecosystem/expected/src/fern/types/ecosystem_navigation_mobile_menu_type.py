

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EcosystemNavigationMobileMenuType(str, enum.Enum):
    ICON = "ICON"
    TEXT = "TEXT"

    def visit(self, icon: typing.Callable[[], T_Result], text: typing.Callable[[], T_Result]) -> T_Result:
        if self is EcosystemNavigationMobileMenuType.ICON:
            return icon()
        if self is EcosystemNavigationMobileMenuType.TEXT:
            return text()
