

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi

if typing.TYPE_CHECKING:
    from .assets.client import AssetsClient, AsyncAssetsClient
    from .copywriter.client import AsyncCopywriterClient, CopywriterClient
    from .editor.client import AsyncEditorClient, EditorClient
    from .extract.client import AsyncExtractClient, ExtractClient
    from .generation_jobs.client import AsyncGenerationJobsClient, GenerationJobsClient
    from .generation_plan.client import AsyncGenerationPlanClient, GenerationPlanClient
    from .imagegen.client import AsyncImagegenClient, ImagegenClient
    from .metrics.client import AsyncMetricsClient, MetricsClient
    from .onboarding.client import AsyncOnboardingClient, OnboardingClient
    from .providers.client import AsyncProvidersClient, ProvidersClient
    from .queue.client import AsyncQueueClient, QueueClient
    from .settings.client import AsyncSettingsClient, SettingsClient
    from .source_images.client import AsyncSourceImagesClient, SourceImagesClient
    from .templates.client import AsyncTemplatesClient, TemplatesClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
        self._assets: typing.Optional[AssetsClient] = None
        self._generation_jobs: typing.Optional[GenerationJobsClient] = None
        self._generation_plan: typing.Optional[GenerationPlanClient] = None
        self._editor: typing.Optional[EditorClient] = None
        self._imagegen: typing.Optional[ImagegenClient] = None
        self._extract: typing.Optional[ExtractClient] = None
        self._copywriter: typing.Optional[CopywriterClient] = None
        self._metrics: typing.Optional[MetricsClient] = None
        self._onboarding: typing.Optional[OnboardingClient] = None
        self._providers: typing.Optional[ProvidersClient] = None
        self._queue: typing.Optional[QueueClient] = None
        self._settings: typing.Optional[SettingsClient] = None
        self._source_images: typing.Optional[SourceImagesClient] = None
        self._templates: typing.Optional[TemplatesClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def health_health_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Probe the configured database with a 2s timeout.

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.health_health_get()
        """
        _response = self._raw_client.health_health_get(request_options=request_options)
        return _response.data

    @property
    def assets(self):
        if self._assets is None:
            from .assets.client import AssetsClient

            self._assets = AssetsClient(client_wrapper=self._client_wrapper)
        return self._assets

    @property
    def generation_jobs(self):
        if self._generation_jobs is None:
            from .generation_jobs.client import GenerationJobsClient

            self._generation_jobs = GenerationJobsClient(client_wrapper=self._client_wrapper)
        return self._generation_jobs

    @property
    def generation_plan(self):
        if self._generation_plan is None:
            from .generation_plan.client import GenerationPlanClient

            self._generation_plan = GenerationPlanClient(client_wrapper=self._client_wrapper)
        return self._generation_plan

    @property
    def editor(self):
        if self._editor is None:
            from .editor.client import EditorClient

            self._editor = EditorClient(client_wrapper=self._client_wrapper)
        return self._editor

    @property
    def imagegen(self):
        if self._imagegen is None:
            from .imagegen.client import ImagegenClient

            self._imagegen = ImagegenClient(client_wrapper=self._client_wrapper)
        return self._imagegen

    @property
    def extract(self):
        if self._extract is None:
            from .extract.client import ExtractClient

            self._extract = ExtractClient(client_wrapper=self._client_wrapper)
        return self._extract

    @property
    def copywriter(self):
        if self._copywriter is None:
            from .copywriter.client import CopywriterClient

            self._copywriter = CopywriterClient(client_wrapper=self._client_wrapper)
        return self._copywriter

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import MetricsClient

            self._metrics = MetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def onboarding(self):
        if self._onboarding is None:
            from .onboarding.client import OnboardingClient

            self._onboarding = OnboardingClient(client_wrapper=self._client_wrapper)
        return self._onboarding

    @property
    def providers(self):
        if self._providers is None:
            from .providers.client import ProvidersClient

            self._providers = ProvidersClient(client_wrapper=self._client_wrapper)
        return self._providers

    @property
    def queue(self):
        if self._queue is None:
            from .queue.client import QueueClient

            self._queue = QueueClient(client_wrapper=self._client_wrapper)
        return self._queue

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import SettingsClient

            self._settings = SettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def source_images(self):
        if self._source_images is None:
            from .source_images.client import SourceImagesClient

            self._source_images = SourceImagesClient(client_wrapper=self._client_wrapper)
        return self._source_images

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import TemplatesClient

            self._templates = TemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates


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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._assets: typing.Optional[AsyncAssetsClient] = None
        self._generation_jobs: typing.Optional[AsyncGenerationJobsClient] = None
        self._generation_plan: typing.Optional[AsyncGenerationPlanClient] = None
        self._editor: typing.Optional[AsyncEditorClient] = None
        self._imagegen: typing.Optional[AsyncImagegenClient] = None
        self._extract: typing.Optional[AsyncExtractClient] = None
        self._copywriter: typing.Optional[AsyncCopywriterClient] = None
        self._metrics: typing.Optional[AsyncMetricsClient] = None
        self._onboarding: typing.Optional[AsyncOnboardingClient] = None
        self._providers: typing.Optional[AsyncProvidersClient] = None
        self._queue: typing.Optional[AsyncQueueClient] = None
        self._settings: typing.Optional[AsyncSettingsClient] = None
        self._source_images: typing.Optional[AsyncSourceImagesClient] = None
        self._templates: typing.Optional[AsyncTemplatesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def health_health_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Probe the configured database with a 2s timeout.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health_health_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_health_get(request_options=request_options)
        return _response.data

    @property
    def assets(self):
        if self._assets is None:
            from .assets.client import AsyncAssetsClient

            self._assets = AsyncAssetsClient(client_wrapper=self._client_wrapper)
        return self._assets

    @property
    def generation_jobs(self):
        if self._generation_jobs is None:
            from .generation_jobs.client import AsyncGenerationJobsClient

            self._generation_jobs = AsyncGenerationJobsClient(client_wrapper=self._client_wrapper)
        return self._generation_jobs

    @property
    def generation_plan(self):
        if self._generation_plan is None:
            from .generation_plan.client import AsyncGenerationPlanClient

            self._generation_plan = AsyncGenerationPlanClient(client_wrapper=self._client_wrapper)
        return self._generation_plan

    @property
    def editor(self):
        if self._editor is None:
            from .editor.client import AsyncEditorClient

            self._editor = AsyncEditorClient(client_wrapper=self._client_wrapper)
        return self._editor

    @property
    def imagegen(self):
        if self._imagegen is None:
            from .imagegen.client import AsyncImagegenClient

            self._imagegen = AsyncImagegenClient(client_wrapper=self._client_wrapper)
        return self._imagegen

    @property
    def extract(self):
        if self._extract is None:
            from .extract.client import AsyncExtractClient

            self._extract = AsyncExtractClient(client_wrapper=self._client_wrapper)
        return self._extract

    @property
    def copywriter(self):
        if self._copywriter is None:
            from .copywriter.client import AsyncCopywriterClient

            self._copywriter = AsyncCopywriterClient(client_wrapper=self._client_wrapper)
        return self._copywriter

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import AsyncMetricsClient

            self._metrics = AsyncMetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def onboarding(self):
        if self._onboarding is None:
            from .onboarding.client import AsyncOnboardingClient

            self._onboarding = AsyncOnboardingClient(client_wrapper=self._client_wrapper)
        return self._onboarding

    @property
    def providers(self):
        if self._providers is None:
            from .providers.client import AsyncProvidersClient

            self._providers = AsyncProvidersClient(client_wrapper=self._client_wrapper)
        return self._providers

    @property
    def queue(self):
        if self._queue is None:
            from .queue.client import AsyncQueueClient

            self._queue = AsyncQueueClient(client_wrapper=self._client_wrapper)
        return self._queue

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import AsyncSettingsClient

            self._settings = AsyncSettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def source_images(self):
        if self._source_images is None:
            from .source_images.client import AsyncSourceImagesClient

            self._source_images = AsyncSourceImagesClient(client_wrapper=self._client_wrapper)
        return self._source_images

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import AsyncTemplatesClient

            self._templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates
