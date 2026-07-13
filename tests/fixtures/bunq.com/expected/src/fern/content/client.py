

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attachment_conversation_content_listing import AttachmentConversationContentListing
from ..types.attachment_monetary_account_content_listing import AttachmentMonetaryAccountContentListing
from ..types.attachment_public_content_listing import AttachmentPublicContentListing
from ..types.attachment_user_content_listing import AttachmentUserContentListing
from ..types.export_annual_overview_content_listing import ExportAnnualOverviewContentListing
from ..types.export_rib_content_listing import ExportRibContentListing
from ..types.export_statement_card_content_listing import ExportStatementCardContentListing
from ..types.export_statement_content_listing import ExportStatementContentListing
from ..types.export_statement_payment_content_listing import ExportStatementPaymentContentListing
from ..types.place_photo_lookup_content_listing import PlacePhotoLookupContentListing
from .raw_client import AsyncRawContentClient, RawContentClient


class ContentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentClient
        """
        return self._raw_client

    def list_all_content_for_attachment_public(
        self, attachment_public_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AttachmentPublicContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        attachment_public_uuid : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentPublicContentListing]
            Fetch the raw content of a public attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.

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
        client.content.list_all_content_for_attachment_public(
            attachment_public_uuid="attachment-publicUUID",
        )
        """
        _response = self._raw_client.list_all_content_for_attachment_public(
            attachment_public_uuid, request_options=request_options
        )
        return _response.data

    def list_all_content_for_place_lookup_photo(
        self, place_lookup_id: int, photo_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PlacePhotoLookupContentListing]:
        """
        View endpoint for place opening periods.

        Parameters
        ----------
        place_lookup_id : int


        photo_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PlacePhotoLookupContentListing]
            View endpoint for place opening periods.

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
        client.content.list_all_content_for_place_lookup_photo(
            place_lookup_id=1,
            photo_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_place_lookup_photo(
            place_lookup_id, photo_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_attachment(
        self, user_id: int, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AttachmentUserContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        user_id : int


        attachment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentUserContentListing]
            Fetch the raw content of a user attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.

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
        client.content.list_all_content_for_user_attachment(
            user_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_attachment(
            user_id, attachment_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_card_export_statement_card(
        self,
        user_id: int,
        card_id: int,
        export_statement_card_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportStatementCardContentListing]:
        """
        Fetch the raw content of a card statement export. The returned file format could be CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

        Parameters
        ----------
        user_id : int


        card_id : int


        export_statement_card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardContentListing]
            Fetch the raw content of a card statement export. The returned file format could be CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

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
        client.content.list_all_content_for_user_card_export_statement_card(
            user_id=1,
            card_id=1,
            export_statement_card_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_card_export_statement_card(
            user_id, card_id, export_statement_card_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_chat_conversation_attachment(
        self,
        user_id: int,
        chat_conversation_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AttachmentConversationContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        user_id : int


        chat_conversation_id : int


        attachment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentConversationContentListing]
            Fetch the raw content of an attachment with given ID. The raw content is the base64 of a file, without any JSON wrapping.

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
        client.content.list_all_content_for_user_chat_conversation_attachment(
            user_id=1,
            chat_conversation_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_chat_conversation_attachment(
            user_id, chat_conversation_id, attachment_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_export_annual_overview(
        self, user_id: int, export_annual_overview_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportAnnualOverviewContentListing]:
        """
        Used to retrieve the raw content of an annual overview.

        Parameters
        ----------
        user_id : int


        export_annual_overview_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportAnnualOverviewContentListing]
            Fetch the raw content of an annual overview. The annual overview is always in PDF format. Doc won't display the response of a request to get the content of an annual overview.

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
        client.content.list_all_content_for_user_export_annual_overview(
            user_id=1,
            export_annual_overview_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_export_annual_overview(
            user_id, export_annual_overview_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_monetary_account_attachment(
        self,
        user_id: int,
        monetary_account_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AttachmentMonetaryAccountContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        attachment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentMonetaryAccountContentListing]
            Fetch the raw content of a monetary account attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.

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
        client.content.list_all_content_for_user_monetary_account_attachment(
            user_id=1,
            monetary_account_id=1,
            attachment_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_monetary_account_attachment(
            user_id, monetary_account_id, attachment_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_monetary_account_customer_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        customer_statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportStatementContentListing]:
        """
        Fetch the raw content of a statement export. The returned file format could be MT940, CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        customer_statement_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementContentListing]
            Fetch the raw content of a statement export. The returned file format could be MT940, CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

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
        client.content.list_all_content_for_user_monetary_account_customer_statement(
            user_id=1,
            monetary_account_id=1,
            customer_statement_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_monetary_account_customer_statement(
            user_id, monetary_account_id, customer_statement_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_monetary_account_event_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportStatementPaymentContentListing]:
        """
        Fetch the raw content of a payment statement export.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : int


        statement_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementPaymentContentListing]
            Fetch the raw content of a payment statement export.

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
        client.content.list_all_content_for_user_monetary_account_event_statement(
            user_id=1,
            monetary_account_id=1,
            event_id=1,
            statement_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_monetary_account_event_statement(
            user_id, monetary_account_id, event_id, statement_id, request_options=request_options
        )
        return _response.data

    def list_all_content_for_user_monetary_account_export_rib(
        self,
        user_id: int,
        monetary_account_id: int,
        export_rib_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportRibContentListing]:
        """
        Used to retrieve the raw content of an RIB.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        export_rib_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportRibContentListing]
            Fetch the raw content of an RIB. The RIB is always in PDF format.

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
        client.content.list_all_content_for_user_monetary_account_export_rib(
            user_id=1,
            monetary_account_id=1,
            export_rib_id=1,
        )
        """
        _response = self._raw_client.list_all_content_for_user_monetary_account_export_rib(
            user_id, monetary_account_id, export_rib_id, request_options=request_options
        )
        return _response.data


class AsyncContentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentClient
        """
        return self._raw_client

    async def list_all_content_for_attachment_public(
        self, attachment_public_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AttachmentPublicContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        attachment_public_uuid : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentPublicContentListing]
            Fetch the raw content of a public attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.

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
            await client.content.list_all_content_for_attachment_public(
                attachment_public_uuid="attachment-publicUUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_attachment_public(
            attachment_public_uuid, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_place_lookup_photo(
        self, place_lookup_id: int, photo_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PlacePhotoLookupContentListing]:
        """
        View endpoint for place opening periods.

        Parameters
        ----------
        place_lookup_id : int


        photo_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PlacePhotoLookupContentListing]
            View endpoint for place opening periods.

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
            await client.content.list_all_content_for_place_lookup_photo(
                place_lookup_id=1,
                photo_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_place_lookup_photo(
            place_lookup_id, photo_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_attachment(
        self, user_id: int, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AttachmentUserContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        user_id : int


        attachment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentUserContentListing]
            Fetch the raw content of a user attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.

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
            await client.content.list_all_content_for_user_attachment(
                user_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_attachment(
            user_id, attachment_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_card_export_statement_card(
        self,
        user_id: int,
        card_id: int,
        export_statement_card_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportStatementCardContentListing]:
        """
        Fetch the raw content of a card statement export. The returned file format could be CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

        Parameters
        ----------
        user_id : int


        card_id : int


        export_statement_card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardContentListing]
            Fetch the raw content of a card statement export. The returned file format could be CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

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
            await client.content.list_all_content_for_user_card_export_statement_card(
                user_id=1,
                card_id=1,
                export_statement_card_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_card_export_statement_card(
            user_id, card_id, export_statement_card_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_chat_conversation_attachment(
        self,
        user_id: int,
        chat_conversation_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AttachmentConversationContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        user_id : int


        chat_conversation_id : int


        attachment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentConversationContentListing]
            Fetch the raw content of an attachment with given ID. The raw content is the base64 of a file, without any JSON wrapping.

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
            await client.content.list_all_content_for_user_chat_conversation_attachment(
                user_id=1,
                chat_conversation_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_chat_conversation_attachment(
            user_id, chat_conversation_id, attachment_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_export_annual_overview(
        self, user_id: int, export_annual_overview_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportAnnualOverviewContentListing]:
        """
        Used to retrieve the raw content of an annual overview.

        Parameters
        ----------
        user_id : int


        export_annual_overview_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportAnnualOverviewContentListing]
            Fetch the raw content of an annual overview. The annual overview is always in PDF format. Doc won't display the response of a request to get the content of an annual overview.

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
            await client.content.list_all_content_for_user_export_annual_overview(
                user_id=1,
                export_annual_overview_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_export_annual_overview(
            user_id, export_annual_overview_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_monetary_account_attachment(
        self,
        user_id: int,
        monetary_account_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AttachmentMonetaryAccountContentListing]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        attachment_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AttachmentMonetaryAccountContentListing]
            Fetch the raw content of a monetary account attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.

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
            await client.content.list_all_content_for_user_monetary_account_attachment(
                user_id=1,
                monetary_account_id=1,
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_monetary_account_attachment(
            user_id, monetary_account_id, attachment_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_monetary_account_customer_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        customer_statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportStatementContentListing]:
        """
        Fetch the raw content of a statement export. The returned file format could be MT940, CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        customer_statement_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementContentListing]
            Fetch the raw content of a statement export. The returned file format could be MT940, CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.

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
            await client.content.list_all_content_for_user_monetary_account_customer_statement(
                user_id=1,
                monetary_account_id=1,
                customer_statement_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_monetary_account_customer_statement(
            user_id, monetary_account_id, customer_statement_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_monetary_account_event_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportStatementPaymentContentListing]:
        """
        Fetch the raw content of a payment statement export.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : int


        statement_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementPaymentContentListing]
            Fetch the raw content of a payment statement export.

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
            await client.content.list_all_content_for_user_monetary_account_event_statement(
                user_id=1,
                monetary_account_id=1,
                event_id=1,
                statement_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_monetary_account_event_statement(
            user_id, monetary_account_id, event_id, statement_id, request_options=request_options
        )
        return _response.data

    async def list_all_content_for_user_monetary_account_export_rib(
        self,
        user_id: int,
        monetary_account_id: int,
        export_rib_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExportRibContentListing]:
        """
        Used to retrieve the raw content of an RIB.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        export_rib_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportRibContentListing]
            Fetch the raw content of an RIB. The RIB is always in PDF format.

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
            await client.content.list_all_content_for_user_monetary_account_export_rib(
                user_id=1,
                monetary_account_id=1,
                export_rib_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_content_for_user_monetary_account_export_rib(
            user_id, monetary_account_id, export_rib_id, request_options=request_options
        )
        return _response.data
