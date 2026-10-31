

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multi_series_anomaly_model import MultiSeriesAnomalyModel
from .multi_series_input import MultiSeriesInput


class MultiSeriesAnomaly(UniversalBaseModel):
    model: typing.Optional[MultiSeriesAnomalyModel] = pydantic.Field(default=None)
    """
    Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.
    """

    freq: typing.Optional[str] = pydantic.Field(default=None)
    """
    The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.
    """

    level: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Specifies the confidence level for the prediction interval used in anomaly detection. It is represented as a percentage between 0 and 100. For instance, a level of 95 indicates that the generated prediction interval captures the true future observation 95% of the time. Any observed values outside of this interval would be considered anomalies. A higher level leads to wider prediction intervals and potentially fewer detected anomalies, whereas a lower level results in narrower intervals and potentially more detected anomalies. Default: 99.
    """

    y: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.
    """

    x: typing.Optional[MultiSeriesInput] = pydantic.Field(default=None)
    """
    The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.
    """

    clean_ex_first: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
