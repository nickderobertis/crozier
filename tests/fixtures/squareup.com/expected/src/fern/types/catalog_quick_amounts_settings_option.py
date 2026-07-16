

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CatalogQuickAmountsSettingsOption(str, enum.Enum):
    """
    Determines a seller's option on Quick Amounts feature.
    """

    DISABLED = "DISABLED"
    MANUAL = "MANUAL"
    AUTO = "AUTO"

    def visit(
        self,
        disabled: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogQuickAmountsSettingsOption.DISABLED:
            return disabled()
        if self is CatalogQuickAmountsSettingsOption.MANUAL:
            return manual()
        if self is CatalogQuickAmountsSettingsOption.AUTO:
            return auto()
