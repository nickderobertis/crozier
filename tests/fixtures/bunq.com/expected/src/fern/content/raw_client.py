

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
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


class RawContentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_content_for_attachment_public(
        self, attachment_public_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AttachmentPublicContentListing]]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        attachment_public_uuid : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AttachmentPublicContentListing]]
            Fetch the raw content of a public attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"attachment-public/{jsonable_encoder(attachment_public_uuid)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentPublicContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentPublicContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_place_lookup_photo(
        self, place_lookup_id: int, photo_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PlacePhotoLookupContentListing]]:
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
        HttpResponse[typing.List[PlacePhotoLookupContentListing]]
            View endpoint for place opening periods.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"place-lookup/{jsonable_encoder(place_lookup_id)}/photo/{jsonable_encoder(photo_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PlacePhotoLookupContentListing],
                    parse_obj_as(
                        type_=typing.List[PlacePhotoLookupContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_attachment(
        self, user_id: int, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AttachmentUserContentListing]]:
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
        HttpResponse[typing.List[AttachmentUserContentListing]]
            Fetch the raw content of a user attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/attachment/{jsonable_encoder(attachment_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentUserContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentUserContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_card_export_statement_card(
        self,
        user_id: int,
        card_id: int,
        export_statement_card_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ExportStatementCardContentListing]]:
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
        HttpResponse[typing.List[ExportStatementCardContentListing]]
            Fetch the raw content of a card statement export. The returned file format could be CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card/{jsonable_encoder(export_statement_card_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementCardContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementCardContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_chat_conversation_attachment(
        self,
        user_id: int,
        chat_conversation_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AttachmentConversationContentListing]]:
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
        HttpResponse[typing.List[AttachmentConversationContentListing]]
            Fetch the raw content of an attachment with given ID. The raw content is the base64 of a file, without any JSON wrapping.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/chat-conversation/{jsonable_encoder(chat_conversation_id)}/attachment/{jsonable_encoder(attachment_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentConversationContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentConversationContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_export_annual_overview(
        self, user_id: int, export_annual_overview_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ExportAnnualOverviewContentListing]]:
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
        HttpResponse[typing.List[ExportAnnualOverviewContentListing]]
            Fetch the raw content of an annual overview. The annual overview is always in PDF format. Doc won't display the response of a request to get the content of an annual overview.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/export-annual-overview/{jsonable_encoder(export_annual_overview_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportAnnualOverviewContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportAnnualOverviewContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_monetary_account_attachment(
        self,
        user_id: int,
        monetary_account_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AttachmentMonetaryAccountContentListing]]:
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
        HttpResponse[typing.List[AttachmentMonetaryAccountContentListing]]
            Fetch the raw content of a monetary account attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/attachment/{jsonable_encoder(attachment_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentMonetaryAccountContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentMonetaryAccountContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_monetary_account_customer_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        customer_statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ExportStatementContentListing]]:
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
        HttpResponse[typing.List[ExportStatementContentListing]]
            Fetch the raw content of a statement export. The returned file format could be MT940, CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement/{jsonable_encoder(customer_statement_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_monetary_account_event_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ExportStatementPaymentContentListing]]:
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
        HttpResponse[typing.List[ExportStatementPaymentContentListing]]
            Fetch the raw content of a payment statement export.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/event/{jsonable_encoder(event_id)}/statement/{jsonable_encoder(statement_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementPaymentContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementPaymentContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_content_for_user_monetary_account_export_rib(
        self,
        user_id: int,
        monetary_account_id: int,
        export_rib_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ExportRibContentListing]]:
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
        HttpResponse[typing.List[ExportRibContentListing]]
            Fetch the raw content of an RIB. The RIB is always in PDF format.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/export-rib/{jsonable_encoder(export_rib_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportRibContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportRibContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawContentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_content_for_attachment_public(
        self, attachment_public_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AttachmentPublicContentListing]]:
        """
        Get the raw content of a specific attachment.

        Parameters
        ----------
        attachment_public_uuid : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AttachmentPublicContentListing]]
            Fetch the raw content of a public attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"attachment-public/{jsonable_encoder(attachment_public_uuid)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentPublicContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentPublicContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_place_lookup_photo(
        self, place_lookup_id: int, photo_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PlacePhotoLookupContentListing]]:
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
        AsyncHttpResponse[typing.List[PlacePhotoLookupContentListing]]
            View endpoint for place opening periods.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"place-lookup/{jsonable_encoder(place_lookup_id)}/photo/{jsonable_encoder(photo_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PlacePhotoLookupContentListing],
                    parse_obj_as(
                        type_=typing.List[PlacePhotoLookupContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_attachment(
        self, user_id: int, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AttachmentUserContentListing]]:
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
        AsyncHttpResponse[typing.List[AttachmentUserContentListing]]
            Fetch the raw content of a user attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/attachment/{jsonable_encoder(attachment_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentUserContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentUserContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_card_export_statement_card(
        self,
        user_id: int,
        card_id: int,
        export_statement_card_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ExportStatementCardContentListing]]:
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
        AsyncHttpResponse[typing.List[ExportStatementCardContentListing]]
            Fetch the raw content of a card statement export. The returned file format could be CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card/{jsonable_encoder(export_statement_card_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementCardContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementCardContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_chat_conversation_attachment(
        self,
        user_id: int,
        chat_conversation_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AttachmentConversationContentListing]]:
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
        AsyncHttpResponse[typing.List[AttachmentConversationContentListing]]
            Fetch the raw content of an attachment with given ID. The raw content is the base64 of a file, without any JSON wrapping.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/chat-conversation/{jsonable_encoder(chat_conversation_id)}/attachment/{jsonable_encoder(attachment_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentConversationContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentConversationContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_export_annual_overview(
        self, user_id: int, export_annual_overview_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ExportAnnualOverviewContentListing]]:
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
        AsyncHttpResponse[typing.List[ExportAnnualOverviewContentListing]]
            Fetch the raw content of an annual overview. The annual overview is always in PDF format. Doc won't display the response of a request to get the content of an annual overview.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/export-annual-overview/{jsonable_encoder(export_annual_overview_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportAnnualOverviewContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportAnnualOverviewContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_monetary_account_attachment(
        self,
        user_id: int,
        monetary_account_id: int,
        attachment_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AttachmentMonetaryAccountContentListing]]:
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
        AsyncHttpResponse[typing.List[AttachmentMonetaryAccountContentListing]]
            Fetch the raw content of a monetary account attachment with given ID. The raw content is the binary representation of a file, without any JSON wrapping.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/attachment/{jsonable_encoder(attachment_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AttachmentMonetaryAccountContentListing],
                    parse_obj_as(
                        type_=typing.List[AttachmentMonetaryAccountContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_monetary_account_customer_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        customer_statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ExportStatementContentListing]]:
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
        AsyncHttpResponse[typing.List[ExportStatementContentListing]]
            Fetch the raw content of a statement export. The returned file format could be MT940, CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement/{jsonable_encoder(customer_statement_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_monetary_account_event_statement(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        statement_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ExportStatementPaymentContentListing]]:
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
        AsyncHttpResponse[typing.List[ExportStatementPaymentContentListing]]
            Fetch the raw content of a payment statement export.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/event/{jsonable_encoder(event_id)}/statement/{jsonable_encoder(statement_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementPaymentContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementPaymentContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_content_for_user_monetary_account_export_rib(
        self,
        user_id: int,
        monetary_account_id: int,
        export_rib_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ExportRibContentListing]]:
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
        AsyncHttpResponse[typing.List[ExportRibContentListing]]
            Fetch the raw content of an RIB. The RIB is always in PDF format.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/export-rib/{jsonable_encoder(export_rib_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportRibContentListing],
                    parse_obj_as(
                        type_=typing.List[ExportRibContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
