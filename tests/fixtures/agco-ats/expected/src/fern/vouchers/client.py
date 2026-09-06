

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_dealer_db_models_voucher_history import ApiPagedResponseDealerDbModelsVoucherHistory
from ..types.dealer_db_models_voucher import DealerDbModelsVoucher
from ..types.dealer_db_models_voucher_type import DealerDbModelsVoucherType
from .raw_client import AsyncRawVouchersClient, RawVouchersClient
from .types.vouchers_get_request_deleted import VouchersGetRequestDeleted


OMIT = typing.cast(typing.Any, ...)


class VouchersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVouchersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVouchersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVouchersClient
        """
        return self._raw_client

    def get(
        self,
        voucher_code: str,
        *,
        deleted: typing.Optional[VouchersGetRequestDeleted] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DealerDbModelsVoucher:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to get.

        deleted : typing.Optional[VouchersGetRequestDeleted]
            Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsVoucher
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vouchers.get(
            voucher_code="VoucherCode",
        )
        """
        _response = self._raw_client.get(voucher_code, deleted=deleted, request_options=request_options)
        return _response.data

    def post(
        self,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vouchers.post()
        """
        _response = self._raw_client.post(
            created_date=created_date,
            dealer_code=dealer_code,
            deleted=deleted,
            email=email,
            expiration_date=expiration_date,
            license_to=license_to,
            modified_by=modified_by,
            order_number=order_number,
            punched=punched,
            punched_date=punched_date,
            purpose=purpose,
            type=type,
            voucher_code=voucher_code,
            request_options=request_options,
        )
        return _response.data

    def put(
        self,
        voucher_code_: str,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code_ : str
            The voucher code of the voucher to update.

        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vouchers.put(
            voucher_code_="VoucherCode",
        )
        """
        _response = self._raw_client.put(
            voucher_code_,
            created_date=created_date,
            dealer_code=dealer_code,
            deleted=deleted,
            email=email,
            expiration_date=expiration_date,
            license_to=license_to,
            modified_by=modified_by,
            order_number=order_number,
            punched=punched,
            punched_date=punched_date,
            purpose=purpose,
            type=type,
            voucher_code=voucher_code,
            request_options=request_options,
        )
        return _response.data

    def delete(self, voucher_code: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vouchers.delete(
            voucher_code="VoucherCode",
        )
        """
        _response = self._raw_client.delete(voucher_code, request_options=request_options)
        return _response.data

    def getvoucherhistory(
        self,
        voucher_code: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsVoucherHistory:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code to get history for.

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
        client.vouchers.getvoucherhistory(
            voucher_code="VoucherCode",
        )
        """
        _response = self._raw_client.getvoucherhistory(
            voucher_code, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data


class AsyncVouchersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVouchersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVouchersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVouchersClient
        """
        return self._raw_client

    async def get(
        self,
        voucher_code: str,
        *,
        deleted: typing.Optional[VouchersGetRequestDeleted] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DealerDbModelsVoucher:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to get.

        deleted : typing.Optional[VouchersGetRequestDeleted]
            Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsVoucher
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.vouchers.get(
                voucher_code="VoucherCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(voucher_code, deleted=deleted, request_options=request_options)
        return _response.data

    async def post(
        self,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.vouchers.post()


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            created_date=created_date,
            dealer_code=dealer_code,
            deleted=deleted,
            email=email,
            expiration_date=expiration_date,
            license_to=license_to,
            modified_by=modified_by,
            order_number=order_number,
            punched=punched,
            punched_date=punched_date,
            purpose=purpose,
            type=type,
            voucher_code=voucher_code,
            request_options=request_options,
        )
        return _response.data

    async def put(
        self,
        voucher_code_: str,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code_ : str
            The voucher code of the voucher to update.

        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

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
            await client.vouchers.put(
                voucher_code_="VoucherCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            voucher_code_,
            created_date=created_date,
            dealer_code=dealer_code,
            deleted=deleted,
            email=email,
            expiration_date=expiration_date,
            license_to=license_to,
            modified_by=modified_by,
            order_number=order_number,
            punched=punched,
            punched_date=punched_date,
            purpose=purpose,
            type=type,
            voucher_code=voucher_code,
            request_options=request_options,
        )
        return _response.data

    async def delete(self, voucher_code: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to delete.

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
            await client.vouchers.delete(
                voucher_code="VoucherCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(voucher_code, request_options=request_options)
        return _response.data

    async def getvoucherhistory(
        self,
        voucher_code: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsVoucherHistory:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code to get history for.

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
            await client.vouchers.getvoucherhistory(
                voucher_code="VoucherCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getvoucherhistory(
            voucher_code, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
