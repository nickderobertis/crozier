

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_annual_overview_create import ExportAnnualOverviewCreate
from ..types.export_annual_overview_delete import ExportAnnualOverviewDelete
from ..types.export_annual_overview_listing import ExportAnnualOverviewListing
from ..types.export_annual_overview_read import ExportAnnualOverviewRead
from .raw_client import AsyncRawExportAnnualOverviewClient, RawExportAnnualOverviewClient


OMIT = typing.cast(typing.Any, ...)


class ExportAnnualOverviewClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExportAnnualOverviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExportAnnualOverviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExportAnnualOverviewClient
        """
        return self._raw_client

    def list_all_export_annual_overview_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportAnnualOverviewListing]:
        """
        List all the annual overviews for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportAnnualOverviewListing]
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
        client.export_annual_overview.list_all_export_annual_overview_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_export_annual_overview_for_user(user_id, request_options=request_options)
        return _response.data

    def create_export_annual_overview_for_user(
        self, user_id: int, *, year: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAnnualOverviewCreate:
        """
        Create a new annual overview for a specific year. An overview can be generated only for a past year.

        Parameters
        ----------
        user_id : int


        year : int
            The year for which the overview is.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAnnualOverviewCreate
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
        client.export_annual_overview.create_export_annual_overview_for_user(
            user_id=1,
            year=1,
        )
        """
        _response = self._raw_client.create_export_annual_overview_for_user(
            user_id, year=year, request_options=request_options
        )
        return _response.data

    def read_export_annual_overview_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAnnualOverviewRead:
        """
        Get an annual overview for a user by its id.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAnnualOverviewRead
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
        client.export_annual_overview.read_export_annual_overview_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_export_annual_overview_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def delete_export_annual_overview_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAnnualOverviewDelete:
        """
        Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAnnualOverviewDelete
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
        client.export_annual_overview.delete_export_annual_overview_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_export_annual_overview_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncExportAnnualOverviewClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExportAnnualOverviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExportAnnualOverviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExportAnnualOverviewClient
        """
        return self._raw_client

    async def list_all_export_annual_overview_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportAnnualOverviewListing]:
        """
        List all the annual overviews for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportAnnualOverviewListing]
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
            await client.export_annual_overview.list_all_export_annual_overview_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_export_annual_overview_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_export_annual_overview_for_user(
        self, user_id: int, *, year: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAnnualOverviewCreate:
        """
        Create a new annual overview for a specific year. An overview can be generated only for a past year.

        Parameters
        ----------
        user_id : int


        year : int
            The year for which the overview is.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAnnualOverviewCreate
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
            await client.export_annual_overview.create_export_annual_overview_for_user(
                user_id=1,
                year=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_export_annual_overview_for_user(
            user_id, year=year, request_options=request_options
        )
        return _response.data

    async def read_export_annual_overview_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAnnualOverviewRead:
        """
        Get an annual overview for a user by its id.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAnnualOverviewRead
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
            await client.export_annual_overview.read_export_annual_overview_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_export_annual_overview_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def delete_export_annual_overview_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAnnualOverviewDelete:
        """
        Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAnnualOverviewDelete
            Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.

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
            await client.export_annual_overview.delete_export_annual_overview_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_export_annual_overview_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
