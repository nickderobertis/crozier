

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.unprocessable_entity_error import UnprocessableEntityError
from .types.http_validation_error import HttpValidationError
from .types.multi_series_anomaly_model import MultiSeriesAnomalyModel
from .types.multi_series_cross_validation_fewshot_loss import MultiSeriesCrossValidationFewshotLoss
from .types.multi_series_cross_validation_finetune_loss import MultiSeriesCrossValidationFinetuneLoss
from .types.multi_series_cross_validation_model import MultiSeriesCrossValidationModel
from .types.multi_series_forecast_fewshot_loss import MultiSeriesForecastFewshotLoss
from .types.multi_series_forecast_finetune_loss import MultiSeriesForecastFinetuneLoss
from .types.multi_series_forecast_model import MultiSeriesForecastModel
from .types.multi_series_input import MultiSeriesInput
from .types.multi_series_insample_forecast_model import MultiSeriesInsampleForecastModel
from .types.single_series_forecast_fewshot_loss import SingleSeriesForecastFewshotLoss
from .types.single_series_forecast_finetune_loss import SingleSeriesForecastFinetuneLoss
from .types.single_series_forecast_model import SingleSeriesForecastModel
from .types.single_series_insample_forecast_model import SingleSeriesInsampleForecastModel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def validate_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "validate_token",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def validate_token_front(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "validate_token_front",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def health_health_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Check if server is healthy. Used by the readiness probe to check server is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def forecast(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        This endpoint predicts the future values of a single time series based on the provided data. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "forecast",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def historic_forecast(
        self,
        *,
        model: typing.Optional[SingleSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Any] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts time series data for the in-sample period (historical period). It takes a JSON as an input, including information like the series frequency and the historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[SingleSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Any]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "historic_forecast",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def forecast_multi_series(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the future values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for each series based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "forecast_multi_series",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def historic_forecast_multi_series(
        self,
        *,
        model: typing.Optional[MultiSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the in-sample period (historical period) values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "historic_forecast_multi_series",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def anomaly_detection_multi_series(
        self,
        *,
        model: typing.Optional[MultiSeriesAnomalyModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint detects the anomalies in the historical perdiod of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains a flag indicating if the date has a anomaly and also provides the prediction interval used to define if an observation is an anomaly.Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesAnomalyModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            Specifies the confidence level for the prediction interval used in anomaly detection. It is represented as a percentage between 0 and 100. For instance, a level of 95 indicates that the generated prediction interval captures the true future observation 95% of the time. Any observed values outside of this interval would be considered anomalies. A higher level leads to wider prediction intervals and potentially fewer detected anomalies, whereas a lower level results in narrower intervals and potentially more detected anomalies. Default: 99.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "anomaly_detection_multi_series",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cross_validation_multi_series(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesCrossValidationFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesCrossValidationModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        n_windows: typing.Optional[int] = OMIT,
        step_size: typing.Optional[int] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesCrossValidationFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Perform Cross Validation for multiple series

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesCrossValidationFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesCrossValidationModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        n_windows : typing.Optional[int]
            Number of windows to evaluate.

        step_size : typing.Optional[int]
            Step size between each cross validation window. If None it will be equal to the forecasting horizon.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesCrossValidationFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "cross_validation_multi_series",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "n_windows": n_windows,
                "step_size": step_size,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def model_input_size(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "model_input_size",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def model_params(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "model_params",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        This endpoint predicts the future values of a single time series based on the provided data. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt_historic(
        self,
        *,
        model: typing.Optional[SingleSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Any] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts time series data for the in-sample period (historical period). It takes a JSON as an input, including information like the series frequency and the historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[SingleSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Any]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt_historic",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt_multi_series(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the future values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for each series based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt_multi_series",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt_multi_series_historic(
        self,
        *,
        model: typing.Optional[MultiSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the in-sample period (historical period) values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt_multi_series_historic",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt_multi_series_anomalies(
        self,
        *,
        model: typing.Optional[MultiSeriesAnomalyModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint detects the anomalies in the historical perdiod of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains a flag indicating if the date has a anomaly and also provides the prediction interval used to define if an observation is an anomaly.Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesAnomalyModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            Specifies the confidence level for the prediction interval used in anomaly detection. It is represented as a percentage between 0 and 100. For instance, a level of 95 indicates that the generated prediction interval captures the true future observation 95% of the time. Any observed values outside of this interval would be considered anomalies. A higher level leads to wider prediction intervals and potentially fewer detected anomalies, whereas a lower level results in narrower intervals and potentially more detected anomalies. Default: 99.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt_multi_series_anomalies",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt_multi_series_cross_validation(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesCrossValidationFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesCrossValidationModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        n_windows: typing.Optional[int] = OMIT,
        step_size: typing.Optional[int] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesCrossValidationFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Perform Cross Validation for multiple series

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesCrossValidationFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesCrossValidationModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        n_windows : typing.Optional[int]
            Number of windows to evaluate.

        step_size : typing.Optional[int]
            Step size between each cross validation window. If None it will be equal to the forecasting horizon.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesCrossValidationFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt_multi_series_cross_validation",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "n_windows": n_windows,
                "step_size": step_size,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt_input_size(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt_input_size",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def timegpt_model_params(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timegpt_model_params",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def validate_token(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validate_token",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def validate_token_front(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validate_token_front",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def health_health_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Check if server is healthy. Used by the readiness probe to check server is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def forecast(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This endpoint predicts the future values of a single time series based on the provided data. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "forecast",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def historic_forecast(
        self,
        *,
        model: typing.Optional[SingleSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Any] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts time series data for the in-sample period (historical period). It takes a JSON as an input, including information like the series frequency and the historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[SingleSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Any]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "historic_forecast",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def forecast_multi_series(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the future values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for each series based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "forecast_multi_series",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def historic_forecast_multi_series(
        self,
        *,
        model: typing.Optional[MultiSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the in-sample period (historical period) values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "historic_forecast_multi_series",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def anomaly_detection_multi_series(
        self,
        *,
        model: typing.Optional[MultiSeriesAnomalyModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint detects the anomalies in the historical perdiod of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains a flag indicating if the date has a anomaly and also provides the prediction interval used to define if an observation is an anomaly.Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesAnomalyModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            Specifies the confidence level for the prediction interval used in anomaly detection. It is represented as a percentage between 0 and 100. For instance, a level of 95 indicates that the generated prediction interval captures the true future observation 95% of the time. Any observed values outside of this interval would be considered anomalies. A higher level leads to wider prediction intervals and potentially fewer detected anomalies, whereas a lower level results in narrower intervals and potentially more detected anomalies. Default: 99.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "anomaly_detection_multi_series",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cross_validation_multi_series(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesCrossValidationFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesCrossValidationModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        n_windows: typing.Optional[int] = OMIT,
        step_size: typing.Optional[int] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesCrossValidationFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Perform Cross Validation for multiple series

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesCrossValidationFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesCrossValidationModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        n_windows : typing.Optional[int]
            Number of windows to evaluate.

        step_size : typing.Optional[int]
            Step size between each cross validation window. If None it will be equal to the forecasting horizon.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesCrossValidationFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "cross_validation_multi_series",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "n_windows": n_windows,
                "step_size": step_size,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def model_input_size(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "model_input_size",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def model_params(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "model_params",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This endpoint predicts the future values of a single time series based on the provided data. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt_historic(
        self,
        *,
        model: typing.Optional[SingleSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Any] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts time series data for the in-sample period (historical period). It takes a JSON as an input, including information like the series frequency and the historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[SingleSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Any]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt_historic",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt_multi_series(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the future values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for each series based on the input arguments. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt_multi_series",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt_multi_series_historic(
        self,
        *,
        model: typing.Optional[MultiSeriesInsampleForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint predicts the in-sample period (historical period) values of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains the predicted values for the historical period. Usually useful for anomaly detection. Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesInsampleForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt_multi_series_historic",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt_multi_series_anomalies(
        self,
        *,
        model: typing.Optional[MultiSeriesAnomalyModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Based on the provided data, this endpoint detects the anomalies in the historical perdiod of multiple time series at once. It takes a JSON as an input containing information like the series frequency and historical data. (See below for a full description of the parameters.) The response contains a flag indicating if the date has a anomaly and also provides the prediction interval used to define if an observation is an anomaly.Get your token for private beta at https://dashboard.nixtla.io.

        Parameters
        ----------
        model : typing.Optional[MultiSeriesAnomalyModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            Specifies the confidence level for the prediction interval used in anomaly detection. It is represented as a percentage between 0 and 100. For instance, a level of 95 indicates that the generated prediction interval captures the true future observation 95% of the time. Any observed values outside of this interval would be considered anomalies. A higher level leads to wider prediction intervals and potentially fewer detected anomalies, whereas a lower level results in narrower intervals and potentially more detected anomalies. Default: 99.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt_multi_series_anomalies",
            method="POST",
            json={
                "model": model,
                "freq": freq,
                "level": level,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "clean_ex_first": clean_ex_first,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt_multi_series_cross_validation(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[MultiSeriesCrossValidationFewshotLoss] = OMIT,
        model: typing.Optional[MultiSeriesCrossValidationModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[MultiSeriesInput] = OMIT,
        n_windows: typing.Optional[int] = OMIT,
        step_size: typing.Optional[int] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[MultiSeriesCrossValidationFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Perform Cross Validation for multiple series

        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[MultiSeriesCrossValidationFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[MultiSeriesCrossValidationModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "y"], "data": [["ts_0", "2021-01-01", 0.7], ["ts_0", "2021-01-02", 0.8]}.

        x : typing.Optional[MultiSeriesInput]
            The exogenous  variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.

        n_windows : typing.Optional[int]
            Number of windows to evaluate.

        step_size : typing.Optional[int]
            Step size between each cross validation window. If None it will be equal to the forecasting horizon.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[MultiSeriesCrossValidationFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt_multi_series_cross_validation",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": convert_and_respect_annotation_metadata(object_=x, annotation=MultiSeriesInput, direction="write"),
                "n_windows": n_windows,
                "step_size": step_size,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt_input_size(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt_input_size",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def timegpt_model_params(
        self,
        *,
        fewshot_steps: typing.Optional[int] = OMIT,
        fewshot_loss: typing.Optional[SingleSeriesForecastFewshotLoss] = OMIT,
        model: typing.Optional[SingleSeriesForecastModel] = OMIT,
        freq: typing.Optional[str] = OMIT,
        level: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        fh: typing.Optional[int] = OMIT,
        y: typing.Optional[typing.Any] = OMIT,
        x: typing.Optional[typing.Dict[str, typing.Sequence[float]]] = OMIT,
        clean_ex_first: typing.Optional[bool] = OMIT,
        finetune_steps: typing.Optional[int] = OMIT,
        finetune_loss: typing.Optional[SingleSeriesForecastFinetuneLoss] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        fewshot_steps : typing.Optional[int]
            Deprecated. Please use finetune_steps instead.

        fewshot_loss : typing.Optional[SingleSeriesForecastFewshotLoss]
            Deprecated. Please use finetune_loss instead.

        model : typing.Optional[SingleSeriesForecastModel]
            Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.

        freq : typing.Optional[str]
            The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.

        level : typing.Optional[typing.Sequence[typing.Any]]
            A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.

        fh : typing.Optional[int]
            The forecasting horizon. This represents the number of time steps into the future that the forecast should predict.

        y : typing.Optional[typing.Any]
            The historical time series data provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is the observation at that time point. For example: {"2021-01-01": 0.1, "2021-01-02": 0.4}.

        x : typing.Optional[typing.Dict[str, typing.Sequence[float]]]
            The exogenous variables provided as a dictionary. Each key is a timestamp (string format: YYYY-MM-DD) and the corresponding value is a list of exogenous variable values at that time point. For example: {"2021-01-01": [0.1], "2021-01-02": [0.4]}. This should also include forecasting horizon (fh) additional timestamps to calculate the future values.

        clean_ex_first : typing.Optional[bool]
            A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.

        finetune_steps : typing.Optional[int]
            The number of tuning steps used to train the large time model on the data. Set this value to 0 for zero-shot inference, i.e., to make predictions without any further model tuning.

        finetune_loss : typing.Optional[SingleSeriesForecastFinetuneLoss]
            The loss used to train the large time model on the data. Select from ['default', 'mae', 'mse', 'rmse', 'mape', 'smape']. It will only be used if finetune_steps larger than 0. Default is a robust loss function that is less sensitive to outliers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timegpt_model_params",
            method="POST",
            json={
                "fewshot_steps": fewshot_steps,
                "fewshot_loss": fewshot_loss,
                "model": model,
                "freq": freq,
                "level": level,
                "fh": fh,
                "y": y,
                "x": x,
                "clean_ex_first": clean_ex_first,
                "finetune_steps": finetune_steps,
                "finetune_loss": finetune_loss,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
