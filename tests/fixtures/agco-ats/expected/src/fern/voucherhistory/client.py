

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_dealer_db_models_voucher_history import ApiPagedResponseDealerDbModelsVoucherHistory
from .raw_client import AsyncRawVoucherhistoryClient, RawVoucherhistoryClient


class VoucherhistoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoucherhistoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoucherhistoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoucherhistoryClient
        """
        return self._raw_client

    def getvoucherhistory(
        self,
        *,
        voucher_code: typing.Optional[str] = None,
        changed_before: typing.Optional[dt.datetime] = None,
        changed_after: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsVoucherHistory:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : typing.Optional[str]
            Optional. Filter history data by Voucher Code.

        changed_before : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured before provided date.

        changed_after : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured after provided date.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseDealerDbModelsVoucherHistory
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.voucherhistory.getvoucherhistory()
        """
        _response = self._raw_client.getvoucherhistory(
            voucher_code=voucher_code,
            changed_before=changed_before,
            changed_after=changed_after,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data


class AsyncVoucherhistoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoucherhistoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoucherhistoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoucherhistoryClient
        """
        return self._raw_client

    async def getvoucherhistory(
        self,
        *,
        voucher_code: typing.Optional[str] = None,
        changed_before: typing.Optional[dt.datetime] = None,
        changed_after: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsVoucherHistory:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : typing.Optional[str]
            Optional. Filter history data by Voucher Code.

        changed_before : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured before provided date.

        changed_after : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured after provided date.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseDealerDbModelsVoucherHistory
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.voucherhistory.getvoucherhistory()


        asyncio.run(main())
        """
        _response = await self._raw_client.getvoucherhistory(
            voucher_code=voucher_code,
            changed_before=changed_before,
            changed_after=changed_after,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data
