

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .collections.client import AsyncCollectionsClient, CollectionsClient
    from .comments.client import AsyncCommentsClient, CommentsClient
    from .tags.client import AsyncTagsClient, TagsClient
    from .tickets.client import AsyncTicketsClient, TicketsClient
    from .users.client import AsyncUsersClient, UsersClient


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._collections: typing.Optional[CollectionsClient] = None
        self._tags: typing.Optional[TagsClient] = None
        self._tickets: typing.Optional[TicketsClient] = None
        self._comments: typing.Optional[CommentsClient] = None
        self._users: typing.Optional[UsersClient] = None

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import CollectionsClient

            self._collections = CollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import TagsClient

            self._tags = TagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def tickets(self):
        if self._tickets is None:
            from .tickets.client import TicketsClient

            self._tickets = TicketsClient(client_wrapper=self._client_wrapper)
        return self._tickets

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import CommentsClient

            self._comments = CommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._collections: typing.Optional[AsyncCollectionsClient] = None
        self._tags: typing.Optional[AsyncTagsClient] = None
        self._tickets: typing.Optional[AsyncTicketsClient] = None
        self._comments: typing.Optional[AsyncCommentsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import AsyncCollectionsClient

            self._collections = AsyncCollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import AsyncTagsClient

            self._tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def tickets(self):
        if self._tickets is None:
            from .tickets.client import AsyncTicketsClient

            self._tickets = AsyncTicketsClient(client_wrapper=self._client_wrapper)
        return self._tickets

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import AsyncCommentsClient

            self._comments = AsyncCommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
