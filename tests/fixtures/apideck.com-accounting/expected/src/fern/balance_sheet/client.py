

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.balance_sheet_filter import BalanceSheetFilter
from ..types.get_balance_sheet_response import GetBalanceSheetResponse
from ..types.pass_through_query import PassThroughQuery
from .raw_client import AsyncRawBalanceSheetClient, RawBalanceSheetClient


class BalanceSheetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBalanceSheetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBalanceSheetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBalanceSheetClient
        """
        return self._raw_client

    def one(
        self,
        *,
        pass_through: typing.Optional[PassThroughQuery] = None,
        filter: typing.Optional[BalanceSheetFilter] = None,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBalanceSheetResponse:
        """
        Get BalanceSheet

        Parameters
        ----------
        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        filter : typing.Optional[BalanceSheetFilter]
            Apply filters

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBalanceSheetResponse
            BalanceSheet

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.balance_sheet.one()
        """
        _response = self._raw_client.one(
            pass_through=pass_through, filter=filter, raw=raw, request_options=request_options
        )
        return _response.data


class AsyncBalanceSheetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBalanceSheetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBalanceSheetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBalanceSheetClient
        """
        return self._raw_client

    async def one(
        self,
        *,
        pass_through: typing.Optional[PassThroughQuery] = None,
        filter: typing.Optional[BalanceSheetFilter] = None,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBalanceSheetResponse:
        """
        Get BalanceSheet

        Parameters
        ----------
        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        filter : typing.Optional[BalanceSheetFilter]
            Apply filters

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBalanceSheetResponse
            BalanceSheet

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.balance_sheet.one()


        asyncio.run(main())
        """
        _response = await self._raw_client.one(
            pass_through=pass_through, filter=filter, raw=raw, request_options=request_options
        )
        return _response.data
