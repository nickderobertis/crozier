

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
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


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    token : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def validate_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.validate_token()
        """
        _response = self._raw_client.validate_token(request_options=request_options)
        return _response.data

    def validate_token_front(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.validate_token_front()
        """
        _response = self._raw_client.validate_token_front(request_options=request_options)
        return _response.data

    def health_health_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Check if server is healthy. Used by the readiness probe to check server is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.health_health_get()
        """
        _response = self._raw_client.health_health_get(request_options=request_options)
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, SingleSeriesForecastModel

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.forecast(
            model=SingleSeriesForecastModel.TIMEGPT1,
            freq="D",
            level=[90],
            fh=7,
            y={
                "2015-12-02": 8.71177264560569,
                "2015-12-03": 8.05610965954506,
                "2015-12-04": 8.08147504013705,
                "2015-12-05": 7.45876269238096,
                "2015-12-06": 8.01400499477946,
                "2015-12-07": 8.49678638163858,
                "2015-12-08": 7.98104975966596,
                "2015-12-09": 7.77779262633883,
                "2015-12-10": 8.2602342916073,
                "2015-12-11": 7.86633892304654,
                "2015-12-12": 7.31055015853442,
                "2015-12-13": 7.71824095195932,
                "2015-12-14": 8.31947369244219,
                "2015-12-15": 8.23668532271246,
                "2015-12-16": 7.80751004221619,
                "2015-12-17": 7.59186171488993,
                "2015-12-18": 7.52886925664225,
                "2015-12-19": 7.17165682276851,
                "2015-12-20": 7.89133075766189,
                "2015-12-21": 8.36007143564403,
                "2015-12-22": 8.11042723757502,
                "2015-12-23": 7.77527584648686,
                "2015-12-24": 7.34729970074316,
                "2015-12-25": 7.30182234213793,
                "2015-12-26": 7.12044437239249,
                "2015-12-27": 8.87877607170755,
                "2015-12-28": 9.25061821847475,
                "2015-12-29": 9.24792513230345,
                "2015-12-30": 8.39140318535794,
                "2015-12-31": 8.00469951054955,
                "2016-01-01": 7.58933582317062,
                "2016-01-02": 7.82524529143177,
                "2016-01-03": 8.24931374626064,
                "2016-01-04": 9.29514097366865,
                "2016-01-05": 8.56826646160024,
                "2016-01-06": 8.35255436947459,
                "2016-01-07": 8.29579811063615,
                "2016-01-08": 8.29029259122431,
                "2016-01-09": 7.78572089653462,
                "2016-01-10": 8.28172399041139,
                "2016-01-11": 8.4707303170059,
                "2016-01-12": 8.13505390861157,
                "2016-01-13": 8.06714903991011,
            },
            x={
                "2015-12-02": [0.47914512134886633, 0.15759798422978488],
                "2015-12-03": [0.3871397019785533, 0.35449477858215317],
                "2015-12-04": [0.9056171938719492, 0.3180404540017956],
                "2015-12-05": [0.8341924745940501, 0.1345432562146388],
                "2015-12-06": [0.9345407030264767, 0.688343987845517],
                "2015-12-07": [0.48729867539182836, 0.4078489909891331],
                "2015-12-08": [0.372592361808496, 0.9657378388402957],
                "2015-12-09": [0.8246299079349072, 0.39136849723836475],
                "2015-12-10": [0.10775659682068173, 0.7158552999785821],
                "2015-12-11": [0.8714315742323742, 0.6959379478245031],
                "2015-12-12": [0.983802256917285, 0.5028086048974361],
                "2015-12-13": [0.1637276788158426, 0.010905206265749978],
                "2015-12-14": [0.02385161083272247, 0.6959627057263087],
                "2015-12-15": [0.6601897150570875, 0.33970973534268967],
                "2015-12-16": [0.050941494525972186, 0.11738703133470063],
                "2015-12-17": [0.3959302454356002, 0.8728419968758135],
                "2015-12-18": [0.5860088140443799, 0.5731410710012429],
                "2015-12-19": [0.3857084524732245, 0.7271245785381963],
                "2015-12-20": [0.37342450516631565, 0.17888199947035843],
                "2015-12-21": [0.6981516773360145, 0.6983330714339858],
                "2015-12-22": [0.08978675718655482, 0.45744085066175544],
                "2015-12-23": [0.6879810190692012, 0.7650472745914928],
                "2015-12-24": [0.3780817922426982, 0.26541942400861085],
                "2015-12-25": [0.36377456228425953, 0.631351987243267],
                "2015-12-26": [0.8858056528262828, 0.9929861335485208],
                "2015-12-27": [0.7655012724712326, 0.8089415357086998],
                "2015-12-28": [0.7802318350754168, 0.7507408790195511],
                "2015-12-29": [0.21655713897782725, 0.39237400153061963],
                "2015-12-30": [0.1424758142857997, 0.8902624055897677],
                "2015-12-31": [0.643477187971131, 0.8789182584456643],
                "2016-01-01": [0.9369855677078311, 0.609162462729402],
                "2016-01-02": [0.0002858612957059581, 0.23697970143653724],
                "2016-01-03": [0.16280370690002544, 0.5975722202856767],
                "2016-01-04": [0.49310729499396044, 0.30125004072447636],
                "2016-01-05": [0.6780776618690909, 0.06790772949375545],
                "2016-01-06": [0.14663698589706664, 0.8886978154852969],
                "2016-01-07": [0.4422143343461119, 0.9217301518957838],
                "2016-01-08": [0.5100515329575456, 0.8433884706466771],
                "2016-01-09": [0.9304379891825107, 0.7132184980129253],
                "2016-01-10": [0.7611198221207496, 0.08381565314231354],
                "2016-01-11": [0.4876994455855225, 0.6305043963566345],
                "2016-01-12": [0.3807596362774567, 0.44155005068612574],
                "2016-01-13": [0.022917032041831265, 0.8746566219855559],
                "2016-01-14": [0.06744988617005221, 0.4867830182954117],
                "2016-01-15": [0.2876166788506098, 0.34029767862172733],
                "2016-01-16": [0.03136920601698312, 0.7473159671597568],
                "2016-01-17": [0.8903106284115768, 0.6144929198235487],
                "2016-01-18": [0.7692999747639573, 0.7318695022998711],
                "2016-01-19": [0.8265506190532937, 0.8094527295780038],
                "2016-01-20": [0.9902157088998235, 0.22917399968565122],
            },
            clean_ex_first=True,
        )
        """
        _response = self._raw_client.forecast(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, SingleSeriesInsampleForecastModel

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.historic_forecast(
            model=SingleSeriesInsampleForecastModel.TIMEGPT1,
            freq="D",
            level=[90],
            y={
                "2015-12-02": 8.71177264560569,
                "2015-12-03": 8.05610965954506,
                "2015-12-04": 8.08147504013705,
                "2015-12-05": 7.45876269238096,
                "2015-12-06": 8.01400499477946,
                "2015-12-07": 8.49678638163858,
                "2015-12-08": 7.98104975966596,
                "2015-12-09": 7.77779262633883,
                "2015-12-10": 8.2602342916073,
                "2015-12-11": 7.86633892304654,
                "2015-12-12": 7.31055015853442,
                "2015-12-13": 7.71824095195932,
                "2015-12-14": 8.31947369244219,
                "2015-12-15": 8.23668532271246,
                "2015-12-16": 7.80751004221619,
                "2015-12-17": 7.59186171488993,
                "2015-12-18": 7.52886925664225,
                "2015-12-19": 7.17165682276851,
                "2015-12-20": 7.89133075766189,
                "2015-12-21": 8.36007143564403,
                "2015-12-22": 8.11042723757502,
                "2015-12-23": 7.77527584648686,
                "2015-12-24": 7.34729970074316,
                "2015-12-25": 7.30182234213793,
                "2015-12-26": 7.12044437239249,
                "2015-12-27": 8.87877607170755,
                "2015-12-28": 9.25061821847475,
                "2015-12-29": 9.24792513230345,
                "2015-12-30": 8.39140318535794,
                "2015-12-31": 8.00469951054955,
                "2016-01-01": 7.58933582317062,
                "2016-01-02": 7.82524529143177,
                "2016-01-03": 8.24931374626064,
                "2016-01-04": 9.29514097366865,
                "2016-01-05": 8.56826646160024,
                "2016-01-06": 8.35255436947459,
                "2016-01-07": 8.29579811063615,
                "2016-01-08": 8.29029259122431,
                "2016-01-09": 7.78572089653462,
                "2016-01-10": 8.28172399041139,
                "2016-01-11": 8.4707303170059,
                "2016-01-12": 8.13505390861157,
                "2016-01-13": 8.06714903991011,
            },
            clean_ex_first=True,
        )
        """
        _response = self._raw_client.historic_forecast(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.forecast_multi_series()
        """
        _response = self._raw_client.forecast_multi_series(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, MultiSeriesInsampleForecastModel

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.historic_forecast_multi_series(
            model=MultiSeriesInsampleForecastModel.TIMEGPT1,
            freq="D",
            level=[90],
            y={
                "columns": ["unique_id", "ds", "y"],
                "data": [
                    ["PeytonManning", "2015-12-02", 8.71177264560569],
                    ["PeytonManning", "2015-12-03", 8.05610965954506],
                    ["PeytonManning", "2015-12-04", 8.08147504013705],
                    ["PeytonManning", "2015-12-05", 7.45876269238096],
                    ["PeytonManning", "2015-12-06", 8.01400499477946],
                    ["PeytonManning", "2015-12-07", 8.49678638163858],
                    ["PeytonManning", "2015-12-08", 7.98104975966596],
                    ["PeytonManning", "2015-12-09", 7.77779262633883],
                    ["PeytonManning", "2015-12-10", 8.2602342916073],
                    ["PeytonManning", "2015-12-11", 7.86633892304654],
                    ["PeytonManning", "2015-12-12", 7.31055015853442],
                    ["PeytonManning", "2015-12-13", 7.71824095195932],
                    ["PeytonManning", "2015-12-14", 8.31947369244219],
                    ["PeytonManning", "2015-12-15", 8.23668532271246],
                    ["PeytonManning", "2015-12-16", 7.80751004221619],
                    ["PeytonManning", "2015-12-17", 7.59186171488993],
                    ["PeytonManning", "2015-12-18", 7.52886925664225],
                    ["PeytonManning", "2015-12-19", 7.17165682276851],
                    ["PeytonManning", "2015-12-20", 7.89133075766189],
                    ["PeytonManning", "2015-12-21", 8.36007143564403],
                    ["PeytonManning", "2015-12-22", 8.11042723757502],
                    ["PeytonManning", "2015-12-23", 7.77527584648686],
                    ["PeytonManning", "2015-12-24", 7.34729970074316],
                    ["PeytonManning", "2015-12-25", 7.30182234213793],
                    ["PeytonManning", "2015-12-26", 7.12044437239249],
                    ["PeytonManning", "2015-12-27", 8.87877607170755],
                    ["PeytonManning", "2015-12-28", 9.25061821847475],
                    ["PeytonManning", "2015-12-29", 9.24792513230345],
                    ["PeytonManning", "2015-12-30", 8.39140318535794],
                    ["PeytonManning", "2015-12-31", 8.00469951054955],
                    ["PeytonManning", "2016-01-01", 7.58933582317062],
                    ["PeytonManning", "2016-01-02", 7.82524529143177],
                    ["PeytonManning", "2016-01-03", 8.24931374626064],
                    ["PeytonManning", "2016-01-04", 9.29514097366865],
                    ["PeytonManning", "2016-01-05", 8.56826646160024],
                    ["PeytonManning", "2016-01-06", 8.35255436947459],
                    ["PeytonManning", "2016-01-07", 8.29579811063615],
                    ["PeytonManning", "2016-01-08", 8.29029259122431],
                    ["PeytonManning", "2016-01-09", 7.78572089653462],
                    ["PeytonManning", "2016-01-10", 8.28172399041139],
                    ["PeytonManning", "2016-01-11", 8.4707303170059],
                    ["PeytonManning", "2016-01-12", 8.13505390861157],
                    ["PeytonManning", "2016-01-13", 8.06714903991011],
                    ["TomBrady", "2015-12-02", 8.71177264560569],
                    ["TomBrady", "2015-12-03", 8.05610965954506],
                    ["TomBrady", "2015-12-04", 8.08147504013705],
                    ["TomBrady", "2015-12-05", 7.45876269238096],
                    ["TomBrady", "2015-12-06", 8.01400499477946],
                    ["TomBrady", "2015-12-07", 8.49678638163858],
                    ["TomBrady", "2015-12-08", 7.98104975966596],
                    ["TomBrady", "2015-12-09", 7.77779262633883],
                    ["TomBrady", "2015-12-10", 8.2602342916073],
                    ["TomBrady", "2015-12-11", 7.86633892304654],
                    ["TomBrady", "2015-12-12", 7.31055015853442],
                    ["TomBrady", "2015-12-13", 7.71824095195932],
                    ["TomBrady", "2015-12-14", 8.31947369244219],
                    ["TomBrady", "2015-12-15", 8.23668532271246],
                    ["TomBrady", "2015-12-16", 7.80751004221619],
                    ["TomBrady", "2015-12-17", 7.59186171488993],
                    ["TomBrady", "2015-12-18", 7.52886925664225],
                    ["TomBrady", "2015-12-19", 7.17165682276851],
                    ["TomBrady", "2015-12-20", 7.89133075766189],
                    ["TomBrady", "2015-12-21", 8.36007143564403],
                    ["TomBrady", "2015-12-22", 8.11042723757502],
                    ["TomBrady", "2015-12-23", 7.77527584648686],
                    ["TomBrady", "2015-12-24", 7.34729970074316],
                    ["TomBrady", "2015-12-25", 7.30182234213793],
                    ["TomBrady", "2015-12-26", 7.12044437239249],
                    ["TomBrady", "2015-12-27", 8.87877607170755],
                    ["TomBrady", "2015-12-28", 9.25061821847475],
                    ["TomBrady", "2015-12-29", 9.24792513230345],
                    ["TomBrady", "2015-12-30", 8.39140318535794],
                    ["TomBrady", "2015-12-31", 8.00469951054955],
                    ["TomBrady", "2016-01-01", 7.58933582317062],
                    ["TomBrady", "2016-01-02", 7.82524529143177],
                    ["TomBrady", "2016-01-03", 8.24931374626064],
                    ["TomBrady", "2016-01-04", 9.29514097366865],
                    ["TomBrady", "2016-01-05", 8.56826646160024],
                    ["TomBrady", "2016-01-06", 8.35255436947459],
                    ["TomBrady", "2016-01-07", 8.29579811063615],
                    ["TomBrady", "2016-01-08", 8.29029259122431],
                    ["TomBrady", "2016-01-09", 7.78572089653462],
                    ["TomBrady", "2016-01-10", 8.28172399041139],
                    ["TomBrady", "2016-01-11", 8.4707303170059],
                    ["TomBrady", "2016-01-12", 8.13505390861157],
                    ["TomBrady", "2016-01-13", 8.06714903991011],
                ],
            },
        )
        """
        _response = self._raw_client.historic_forecast_multi_series(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.anomaly_detection_multi_series()
        """
        _response = self._raw_client.anomaly_detection_multi_series(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, MultiSeriesCrossValidationModel, MultiSeriesInput

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cross_validation_multi_series(
            model=MultiSeriesCrossValidationModel.TIMEGPT1,
            freq="D",
            level=[99],
            y={
                "columns": ["unique_id", "ds", "y"],
                "data": [
                    ["PeytonManning", "2015-12-02", 8.71177264560569],
                    ["PeytonManning", "2015-12-03", 8.05610965954506],
                    ["PeytonManning", "2015-12-04", 8.08147504013705],
                    ["PeytonManning", "2015-12-05", 7.45876269238096],
                    ["PeytonManning", "2015-12-06", 8.01400499477946],
                    ["PeytonManning", "2015-12-07", 8.49678638163858],
                    ["PeytonManning", "2015-12-08", 7.98104975966596],
                    ["PeytonManning", "2015-12-09", 7.77779262633883],
                    ["PeytonManning", "2015-12-10", 8.2602342916073],
                    ["PeytonManning", "2015-12-11", 7.86633892304654],
                    ["PeytonManning", "2015-12-12", 7.31055015853442],
                    ["PeytonManning", "2015-12-13", 7.71824095195932],
                    ["PeytonManning", "2015-12-14", 8.31947369244219],
                    ["PeytonManning", "2015-12-15", 8.23668532271246],
                    ["PeytonManning", "2015-12-16", 7.80751004221619],
                    ["PeytonManning", "2015-12-17", 7.59186171488993],
                    ["PeytonManning", "2015-12-18", 7.52886925664225],
                    ["PeytonManning", "2015-12-19", 7.17165682276851],
                    ["PeytonManning", "2015-12-20", 7.89133075766189],
                    ["PeytonManning", "2015-12-21", 8.36007143564403],
                    ["PeytonManning", "2015-12-22", 8.11042723757502],
                    ["PeytonManning", "2015-12-23", 7.77527584648686],
                    ["PeytonManning", "2015-12-24", 7.34729970074316],
                    ["PeytonManning", "2015-12-25", 7.30182234213793],
                    ["PeytonManning", "2015-12-26", 7.12044437239249],
                    ["PeytonManning", "2015-12-27", 8.87877607170755],
                    ["PeytonManning", "2015-12-28", 9.25061821847475],
                    ["PeytonManning", "2015-12-29", 9.24792513230345],
                    ["PeytonManning", "2015-12-30", 8.39140318535794],
                    ["PeytonManning", "2015-12-31", 8.00469951054955],
                    ["PeytonManning", "2016-01-01", 7.58933582317062],
                    ["PeytonManning", "2016-01-02", 7.82524529143177],
                    ["PeytonManning", "2016-01-03", 8.24931374626064],
                    ["PeytonManning", "2016-01-04", 9.29514097366865],
                    ["PeytonManning", "2016-01-05", 8.56826646160024],
                    ["PeytonManning", "2016-01-06", 8.35255436947459],
                    ["PeytonManning", "2016-01-07", 8.29579811063615],
                    ["PeytonManning", "2016-01-08", 8.29029259122431],
                    ["PeytonManning", "2016-01-09", 7.78572089653462],
                    ["PeytonManning", "2016-01-10", 8.28172399041139],
                    ["PeytonManning", "2016-01-11", 8.4707303170059],
                    ["PeytonManning", "2016-01-12", 8.13505390861157],
                    ["PeytonManning", "2016-01-13", 8.06714903991011],
                    ["TomBrady", "2015-12-02", 8.71177264560569],
                    ["TomBrady", "2015-12-03", 8.05610965954506],
                    ["TomBrady", "2015-12-04", 8.08147504013705],
                    ["TomBrady", "2015-12-05", 7.45876269238096],
                    ["TomBrady", "2015-12-06", 8.01400499477946],
                    ["TomBrady", "2015-12-07", 8.49678638163858],
                    ["TomBrady", "2015-12-08", 7.98104975966596],
                    ["TomBrady", "2015-12-09", 7.77779262633883],
                    ["TomBrady", "2015-12-10", 8.2602342916073],
                    ["TomBrady", "2015-12-11", 7.86633892304654],
                    ["TomBrady", "2015-12-12", 7.31055015853442],
                    ["TomBrady", "2015-12-13", 7.71824095195932],
                    ["TomBrady", "2015-12-14", 8.31947369244219],
                    ["TomBrady", "2015-12-15", 8.23668532271246],
                    ["TomBrady", "2015-12-16", 7.80751004221619],
                    ["TomBrady", "2015-12-17", 7.59186171488993],
                    ["TomBrady", "2015-12-18", 7.52886925664225],
                    ["TomBrady", "2015-12-19", 7.17165682276851],
                    ["TomBrady", "2015-12-20", 7.89133075766189],
                    ["TomBrady", "2015-12-21", 8.36007143564403],
                    ["TomBrady", "2015-12-22", 8.11042723757502],
                    ["TomBrady", "2015-12-23", 7.77527584648686],
                    ["TomBrady", "2015-12-24", 7.34729970074316],
                    ["TomBrady", "2015-12-25", 7.30182234213793],
                    ["TomBrady", "2015-12-26", 7.12044437239249],
                    ["TomBrady", "2015-12-27", 8.87877607170755],
                    ["TomBrady", "2015-12-28", 9.25061821847475],
                    ["TomBrady", "2015-12-29", 9.24792513230345],
                    ["TomBrady", "2015-12-30", 8.39140318535794],
                    ["TomBrady", "2015-12-31", 8.00469951054955],
                    ["TomBrady", "2016-01-01", 7.58933582317062],
                    ["TomBrady", "2016-01-02", 7.82524529143177],
                    ["TomBrady", "2016-01-03", 8.24931374626064],
                    ["TomBrady", "2016-01-04", 9.29514097366865],
                    ["TomBrady", "2016-01-05", 8.56826646160024],
                    ["TomBrady", "2016-01-06", 8.35255436947459],
                    ["TomBrady", "2016-01-07", 8.29579811063615],
                    ["TomBrady", "2016-01-08", 8.29029259122431],
                    ["TomBrady", "2016-01-09", 7.78572089653462],
                    ["TomBrady", "2016-01-10", 8.28172399041139],
                    ["TomBrady", "2016-01-11", 8.4707303170059],
                    ["TomBrady", "2016-01-12", 8.13505390861157],
                    ["TomBrady", "2016-01-13", 8.06714903991011],
                ],
            },
            x=MultiSeriesInput(
                columns=[
                    "unique_id",
                    "ds",
                    "normalized_fb_marketing_spend",
                    "normalized_google_marketing_spend",
                ],
                data=[
                    [
                        "PeytonManning",
                        "2015-12-02",
                        0.11477860928915096,
                        0.5844987825930846,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-03",
                        0.33533486335091345,
                        0.35513740030391416,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-04",
                        0.17530305631523613,
                        0.7727084723706166,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-05",
                        0.8299454704953892,
                        0.367618075472813,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-06",
                        0.15521852990872909,
                        0.3003195772529532,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-07",
                        0.14306595403784284,
                        0.7070431427763944,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-08",
                        0.19385462445583268,
                        0.3548795168204949,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-09",
                        0.13255788839340688,
                        0.17898066409986724,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-10",
                        0.1861402159494574,
                        0.7109080209067455,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-11",
                        0.6416719826327762,
                        0.029753630490418792,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-12",
                        0.07255444629238816,
                        0.29036094427412484,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-13",
                        0.5908563921496247,
                        0.4391612122175276,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-14",
                        0.4564108681832745,
                        0.36666762551686216,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-15",
                        0.5842063222179616,
                        0.7725253746268812,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-16",
                        0.7032064831874294,
                        0.011741920837716524,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-17",
                        0.1819442499802637,
                        0.024847038984041947,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-18",
                        0.0236088273599101,
                        0.6750163977742368,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-19",
                        0.05606508858414727,
                        0.7476944076745794,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-20",
                        0.23105144001754685,
                        0.0975599293231374,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-21",
                        0.046529460623970675,
                        0.27870858983273483,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-22",
                        0.8924837450040128,
                        0.17445021431427998,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-23",
                        0.7920741814997206,
                        0.7697260533294017,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-24",
                        0.8211104441803947,
                        0.04784956766271531,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-25",
                        0.007443038001649138,
                        0.14607178743713456,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-26",
                        0.007103558258280018,
                        0.9906539418801805,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-27",
                        0.6056133597337183,
                        0.3016989995056749,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-28",
                        0.888562531622971,
                        0.2644957566378502,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-29",
                        0.6596339635369193,
                        0.7132049526406711,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-30",
                        0.28384590920981123,
                        0.33014709090685734,
                    ],
                    [
                        "PeytonManning",
                        "2015-12-31",
                        0.8909381460163546,
                        0.30893091621071356,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-01",
                        0.40276798240151035,
                        0.2879315229860593,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-02",
                        0.4429162268378485,
                        0.11018732403878562,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-03",
                        0.3828367947132504,
                        0.8222282482537393,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-04",
                        0.058573708628411714,
                        0.0882973927279318,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-05",
                        0.47488775903843816,
                        0.6966251353738419,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-06",
                        0.5977462692254242,
                        0.047135156470394235,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-07",
                        0.3717147185460784,
                        0.8692903226725259,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-08",
                        0.9309630632764513,
                        0.9735989812217806,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-09",
                        0.16911221748337524,
                        0.8789858343082052,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-10",
                        0.27006313791342074,
                        0.11164112580033247,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-11",
                        0.7963113076957269,
                        0.20769916997452176,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-12",
                        0.6303426283630738,
                        0.18090725407449992,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-13",
                        0.8493379197928459,
                        0.47689004776049004,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-14",
                        0.23526591138844477,
                        0.8789956293235727,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-15",
                        0.007675903871696255,
                        0.43933947505823356,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-16",
                        0.47352555302489163,
                        0.2152806277171031,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-17",
                        0.15708565708379674,
                        0.3691423619421067,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-18",
                        0.1455797785998202,
                        0.12414992893989352,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-19",
                        0.18260071049899873,
                        0.4700149101718504,
                    ],
                    [
                        "PeytonManning",
                        "2016-01-20",
                        0.815333051511914,
                        0.6872087681704713,
                    ],
                    ["TomBrady", "2015-12-02", 0.11477860928915096, 0.5844987825930846],
                    [
                        "TomBrady",
                        "2015-12-03",
                        0.33533486335091345,
                        0.35513740030391416,
                    ],
                    ["TomBrady", "2015-12-04", 0.17530305631523613, 0.7727084723706166],
                    ["TomBrady", "2015-12-05", 0.8299454704953892, 0.367618075472813],
                    ["TomBrady", "2015-12-06", 0.15521852990872909, 0.3003195772529532],
                    ["TomBrady", "2015-12-07", 0.14306595403784284, 0.7070431427763944],
                    ["TomBrady", "2015-12-08", 0.19385462445583268, 0.3548795168204949],
                    [
                        "TomBrady",
                        "2015-12-09",
                        0.13255788839340688,
                        0.17898066409986724,
                    ],
                    ["TomBrady", "2015-12-10", 0.1861402159494574, 0.7109080209067455],
                    [
                        "TomBrady",
                        "2015-12-11",
                        0.6416719826327762,
                        0.029753630490418792,
                    ],
                    [
                        "TomBrady",
                        "2015-12-12",
                        0.07255444629238816,
                        0.29036094427412484,
                    ],
                    ["TomBrady", "2015-12-13", 0.5908563921496247, 0.4391612122175276],
                    ["TomBrady", "2015-12-14", 0.4564108681832745, 0.36666762551686216],
                    ["TomBrady", "2015-12-15", 0.5842063222179616, 0.7725253746268812],
                    [
                        "TomBrady",
                        "2015-12-16",
                        0.7032064831874294,
                        0.011741920837716524,
                    ],
                    [
                        "TomBrady",
                        "2015-12-17",
                        0.1819442499802637,
                        0.024847038984041947,
                    ],
                    ["TomBrady", "2015-12-18", 0.0236088273599101, 0.6750163977742368],
                    ["TomBrady", "2015-12-19", 0.05606508858414727, 0.7476944076745794],
                    ["TomBrady", "2015-12-20", 0.23105144001754685, 0.0975599293231374],
                    [
                        "TomBrady",
                        "2015-12-21",
                        0.046529460623970675,
                        0.27870858983273483,
                    ],
                    ["TomBrady", "2015-12-22", 0.8924837450040128, 0.17445021431427998],
                    ["TomBrady", "2015-12-23", 0.7920741814997206, 0.7697260533294017],
                    ["TomBrady", "2015-12-24", 0.8211104441803947, 0.04784956766271531],
                    [
                        "TomBrady",
                        "2015-12-25",
                        0.007443038001649138,
                        0.14607178743713456,
                    ],
                    [
                        "TomBrady",
                        "2015-12-26",
                        0.007103558258280018,
                        0.9906539418801805,
                    ],
                    ["TomBrady", "2015-12-27", 0.6056133597337183, 0.3016989995056749],
                    ["TomBrady", "2015-12-28", 0.888562531622971, 0.2644957566378502],
                    ["TomBrady", "2015-12-29", 0.6596339635369193, 0.7132049526406711],
                    [
                        "TomBrady",
                        "2015-12-30",
                        0.28384590920981123,
                        0.33014709090685734,
                    ],
                    ["TomBrady", "2015-12-31", 0.8909381460163546, 0.30893091621071356],
                    ["TomBrady", "2016-01-01", 0.40276798240151035, 0.2879315229860593],
                    ["TomBrady", "2016-01-02", 0.4429162268378485, 0.11018732403878562],
                    ["TomBrady", "2016-01-03", 0.3828367947132504, 0.8222282482537393],
                    [
                        "TomBrady",
                        "2016-01-04",
                        0.058573708628411714,
                        0.0882973927279318,
                    ],
                    ["TomBrady", "2016-01-05", 0.47488775903843816, 0.6966251353738419],
                    [
                        "TomBrady",
                        "2016-01-06",
                        0.5977462692254242,
                        0.047135156470394235,
                    ],
                    ["TomBrady", "2016-01-07", 0.3717147185460784, 0.8692903226725259],
                    ["TomBrady", "2016-01-08", 0.9309630632764513, 0.9735989812217806],
                    ["TomBrady", "2016-01-09", 0.16911221748337524, 0.8789858343082052],
                    [
                        "TomBrady",
                        "2016-01-10",
                        0.27006313791342074,
                        0.11164112580033247,
                    ],
                    ["TomBrady", "2016-01-11", 0.7963113076957269, 0.20769916997452176],
                    ["TomBrady", "2016-01-12", 0.6303426283630738, 0.18090725407449992],
                    ["TomBrady", "2016-01-13", 0.8493379197928459, 0.47689004776049004],
                    ["TomBrady", "2016-01-14", 0.23526591138844477, 0.8789956293235727],
                    [
                        "TomBrady",
                        "2016-01-15",
                        0.007675903871696255,
                        0.43933947505823356,
                    ],
                    ["TomBrady", "2016-01-16", 0.47352555302489163, 0.2152806277171031],
                    ["TomBrady", "2016-01-17", 0.15708565708379674, 0.3691423619421067],
                    ["TomBrady", "2016-01-18", 0.1455797785998202, 0.12414992893989352],
                    ["TomBrady", "2016-01-19", 0.18260071049899873, 0.4700149101718504],
                    ["TomBrady", "2016-01-20", 0.815333051511914, 0.6872087681704713],
                ],
            ),
        )
        """
        _response = self._raw_client.cross_validation_multi_series(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            n_windows=n_windows,
            step_size=step_size,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_input_size()
        """
        _response = self._raw_client.model_input_size(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_params()
        """
        _response = self._raw_client.model_params(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, SingleSeriesForecastModel

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt(
            model=SingleSeriesForecastModel.TIMEGPT1,
            freq="D",
            level=[90],
            fh=7,
            y={
                "2015-12-02": 8.71177264560569,
                "2015-12-03": 8.05610965954506,
                "2015-12-04": 8.08147504013705,
                "2015-12-05": 7.45876269238096,
                "2015-12-06": 8.01400499477946,
                "2015-12-07": 8.49678638163858,
                "2015-12-08": 7.98104975966596,
                "2015-12-09": 7.77779262633883,
                "2015-12-10": 8.2602342916073,
                "2015-12-11": 7.86633892304654,
                "2015-12-12": 7.31055015853442,
                "2015-12-13": 7.71824095195932,
                "2015-12-14": 8.31947369244219,
                "2015-12-15": 8.23668532271246,
                "2015-12-16": 7.80751004221619,
                "2015-12-17": 7.59186171488993,
                "2015-12-18": 7.52886925664225,
                "2015-12-19": 7.17165682276851,
                "2015-12-20": 7.89133075766189,
                "2015-12-21": 8.36007143564403,
                "2015-12-22": 8.11042723757502,
                "2015-12-23": 7.77527584648686,
                "2015-12-24": 7.34729970074316,
                "2015-12-25": 7.30182234213793,
                "2015-12-26": 7.12044437239249,
                "2015-12-27": 8.87877607170755,
                "2015-12-28": 9.25061821847475,
                "2015-12-29": 9.24792513230345,
                "2015-12-30": 8.39140318535794,
                "2015-12-31": 8.00469951054955,
                "2016-01-01": 7.58933582317062,
                "2016-01-02": 7.82524529143177,
                "2016-01-03": 8.24931374626064,
                "2016-01-04": 9.29514097366865,
                "2016-01-05": 8.56826646160024,
                "2016-01-06": 8.35255436947459,
                "2016-01-07": 8.29579811063615,
                "2016-01-08": 8.29029259122431,
                "2016-01-09": 7.78572089653462,
                "2016-01-10": 8.28172399041139,
                "2016-01-11": 8.4707303170059,
                "2016-01-12": 8.13505390861157,
                "2016-01-13": 8.06714903991011,
            },
            x={
                "2015-12-02": [0.09323074669638598, 0.6368254238538134],
                "2015-12-03": [0.3112324026372236, 0.6889811850504678],
                "2015-12-04": [0.481377116596614, 0.9499072761820243],
                "2015-12-05": [0.828714746663481, 0.8041572577576312],
                "2015-12-06": [0.9057716575675051, 0.9704840572309358],
                "2015-12-07": [0.11973559067683959, 0.5511723211494531],
                "2015-12-08": [0.7606320950967038, 0.6502204496427739],
                "2015-12-09": [0.6674402019606482, 0.5371174184068592],
                "2015-12-10": [0.6309756549373285, 0.5962737337684483],
                "2015-12-11": [0.43906877315373927, 0.1654105249520328],
                "2015-12-12": [0.04035053656768495, 0.015327409476712961],
                "2015-12-13": [0.24377685055222176, 0.8627561902830486],
                "2015-12-14": [0.4681463148103986, 0.7889604220806076],
                "2015-12-15": [0.08345764193688965, 0.1003789877662995],
                "2015-12-16": [0.4771178995736667, 0.4958892103475401],
                "2015-12-17": [0.3486535805107692, 0.1148378356945654],
                "2015-12-18": [0.6630786017711142, 0.3849924472769859],
                "2015-12-19": [0.011778418994099704, 0.5115520644698133],
                "2015-12-20": [0.9038837166773512, 0.8848353753020387],
                "2015-12-21": [0.7843282827835409, 0.3103093475671188],
                "2015-12-22": [0.25362104487399484, 0.9254139777164822],
                "2015-12-23": [0.30107456907444907, 0.33020953364803796],
                "2015-12-24": [0.027255284501599086, 0.9447565679813503],
                "2015-12-25": [0.40549024123597277, 0.9460884659190596],
                "2015-12-26": [0.5016171568983224, 0.7067171277571931],
                "2015-12-27": [0.827190957653689, 0.4005053404479477],
                "2015-12-28": [0.2596591659030716, 0.47506589627248297],
                "2015-12-29": [0.49720915846888825, 0.6751702910147392],
                "2015-12-30": [0.6674937132903789, 0.9931963725210304],
                "2015-12-31": [0.9291459144099821, 0.43747139612392505],
                "2016-01-01": [0.9582822834991531, 0.04487218641374102],
                "2016-01-02": [0.029270976123749515, 0.23398035651852978],
                "2016-01-03": [0.515109021575783, 0.808477728186397],
                "2016-01-04": [0.5435684835160831, 0.07870797706843025],
                "2016-01-05": [0.7621319274444724, 0.8516085958801328],
                "2016-01-06": [0.26156943890310125, 0.5111017026367417],
                "2016-01-07": [0.0564861467325366, 0.12697067125791017],
                "2016-01-08": [0.37440546078742454, 0.2012358008441526],
                "2016-01-09": [0.29688542060907375, 0.43556021285702873],
                "2016-01-10": [0.9898730907589448, 0.7713248129524874],
                "2016-01-11": [0.49238285777903246, 0.7197147811618813],
                "2016-01-12": [0.8318652201289694, 0.6091414491883265],
                "2016-01-13": [0.02343720965025453, 0.7961211448973647],
                "2016-01-14": [0.7633021263247786, 0.018469346610634263],
                "2016-01-15": [0.493855721362772, 0.7451084649371831],
                "2016-01-16": [0.21962262556226464, 0.9274272764531087],
                "2016-01-17": [0.885379459035442, 0.3507870357790486],
                "2016-01-18": [0.6460546060324733, 0.8225983771798888],
                "2016-01-19": [0.3604601800609517, 0.4588944740666544],
                "2016-01-20": [0.4191777260908942, 0.2500836388909915],
            },
            clean_ex_first=True,
        )
        """
        _response = self._raw_client.timegpt(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, SingleSeriesInsampleForecastModel

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt_historic(
            model=SingleSeriesInsampleForecastModel.TIMEGPT1,
            freq="D",
            level=[90],
            y={
                "2015-12-02": 8.71177264560569,
                "2015-12-03": 8.05610965954506,
                "2015-12-04": 8.08147504013705,
                "2015-12-05": 7.45876269238096,
                "2015-12-06": 8.01400499477946,
                "2015-12-07": 8.49678638163858,
                "2015-12-08": 7.98104975966596,
                "2015-12-09": 7.77779262633883,
                "2015-12-10": 8.2602342916073,
                "2015-12-11": 7.86633892304654,
                "2015-12-12": 7.31055015853442,
                "2015-12-13": 7.71824095195932,
                "2015-12-14": 8.31947369244219,
                "2015-12-15": 8.23668532271246,
                "2015-12-16": 7.80751004221619,
                "2015-12-17": 7.59186171488993,
                "2015-12-18": 7.52886925664225,
                "2015-12-19": 7.17165682276851,
                "2015-12-20": 7.89133075766189,
                "2015-12-21": 8.36007143564403,
                "2015-12-22": 8.11042723757502,
                "2015-12-23": 7.77527584648686,
                "2015-12-24": 7.34729970074316,
                "2015-12-25": 7.30182234213793,
                "2015-12-26": 7.12044437239249,
                "2015-12-27": 8.87877607170755,
                "2015-12-28": 9.25061821847475,
                "2015-12-29": 9.24792513230345,
                "2015-12-30": 8.39140318535794,
                "2015-12-31": 8.00469951054955,
                "2016-01-01": 7.58933582317062,
                "2016-01-02": 7.82524529143177,
                "2016-01-03": 8.24931374626064,
                "2016-01-04": 9.29514097366865,
                "2016-01-05": 8.56826646160024,
                "2016-01-06": 8.35255436947459,
                "2016-01-07": 8.29579811063615,
                "2016-01-08": 8.29029259122431,
                "2016-01-09": 7.78572089653462,
                "2016-01-10": 8.28172399041139,
                "2016-01-11": 8.4707303170059,
                "2016-01-12": 8.13505390861157,
                "2016-01-13": 8.06714903991011,
            },
            clean_ex_first=True,
        )
        """
        _response = self._raw_client.timegpt_historic(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt_multi_series()
        """
        _response = self._raw_client.timegpt_multi_series(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, MultiSeriesInsampleForecastModel

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt_multi_series_historic(
            model=MultiSeriesInsampleForecastModel.TIMEGPT1,
            freq="D",
            level=[90],
            y={
                "columns": ["unique_id", "ds", "y"],
                "data": [
                    ["PeytonManning", "2015-12-02", 8.71177264560569],
                    ["PeytonManning", "2015-12-03", 8.05610965954506],
                    ["PeytonManning", "2015-12-04", 8.08147504013705],
                    ["PeytonManning", "2015-12-05", 7.45876269238096],
                    ["PeytonManning", "2015-12-06", 8.01400499477946],
                    ["PeytonManning", "2015-12-07", 8.49678638163858],
                    ["PeytonManning", "2015-12-08", 7.98104975966596],
                    ["PeytonManning", "2015-12-09", 7.77779262633883],
                    ["PeytonManning", "2015-12-10", 8.2602342916073],
                    ["PeytonManning", "2015-12-11", 7.86633892304654],
                    ["PeytonManning", "2015-12-12", 7.31055015853442],
                    ["PeytonManning", "2015-12-13", 7.71824095195932],
                    ["PeytonManning", "2015-12-14", 8.31947369244219],
                    ["PeytonManning", "2015-12-15", 8.23668532271246],
                    ["PeytonManning", "2015-12-16", 7.80751004221619],
                    ["PeytonManning", "2015-12-17", 7.59186171488993],
                    ["PeytonManning", "2015-12-18", 7.52886925664225],
                    ["PeytonManning", "2015-12-19", 7.17165682276851],
                    ["PeytonManning", "2015-12-20", 7.89133075766189],
                    ["PeytonManning", "2015-12-21", 8.36007143564403],
                    ["PeytonManning", "2015-12-22", 8.11042723757502],
                    ["PeytonManning", "2015-12-23", 7.77527584648686],
                    ["PeytonManning", "2015-12-24", 7.34729970074316],
                    ["PeytonManning", "2015-12-25", 7.30182234213793],
                    ["PeytonManning", "2015-12-26", 7.12044437239249],
                    ["PeytonManning", "2015-12-27", 8.87877607170755],
                    ["PeytonManning", "2015-12-28", 9.25061821847475],
                    ["PeytonManning", "2015-12-29", 9.24792513230345],
                    ["PeytonManning", "2015-12-30", 8.39140318535794],
                    ["PeytonManning", "2015-12-31", 8.00469951054955],
                    ["PeytonManning", "2016-01-01", 7.58933582317062],
                    ["PeytonManning", "2016-01-02", 7.82524529143177],
                    ["PeytonManning", "2016-01-03", 8.24931374626064],
                    ["PeytonManning", "2016-01-04", 9.29514097366865],
                    ["PeytonManning", "2016-01-05", 8.56826646160024],
                    ["PeytonManning", "2016-01-06", 8.35255436947459],
                    ["PeytonManning", "2016-01-07", 8.29579811063615],
                    ["PeytonManning", "2016-01-08", 8.29029259122431],
                    ["PeytonManning", "2016-01-09", 7.78572089653462],
                    ["PeytonManning", "2016-01-10", 8.28172399041139],
                    ["PeytonManning", "2016-01-11", 8.4707303170059],
                    ["PeytonManning", "2016-01-12", 8.13505390861157],
                    ["PeytonManning", "2016-01-13", 8.06714903991011],
                    ["TomBrady", "2015-12-02", 8.71177264560569],
                    ["TomBrady", "2015-12-03", 8.05610965954506],
                    ["TomBrady", "2015-12-04", 8.08147504013705],
                    ["TomBrady", "2015-12-05", 7.45876269238096],
                    ["TomBrady", "2015-12-06", 8.01400499477946],
                    ["TomBrady", "2015-12-07", 8.49678638163858],
                    ["TomBrady", "2015-12-08", 7.98104975966596],
                    ["TomBrady", "2015-12-09", 7.77779262633883],
                    ["TomBrady", "2015-12-10", 8.2602342916073],
                    ["TomBrady", "2015-12-11", 7.86633892304654],
                    ["TomBrady", "2015-12-12", 7.31055015853442],
                    ["TomBrady", "2015-12-13", 7.71824095195932],
                    ["TomBrady", "2015-12-14", 8.31947369244219],
                    ["TomBrady", "2015-12-15", 8.23668532271246],
                    ["TomBrady", "2015-12-16", 7.80751004221619],
                    ["TomBrady", "2015-12-17", 7.59186171488993],
                    ["TomBrady", "2015-12-18", 7.52886925664225],
                    ["TomBrady", "2015-12-19", 7.17165682276851],
                    ["TomBrady", "2015-12-20", 7.89133075766189],
                    ["TomBrady", "2015-12-21", 8.36007143564403],
                    ["TomBrady", "2015-12-22", 8.11042723757502],
                    ["TomBrady", "2015-12-23", 7.77527584648686],
                    ["TomBrady", "2015-12-24", 7.34729970074316],
                    ["TomBrady", "2015-12-25", 7.30182234213793],
                    ["TomBrady", "2015-12-26", 7.12044437239249],
                    ["TomBrady", "2015-12-27", 8.87877607170755],
                    ["TomBrady", "2015-12-28", 9.25061821847475],
                    ["TomBrady", "2015-12-29", 9.24792513230345],
                    ["TomBrady", "2015-12-30", 8.39140318535794],
                    ["TomBrady", "2015-12-31", 8.00469951054955],
                    ["TomBrady", "2016-01-01", 7.58933582317062],
                    ["TomBrady", "2016-01-02", 7.82524529143177],
                    ["TomBrady", "2016-01-03", 8.24931374626064],
                    ["TomBrady", "2016-01-04", 9.29514097366865],
                    ["TomBrady", "2016-01-05", 8.56826646160024],
                    ["TomBrady", "2016-01-06", 8.35255436947459],
                    ["TomBrady", "2016-01-07", 8.29579811063615],
                    ["TomBrady", "2016-01-08", 8.29029259122431],
                    ["TomBrady", "2016-01-09", 7.78572089653462],
                    ["TomBrady", "2016-01-10", 8.28172399041139],
                    ["TomBrady", "2016-01-11", 8.4707303170059],
                    ["TomBrady", "2016-01-12", 8.13505390861157],
                    ["TomBrady", "2016-01-13", 8.06714903991011],
                ],
            },
        )
        """
        _response = self._raw_client.timegpt_multi_series_historic(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt_multi_series_anomalies()
        """
        _response = self._raw_client.timegpt_multi_series_anomalies(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt_multi_series_cross_validation()
        """
        _response = self._raw_client.timegpt_multi_series_cross_validation(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            n_windows=n_windows,
            step_size=step_size,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt_input_size()
        """
        _response = self._raw_client.timegpt_input_size(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.timegpt_model_params()
        """
        _response = self._raw_client.timegpt_model_params(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    token : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def validate_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.validate_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_token(request_options=request_options)
        return _response.data

    async def validate_token_front(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.validate_token_front()


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_token_front(request_options=request_options)
        return _response.data

    async def health_health_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Check if server is healthy. Used by the readiness probe to check server is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health_health_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_health_get(request_options=request_options)
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SingleSeriesForecastModel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.forecast(
                model=SingleSeriesForecastModel.TIMEGPT1,
                freq="D",
                level=[90],
                fh=7,
                y={
                    "2015-12-02": 8.71177264560569,
                    "2015-12-03": 8.05610965954506,
                    "2015-12-04": 8.08147504013705,
                    "2015-12-05": 7.45876269238096,
                    "2015-12-06": 8.01400499477946,
                    "2015-12-07": 8.49678638163858,
                    "2015-12-08": 7.98104975966596,
                    "2015-12-09": 7.77779262633883,
                    "2015-12-10": 8.2602342916073,
                    "2015-12-11": 7.86633892304654,
                    "2015-12-12": 7.31055015853442,
                    "2015-12-13": 7.71824095195932,
                    "2015-12-14": 8.31947369244219,
                    "2015-12-15": 8.23668532271246,
                    "2015-12-16": 7.80751004221619,
                    "2015-12-17": 7.59186171488993,
                    "2015-12-18": 7.52886925664225,
                    "2015-12-19": 7.17165682276851,
                    "2015-12-20": 7.89133075766189,
                    "2015-12-21": 8.36007143564403,
                    "2015-12-22": 8.11042723757502,
                    "2015-12-23": 7.77527584648686,
                    "2015-12-24": 7.34729970074316,
                    "2015-12-25": 7.30182234213793,
                    "2015-12-26": 7.12044437239249,
                    "2015-12-27": 8.87877607170755,
                    "2015-12-28": 9.25061821847475,
                    "2015-12-29": 9.24792513230345,
                    "2015-12-30": 8.39140318535794,
                    "2015-12-31": 8.00469951054955,
                    "2016-01-01": 7.58933582317062,
                    "2016-01-02": 7.82524529143177,
                    "2016-01-03": 8.24931374626064,
                    "2016-01-04": 9.29514097366865,
                    "2016-01-05": 8.56826646160024,
                    "2016-01-06": 8.35255436947459,
                    "2016-01-07": 8.29579811063615,
                    "2016-01-08": 8.29029259122431,
                    "2016-01-09": 7.78572089653462,
                    "2016-01-10": 8.28172399041139,
                    "2016-01-11": 8.4707303170059,
                    "2016-01-12": 8.13505390861157,
                    "2016-01-13": 8.06714903991011,
                },
                x={
                    "2015-12-02": [0.47914512134886633, 0.15759798422978488],
                    "2015-12-03": [0.3871397019785533, 0.35449477858215317],
                    "2015-12-04": [0.9056171938719492, 0.3180404540017956],
                    "2015-12-05": [0.8341924745940501, 0.1345432562146388],
                    "2015-12-06": [0.9345407030264767, 0.688343987845517],
                    "2015-12-07": [0.48729867539182836, 0.4078489909891331],
                    "2015-12-08": [0.372592361808496, 0.9657378388402957],
                    "2015-12-09": [0.8246299079349072, 0.39136849723836475],
                    "2015-12-10": [0.10775659682068173, 0.7158552999785821],
                    "2015-12-11": [0.8714315742323742, 0.6959379478245031],
                    "2015-12-12": [0.983802256917285, 0.5028086048974361],
                    "2015-12-13": [0.1637276788158426, 0.010905206265749978],
                    "2015-12-14": [0.02385161083272247, 0.6959627057263087],
                    "2015-12-15": [0.6601897150570875, 0.33970973534268967],
                    "2015-12-16": [0.050941494525972186, 0.11738703133470063],
                    "2015-12-17": [0.3959302454356002, 0.8728419968758135],
                    "2015-12-18": [0.5860088140443799, 0.5731410710012429],
                    "2015-12-19": [0.3857084524732245, 0.7271245785381963],
                    "2015-12-20": [0.37342450516631565, 0.17888199947035843],
                    "2015-12-21": [0.6981516773360145, 0.6983330714339858],
                    "2015-12-22": [0.08978675718655482, 0.45744085066175544],
                    "2015-12-23": [0.6879810190692012, 0.7650472745914928],
                    "2015-12-24": [0.3780817922426982, 0.26541942400861085],
                    "2015-12-25": [0.36377456228425953, 0.631351987243267],
                    "2015-12-26": [0.8858056528262828, 0.9929861335485208],
                    "2015-12-27": [0.7655012724712326, 0.8089415357086998],
                    "2015-12-28": [0.7802318350754168, 0.7507408790195511],
                    "2015-12-29": [0.21655713897782725, 0.39237400153061963],
                    "2015-12-30": [0.1424758142857997, 0.8902624055897677],
                    "2015-12-31": [0.643477187971131, 0.8789182584456643],
                    "2016-01-01": [0.9369855677078311, 0.609162462729402],
                    "2016-01-02": [0.0002858612957059581, 0.23697970143653724],
                    "2016-01-03": [0.16280370690002544, 0.5975722202856767],
                    "2016-01-04": [0.49310729499396044, 0.30125004072447636],
                    "2016-01-05": [0.6780776618690909, 0.06790772949375545],
                    "2016-01-06": [0.14663698589706664, 0.8886978154852969],
                    "2016-01-07": [0.4422143343461119, 0.9217301518957838],
                    "2016-01-08": [0.5100515329575456, 0.8433884706466771],
                    "2016-01-09": [0.9304379891825107, 0.7132184980129253],
                    "2016-01-10": [0.7611198221207496, 0.08381565314231354],
                    "2016-01-11": [0.4876994455855225, 0.6305043963566345],
                    "2016-01-12": [0.3807596362774567, 0.44155005068612574],
                    "2016-01-13": [0.022917032041831265, 0.8746566219855559],
                    "2016-01-14": [0.06744988617005221, 0.4867830182954117],
                    "2016-01-15": [0.2876166788506098, 0.34029767862172733],
                    "2016-01-16": [0.03136920601698312, 0.7473159671597568],
                    "2016-01-17": [0.8903106284115768, 0.6144929198235487],
                    "2016-01-18": [0.7692999747639573, 0.7318695022998711],
                    "2016-01-19": [0.8265506190532937, 0.8094527295780038],
                    "2016-01-20": [0.9902157088998235, 0.22917399968565122],
                },
                clean_ex_first=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.forecast(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SingleSeriesInsampleForecastModel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.historic_forecast(
                model=SingleSeriesInsampleForecastModel.TIMEGPT1,
                freq="D",
                level=[90],
                y={
                    "2015-12-02": 8.71177264560569,
                    "2015-12-03": 8.05610965954506,
                    "2015-12-04": 8.08147504013705,
                    "2015-12-05": 7.45876269238096,
                    "2015-12-06": 8.01400499477946,
                    "2015-12-07": 8.49678638163858,
                    "2015-12-08": 7.98104975966596,
                    "2015-12-09": 7.77779262633883,
                    "2015-12-10": 8.2602342916073,
                    "2015-12-11": 7.86633892304654,
                    "2015-12-12": 7.31055015853442,
                    "2015-12-13": 7.71824095195932,
                    "2015-12-14": 8.31947369244219,
                    "2015-12-15": 8.23668532271246,
                    "2015-12-16": 7.80751004221619,
                    "2015-12-17": 7.59186171488993,
                    "2015-12-18": 7.52886925664225,
                    "2015-12-19": 7.17165682276851,
                    "2015-12-20": 7.89133075766189,
                    "2015-12-21": 8.36007143564403,
                    "2015-12-22": 8.11042723757502,
                    "2015-12-23": 7.77527584648686,
                    "2015-12-24": 7.34729970074316,
                    "2015-12-25": 7.30182234213793,
                    "2015-12-26": 7.12044437239249,
                    "2015-12-27": 8.87877607170755,
                    "2015-12-28": 9.25061821847475,
                    "2015-12-29": 9.24792513230345,
                    "2015-12-30": 8.39140318535794,
                    "2015-12-31": 8.00469951054955,
                    "2016-01-01": 7.58933582317062,
                    "2016-01-02": 7.82524529143177,
                    "2016-01-03": 8.24931374626064,
                    "2016-01-04": 9.29514097366865,
                    "2016-01-05": 8.56826646160024,
                    "2016-01-06": 8.35255436947459,
                    "2016-01-07": 8.29579811063615,
                    "2016-01-08": 8.29029259122431,
                    "2016-01-09": 7.78572089653462,
                    "2016-01-10": 8.28172399041139,
                    "2016-01-11": 8.4707303170059,
                    "2016-01-12": 8.13505390861157,
                    "2016-01-13": 8.06714903991011,
                },
                clean_ex_first=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.historic_forecast(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.forecast_multi_series()


        asyncio.run(main())
        """
        _response = await self._raw_client.forecast_multi_series(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MultiSeriesInsampleForecastModel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.historic_forecast_multi_series(
                model=MultiSeriesInsampleForecastModel.TIMEGPT1,
                freq="D",
                level=[90],
                y={
                    "columns": ["unique_id", "ds", "y"],
                    "data": [
                        ["PeytonManning", "2015-12-02", 8.71177264560569],
                        ["PeytonManning", "2015-12-03", 8.05610965954506],
                        ["PeytonManning", "2015-12-04", 8.08147504013705],
                        ["PeytonManning", "2015-12-05", 7.45876269238096],
                        ["PeytonManning", "2015-12-06", 8.01400499477946],
                        ["PeytonManning", "2015-12-07", 8.49678638163858],
                        ["PeytonManning", "2015-12-08", 7.98104975966596],
                        ["PeytonManning", "2015-12-09", 7.77779262633883],
                        ["PeytonManning", "2015-12-10", 8.2602342916073],
                        ["PeytonManning", "2015-12-11", 7.86633892304654],
                        ["PeytonManning", "2015-12-12", 7.31055015853442],
                        ["PeytonManning", "2015-12-13", 7.71824095195932],
                        ["PeytonManning", "2015-12-14", 8.31947369244219],
                        ["PeytonManning", "2015-12-15", 8.23668532271246],
                        ["PeytonManning", "2015-12-16", 7.80751004221619],
                        ["PeytonManning", "2015-12-17", 7.59186171488993],
                        ["PeytonManning", "2015-12-18", 7.52886925664225],
                        ["PeytonManning", "2015-12-19", 7.17165682276851],
                        ["PeytonManning", "2015-12-20", 7.89133075766189],
                        ["PeytonManning", "2015-12-21", 8.36007143564403],
                        ["PeytonManning", "2015-12-22", 8.11042723757502],
                        ["PeytonManning", "2015-12-23", 7.77527584648686],
                        ["PeytonManning", "2015-12-24", 7.34729970074316],
                        ["PeytonManning", "2015-12-25", 7.30182234213793],
                        ["PeytonManning", "2015-12-26", 7.12044437239249],
                        ["PeytonManning", "2015-12-27", 8.87877607170755],
                        ["PeytonManning", "2015-12-28", 9.25061821847475],
                        ["PeytonManning", "2015-12-29", 9.24792513230345],
                        ["PeytonManning", "2015-12-30", 8.39140318535794],
                        ["PeytonManning", "2015-12-31", 8.00469951054955],
                        ["PeytonManning", "2016-01-01", 7.58933582317062],
                        ["PeytonManning", "2016-01-02", 7.82524529143177],
                        ["PeytonManning", "2016-01-03", 8.24931374626064],
                        ["PeytonManning", "2016-01-04", 9.29514097366865],
                        ["PeytonManning", "2016-01-05", 8.56826646160024],
                        ["PeytonManning", "2016-01-06", 8.35255436947459],
                        ["PeytonManning", "2016-01-07", 8.29579811063615],
                        ["PeytonManning", "2016-01-08", 8.29029259122431],
                        ["PeytonManning", "2016-01-09", 7.78572089653462],
                        ["PeytonManning", "2016-01-10", 8.28172399041139],
                        ["PeytonManning", "2016-01-11", 8.4707303170059],
                        ["PeytonManning", "2016-01-12", 8.13505390861157],
                        ["PeytonManning", "2016-01-13", 8.06714903991011],
                        ["TomBrady", "2015-12-02", 8.71177264560569],
                        ["TomBrady", "2015-12-03", 8.05610965954506],
                        ["TomBrady", "2015-12-04", 8.08147504013705],
                        ["TomBrady", "2015-12-05", 7.45876269238096],
                        ["TomBrady", "2015-12-06", 8.01400499477946],
                        ["TomBrady", "2015-12-07", 8.49678638163858],
                        ["TomBrady", "2015-12-08", 7.98104975966596],
                        ["TomBrady", "2015-12-09", 7.77779262633883],
                        ["TomBrady", "2015-12-10", 8.2602342916073],
                        ["TomBrady", "2015-12-11", 7.86633892304654],
                        ["TomBrady", "2015-12-12", 7.31055015853442],
                        ["TomBrady", "2015-12-13", 7.71824095195932],
                        ["TomBrady", "2015-12-14", 8.31947369244219],
                        ["TomBrady", "2015-12-15", 8.23668532271246],
                        ["TomBrady", "2015-12-16", 7.80751004221619],
                        ["TomBrady", "2015-12-17", 7.59186171488993],
                        ["TomBrady", "2015-12-18", 7.52886925664225],
                        ["TomBrady", "2015-12-19", 7.17165682276851],
                        ["TomBrady", "2015-12-20", 7.89133075766189],
                        ["TomBrady", "2015-12-21", 8.36007143564403],
                        ["TomBrady", "2015-12-22", 8.11042723757502],
                        ["TomBrady", "2015-12-23", 7.77527584648686],
                        ["TomBrady", "2015-12-24", 7.34729970074316],
                        ["TomBrady", "2015-12-25", 7.30182234213793],
                        ["TomBrady", "2015-12-26", 7.12044437239249],
                        ["TomBrady", "2015-12-27", 8.87877607170755],
                        ["TomBrady", "2015-12-28", 9.25061821847475],
                        ["TomBrady", "2015-12-29", 9.24792513230345],
                        ["TomBrady", "2015-12-30", 8.39140318535794],
                        ["TomBrady", "2015-12-31", 8.00469951054955],
                        ["TomBrady", "2016-01-01", 7.58933582317062],
                        ["TomBrady", "2016-01-02", 7.82524529143177],
                        ["TomBrady", "2016-01-03", 8.24931374626064],
                        ["TomBrady", "2016-01-04", 9.29514097366865],
                        ["TomBrady", "2016-01-05", 8.56826646160024],
                        ["TomBrady", "2016-01-06", 8.35255436947459],
                        ["TomBrady", "2016-01-07", 8.29579811063615],
                        ["TomBrady", "2016-01-08", 8.29029259122431],
                        ["TomBrady", "2016-01-09", 7.78572089653462],
                        ["TomBrady", "2016-01-10", 8.28172399041139],
                        ["TomBrady", "2016-01-11", 8.4707303170059],
                        ["TomBrady", "2016-01-12", 8.13505390861157],
                        ["TomBrady", "2016-01-13", 8.06714903991011],
                    ],
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.historic_forecast_multi_series(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.anomaly_detection_multi_series()


        asyncio.run(main())
        """
        _response = await self._raw_client.anomaly_detection_multi_series(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MultiSeriesCrossValidationModel, MultiSeriesInput

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cross_validation_multi_series(
                model=MultiSeriesCrossValidationModel.TIMEGPT1,
                freq="D",
                level=[99],
                y={
                    "columns": ["unique_id", "ds", "y"],
                    "data": [
                        ["PeytonManning", "2015-12-02", 8.71177264560569],
                        ["PeytonManning", "2015-12-03", 8.05610965954506],
                        ["PeytonManning", "2015-12-04", 8.08147504013705],
                        ["PeytonManning", "2015-12-05", 7.45876269238096],
                        ["PeytonManning", "2015-12-06", 8.01400499477946],
                        ["PeytonManning", "2015-12-07", 8.49678638163858],
                        ["PeytonManning", "2015-12-08", 7.98104975966596],
                        ["PeytonManning", "2015-12-09", 7.77779262633883],
                        ["PeytonManning", "2015-12-10", 8.2602342916073],
                        ["PeytonManning", "2015-12-11", 7.86633892304654],
                        ["PeytonManning", "2015-12-12", 7.31055015853442],
                        ["PeytonManning", "2015-12-13", 7.71824095195932],
                        ["PeytonManning", "2015-12-14", 8.31947369244219],
                        ["PeytonManning", "2015-12-15", 8.23668532271246],
                        ["PeytonManning", "2015-12-16", 7.80751004221619],
                        ["PeytonManning", "2015-12-17", 7.59186171488993],
                        ["PeytonManning", "2015-12-18", 7.52886925664225],
                        ["PeytonManning", "2015-12-19", 7.17165682276851],
                        ["PeytonManning", "2015-12-20", 7.89133075766189],
                        ["PeytonManning", "2015-12-21", 8.36007143564403],
                        ["PeytonManning", "2015-12-22", 8.11042723757502],
                        ["PeytonManning", "2015-12-23", 7.77527584648686],
                        ["PeytonManning", "2015-12-24", 7.34729970074316],
                        ["PeytonManning", "2015-12-25", 7.30182234213793],
                        ["PeytonManning", "2015-12-26", 7.12044437239249],
                        ["PeytonManning", "2015-12-27", 8.87877607170755],
                        ["PeytonManning", "2015-12-28", 9.25061821847475],
                        ["PeytonManning", "2015-12-29", 9.24792513230345],
                        ["PeytonManning", "2015-12-30", 8.39140318535794],
                        ["PeytonManning", "2015-12-31", 8.00469951054955],
                        ["PeytonManning", "2016-01-01", 7.58933582317062],
                        ["PeytonManning", "2016-01-02", 7.82524529143177],
                        ["PeytonManning", "2016-01-03", 8.24931374626064],
                        ["PeytonManning", "2016-01-04", 9.29514097366865],
                        ["PeytonManning", "2016-01-05", 8.56826646160024],
                        ["PeytonManning", "2016-01-06", 8.35255436947459],
                        ["PeytonManning", "2016-01-07", 8.29579811063615],
                        ["PeytonManning", "2016-01-08", 8.29029259122431],
                        ["PeytonManning", "2016-01-09", 7.78572089653462],
                        ["PeytonManning", "2016-01-10", 8.28172399041139],
                        ["PeytonManning", "2016-01-11", 8.4707303170059],
                        ["PeytonManning", "2016-01-12", 8.13505390861157],
                        ["PeytonManning", "2016-01-13", 8.06714903991011],
                        ["TomBrady", "2015-12-02", 8.71177264560569],
                        ["TomBrady", "2015-12-03", 8.05610965954506],
                        ["TomBrady", "2015-12-04", 8.08147504013705],
                        ["TomBrady", "2015-12-05", 7.45876269238096],
                        ["TomBrady", "2015-12-06", 8.01400499477946],
                        ["TomBrady", "2015-12-07", 8.49678638163858],
                        ["TomBrady", "2015-12-08", 7.98104975966596],
                        ["TomBrady", "2015-12-09", 7.77779262633883],
                        ["TomBrady", "2015-12-10", 8.2602342916073],
                        ["TomBrady", "2015-12-11", 7.86633892304654],
                        ["TomBrady", "2015-12-12", 7.31055015853442],
                        ["TomBrady", "2015-12-13", 7.71824095195932],
                        ["TomBrady", "2015-12-14", 8.31947369244219],
                        ["TomBrady", "2015-12-15", 8.23668532271246],
                        ["TomBrady", "2015-12-16", 7.80751004221619],
                        ["TomBrady", "2015-12-17", 7.59186171488993],
                        ["TomBrady", "2015-12-18", 7.52886925664225],
                        ["TomBrady", "2015-12-19", 7.17165682276851],
                        ["TomBrady", "2015-12-20", 7.89133075766189],
                        ["TomBrady", "2015-12-21", 8.36007143564403],
                        ["TomBrady", "2015-12-22", 8.11042723757502],
                        ["TomBrady", "2015-12-23", 7.77527584648686],
                        ["TomBrady", "2015-12-24", 7.34729970074316],
                        ["TomBrady", "2015-12-25", 7.30182234213793],
                        ["TomBrady", "2015-12-26", 7.12044437239249],
                        ["TomBrady", "2015-12-27", 8.87877607170755],
                        ["TomBrady", "2015-12-28", 9.25061821847475],
                        ["TomBrady", "2015-12-29", 9.24792513230345],
                        ["TomBrady", "2015-12-30", 8.39140318535794],
                        ["TomBrady", "2015-12-31", 8.00469951054955],
                        ["TomBrady", "2016-01-01", 7.58933582317062],
                        ["TomBrady", "2016-01-02", 7.82524529143177],
                        ["TomBrady", "2016-01-03", 8.24931374626064],
                        ["TomBrady", "2016-01-04", 9.29514097366865],
                        ["TomBrady", "2016-01-05", 8.56826646160024],
                        ["TomBrady", "2016-01-06", 8.35255436947459],
                        ["TomBrady", "2016-01-07", 8.29579811063615],
                        ["TomBrady", "2016-01-08", 8.29029259122431],
                        ["TomBrady", "2016-01-09", 7.78572089653462],
                        ["TomBrady", "2016-01-10", 8.28172399041139],
                        ["TomBrady", "2016-01-11", 8.4707303170059],
                        ["TomBrady", "2016-01-12", 8.13505390861157],
                        ["TomBrady", "2016-01-13", 8.06714903991011],
                    ],
                },
                x=MultiSeriesInput(
                    columns=[
                        "unique_id",
                        "ds",
                        "normalized_fb_marketing_spend",
                        "normalized_google_marketing_spend",
                    ],
                    data=[
                        [
                            "PeytonManning",
                            "2015-12-02",
                            0.11477860928915096,
                            0.5844987825930846,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-03",
                            0.33533486335091345,
                            0.35513740030391416,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-04",
                            0.17530305631523613,
                            0.7727084723706166,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-05",
                            0.8299454704953892,
                            0.367618075472813,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-06",
                            0.15521852990872909,
                            0.3003195772529532,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-07",
                            0.14306595403784284,
                            0.7070431427763944,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-08",
                            0.19385462445583268,
                            0.3548795168204949,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-09",
                            0.13255788839340688,
                            0.17898066409986724,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-10",
                            0.1861402159494574,
                            0.7109080209067455,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-11",
                            0.6416719826327762,
                            0.029753630490418792,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-12",
                            0.07255444629238816,
                            0.29036094427412484,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-13",
                            0.5908563921496247,
                            0.4391612122175276,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-14",
                            0.4564108681832745,
                            0.36666762551686216,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-15",
                            0.5842063222179616,
                            0.7725253746268812,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-16",
                            0.7032064831874294,
                            0.011741920837716524,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-17",
                            0.1819442499802637,
                            0.024847038984041947,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-18",
                            0.0236088273599101,
                            0.6750163977742368,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-19",
                            0.05606508858414727,
                            0.7476944076745794,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-20",
                            0.23105144001754685,
                            0.0975599293231374,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-21",
                            0.046529460623970675,
                            0.27870858983273483,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-22",
                            0.8924837450040128,
                            0.17445021431427998,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-23",
                            0.7920741814997206,
                            0.7697260533294017,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-24",
                            0.8211104441803947,
                            0.04784956766271531,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-25",
                            0.007443038001649138,
                            0.14607178743713456,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-26",
                            0.007103558258280018,
                            0.9906539418801805,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-27",
                            0.6056133597337183,
                            0.3016989995056749,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-28",
                            0.888562531622971,
                            0.2644957566378502,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-29",
                            0.6596339635369193,
                            0.7132049526406711,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-30",
                            0.28384590920981123,
                            0.33014709090685734,
                        ],
                        [
                            "PeytonManning",
                            "2015-12-31",
                            0.8909381460163546,
                            0.30893091621071356,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-01",
                            0.40276798240151035,
                            0.2879315229860593,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-02",
                            0.4429162268378485,
                            0.11018732403878562,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-03",
                            0.3828367947132504,
                            0.8222282482537393,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-04",
                            0.058573708628411714,
                            0.0882973927279318,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-05",
                            0.47488775903843816,
                            0.6966251353738419,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-06",
                            0.5977462692254242,
                            0.047135156470394235,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-07",
                            0.3717147185460784,
                            0.8692903226725259,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-08",
                            0.9309630632764513,
                            0.9735989812217806,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-09",
                            0.16911221748337524,
                            0.8789858343082052,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-10",
                            0.27006313791342074,
                            0.11164112580033247,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-11",
                            0.7963113076957269,
                            0.20769916997452176,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-12",
                            0.6303426283630738,
                            0.18090725407449992,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-13",
                            0.8493379197928459,
                            0.47689004776049004,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-14",
                            0.23526591138844477,
                            0.8789956293235727,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-15",
                            0.007675903871696255,
                            0.43933947505823356,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-16",
                            0.47352555302489163,
                            0.2152806277171031,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-17",
                            0.15708565708379674,
                            0.3691423619421067,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-18",
                            0.1455797785998202,
                            0.12414992893989352,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-19",
                            0.18260071049899873,
                            0.4700149101718504,
                        ],
                        [
                            "PeytonManning",
                            "2016-01-20",
                            0.815333051511914,
                            0.6872087681704713,
                        ],
                        [
                            "TomBrady",
                            "2015-12-02",
                            0.11477860928915096,
                            0.5844987825930846,
                        ],
                        [
                            "TomBrady",
                            "2015-12-03",
                            0.33533486335091345,
                            0.35513740030391416,
                        ],
                        [
                            "TomBrady",
                            "2015-12-04",
                            0.17530305631523613,
                            0.7727084723706166,
                        ],
                        [
                            "TomBrady",
                            "2015-12-05",
                            0.8299454704953892,
                            0.367618075472813,
                        ],
                        [
                            "TomBrady",
                            "2015-12-06",
                            0.15521852990872909,
                            0.3003195772529532,
                        ],
                        [
                            "TomBrady",
                            "2015-12-07",
                            0.14306595403784284,
                            0.7070431427763944,
                        ],
                        [
                            "TomBrady",
                            "2015-12-08",
                            0.19385462445583268,
                            0.3548795168204949,
                        ],
                        [
                            "TomBrady",
                            "2015-12-09",
                            0.13255788839340688,
                            0.17898066409986724,
                        ],
                        [
                            "TomBrady",
                            "2015-12-10",
                            0.1861402159494574,
                            0.7109080209067455,
                        ],
                        [
                            "TomBrady",
                            "2015-12-11",
                            0.6416719826327762,
                            0.029753630490418792,
                        ],
                        [
                            "TomBrady",
                            "2015-12-12",
                            0.07255444629238816,
                            0.29036094427412484,
                        ],
                        [
                            "TomBrady",
                            "2015-12-13",
                            0.5908563921496247,
                            0.4391612122175276,
                        ],
                        [
                            "TomBrady",
                            "2015-12-14",
                            0.4564108681832745,
                            0.36666762551686216,
                        ],
                        [
                            "TomBrady",
                            "2015-12-15",
                            0.5842063222179616,
                            0.7725253746268812,
                        ],
                        [
                            "TomBrady",
                            "2015-12-16",
                            0.7032064831874294,
                            0.011741920837716524,
                        ],
                        [
                            "TomBrady",
                            "2015-12-17",
                            0.1819442499802637,
                            0.024847038984041947,
                        ],
                        [
                            "TomBrady",
                            "2015-12-18",
                            0.0236088273599101,
                            0.6750163977742368,
                        ],
                        [
                            "TomBrady",
                            "2015-12-19",
                            0.05606508858414727,
                            0.7476944076745794,
                        ],
                        [
                            "TomBrady",
                            "2015-12-20",
                            0.23105144001754685,
                            0.0975599293231374,
                        ],
                        [
                            "TomBrady",
                            "2015-12-21",
                            0.046529460623970675,
                            0.27870858983273483,
                        ],
                        [
                            "TomBrady",
                            "2015-12-22",
                            0.8924837450040128,
                            0.17445021431427998,
                        ],
                        [
                            "TomBrady",
                            "2015-12-23",
                            0.7920741814997206,
                            0.7697260533294017,
                        ],
                        [
                            "TomBrady",
                            "2015-12-24",
                            0.8211104441803947,
                            0.04784956766271531,
                        ],
                        [
                            "TomBrady",
                            "2015-12-25",
                            0.007443038001649138,
                            0.14607178743713456,
                        ],
                        [
                            "TomBrady",
                            "2015-12-26",
                            0.007103558258280018,
                            0.9906539418801805,
                        ],
                        [
                            "TomBrady",
                            "2015-12-27",
                            0.6056133597337183,
                            0.3016989995056749,
                        ],
                        [
                            "TomBrady",
                            "2015-12-28",
                            0.888562531622971,
                            0.2644957566378502,
                        ],
                        [
                            "TomBrady",
                            "2015-12-29",
                            0.6596339635369193,
                            0.7132049526406711,
                        ],
                        [
                            "TomBrady",
                            "2015-12-30",
                            0.28384590920981123,
                            0.33014709090685734,
                        ],
                        [
                            "TomBrady",
                            "2015-12-31",
                            0.8909381460163546,
                            0.30893091621071356,
                        ],
                        [
                            "TomBrady",
                            "2016-01-01",
                            0.40276798240151035,
                            0.2879315229860593,
                        ],
                        [
                            "TomBrady",
                            "2016-01-02",
                            0.4429162268378485,
                            0.11018732403878562,
                        ],
                        [
                            "TomBrady",
                            "2016-01-03",
                            0.3828367947132504,
                            0.8222282482537393,
                        ],
                        [
                            "TomBrady",
                            "2016-01-04",
                            0.058573708628411714,
                            0.0882973927279318,
                        ],
                        [
                            "TomBrady",
                            "2016-01-05",
                            0.47488775903843816,
                            0.6966251353738419,
                        ],
                        [
                            "TomBrady",
                            "2016-01-06",
                            0.5977462692254242,
                            0.047135156470394235,
                        ],
                        [
                            "TomBrady",
                            "2016-01-07",
                            0.3717147185460784,
                            0.8692903226725259,
                        ],
                        [
                            "TomBrady",
                            "2016-01-08",
                            0.9309630632764513,
                            0.9735989812217806,
                        ],
                        [
                            "TomBrady",
                            "2016-01-09",
                            0.16911221748337524,
                            0.8789858343082052,
                        ],
                        [
                            "TomBrady",
                            "2016-01-10",
                            0.27006313791342074,
                            0.11164112580033247,
                        ],
                        [
                            "TomBrady",
                            "2016-01-11",
                            0.7963113076957269,
                            0.20769916997452176,
                        ],
                        [
                            "TomBrady",
                            "2016-01-12",
                            0.6303426283630738,
                            0.18090725407449992,
                        ],
                        [
                            "TomBrady",
                            "2016-01-13",
                            0.8493379197928459,
                            0.47689004776049004,
                        ],
                        [
                            "TomBrady",
                            "2016-01-14",
                            0.23526591138844477,
                            0.8789956293235727,
                        ],
                        [
                            "TomBrady",
                            "2016-01-15",
                            0.007675903871696255,
                            0.43933947505823356,
                        ],
                        [
                            "TomBrady",
                            "2016-01-16",
                            0.47352555302489163,
                            0.2152806277171031,
                        ],
                        [
                            "TomBrady",
                            "2016-01-17",
                            0.15708565708379674,
                            0.3691423619421067,
                        ],
                        [
                            "TomBrady",
                            "2016-01-18",
                            0.1455797785998202,
                            0.12414992893989352,
                        ],
                        [
                            "TomBrady",
                            "2016-01-19",
                            0.18260071049899873,
                            0.4700149101718504,
                        ],
                        [
                            "TomBrady",
                            "2016-01-20",
                            0.815333051511914,
                            0.6872087681704713,
                        ],
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cross_validation_multi_series(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            n_windows=n_windows,
            step_size=step_size,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.model_input_size()


        asyncio.run(main())
        """
        _response = await self._raw_client.model_input_size(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.model_params()


        asyncio.run(main())
        """
        _response = await self._raw_client.model_params(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SingleSeriesForecastModel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt(
                model=SingleSeriesForecastModel.TIMEGPT1,
                freq="D",
                level=[90],
                fh=7,
                y={
                    "2015-12-02": 8.71177264560569,
                    "2015-12-03": 8.05610965954506,
                    "2015-12-04": 8.08147504013705,
                    "2015-12-05": 7.45876269238096,
                    "2015-12-06": 8.01400499477946,
                    "2015-12-07": 8.49678638163858,
                    "2015-12-08": 7.98104975966596,
                    "2015-12-09": 7.77779262633883,
                    "2015-12-10": 8.2602342916073,
                    "2015-12-11": 7.86633892304654,
                    "2015-12-12": 7.31055015853442,
                    "2015-12-13": 7.71824095195932,
                    "2015-12-14": 8.31947369244219,
                    "2015-12-15": 8.23668532271246,
                    "2015-12-16": 7.80751004221619,
                    "2015-12-17": 7.59186171488993,
                    "2015-12-18": 7.52886925664225,
                    "2015-12-19": 7.17165682276851,
                    "2015-12-20": 7.89133075766189,
                    "2015-12-21": 8.36007143564403,
                    "2015-12-22": 8.11042723757502,
                    "2015-12-23": 7.77527584648686,
                    "2015-12-24": 7.34729970074316,
                    "2015-12-25": 7.30182234213793,
                    "2015-12-26": 7.12044437239249,
                    "2015-12-27": 8.87877607170755,
                    "2015-12-28": 9.25061821847475,
                    "2015-12-29": 9.24792513230345,
                    "2015-12-30": 8.39140318535794,
                    "2015-12-31": 8.00469951054955,
                    "2016-01-01": 7.58933582317062,
                    "2016-01-02": 7.82524529143177,
                    "2016-01-03": 8.24931374626064,
                    "2016-01-04": 9.29514097366865,
                    "2016-01-05": 8.56826646160024,
                    "2016-01-06": 8.35255436947459,
                    "2016-01-07": 8.29579811063615,
                    "2016-01-08": 8.29029259122431,
                    "2016-01-09": 7.78572089653462,
                    "2016-01-10": 8.28172399041139,
                    "2016-01-11": 8.4707303170059,
                    "2016-01-12": 8.13505390861157,
                    "2016-01-13": 8.06714903991011,
                },
                x={
                    "2015-12-02": [0.09323074669638598, 0.6368254238538134],
                    "2015-12-03": [0.3112324026372236, 0.6889811850504678],
                    "2015-12-04": [0.481377116596614, 0.9499072761820243],
                    "2015-12-05": [0.828714746663481, 0.8041572577576312],
                    "2015-12-06": [0.9057716575675051, 0.9704840572309358],
                    "2015-12-07": [0.11973559067683959, 0.5511723211494531],
                    "2015-12-08": [0.7606320950967038, 0.6502204496427739],
                    "2015-12-09": [0.6674402019606482, 0.5371174184068592],
                    "2015-12-10": [0.6309756549373285, 0.5962737337684483],
                    "2015-12-11": [0.43906877315373927, 0.1654105249520328],
                    "2015-12-12": [0.04035053656768495, 0.015327409476712961],
                    "2015-12-13": [0.24377685055222176, 0.8627561902830486],
                    "2015-12-14": [0.4681463148103986, 0.7889604220806076],
                    "2015-12-15": [0.08345764193688965, 0.1003789877662995],
                    "2015-12-16": [0.4771178995736667, 0.4958892103475401],
                    "2015-12-17": [0.3486535805107692, 0.1148378356945654],
                    "2015-12-18": [0.6630786017711142, 0.3849924472769859],
                    "2015-12-19": [0.011778418994099704, 0.5115520644698133],
                    "2015-12-20": [0.9038837166773512, 0.8848353753020387],
                    "2015-12-21": [0.7843282827835409, 0.3103093475671188],
                    "2015-12-22": [0.25362104487399484, 0.9254139777164822],
                    "2015-12-23": [0.30107456907444907, 0.33020953364803796],
                    "2015-12-24": [0.027255284501599086, 0.9447565679813503],
                    "2015-12-25": [0.40549024123597277, 0.9460884659190596],
                    "2015-12-26": [0.5016171568983224, 0.7067171277571931],
                    "2015-12-27": [0.827190957653689, 0.4005053404479477],
                    "2015-12-28": [0.2596591659030716, 0.47506589627248297],
                    "2015-12-29": [0.49720915846888825, 0.6751702910147392],
                    "2015-12-30": [0.6674937132903789, 0.9931963725210304],
                    "2015-12-31": [0.9291459144099821, 0.43747139612392505],
                    "2016-01-01": [0.9582822834991531, 0.04487218641374102],
                    "2016-01-02": [0.029270976123749515, 0.23398035651852978],
                    "2016-01-03": [0.515109021575783, 0.808477728186397],
                    "2016-01-04": [0.5435684835160831, 0.07870797706843025],
                    "2016-01-05": [0.7621319274444724, 0.8516085958801328],
                    "2016-01-06": [0.26156943890310125, 0.5111017026367417],
                    "2016-01-07": [0.0564861467325366, 0.12697067125791017],
                    "2016-01-08": [0.37440546078742454, 0.2012358008441526],
                    "2016-01-09": [0.29688542060907375, 0.43556021285702873],
                    "2016-01-10": [0.9898730907589448, 0.7713248129524874],
                    "2016-01-11": [0.49238285777903246, 0.7197147811618813],
                    "2016-01-12": [0.8318652201289694, 0.6091414491883265],
                    "2016-01-13": [0.02343720965025453, 0.7961211448973647],
                    "2016-01-14": [0.7633021263247786, 0.018469346610634263],
                    "2016-01-15": [0.493855721362772, 0.7451084649371831],
                    "2016-01-16": [0.21962262556226464, 0.9274272764531087],
                    "2016-01-17": [0.885379459035442, 0.3507870357790486],
                    "2016-01-18": [0.6460546060324733, 0.8225983771798888],
                    "2016-01-19": [0.3604601800609517, 0.4588944740666544],
                    "2016-01-20": [0.4191777260908942, 0.2500836388909915],
                },
                clean_ex_first=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SingleSeriesInsampleForecastModel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt_historic(
                model=SingleSeriesInsampleForecastModel.TIMEGPT1,
                freq="D",
                level=[90],
                y={
                    "2015-12-02": 8.71177264560569,
                    "2015-12-03": 8.05610965954506,
                    "2015-12-04": 8.08147504013705,
                    "2015-12-05": 7.45876269238096,
                    "2015-12-06": 8.01400499477946,
                    "2015-12-07": 8.49678638163858,
                    "2015-12-08": 7.98104975966596,
                    "2015-12-09": 7.77779262633883,
                    "2015-12-10": 8.2602342916073,
                    "2015-12-11": 7.86633892304654,
                    "2015-12-12": 7.31055015853442,
                    "2015-12-13": 7.71824095195932,
                    "2015-12-14": 8.31947369244219,
                    "2015-12-15": 8.23668532271246,
                    "2015-12-16": 7.80751004221619,
                    "2015-12-17": 7.59186171488993,
                    "2015-12-18": 7.52886925664225,
                    "2015-12-19": 7.17165682276851,
                    "2015-12-20": 7.89133075766189,
                    "2015-12-21": 8.36007143564403,
                    "2015-12-22": 8.11042723757502,
                    "2015-12-23": 7.77527584648686,
                    "2015-12-24": 7.34729970074316,
                    "2015-12-25": 7.30182234213793,
                    "2015-12-26": 7.12044437239249,
                    "2015-12-27": 8.87877607170755,
                    "2015-12-28": 9.25061821847475,
                    "2015-12-29": 9.24792513230345,
                    "2015-12-30": 8.39140318535794,
                    "2015-12-31": 8.00469951054955,
                    "2016-01-01": 7.58933582317062,
                    "2016-01-02": 7.82524529143177,
                    "2016-01-03": 8.24931374626064,
                    "2016-01-04": 9.29514097366865,
                    "2016-01-05": 8.56826646160024,
                    "2016-01-06": 8.35255436947459,
                    "2016-01-07": 8.29579811063615,
                    "2016-01-08": 8.29029259122431,
                    "2016-01-09": 7.78572089653462,
                    "2016-01-10": 8.28172399041139,
                    "2016-01-11": 8.4707303170059,
                    "2016-01-12": 8.13505390861157,
                    "2016-01-13": 8.06714903991011,
                },
                clean_ex_first=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt_historic(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt_multi_series()


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt_multi_series(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MultiSeriesInsampleForecastModel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt_multi_series_historic(
                model=MultiSeriesInsampleForecastModel.TIMEGPT1,
                freq="D",
                level=[90],
                y={
                    "columns": ["unique_id", "ds", "y"],
                    "data": [
                        ["PeytonManning", "2015-12-02", 8.71177264560569],
                        ["PeytonManning", "2015-12-03", 8.05610965954506],
                        ["PeytonManning", "2015-12-04", 8.08147504013705],
                        ["PeytonManning", "2015-12-05", 7.45876269238096],
                        ["PeytonManning", "2015-12-06", 8.01400499477946],
                        ["PeytonManning", "2015-12-07", 8.49678638163858],
                        ["PeytonManning", "2015-12-08", 7.98104975966596],
                        ["PeytonManning", "2015-12-09", 7.77779262633883],
                        ["PeytonManning", "2015-12-10", 8.2602342916073],
                        ["PeytonManning", "2015-12-11", 7.86633892304654],
                        ["PeytonManning", "2015-12-12", 7.31055015853442],
                        ["PeytonManning", "2015-12-13", 7.71824095195932],
                        ["PeytonManning", "2015-12-14", 8.31947369244219],
                        ["PeytonManning", "2015-12-15", 8.23668532271246],
                        ["PeytonManning", "2015-12-16", 7.80751004221619],
                        ["PeytonManning", "2015-12-17", 7.59186171488993],
                        ["PeytonManning", "2015-12-18", 7.52886925664225],
                        ["PeytonManning", "2015-12-19", 7.17165682276851],
                        ["PeytonManning", "2015-12-20", 7.89133075766189],
                        ["PeytonManning", "2015-12-21", 8.36007143564403],
                        ["PeytonManning", "2015-12-22", 8.11042723757502],
                        ["PeytonManning", "2015-12-23", 7.77527584648686],
                        ["PeytonManning", "2015-12-24", 7.34729970074316],
                        ["PeytonManning", "2015-12-25", 7.30182234213793],
                        ["PeytonManning", "2015-12-26", 7.12044437239249],
                        ["PeytonManning", "2015-12-27", 8.87877607170755],
                        ["PeytonManning", "2015-12-28", 9.25061821847475],
                        ["PeytonManning", "2015-12-29", 9.24792513230345],
                        ["PeytonManning", "2015-12-30", 8.39140318535794],
                        ["PeytonManning", "2015-12-31", 8.00469951054955],
                        ["PeytonManning", "2016-01-01", 7.58933582317062],
                        ["PeytonManning", "2016-01-02", 7.82524529143177],
                        ["PeytonManning", "2016-01-03", 8.24931374626064],
                        ["PeytonManning", "2016-01-04", 9.29514097366865],
                        ["PeytonManning", "2016-01-05", 8.56826646160024],
                        ["PeytonManning", "2016-01-06", 8.35255436947459],
                        ["PeytonManning", "2016-01-07", 8.29579811063615],
                        ["PeytonManning", "2016-01-08", 8.29029259122431],
                        ["PeytonManning", "2016-01-09", 7.78572089653462],
                        ["PeytonManning", "2016-01-10", 8.28172399041139],
                        ["PeytonManning", "2016-01-11", 8.4707303170059],
                        ["PeytonManning", "2016-01-12", 8.13505390861157],
                        ["PeytonManning", "2016-01-13", 8.06714903991011],
                        ["TomBrady", "2015-12-02", 8.71177264560569],
                        ["TomBrady", "2015-12-03", 8.05610965954506],
                        ["TomBrady", "2015-12-04", 8.08147504013705],
                        ["TomBrady", "2015-12-05", 7.45876269238096],
                        ["TomBrady", "2015-12-06", 8.01400499477946],
                        ["TomBrady", "2015-12-07", 8.49678638163858],
                        ["TomBrady", "2015-12-08", 7.98104975966596],
                        ["TomBrady", "2015-12-09", 7.77779262633883],
                        ["TomBrady", "2015-12-10", 8.2602342916073],
                        ["TomBrady", "2015-12-11", 7.86633892304654],
                        ["TomBrady", "2015-12-12", 7.31055015853442],
                        ["TomBrady", "2015-12-13", 7.71824095195932],
                        ["TomBrady", "2015-12-14", 8.31947369244219],
                        ["TomBrady", "2015-12-15", 8.23668532271246],
                        ["TomBrady", "2015-12-16", 7.80751004221619],
                        ["TomBrady", "2015-12-17", 7.59186171488993],
                        ["TomBrady", "2015-12-18", 7.52886925664225],
                        ["TomBrady", "2015-12-19", 7.17165682276851],
                        ["TomBrady", "2015-12-20", 7.89133075766189],
                        ["TomBrady", "2015-12-21", 8.36007143564403],
                        ["TomBrady", "2015-12-22", 8.11042723757502],
                        ["TomBrady", "2015-12-23", 7.77527584648686],
                        ["TomBrady", "2015-12-24", 7.34729970074316],
                        ["TomBrady", "2015-12-25", 7.30182234213793],
                        ["TomBrady", "2015-12-26", 7.12044437239249],
                        ["TomBrady", "2015-12-27", 8.87877607170755],
                        ["TomBrady", "2015-12-28", 9.25061821847475],
                        ["TomBrady", "2015-12-29", 9.24792513230345],
                        ["TomBrady", "2015-12-30", 8.39140318535794],
                        ["TomBrady", "2015-12-31", 8.00469951054955],
                        ["TomBrady", "2016-01-01", 7.58933582317062],
                        ["TomBrady", "2016-01-02", 7.82524529143177],
                        ["TomBrady", "2016-01-03", 8.24931374626064],
                        ["TomBrady", "2016-01-04", 9.29514097366865],
                        ["TomBrady", "2016-01-05", 8.56826646160024],
                        ["TomBrady", "2016-01-06", 8.35255436947459],
                        ["TomBrady", "2016-01-07", 8.29579811063615],
                        ["TomBrady", "2016-01-08", 8.29029259122431],
                        ["TomBrady", "2016-01-09", 7.78572089653462],
                        ["TomBrady", "2016-01-10", 8.28172399041139],
                        ["TomBrady", "2016-01-11", 8.4707303170059],
                        ["TomBrady", "2016-01-12", 8.13505390861157],
                        ["TomBrady", "2016-01-13", 8.06714903991011],
                    ],
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt_multi_series_historic(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt_multi_series_anomalies()


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt_multi_series_anomalies(
            model=model,
            freq=freq,
            level=level,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt_multi_series_cross_validation()


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt_multi_series_cross_validation(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            n_windows=n_windows,
            step_size=step_size,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt_input_size()


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt_input_size(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.timegpt_model_params()


        asyncio.run(main())
        """
        _response = await self._raw_client.timegpt_model_params(
            fewshot_steps=fewshot_steps,
            fewshot_loss=fewshot_loss,
            model=model,
            freq=freq,
            level=level,
            fh=fh,
            y=y,
            x=x,
            clean_ex_first=clean_ex_first,
            finetune_steps=finetune_steps,
            finetune_loss=finetune_loss,
            request_options=request_options,
        )
        return _response.data
