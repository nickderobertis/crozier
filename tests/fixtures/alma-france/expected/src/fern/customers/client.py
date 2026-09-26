

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCustomersClient, RawCustomersClient


OMIT = typing.cast(typing.Any, ...)


class CustomersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomersClient
        """
        return self._raw_client

    def get_customer(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieve customer data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Customer data retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.customers.get_customer()
        """
        _response = self._raw_client.get_customer(request_options=request_options)
        return _response.data

    def create_customer(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Create a new customer record.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Customer created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.customers.create_customer(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.create_customer(request=request, request_options=request_options)
        return _response.data


class AsyncCustomersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomersClient
        """
        return self._raw_client

    async def get_customer(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieve customer data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Customer data retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.customers.get_customer()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer(request_options=request_options)
        return _response.data

    async def create_customer(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Create a new customer record.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Customer created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.customers.create_customer(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_customer(request=request, request_options=request_options)
        return _response.data
