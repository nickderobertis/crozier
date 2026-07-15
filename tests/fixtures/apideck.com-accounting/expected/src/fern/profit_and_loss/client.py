

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_profit_and_loss_response import GetProfitAndLossResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.profit_and_loss_filter import ProfitAndLossFilter
from .raw_client import AsyncRawProfitAndLossClient, RawProfitAndLossClient


class ProfitAndLossClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProfitAndLossClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProfitAndLossClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProfitAndLossClient
        """
        return self._raw_client

    def one(
        self,
        *,
        raw: typing.Optional[bool] = None,
        filter: typing.Optional[ProfitAndLossFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProfitAndLossResponse:
        """
        Get Profit and Loss

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        filter : typing.Optional[ProfitAndLossFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProfitAndLossResponse
            Profit & Loss Report

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.profit_and_loss.one(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(
            raw=raw, filter=filter, pass_through=pass_through, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncProfitAndLossClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProfitAndLossClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProfitAndLossClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProfitAndLossClient
        """
        return self._raw_client

    async def one(
        self,
        *,
        raw: typing.Optional[bool] = None,
        filter: typing.Optional[ProfitAndLossFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProfitAndLossResponse:
        """
        Get Profit and Loss

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        filter : typing.Optional[ProfitAndLossFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProfitAndLossResponse
            Profit & Loss Report

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
            await client.profit_and_loss.one(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(
            raw=raw, filter=filter, pass_through=pass_through, fields=fields, request_options=request_options
        )
        return _response.data
