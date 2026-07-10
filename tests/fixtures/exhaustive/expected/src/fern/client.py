

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper

if typing.TYPE_CHECKING:
    from .endpoints_container.client import AsyncEndpointsContainerClient, EndpointsContainerClient
    from .endpoints_content_type.client import AsyncEndpointsContentTypeClient, EndpointsContentTypeClient
    from .endpoints_enum.client import AsyncEndpointsEnumClient, EndpointsEnumClient
    from .endpoints_http_methods.client import AsyncEndpointsHttpMethodsClient, EndpointsHttpMethodsClient
    from .endpoints_object.client import AsyncEndpointsObjectClient, EndpointsObjectClient
    from .endpoints_pagination.client import AsyncEndpointsPaginationClient, EndpointsPaginationClient
    from .endpoints_params.client import AsyncEndpointsParamsClient, EndpointsParamsClient
    from .endpoints_primitive.client import AsyncEndpointsPrimitiveClient, EndpointsPrimitiveClient
    from .endpoints_put.client import AsyncEndpointsPutClient, EndpointsPutClient
    from .endpoints_union.client import AsyncEndpointsUnionClient, EndpointsUnionClient
    from .endpoints_urls.client import AsyncEndpointsUrlsClient, EndpointsUrlsClient
    from .inlinedrequests.client import AsyncInlinedrequestsClient, InlinedrequestsClient
    from .noauth.client import AsyncNoauthClient, NoauthClient
    from .noreqbody.client import AsyncNoreqbodyClient, NoreqbodyClient
    from .reqwithheaders.client import AsyncReqwithheadersClient, ReqwithheadersClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
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
        )
        self._endpoints_container: typing.Optional[EndpointsContainerClient] = None
        self._endpoints_content_type: typing.Optional[EndpointsContentTypeClient] = None
        self._endpoints_enum: typing.Optional[EndpointsEnumClient] = None
        self._endpoints_http_methods: typing.Optional[EndpointsHttpMethodsClient] = None
        self._endpoints_object: typing.Optional[EndpointsObjectClient] = None
        self._endpoints_pagination: typing.Optional[EndpointsPaginationClient] = None
        self._endpoints_params: typing.Optional[EndpointsParamsClient] = None
        self._endpoints_primitive: typing.Optional[EndpointsPrimitiveClient] = None
        self._endpoints_put: typing.Optional[EndpointsPutClient] = None
        self._endpoints_union: typing.Optional[EndpointsUnionClient] = None
        self._endpoints_urls: typing.Optional[EndpointsUrlsClient] = None
        self._inlinedrequests: typing.Optional[InlinedrequestsClient] = None
        self._noauth: typing.Optional[NoauthClient] = None
        self._noreqbody: typing.Optional[NoreqbodyClient] = None
        self._reqwithheaders: typing.Optional[ReqwithheadersClient] = None

    @property
    def endpoints_container(self):
        if self._endpoints_container is None:
            from .endpoints_container.client import EndpointsContainerClient

            self._endpoints_container = EndpointsContainerClient(client_wrapper=self._client_wrapper)
        return self._endpoints_container

    @property
    def endpoints_content_type(self):
        if self._endpoints_content_type is None:
            from .endpoints_content_type.client import EndpointsContentTypeClient

            self._endpoints_content_type = EndpointsContentTypeClient(client_wrapper=self._client_wrapper)
        return self._endpoints_content_type

    @property
    def endpoints_enum(self):
        if self._endpoints_enum is None:
            from .endpoints_enum.client import EndpointsEnumClient

            self._endpoints_enum = EndpointsEnumClient(client_wrapper=self._client_wrapper)
        return self._endpoints_enum

    @property
    def endpoints_http_methods(self):
        if self._endpoints_http_methods is None:
            from .endpoints_http_methods.client import EndpointsHttpMethodsClient

            self._endpoints_http_methods = EndpointsHttpMethodsClient(client_wrapper=self._client_wrapper)
        return self._endpoints_http_methods

    @property
    def endpoints_object(self):
        if self._endpoints_object is None:
            from .endpoints_object.client import EndpointsObjectClient

            self._endpoints_object = EndpointsObjectClient(client_wrapper=self._client_wrapper)
        return self._endpoints_object

    @property
    def endpoints_pagination(self):
        if self._endpoints_pagination is None:
            from .endpoints_pagination.client import EndpointsPaginationClient

            self._endpoints_pagination = EndpointsPaginationClient(client_wrapper=self._client_wrapper)
        return self._endpoints_pagination

    @property
    def endpoints_params(self):
        if self._endpoints_params is None:
            from .endpoints_params.client import EndpointsParamsClient

            self._endpoints_params = EndpointsParamsClient(client_wrapper=self._client_wrapper)
        return self._endpoints_params

    @property
    def endpoints_primitive(self):
        if self._endpoints_primitive is None:
            from .endpoints_primitive.client import EndpointsPrimitiveClient

            self._endpoints_primitive = EndpointsPrimitiveClient(client_wrapper=self._client_wrapper)
        return self._endpoints_primitive

    @property
    def endpoints_put(self):
        if self._endpoints_put is None:
            from .endpoints_put.client import EndpointsPutClient

            self._endpoints_put = EndpointsPutClient(client_wrapper=self._client_wrapper)
        return self._endpoints_put

    @property
    def endpoints_union(self):
        if self._endpoints_union is None:
            from .endpoints_union.client import EndpointsUnionClient

            self._endpoints_union = EndpointsUnionClient(client_wrapper=self._client_wrapper)
        return self._endpoints_union

    @property
    def endpoints_urls(self):
        if self._endpoints_urls is None:
            from .endpoints_urls.client import EndpointsUrlsClient

            self._endpoints_urls = EndpointsUrlsClient(client_wrapper=self._client_wrapper)
        return self._endpoints_urls

    @property
    def inlinedrequests(self):
        if self._inlinedrequests is None:
            from .inlinedrequests.client import InlinedrequestsClient

            self._inlinedrequests = InlinedrequestsClient(client_wrapper=self._client_wrapper)
        return self._inlinedrequests

    @property
    def noauth(self):
        if self._noauth is None:
            from .noauth.client import NoauthClient

            self._noauth = NoauthClient(client_wrapper=self._client_wrapper)
        return self._noauth

    @property
    def noreqbody(self):
        if self._noreqbody is None:
            from .noreqbody.client import NoreqbodyClient

            self._noreqbody = NoreqbodyClient(client_wrapper=self._client_wrapper)
        return self._noreqbody

    @property
    def reqwithheaders(self):
        if self._reqwithheaders is None:
            from .reqwithheaders.client import ReqwithheadersClient

            self._reqwithheaders = ReqwithheadersClient(client_wrapper=self._client_wrapper)
        return self._reqwithheaders


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._endpoints_container: typing.Optional[AsyncEndpointsContainerClient] = None
        self._endpoints_content_type: typing.Optional[AsyncEndpointsContentTypeClient] = None
        self._endpoints_enum: typing.Optional[AsyncEndpointsEnumClient] = None
        self._endpoints_http_methods: typing.Optional[AsyncEndpointsHttpMethodsClient] = None
        self._endpoints_object: typing.Optional[AsyncEndpointsObjectClient] = None
        self._endpoints_pagination: typing.Optional[AsyncEndpointsPaginationClient] = None
        self._endpoints_params: typing.Optional[AsyncEndpointsParamsClient] = None
        self._endpoints_primitive: typing.Optional[AsyncEndpointsPrimitiveClient] = None
        self._endpoints_put: typing.Optional[AsyncEndpointsPutClient] = None
        self._endpoints_union: typing.Optional[AsyncEndpointsUnionClient] = None
        self._endpoints_urls: typing.Optional[AsyncEndpointsUrlsClient] = None
        self._inlinedrequests: typing.Optional[AsyncInlinedrequestsClient] = None
        self._noauth: typing.Optional[AsyncNoauthClient] = None
        self._noreqbody: typing.Optional[AsyncNoreqbodyClient] = None
        self._reqwithheaders: typing.Optional[AsyncReqwithheadersClient] = None

    @property
    def endpoints_container(self):
        if self._endpoints_container is None:
            from .endpoints_container.client import AsyncEndpointsContainerClient

            self._endpoints_container = AsyncEndpointsContainerClient(client_wrapper=self._client_wrapper)
        return self._endpoints_container

    @property
    def endpoints_content_type(self):
        if self._endpoints_content_type is None:
            from .endpoints_content_type.client import AsyncEndpointsContentTypeClient

            self._endpoints_content_type = AsyncEndpointsContentTypeClient(client_wrapper=self._client_wrapper)
        return self._endpoints_content_type

    @property
    def endpoints_enum(self):
        if self._endpoints_enum is None:
            from .endpoints_enum.client import AsyncEndpointsEnumClient

            self._endpoints_enum = AsyncEndpointsEnumClient(client_wrapper=self._client_wrapper)
        return self._endpoints_enum

    @property
    def endpoints_http_methods(self):
        if self._endpoints_http_methods is None:
            from .endpoints_http_methods.client import AsyncEndpointsHttpMethodsClient

            self._endpoints_http_methods = AsyncEndpointsHttpMethodsClient(client_wrapper=self._client_wrapper)
        return self._endpoints_http_methods

    @property
    def endpoints_object(self):
        if self._endpoints_object is None:
            from .endpoints_object.client import AsyncEndpointsObjectClient

            self._endpoints_object = AsyncEndpointsObjectClient(client_wrapper=self._client_wrapper)
        return self._endpoints_object

    @property
    def endpoints_pagination(self):
        if self._endpoints_pagination is None:
            from .endpoints_pagination.client import AsyncEndpointsPaginationClient

            self._endpoints_pagination = AsyncEndpointsPaginationClient(client_wrapper=self._client_wrapper)
        return self._endpoints_pagination

    @property
    def endpoints_params(self):
        if self._endpoints_params is None:
            from .endpoints_params.client import AsyncEndpointsParamsClient

            self._endpoints_params = AsyncEndpointsParamsClient(client_wrapper=self._client_wrapper)
        return self._endpoints_params

    @property
    def endpoints_primitive(self):
        if self._endpoints_primitive is None:
            from .endpoints_primitive.client import AsyncEndpointsPrimitiveClient

            self._endpoints_primitive = AsyncEndpointsPrimitiveClient(client_wrapper=self._client_wrapper)
        return self._endpoints_primitive

    @property
    def endpoints_put(self):
        if self._endpoints_put is None:
            from .endpoints_put.client import AsyncEndpointsPutClient

            self._endpoints_put = AsyncEndpointsPutClient(client_wrapper=self._client_wrapper)
        return self._endpoints_put

    @property
    def endpoints_union(self):
        if self._endpoints_union is None:
            from .endpoints_union.client import AsyncEndpointsUnionClient

            self._endpoints_union = AsyncEndpointsUnionClient(client_wrapper=self._client_wrapper)
        return self._endpoints_union

    @property
    def endpoints_urls(self):
        if self._endpoints_urls is None:
            from .endpoints_urls.client import AsyncEndpointsUrlsClient

            self._endpoints_urls = AsyncEndpointsUrlsClient(client_wrapper=self._client_wrapper)
        return self._endpoints_urls

    @property
    def inlinedrequests(self):
        if self._inlinedrequests is None:
            from .inlinedrequests.client import AsyncInlinedrequestsClient

            self._inlinedrequests = AsyncInlinedrequestsClient(client_wrapper=self._client_wrapper)
        return self._inlinedrequests

    @property
    def noauth(self):
        if self._noauth is None:
            from .noauth.client import AsyncNoauthClient

            self._noauth = AsyncNoauthClient(client_wrapper=self._client_wrapper)
        return self._noauth

    @property
    def noreqbody(self):
        if self._noreqbody is None:
            from .noreqbody.client import AsyncNoreqbodyClient

            self._noreqbody = AsyncNoreqbodyClient(client_wrapper=self._client_wrapper)
        return self._noreqbody

    @property
    def reqwithheaders(self):
        if self._reqwithheaders is None:
            from .reqwithheaders.client import AsyncReqwithheadersClient

            self._reqwithheaders = AsyncReqwithheadersClient(client_wrapper=self._client_wrapper)
        return self._reqwithheaders
