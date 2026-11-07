

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPropertiesClient, RawPropertiesClient
from .types.get_account_properties_response import GetAccountPropertiesResponse
from .types.get_user_properties_response import GetUserPropertiesResponse


class PropertiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPropertiesClient
        """
        return self._raw_client

    def get_account_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAccountPropertiesResponse:
        """
        Endpoint to list account properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAccountPropertiesResponse
            Account Properties

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.properties.get_account_properties()
        """
        _response = self._raw_client.get_account_properties(request_options=request_options)
        return _response.data

    def get_user_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserPropertiesResponse:
        """
        Endpoint to list user properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserPropertiesResponse
            User Properties

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.properties.get_user_properties()
        """
        _response = self._raw_client.get_user_properties(request_options=request_options)
        return _response.data


class AsyncPropertiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPropertiesClient
        """
        return self._raw_client

    async def get_account_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAccountPropertiesResponse:
        """
        Endpoint to list account properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAccountPropertiesResponse
            Account Properties

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.properties.get_account_properties()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_properties(request_options=request_options)
        return _response.data

    async def get_user_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserPropertiesResponse:
        """
        Endpoint to list user properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserPropertiesResponse
            User Properties

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.properties.get_user_properties()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_properties(request_options=request_options)
        return _response.data
