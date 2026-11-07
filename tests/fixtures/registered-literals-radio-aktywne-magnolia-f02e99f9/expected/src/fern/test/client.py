

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.test_response_result import TestResponseResult
from .raw_client import AsyncRawTestClient, RawTestClient
from .types.test_test_request_parameters import TestTestRequestParameters


class TestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestClient
        """
        return self._raw_client

    def test_test(
        self,
        *,
        parameters: typing.Optional[TestTestRequestParameters] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestResponseResult:
        """
        Test.

        Parameters
        ----------
        parameters : typing.Optional[TestTestRequestParameters]
            Parameters for testing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResponseResult
            Request fulfilled, document follows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.test.test_test()
        """
        _response = self._raw_client.test_test(parameters=parameters, request_options=request_options)
        return _response.data


class AsyncTestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestClient
        """
        return self._raw_client

    async def test_test(
        self,
        *,
        parameters: typing.Optional[TestTestRequestParameters] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestResponseResult:
        """
        Test.

        Parameters
        ----------
        parameters : typing.Optional[TestTestRequestParameters]
            Parameters for testing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResponseResult
            Request fulfilled, document follows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test.test_test()


        asyncio.run(main())
        """
        _response = await self._raw_client.test_test(parameters=parameters, request_options=request_options)
        return _response.data
