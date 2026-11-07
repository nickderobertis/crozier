

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accounting_create_or_update_vendor_request import AccountingCreateOrUpdateVendorRequest
from ..types.accounting_create_or_update_vendor_response import AccountingCreateOrUpdateVendorResponse
from ..types.accounting_delete_vendor_response import AccountingDeleteVendorResponse
from ..types.accounting_get_vendor_response import AccountingGetVendorResponse
from ..types.accounting_get_vendors_response import AccountingGetVendorsResponse
from .raw_client import AsyncRawAccountingVendorClient, RawAccountingVendorClient


OMIT = typing.cast(typing.Any, ...)


class AccountingVendorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountingVendorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountingVendorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountingVendorClient
        """
        return self._raw_client

    def accounting_vendor_get_vendor(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingGetVendorResponse:
        """
        Get details of a Vendor

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetVendorResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_vendor.accounting_vendor_get_vendor(
            id="id",
        )
        """
        _response = self._raw_client.accounting_vendor_get_vendor(id, fields=fields, request_options=request_options)
        return _response.data

    def accounting_vendor_delete_vendor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingDeleteVendorResponse:
        """
        Delete Vendor

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingDeleteVendorResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_vendor.accounting_vendor_delete_vendor(
            id="id",
        )
        """
        _response = self._raw_client.accounting_vendor_delete_vendor(id, request_options=request_options)
        return _response.data

    def accounting_vendor_update_vendor(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateVendorRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateVendorResponse:
        """
        Update Vendor

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateVendorRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateVendorResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_vendor.accounting_vendor_update_vendor(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.accounting_vendor_update_vendor(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    def accounting_vendor_get_vendors(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingGetVendorsResponse:
        """
        Get all the Vendors

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetVendorsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_vendor.accounting_vendor_get_vendors()
        """
        _response = self._raw_client.accounting_vendor_get_vendors(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def accounting_vendor_create_vendor(
        self,
        *,
        request: AccountingCreateOrUpdateVendorRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateVendorResponse:
        """
        Post Vendor

        Parameters
        ----------
        request : AccountingCreateOrUpdateVendorRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateVendorResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_vendor.accounting_vendor_create_vendor(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.accounting_vendor_create_vendor(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncAccountingVendorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountingVendorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountingVendorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountingVendorClient
        """
        return self._raw_client

    async def accounting_vendor_get_vendor(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingGetVendorResponse:
        """
        Get details of a Vendor

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetVendorResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_vendor.accounting_vendor_get_vendor(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_vendor_get_vendor(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def accounting_vendor_delete_vendor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingDeleteVendorResponse:
        """
        Delete Vendor

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingDeleteVendorResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_vendor.accounting_vendor_delete_vendor(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_vendor_delete_vendor(id, request_options=request_options)
        return _response.data

    async def accounting_vendor_update_vendor(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateVendorRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateVendorResponse:
        """
        Update Vendor

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateVendorRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateVendorResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_vendor.accounting_vendor_update_vendor(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_vendor_update_vendor(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    async def accounting_vendor_get_vendors(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingGetVendorsResponse:
        """
        Get all the Vendors

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetVendorsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_vendor.accounting_vendor_get_vendors()


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_vendor_get_vendors(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def accounting_vendor_create_vendor(
        self,
        *,
        request: AccountingCreateOrUpdateVendorRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateVendorResponse:
        """
        Post Vendor

        Parameters
        ----------
        request : AccountingCreateOrUpdateVendorRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateVendorResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_vendor.accounting_vendor_create_vendor(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_vendor_create_vendor(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data
