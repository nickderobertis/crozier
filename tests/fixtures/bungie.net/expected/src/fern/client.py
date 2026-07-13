

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from ._.client import AsyncClient, Client
    from .app.client import AppClient, AsyncAppClient
    from .communitycontent.client import AsyncCommunitycontentClient, CommunitycontentClient
    from .content.client import AsyncContentClient, ContentClient
    from .destiny2.client import AsyncDestiny2Client, Destiny2Client
    from .fireteam.client import AsyncFireteamClient, FireteamClient
    from .forum.client import AsyncForumClient, ForumClient
    from .groupv2.client import AsyncGroupv2Client, Groupv2Client
    from .social.client import AsyncSocialClient, SocialClient
    from .tokens.client import AsyncTokensClient, TokensClient
    from .trending.client import AsyncTrendingClient, TrendingClient
    from .user.client import AsyncUserClient, UserClient


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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._app: typing.Optional[AppClient] = None
        self._communitycontent: typing.Optional[CommunitycontentClient] = None
        self._content: typing.Optional[ContentClient] = None
        self._destiny2: typing.Optional[Destiny2Client] = None
        self._fireteam: typing.Optional[FireteamClient] = None
        self._forum: typing.Optional[ForumClient] = None
        self.__: typing.Optional[Client] = None
        self._groupv2: typing.Optional[Groupv2Client] = None
        self._social: typing.Optional[SocialClient] = None
        self._tokens: typing.Optional[TokensClient] = None
        self._trending: typing.Optional[TrendingClient] = None
        self._user: typing.Optional[UserClient] = None

    @property
    def app(self):
        if self._app is None:
            from .app.client import AppClient

            self._app = AppClient(client_wrapper=self._client_wrapper)
        return self._app

    @property
    def communitycontent(self):
        if self._communitycontent is None:
            from .communitycontent.client import CommunitycontentClient

            self._communitycontent = CommunitycontentClient(client_wrapper=self._client_wrapper)
        return self._communitycontent

    @property
    def content(self):
        if self._content is None:
            from .content.client import ContentClient

            self._content = ContentClient(client_wrapper=self._client_wrapper)
        return self._content

    @property
    def destiny2(self):
        if self._destiny2 is None:
            from .destiny2.client import Destiny2Client

            self._destiny2 = Destiny2Client(client_wrapper=self._client_wrapper)
        return self._destiny2

    @property
    def fireteam(self):
        if self._fireteam is None:
            from .fireteam.client import FireteamClient

            self._fireteam = FireteamClient(client_wrapper=self._client_wrapper)
        return self._fireteam

    @property
    def forum(self):
        if self._forum is None:
            from .forum.client import ForumClient

            self._forum = ForumClient(client_wrapper=self._client_wrapper)
        return self._forum

    @property
    def _(self):
        if self.__ is None:
            from ._.client import Client

            self.__ = Client(client_wrapper=self._client_wrapper)
        return self.__

    @property
    def groupv2(self):
        if self._groupv2 is None:
            from .groupv2.client import Groupv2Client

            self._groupv2 = Groupv2Client(client_wrapper=self._client_wrapper)
        return self._groupv2

    @property
    def social(self):
        if self._social is None:
            from .social.client import SocialClient

            self._social = SocialClient(client_wrapper=self._client_wrapper)
        return self._social

    @property
    def tokens(self):
        if self._tokens is None:
            from .tokens.client import TokensClient

            self._tokens = TokensClient(client_wrapper=self._client_wrapper)
        return self._tokens

    @property
    def trending(self):
        if self._trending is None:
            from .trending.client import TrendingClient

            self._trending = TrendingClient(client_wrapper=self._client_wrapper)
        return self._trending

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user


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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._app: typing.Optional[AsyncAppClient] = None
        self._communitycontent: typing.Optional[AsyncCommunitycontentClient] = None
        self._content: typing.Optional[AsyncContentClient] = None
        self._destiny2: typing.Optional[AsyncDestiny2Client] = None
        self._fireteam: typing.Optional[AsyncFireteamClient] = None
        self._forum: typing.Optional[AsyncForumClient] = None
        self.__: typing.Optional[AsyncClient] = None
        self._groupv2: typing.Optional[AsyncGroupv2Client] = None
        self._social: typing.Optional[AsyncSocialClient] = None
        self._tokens: typing.Optional[AsyncTokensClient] = None
        self._trending: typing.Optional[AsyncTrendingClient] = None
        self._user: typing.Optional[AsyncUserClient] = None

    @property
    def app(self):
        if self._app is None:
            from .app.client import AsyncAppClient

            self._app = AsyncAppClient(client_wrapper=self._client_wrapper)
        return self._app

    @property
    def communitycontent(self):
        if self._communitycontent is None:
            from .communitycontent.client import AsyncCommunitycontentClient

            self._communitycontent = AsyncCommunitycontentClient(client_wrapper=self._client_wrapper)
        return self._communitycontent

    @property
    def content(self):
        if self._content is None:
            from .content.client import AsyncContentClient

            self._content = AsyncContentClient(client_wrapper=self._client_wrapper)
        return self._content

    @property
    def destiny2(self):
        if self._destiny2 is None:
            from .destiny2.client import AsyncDestiny2Client

            self._destiny2 = AsyncDestiny2Client(client_wrapper=self._client_wrapper)
        return self._destiny2

    @property
    def fireteam(self):
        if self._fireteam is None:
            from .fireteam.client import AsyncFireteamClient

            self._fireteam = AsyncFireteamClient(client_wrapper=self._client_wrapper)
        return self._fireteam

    @property
    def forum(self):
        if self._forum is None:
            from .forum.client import AsyncForumClient

            self._forum = AsyncForumClient(client_wrapper=self._client_wrapper)
        return self._forum

    @property
    def _(self):
        if self.__ is None:
            from ._.client import AsyncClient

            self.__ = AsyncClient(client_wrapper=self._client_wrapper)
        return self.__

    @property
    def groupv2(self):
        if self._groupv2 is None:
            from .groupv2.client import AsyncGroupv2Client

            self._groupv2 = AsyncGroupv2Client(client_wrapper=self._client_wrapper)
        return self._groupv2

    @property
    def social(self):
        if self._social is None:
            from .social.client import AsyncSocialClient

            self._social = AsyncSocialClient(client_wrapper=self._client_wrapper)
        return self._social

    @property
    def tokens(self):
        if self._tokens is None:
            from .tokens.client import AsyncTokensClient

            self._tokens = AsyncTokensClient(client_wrapper=self._client_wrapper)
        return self._tokens

    @property
    def trending(self):
        if self._trending is None:
            from .trending.client import AsyncTrendingClient

            self._trending = AsyncTrendingClient(client_wrapper=self._client_wrapper)
        return self._trending

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
