

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .annotationqueues.client import AnnotationqueuesClient, AsyncAnnotationqueuesClient
    from .comments.client import AsyncCommentsClient, CommentsClient
    from .datasetitems.client import AsyncDatasetitemsClient, DatasetitemsClient
    from .datasetrunitems.client import AsyncDatasetrunitemsClient, DatasetrunitemsClient
    from .datasets.client import AsyncDatasetsClient, DatasetsClient
    from .health.client import AsyncHealthClient, HealthClient
    from .ingestion.client import AsyncIngestionClient, IngestionClient
    from .media.client import AsyncMediaClient, MediaClient
    from .metrics.client import AsyncMetricsClient, MetricsClient
    from .models.client import AsyncModelsClient, ModelsClient
    from .observations.client import AsyncObservationsClient, ObservationsClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .prompts.client import AsyncPromptsClient, PromptsClient
    from .promptversion.client import AsyncPromptversionClient, PromptversionClient
    from .score.client import AsyncScoreClient, ScoreClient
    from .scoreconfigs.client import AsyncScoreconfigsClient, ScoreconfigsClient
    from .sessions.client import AsyncSessionsClient, SessionsClient
    from .trace.client import AsyncTraceClient, TraceClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            username=username,
            password=password,
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
        self._annotationqueues: typing.Optional[AnnotationqueuesClient] = None
        self._comments: typing.Optional[CommentsClient] = None
        self._datasetitems: typing.Optional[DatasetitemsClient] = None
        self._datasetrunitems: typing.Optional[DatasetrunitemsClient] = None
        self._datasets: typing.Optional[DatasetsClient] = None
        self._health: typing.Optional[HealthClient] = None
        self._ingestion: typing.Optional[IngestionClient] = None
        self._media: typing.Optional[MediaClient] = None
        self._metrics: typing.Optional[MetricsClient] = None
        self._models: typing.Optional[ModelsClient] = None
        self._observations: typing.Optional[ObservationsClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._promptversion: typing.Optional[PromptversionClient] = None
        self._prompts: typing.Optional[PromptsClient] = None
        self._scoreconfigs: typing.Optional[ScoreconfigsClient] = None
        self._score: typing.Optional[ScoreClient] = None
        self._sessions: typing.Optional[SessionsClient] = None
        self._trace: typing.Optional[TraceClient] = None

    @property
    def annotationqueues(self):
        if self._annotationqueues is None:
            from .annotationqueues.client import AnnotationqueuesClient

            self._annotationqueues = AnnotationqueuesClient(client_wrapper=self._client_wrapper)
        return self._annotationqueues

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import CommentsClient

            self._comments = CommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def datasetitems(self):
        if self._datasetitems is None:
            from .datasetitems.client import DatasetitemsClient

            self._datasetitems = DatasetitemsClient(client_wrapper=self._client_wrapper)
        return self._datasetitems

    @property
    def datasetrunitems(self):
        if self._datasetrunitems is None:
            from .datasetrunitems.client import DatasetrunitemsClient

            self._datasetrunitems = DatasetrunitemsClient(client_wrapper=self._client_wrapper)
        return self._datasetrunitems

    @property
    def datasets(self):
        if self._datasets is None:
            from .datasets.client import DatasetsClient

            self._datasets = DatasetsClient(client_wrapper=self._client_wrapper)
        return self._datasets

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def ingestion(self):
        if self._ingestion is None:
            from .ingestion.client import IngestionClient

            self._ingestion = IngestionClient(client_wrapper=self._client_wrapper)
        return self._ingestion

    @property
    def media(self):
        if self._media is None:
            from .media.client import MediaClient

            self._media = MediaClient(client_wrapper=self._client_wrapper)
        return self._media

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import MetricsClient

            self._metrics = MetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def models(self):
        if self._models is None:
            from .models.client import ModelsClient

            self._models = ModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def observations(self):
        if self._observations is None:
            from .observations.client import ObservationsClient

            self._observations = ObservationsClient(client_wrapper=self._client_wrapper)
        return self._observations

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def promptversion(self):
        if self._promptversion is None:
            from .promptversion.client import PromptversionClient

            self._promptversion = PromptversionClient(client_wrapper=self._client_wrapper)
        return self._promptversion

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import PromptsClient

            self._prompts = PromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def scoreconfigs(self):
        if self._scoreconfigs is None:
            from .scoreconfigs.client import ScoreconfigsClient

            self._scoreconfigs = ScoreconfigsClient(client_wrapper=self._client_wrapper)
        return self._scoreconfigs

    @property
    def score(self):
        if self._score is None:
            from .score.client import ScoreClient

            self._score = ScoreClient(client_wrapper=self._client_wrapper)
        return self._score

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import SessionsClient

            self._sessions = SessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def trace(self):
        if self._trace is None:
            from .trace.client import TraceClient

            self._trace = TraceClient(client_wrapper=self._client_wrapper)
        return self._trace


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

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
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
            username=username,
            password=password,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._annotationqueues: typing.Optional[AsyncAnnotationqueuesClient] = None
        self._comments: typing.Optional[AsyncCommentsClient] = None
        self._datasetitems: typing.Optional[AsyncDatasetitemsClient] = None
        self._datasetrunitems: typing.Optional[AsyncDatasetrunitemsClient] = None
        self._datasets: typing.Optional[AsyncDatasetsClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None
        self._ingestion: typing.Optional[AsyncIngestionClient] = None
        self._media: typing.Optional[AsyncMediaClient] = None
        self._metrics: typing.Optional[AsyncMetricsClient] = None
        self._models: typing.Optional[AsyncModelsClient] = None
        self._observations: typing.Optional[AsyncObservationsClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._promptversion: typing.Optional[AsyncPromptversionClient] = None
        self._prompts: typing.Optional[AsyncPromptsClient] = None
        self._scoreconfigs: typing.Optional[AsyncScoreconfigsClient] = None
        self._score: typing.Optional[AsyncScoreClient] = None
        self._sessions: typing.Optional[AsyncSessionsClient] = None
        self._trace: typing.Optional[AsyncTraceClient] = None

    @property
    def annotationqueues(self):
        if self._annotationqueues is None:
            from .annotationqueues.client import AsyncAnnotationqueuesClient

            self._annotationqueues = AsyncAnnotationqueuesClient(client_wrapper=self._client_wrapper)
        return self._annotationqueues

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import AsyncCommentsClient

            self._comments = AsyncCommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def datasetitems(self):
        if self._datasetitems is None:
            from .datasetitems.client import AsyncDatasetitemsClient

            self._datasetitems = AsyncDatasetitemsClient(client_wrapper=self._client_wrapper)
        return self._datasetitems

    @property
    def datasetrunitems(self):
        if self._datasetrunitems is None:
            from .datasetrunitems.client import AsyncDatasetrunitemsClient

            self._datasetrunitems = AsyncDatasetrunitemsClient(client_wrapper=self._client_wrapper)
        return self._datasetrunitems

    @property
    def datasets(self):
        if self._datasets is None:
            from .datasets.client import AsyncDatasetsClient

            self._datasets = AsyncDatasetsClient(client_wrapper=self._client_wrapper)
        return self._datasets

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def ingestion(self):
        if self._ingestion is None:
            from .ingestion.client import AsyncIngestionClient

            self._ingestion = AsyncIngestionClient(client_wrapper=self._client_wrapper)
        return self._ingestion

    @property
    def media(self):
        if self._media is None:
            from .media.client import AsyncMediaClient

            self._media = AsyncMediaClient(client_wrapper=self._client_wrapper)
        return self._media

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import AsyncMetricsClient

            self._metrics = AsyncMetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def models(self):
        if self._models is None:
            from .models.client import AsyncModelsClient

            self._models = AsyncModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def observations(self):
        if self._observations is None:
            from .observations.client import AsyncObservationsClient

            self._observations = AsyncObservationsClient(client_wrapper=self._client_wrapper)
        return self._observations

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def promptversion(self):
        if self._promptversion is None:
            from .promptversion.client import AsyncPromptversionClient

            self._promptversion = AsyncPromptversionClient(client_wrapper=self._client_wrapper)
        return self._promptversion

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import AsyncPromptsClient

            self._prompts = AsyncPromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def scoreconfigs(self):
        if self._scoreconfigs is None:
            from .scoreconfigs.client import AsyncScoreconfigsClient

            self._scoreconfigs = AsyncScoreconfigsClient(client_wrapper=self._client_wrapper)
        return self._scoreconfigs

    @property
    def score(self):
        if self._score is None:
            from .score.client import AsyncScoreClient

            self._score = AsyncScoreClient(client_wrapper=self._client_wrapper)
        return self._score

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import AsyncSessionsClient

            self._sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def trace(self):
        if self._trace is None:
            from .trace.client import AsyncTraceClient

            self._trace = AsyncTraceClient(client_wrapper=self._client_wrapper)
        return self._trace
