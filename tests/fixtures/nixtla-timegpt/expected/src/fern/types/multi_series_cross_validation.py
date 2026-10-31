

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multi_series_cross_validation_fewshot_loss import MultiSeriesCrossValidationFewshotLoss
from .multi_series_cross_validation_finetune_loss import MultiSeriesCrossValidationFinetuneLoss
from .multi_series_cross_validation_model import MultiSeriesCrossValidationModel
from .multi_series_input import MultiSeriesInput


class MultiSeriesCrossValidation(UniversalBaseModel):
    fewshot_steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated. Please use finetune_steps instead.
    """

    fewshot_loss: typing.Optional[MultiSeriesCrossValidationFewshotLoss] = pydantic.Field(default=None)
    """
    Deprecated. Please use finetune_loss instead.
    """

    model: typing.Optional[MultiSeriesCrossValidationModel] = pydantic.Field(default=None)
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
    The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.
    """

    x: typing.Optional[MultiSeriesInput] = pydantic.Field(default=None)
    """
    The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.
    """

    n_windows: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of windows to evaluate.
    """

    step_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Step size between each cross validation window. If None it will be equal to the forecasting horizon.
    """

    clean_ex_first: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.
    """

    finetune_steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.
    """

    finetune_loss: typing.Optional[MultiSeriesCrossValidationFinetuneLoss] = pydantic.Field(default=None)
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
