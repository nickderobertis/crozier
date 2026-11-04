

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAccountClient, RawAccountClient
from .types.get_all_accounts_request_provider import GetAllAccountsRequestProvider
from .types.get_all_accounts_response import GetAllAccountsResponse


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def get_all_accounts(
        self,
        *,
        provider: typing.Optional[GetAllAccountsRequestProvider] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAllAccountsResponse:
        """
        Parameters
        ----------
        provider : typing.Optional[GetAllAccountsRequestProvider]
            Filter by provider

        page_number : typing.Optional[int]
            Page number of the results

        page_size : typing.Optional[int]
            Page size of the results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllAccountsResponse
            OK.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.account.get_all_accounts(
            page_number=1,
            page_size=1,
        )
        """
        _response = self._raw_client.get_all_accounts(
            provider=provider, page_number=page_number, page_size=page_size, request_options=request_options
        )
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def get_all_accounts(
        self,
        *,
        provider: typing.Optional[GetAllAccountsRequestProvider] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAllAccountsResponse:
        """
        Parameters
        ----------
        provider : typing.Optional[GetAllAccountsRequestProvider]
            Filter by provider

        page_number : typing.Optional[int]
            Page number of the results

        page_size : typing.Optional[int]
            Page size of the results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllAccountsResponse
            OK.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.account.get_all_accounts(
                page_number=1,
                page_size=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_accounts(
            provider=provider, page_number=page_number, page_size=page_size, request_options=request_options
        )
        return _response.data
