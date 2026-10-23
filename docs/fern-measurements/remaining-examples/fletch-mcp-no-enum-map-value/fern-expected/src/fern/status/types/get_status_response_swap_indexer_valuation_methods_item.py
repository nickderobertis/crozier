

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetStatusResponseSwapIndexerValuationMethodsItem(enum.StrEnum):
    USDG_NOMINAL = "usdg_nominal"
    HISTORICAL_CHAINLINK_WINDOW_START = "historical_chainlink_window_start"

    def visit(
        self,
        usdg_nominal: typing.Callable[[], T_Result],
        historical_chainlink_window_start: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetStatusResponseSwapIndexerValuationMethodsItem.USDG_NOMINAL:
            return usdg_nominal()
        if self is GetStatusResponseSwapIndexerValuationMethodsItem.HISTORICAL_CHAINLINK_WINDOW_START:
            return historical_chainlink_window_start()
