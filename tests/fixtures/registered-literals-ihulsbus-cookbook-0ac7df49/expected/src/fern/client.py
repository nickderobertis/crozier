

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .amount.client import AmountClient, AsyncAmountClient
    from .category.client import AsyncCategoryClient, CategoryClient
    from .cuisinetype.client import AsyncCuisinetypeClient, CuisinetypeClient
    from .difficultylevel.client import AsyncDifficultylevelClient, DifficultylevelClient
    from .image.client import AsyncImageClient, ImageClient
    from .ingredient.client import AsyncIngredientClient, IngredientClient
    from .instruction.client import AsyncInstructionClient, InstructionClient
    from .metadata.client import AsyncMetadataClient, MetadataClient
    from .preparationtime.client import AsyncPreparationtimeClient, PreparationtimeClient
    from .recipe.client import AsyncRecipeClient, RecipeClient
    from .search.client import AsyncSearchClient, SearchClient
    from .tag.client import AsyncTagClient, TagClient
    from .unit.client import AsyncUnitClient, UnitClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._recipe: typing.Optional[RecipeClient] = None
        self._image: typing.Optional[ImageClient] = None
        self._search: typing.Optional[SearchClient] = None
        self._instruction: typing.Optional[InstructionClient] = None
        self._tag: typing.Optional[TagClient] = None
        self._category: typing.Optional[CategoryClient] = None
        self._cuisinetype: typing.Optional[CuisinetypeClient] = None
        self._difficultylevel: typing.Optional[DifficultylevelClient] = None
        self._preparationtime: typing.Optional[PreparationtimeClient] = None
        self._metadata: typing.Optional[MetadataClient] = None
        self._ingredient: typing.Optional[IngredientClient] = None
        self._unit: typing.Optional[UnitClient] = None
        self._amount: typing.Optional[AmountClient] = None

    @property
    def recipe(self):
        if self._recipe is None:
            from .recipe.client import RecipeClient

            self._recipe = RecipeClient(client_wrapper=self._client_wrapper)
        return self._recipe

    @property
    def image(self):
        if self._image is None:
            from .image.client import ImageClient

            self._image = ImageClient(client_wrapper=self._client_wrapper)
        return self._image

    @property
    def search(self):
        if self._search is None:
            from .search.client import SearchClient

            self._search = SearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def instruction(self):
        if self._instruction is None:
            from .instruction.client import InstructionClient

            self._instruction = InstructionClient(client_wrapper=self._client_wrapper)
        return self._instruction

    @property
    def tag(self):
        if self._tag is None:
            from .tag.client import TagClient

            self._tag = TagClient(client_wrapper=self._client_wrapper)
        return self._tag

    @property
    def category(self):
        if self._category is None:
            from .category.client import CategoryClient

            self._category = CategoryClient(client_wrapper=self._client_wrapper)
        return self._category

    @property
    def cuisinetype(self):
        if self._cuisinetype is None:
            from .cuisinetype.client import CuisinetypeClient

            self._cuisinetype = CuisinetypeClient(client_wrapper=self._client_wrapper)
        return self._cuisinetype

    @property
    def difficultylevel(self):
        if self._difficultylevel is None:
            from .difficultylevel.client import DifficultylevelClient

            self._difficultylevel = DifficultylevelClient(client_wrapper=self._client_wrapper)
        return self._difficultylevel

    @property
    def preparationtime(self):
        if self._preparationtime is None:
            from .preparationtime.client import PreparationtimeClient

            self._preparationtime = PreparationtimeClient(client_wrapper=self._client_wrapper)
        return self._preparationtime

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import MetadataClient

            self._metadata = MetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def ingredient(self):
        if self._ingredient is None:
            from .ingredient.client import IngredientClient

            self._ingredient = IngredientClient(client_wrapper=self._client_wrapper)
        return self._ingredient

    @property
    def unit(self):
        if self._unit is None:
            from .unit.client import UnitClient

            self._unit = UnitClient(client_wrapper=self._client_wrapper)
        return self._unit

    @property
    def amount(self):
        if self._amount is None:
            from .amount.client import AmountClient

            self._amount = AmountClient(client_wrapper=self._client_wrapper)
        return self._amount


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
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._recipe: typing.Optional[AsyncRecipeClient] = None
        self._image: typing.Optional[AsyncImageClient] = None
        self._search: typing.Optional[AsyncSearchClient] = None
        self._instruction: typing.Optional[AsyncInstructionClient] = None
        self._tag: typing.Optional[AsyncTagClient] = None
        self._category: typing.Optional[AsyncCategoryClient] = None
        self._cuisinetype: typing.Optional[AsyncCuisinetypeClient] = None
        self._difficultylevel: typing.Optional[AsyncDifficultylevelClient] = None
        self._preparationtime: typing.Optional[AsyncPreparationtimeClient] = None
        self._metadata: typing.Optional[AsyncMetadataClient] = None
        self._ingredient: typing.Optional[AsyncIngredientClient] = None
        self._unit: typing.Optional[AsyncUnitClient] = None
        self._amount: typing.Optional[AsyncAmountClient] = None

    @property
    def recipe(self):
        if self._recipe is None:
            from .recipe.client import AsyncRecipeClient

            self._recipe = AsyncRecipeClient(client_wrapper=self._client_wrapper)
        return self._recipe

    @property
    def image(self):
        if self._image is None:
            from .image.client import AsyncImageClient

            self._image = AsyncImageClient(client_wrapper=self._client_wrapper)
        return self._image

    @property
    def search(self):
        if self._search is None:
            from .search.client import AsyncSearchClient

            self._search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def instruction(self):
        if self._instruction is None:
            from .instruction.client import AsyncInstructionClient

            self._instruction = AsyncInstructionClient(client_wrapper=self._client_wrapper)
        return self._instruction

    @property
    def tag(self):
        if self._tag is None:
            from .tag.client import AsyncTagClient

            self._tag = AsyncTagClient(client_wrapper=self._client_wrapper)
        return self._tag

    @property
    def category(self):
        if self._category is None:
            from .category.client import AsyncCategoryClient

            self._category = AsyncCategoryClient(client_wrapper=self._client_wrapper)
        return self._category

    @property
    def cuisinetype(self):
        if self._cuisinetype is None:
            from .cuisinetype.client import AsyncCuisinetypeClient

            self._cuisinetype = AsyncCuisinetypeClient(client_wrapper=self._client_wrapper)
        return self._cuisinetype

    @property
    def difficultylevel(self):
        if self._difficultylevel is None:
            from .difficultylevel.client import AsyncDifficultylevelClient

            self._difficultylevel = AsyncDifficultylevelClient(client_wrapper=self._client_wrapper)
        return self._difficultylevel

    @property
    def preparationtime(self):
        if self._preparationtime is None:
            from .preparationtime.client import AsyncPreparationtimeClient

            self._preparationtime = AsyncPreparationtimeClient(client_wrapper=self._client_wrapper)
        return self._preparationtime

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import AsyncMetadataClient

            self._metadata = AsyncMetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def ingredient(self):
        if self._ingredient is None:
            from .ingredient.client import AsyncIngredientClient

            self._ingredient = AsyncIngredientClient(client_wrapper=self._client_wrapper)
        return self._ingredient

    @property
    def unit(self):
        if self._unit is None:
            from .unit.client import AsyncUnitClient

            self._unit = AsyncUnitClient(client_wrapper=self._client_wrapper)
        return self._unit

    @property
    def amount(self):
        if self._amount is None:
            from .amount.client import AsyncAmountClient

            self._amount = AsyncAmountClient(client_wrapper=self._client_wrapper)
        return self._amount


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
