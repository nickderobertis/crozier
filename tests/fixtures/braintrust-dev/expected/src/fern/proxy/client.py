

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProxyClient, RawProxyClient
from .types.proxycredentials_request_logging import ProxycredentialsRequestLogging
from .types.proxycredentials_response import ProxycredentialsResponse


OMIT = typing.cast(typing.Any, ...)


class ProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProxyClient
        """
        return self._raw_client

    def proxychat_completions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy a chat/completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.proxy.proxychat_completions()
        """
        _response = self._raw_client.proxychat_completions(request=request, request_options=request_options)
        return _response.data

    def proxycompletions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy a completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.proxy.proxycompletions()
        """
        _response = self._raw_client.proxycompletions(request=request, request_options=request_options)
        return _response.data

    def proxyauto(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy a request to either chat/completions or completions automatically based on the model. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.proxy.proxyauto()
        """
        _response = self._raw_client.proxyauto(request=request, request_options=request_options)
        return _response.data

    def proxyembeddings(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy an embeddings request to the specified model, converting its format as needed. Will cache automatically.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.proxy.proxyembeddings()
        """
        _response = self._raw_client.proxyembeddings(request=request, request_options=request_options)
        return _response.data

    def proxycredentials(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        ttl_seconds: typing.Optional[float] = OMIT,
        logging: typing.Optional[ProxycredentialsRequestLogging] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProxycredentialsResponse:
        """
        Create a temporary credential which can access the proxy for a limited time. The temporary credential will be allowed to make requests on behalf of the Braintrust API key (or model provider API key) provided in the `Authorization` header. See [docs](/docs/deploy/ai-proxy#create-temporary-credentials) for code examples.

        Parameters
        ----------
        model : typing.Optional[str]
            Granted model name. Null/undefined to grant usage of all models.

        ttl_seconds : typing.Optional[float]
            TTL of the temporary credential. 10 minutes by default.

        logging : typing.Optional[ProxycredentialsRequestLogging]
            If present, proxy will log requests to the given Braintrust project name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProxycredentialsResponse
            Successfully created temporary credential

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.proxy.proxycredentials()
        """
        _response = self._raw_client.proxycredentials(
            model=model, ttl_seconds=ttl_seconds, logging=logging, request_options=request_options
        )
        return _response.data

    def path(
        self,
        path: typing.Sequence[str],
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Any requests which do not match the above paths will be proxied directly to the OpenAI API.

        Parameters
        ----------
        path : typing.Sequence[str]
            The path to proxy

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.proxy.path(
            path="path+",
        )
        """
        _response = self._raw_client.path(path, request=request, request_options=request_options)
        return _response.data


class AsyncProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProxyClient
        """
        return self._raw_client

    async def proxychat_completions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy a chat/completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.proxy.proxychat_completions()


        asyncio.run(main())
        """
        _response = await self._raw_client.proxychat_completions(request=request, request_options=request_options)
        return _response.data

    async def proxycompletions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy a completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.proxy.proxycompletions()


        asyncio.run(main())
        """
        _response = await self._raw_client.proxycompletions(request=request, request_options=request_options)
        return _response.data

    async def proxyauto(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy a request to either chat/completions or completions automatically based on the model. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.proxy.proxyauto()


        asyncio.run(main())
        """
        _response = await self._raw_client.proxyauto(request=request, request_options=request_options)
        return _response.data

    async def proxyembeddings(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Proxy an embeddings request to the specified model, converting its format as needed. Will cache automatically.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.proxy.proxyembeddings()


        asyncio.run(main())
        """
        _response = await self._raw_client.proxyembeddings(request=request, request_options=request_options)
        return _response.data

    async def proxycredentials(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        ttl_seconds: typing.Optional[float] = OMIT,
        logging: typing.Optional[ProxycredentialsRequestLogging] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProxycredentialsResponse:
        """
        Create a temporary credential which can access the proxy for a limited time. The temporary credential will be allowed to make requests on behalf of the Braintrust API key (or model provider API key) provided in the `Authorization` header. See [docs](/docs/deploy/ai-proxy#create-temporary-credentials) for code examples.

        Parameters
        ----------
        model : typing.Optional[str]
            Granted model name. Null/undefined to grant usage of all models.

        ttl_seconds : typing.Optional[float]
            TTL of the temporary credential. 10 minutes by default.

        logging : typing.Optional[ProxycredentialsRequestLogging]
            If present, proxy will log requests to the given Braintrust project name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProxycredentialsResponse
            Successfully created temporary credential

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.proxy.proxycredentials()


        asyncio.run(main())
        """
        _response = await self._raw_client.proxycredentials(
            model=model, ttl_seconds=ttl_seconds, logging=logging, request_options=request_options
        )
        return _response.data

    async def path(
        self,
        path: typing.Sequence[str],
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Any requests which do not match the above paths will be proxied directly to the OpenAI API.

        Parameters
        ----------
        path : typing.Sequence[str]
            The path to proxy

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Proxy response (supports both streaming and non-streaming formats)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.proxy.path(
                path="path+",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.path(path, request=request, request_options=request_options)
        return _response.data
