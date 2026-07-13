

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_statement_card_listing import ExportStatementCardListing
from ..types.export_statement_card_read import ExportStatementCardRead
from .raw_client import AsyncRawExportStatementCardClient, RawExportStatementCardClient


class ExportStatementCardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExportStatementCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExportStatementCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExportStatementCardClient
        """
        return self._raw_client

    def list_all_export_statement_card_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementCardListing]:
        """
        Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardListing]
            Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

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
        client.export_statement_card.list_all_export_statement_card_for_user_card(
            user_id=1,
            card_id=1,
        )
        """
        _response = self._raw_client.list_all_export_statement_card_for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    def read_export_statement_card_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardRead:
        """
        Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardRead
            Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

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
        client.export_statement_card.read_export_statement_card_for_user_card(
            user_id=1,
            card_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_export_statement_card_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncExportStatementCardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExportStatementCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExportStatementCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExportStatementCardClient
        """
        return self._raw_client

    async def list_all_export_statement_card_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementCardListing]:
        """
        Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardListing]
            Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

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
            await client.export_statement_card.list_all_export_statement_card_for_user_card(
                user_id=1,
                card_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_export_statement_card_for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    async def read_export_statement_card_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardRead:
        """
        Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardRead
            Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.

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
            await client.export_statement_card.read_export_statement_card_for_user_card(
                user_id=1,
                card_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_export_statement_card_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data
