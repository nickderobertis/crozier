

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .single_series_forecast_fewshot_loss import SingleSeriesForecastFewshotLoss
from .single_series_forecast_finetune_loss import SingleSeriesForecastFinetuneLoss
from .single_series_forecast_model import SingleSeriesForecastModel


class SingleSeriesForecast(UniversalBaseModel):
    fewshot_steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated. Please use finetune_steps instead.
    """

    fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = pydantic.Field(default=None)
    """
    Deprecated. Please use finetune_loss instead.
    """

    model: typing.Optional[SingleSeriesForecastModel] = pydantic.Field(default=None)
    """
    Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.
    """

    freq: typing.Optional[str] = pydantic.Field(default=None)
    """
    The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.
    """

    level: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.
    """

    fh: typing.Optional[int] = pydantic.Field(default=None)
    """
    The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.
    """

    y: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.
    """

    x: typing.Optional[typing.Dict[str, typing.List[float]]] = pydantic.Field(default=None)
    """
    The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.
    """

    clean_ex_first: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.
    """

    finetune_steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.
    """

    finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = pydantic.Field(default=None)
    """
    The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
