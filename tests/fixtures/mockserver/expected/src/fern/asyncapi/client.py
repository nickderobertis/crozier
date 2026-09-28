

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAsyncapiClient, RawAsyncapiClient


OMIT = typing.cast(typing.Any, ...)


class AsyncapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAsyncapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAsyncapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAsyncapiClient
        """
        return self._raw_client

    def retrieve_async_api_mock_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns the status of the currently loaded AsyncAPI mock. Requires the mockserver-async module on the classpath.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            AsyncAPI status returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.asyncapi.retrieve_async_api_mock_status()
        """
        _response = self._raw_client.retrieve_async_api_mock_status(request_options=request_options)
        return _response.data

    def load_an_async_api_specification(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Loads an AsyncAPI specification (JSON or YAML), or a { spec, brokerConfig } document, to mock the described message broker. Requires the mockserver-async module on the classpath.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            AsyncAPI specification loaded

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.asyncapi.load_an_async_api_specification(
            request={
                "spec": "asyncapi: 2.6.0\ninfo:\n  title: Test Service\n  version: 1.0.0\nchannels:\n  user/signedup:\n    publish:\n      message:\n        payload:\n          type: object\n          properties:\n            userId:\n              type: string"
            },
        )
        """
        _response = self._raw_client.load_an_async_api_specification(request=request, request_options=request_options)
        return _response.data

    def verify_async_api_messages(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Verifies that messages were published/received against the loaded AsyncAPI mock. Requires the mockserver-async module on the classpath.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.asyncapi.verify_async_api_messages(
            request={"channel": "user/signedup", "count": {"atLeast": 0}},
        )
        """
        _response = self._raw_client.verify_async_api_messages(request=request, request_options=request_options)
        return _response.data


class AsyncAsyncapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAsyncapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAsyncapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAsyncapiClient
        """
        return self._raw_client

    async def retrieve_async_api_mock_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns the status of the currently loaded AsyncAPI mock. Requires the mockserver-async module on the classpath.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            AsyncAPI status returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.asyncapi.retrieve_async_api_mock_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_async_api_mock_status(request_options=request_options)
        return _response.data

    async def load_an_async_api_specification(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Loads an AsyncAPI specification (JSON or YAML), or a { spec, brokerConfig } document, to mock the described message broker. Requires the mockserver-async module on the classpath.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            AsyncAPI specification loaded

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.asyncapi.load_an_async_api_specification(
                request={
                    "spec": "asyncapi: 2.6.0\ninfo:\n  title: Test Service\n  version: 1.0.0\nchannels:\n  user/signedup:\n    publish:\n      message:\n        payload:\n          type: object\n          properties:\n            userId:\n              type: string"
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load_an_async_api_specification(
            request=request, request_options=request_options
        )
        return _response.data

    async def verify_async_api_messages(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Verifies that messages were published/received against the loaded AsyncAPI mock. Requires the mockserver-async module on the classpath.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.asyncapi.verify_async_api_messages(
                request={"channel": "user/signedup", "count": {"atLeast": 0}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_async_api_messages(request=request, request_options=request_options)
        return _response.data
