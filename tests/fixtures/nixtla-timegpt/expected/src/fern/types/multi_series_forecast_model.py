

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultiSeriesForecastModel(enum.StrEnum):
    """
    Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.
    """

    TIMEGPT1 = "timegpt-1"
    TIMEGPT1LONG_HORIZON = "timegpt-1-long-horizon"
    SHORT_HORIZON = "short-horizon"
    LONG_HORIZON = "long-horizon"
    AZUREAI = "azureai"

    def visit(
        self,
        timegpt1: typing.Callable[[], T_Result],
        timegpt1long_horizon: typing.Callable[[], T_Result],
        short_horizon: typing.Callable[[], T_Result],
        long_horizon: typing.Callable[[], T_Result],
        azureai: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MultiSeriesForecastModel.TIMEGPT1:
            return timegpt1()
        if self is MultiSeriesForecastModel.TIMEGPT1LONG_HORIZON:
            return timegpt1long_horizon()
        if self is MultiSeriesForecastModel.SHORT_HORIZON:
            return short_horizon()
        if self is MultiSeriesForecastModel.LONG_HORIZON:
            return long_horizon()
        if self is MultiSeriesForecastModel.AZUREAI:
            return azureai()
