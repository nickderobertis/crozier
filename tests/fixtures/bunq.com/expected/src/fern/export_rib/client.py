

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_rib import ExportRib
from ..types.export_rib_create import ExportRibCreate
from ..types.export_rib_delete import ExportRibDelete
from ..types.export_rib_listing import ExportRibListing
from ..types.export_rib_read import ExportRibRead
from .raw_client import AsyncRawExportRibClient, RawExportRibClient


OMIT = typing.cast(typing.Any, ...)


class ExportRibClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExportRibClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExportRibClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExportRibClient
        """
        return self._raw_client

    def list_all_export_rib_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportRibListing]:
        """
        List all the RIBs for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportRibListing]
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_rib.list_all_export_rib_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_export_rib_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        request: ExportRib,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRibCreate:
        """
        Create a new RIB.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request : ExportRib

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRibCreate
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_rib.create_export_rib_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, request=request, request_options=request_options
        )
        return _response.data

    def read_export_rib_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRibRead:
        """
        Get a RIB for a monetary account by its id.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRibRead
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_rib.read_export_rib_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def delete_export_rib_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRibDelete:
        """
        Used to create new and read existing RIBs of a monetary account

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRibDelete
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_rib.delete_export_rib_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncExportRibClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExportRibClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExportRibClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExportRibClient
        """
        return self._raw_client

    async def list_all_export_rib_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportRibListing]:
        """
        List all the RIBs for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportRibListing]
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_rib.list_all_export_rib_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_export_rib_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        request: ExportRib,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRibCreate:
        """
        Create a new RIB.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request : ExportRib

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRibCreate
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_rib.create_export_rib_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, request=request, request_options=request_options
        )
        return _response.data

    async def read_export_rib_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRibRead:
        """
        Get a RIB for a monetary account by its id.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRibRead
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_rib.read_export_rib_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def delete_export_rib_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRibDelete:
        """
        Used to create new and read existing RIBs of a monetary account

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRibDelete
            Used to create new and read existing RIBs of a monetary account

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_rib.delete_export_rib_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_export_rib_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
