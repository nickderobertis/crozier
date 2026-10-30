

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultiSeriesForecastFewshotLoss(enum.StrEnum):
    """
    Deprecated. Please use finetune_loss instead.
    """

    DEFAULT = "default"
    MAE = "mae"
    MSE = "mse"
    RMSE = "rmse"
    MAPE = "mape"
    SMAPE = "smape"

    def visit(
        self,
        default: typing.Callable[[], T_Result],
        mae: typing.Callable[[], T_Result],
        mse: typing.Callable[[], T_Result],
        rmse: typing.Callable[[], T_Result],
        mape: typing.Callable[[], T_Result],
        smape: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MultiSeriesForecastFewshotLoss.DEFAULT:
            return default()
        if self is MultiSeriesForecastFewshotLoss.MAE:
            return mae()
        if self is MultiSeriesForecastFewshotLoss.MSE:
            return mse()
        if self is MultiSeriesForecastFewshotLoss.RMSE:
            return rmse()
        if self is MultiSeriesForecastFewshotLoss.MAPE:
            return mape()
        if self is MultiSeriesForecastFewshotLoss.SMAPE:
            return smape()
