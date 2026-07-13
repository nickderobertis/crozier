

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.address import Address
from ..types.amount import Amount
from ..types.attachment import Attachment
from ..types.geolocation import Geolocation
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.label_user import LabelUser
from ..types.request_inquiry_reference import RequestInquiryReference
from ..types.request_response_listing import RequestResponseListing
from ..types.request_response_read import RequestResponseRead
from ..types.request_response_update import RequestResponseUpdate


OMIT = typing.cast(typing.Any, ...)


class RawRequestResponseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_request_response_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RequestResponseListing]]:
        """
        Get all RequestResponses for a MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RequestResponseListing]]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestResponseListing],
                    parse_obj_as(
                        type_=typing.List[RequestResponseListing],
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

    def read_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestResponseRead]:
        """
        Get the details for a specific existing RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestResponseRead]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestResponseRead,
                    parse_obj_as(
                        type_=RequestResponseRead,
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

    def update_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        credit_scheme_identifier: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        eligible_whitelist_id: typing.Optional[int] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        mandate_identifier: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_refund_requested: typing.Optional[str] = OMIT,
        time_refunded: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_refund_requested: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestResponseUpdate]:
        """
        Update the status to accept or reject the RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount this RequestResponse was received on.

        amount_inquired : typing.Optional[Amount]
            The requested Amount.

        amount_responded : typing.Optional[Amount]
            The Amount the RequestResponse was accepted with.

        attachment : typing.Optional[typing.Sequence[Attachment]]
            The Attachments attached to the RequestResponse.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount that is requesting money with this RequestResponse.

        created : typing.Optional[str]
            The timestamp when the Request Response was created.

        credit_scheme_identifier : typing.Optional[str]
            The credit scheme id provided by the counterparty for DIRECT_DEBIT inquiries.

        description : typing.Optional[str]
            The description for the RequestResponse provided by the requesting party. Maximum 9000 characters.

        eligible_whitelist_id : typing.Optional[int]
            The whitelist id for this action or null.

        event_id : typing.Optional[int]
            The ID of the latest event for the request.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the RequestResponse was created.

        id : typing.Optional[int]
            The id of the Request Response.

        mandate_identifier : typing.Optional[str]
            The mandate id provided by the counterparty for DIRECT_DEBIT inquiries.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestResponse must have.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the RequestResponse was received on.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        status : typing.Optional[str]
            The status of the RequestResponse. Can be ACCEPTED, PENDING, REJECTED, REFUND_REQUESTED, REFUNDED or REVOKED.

        sub_type : typing.Optional[str]
            The subtype of the RequestInquiry. Can be ONCE or RECURRING for DIRECT_DEBIT RequestInquiries and NONE for all other.

        time_expiry : typing.Optional[str]
            The timestamp of when the RequestResponse expired or will expire.

        time_refund_requested : typing.Optional[str]
            The timestamp of when a refund request for the RequestResponse was claimed.

        time_refunded : typing.Optional[str]
            The timestamp of when the RequestResponse was refunded.

        time_responded : typing.Optional[str]
            The timestamp of when the RequestResponse was responded to.

        type : typing.Optional[str]
            The type of the RequestInquiry. Can be DIRECT_DEBIT, DIRECT_DEBIT_B2B, IDEAL, SOFORT or INTERNAL.

        updated : typing.Optional[str]
            The timestamp when the Request Response was last updated (will be updated when chat messages are received).

        user_refund_requested : typing.Optional[LabelUser]
            The label of the user that requested the refund.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestResponseUpdate]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id_)}/request-response/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "address_billing": convert_and_respect_annotation_metadata(
                    object_=address_billing, annotation=Address, direction="write"
                ),
                "address_shipping": convert_and_respect_annotation_metadata(
                    object_=address_shipping, annotation=Address, direction="write"
                ),
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "amount_inquired": convert_and_respect_annotation_metadata(
                    object_=amount_inquired, annotation=Amount, direction="write"
                ),
                "amount_responded": convert_and_respect_annotation_metadata(
                    object_=amount_responded, annotation=Amount, direction="write"
                ),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[Attachment], direction="write"
                ),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "credit_scheme_identifier": credit_scheme_identifier,
                "description": description,
                "eligible_whitelist_id": eligible_whitelist_id,
                "event_id": event_id,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "mandate_identifier": mandate_identifier,
                "minimum_age": minimum_age,
                "monetary_account_id": monetary_account_id,
                "redirect_url": redirect_url,
                "request_reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=request_reference_split_the_bill,
                    annotation=typing.Sequence[RequestInquiryReference],
                    direction="write",
                ),
                "require_address": require_address,
                "status": status,
                "sub_type": sub_type,
                "time_expiry": time_expiry,
                "time_refund_requested": time_refund_requested,
                "time_refunded": time_refunded,
                "time_responded": time_responded,
                "type": type,
                "updated": updated,
                "user_refund_requested": convert_and_respect_annotation_metadata(
                    object_=user_refund_requested, annotation=LabelUser, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestResponseUpdate,
                    parse_obj_as(
                        type_=RequestResponseUpdate,
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


class AsyncRawRequestResponseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_request_response_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RequestResponseListing]]:
        """
        Get all RequestResponses for a MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RequestResponseListing]]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestResponseListing],
                    parse_obj_as(
                        type_=typing.List[RequestResponseListing],
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

    async def read_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestResponseRead]:
        """
        Get the details for a specific existing RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestResponseRead]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-response/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestResponseRead,
                    parse_obj_as(
                        type_=RequestResponseRead,
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

    async def update_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        credit_scheme_identifier: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        eligible_whitelist_id: typing.Optional[int] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        mandate_identifier: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_refund_requested: typing.Optional[str] = OMIT,
        time_refunded: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_refund_requested: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestResponseUpdate]:
        """
        Update the status to accept or reject the RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount this RequestResponse was received on.

        amount_inquired : typing.Optional[Amount]
            The requested Amount.

        amount_responded : typing.Optional[Amount]
            The Amount the RequestResponse was accepted with.

        attachment : typing.Optional[typing.Sequence[Attachment]]
            The Attachments attached to the RequestResponse.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount that is requesting money with this RequestResponse.

        created : typing.Optional[str]
            The timestamp when the Request Response was created.

        credit_scheme_identifier : typing.Optional[str]
            The credit scheme id provided by the counterparty for DIRECT_DEBIT inquiries.

        description : typing.Optional[str]
            The description for the RequestResponse provided by the requesting party. Maximum 9000 characters.

        eligible_whitelist_id : typing.Optional[int]
            The whitelist id for this action or null.

        event_id : typing.Optional[int]
            The ID of the latest event for the request.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the RequestResponse was created.

        id : typing.Optional[int]
            The id of the Request Response.

        mandate_identifier : typing.Optional[str]
            The mandate id provided by the counterparty for DIRECT_DEBIT inquiries.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestResponse must have.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the RequestResponse was received on.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        status : typing.Optional[str]
            The status of the RequestResponse. Can be ACCEPTED, PENDING, REJECTED, REFUND_REQUESTED, REFUNDED or REVOKED.

        sub_type : typing.Optional[str]
            The subtype of the RequestInquiry. Can be ONCE or RECURRING for DIRECT_DEBIT RequestInquiries and NONE for all other.

        time_expiry : typing.Optional[str]
            The timestamp of when the RequestResponse expired or will expire.

        time_refund_requested : typing.Optional[str]
            The timestamp of when a refund request for the RequestResponse was claimed.

        time_refunded : typing.Optional[str]
            The timestamp of when the RequestResponse was refunded.

        time_responded : typing.Optional[str]
            The timestamp of when the RequestResponse was responded to.

        type : typing.Optional[str]
            The type of the RequestInquiry. Can be DIRECT_DEBIT, DIRECT_DEBIT_B2B, IDEAL, SOFORT or INTERNAL.

        updated : typing.Optional[str]
            The timestamp when the Request Response was last updated (will be updated when chat messages are received).

        user_refund_requested : typing.Optional[LabelUser]
            The label of the user that requested the refund.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestResponseUpdate]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id_)}/request-response/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "address_billing": convert_and_respect_annotation_metadata(
                    object_=address_billing, annotation=Address, direction="write"
                ),
                "address_shipping": convert_and_respect_annotation_metadata(
                    object_=address_shipping, annotation=Address, direction="write"
                ),
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "amount_inquired": convert_and_respect_annotation_metadata(
                    object_=amount_inquired, annotation=Amount, direction="write"
                ),
                "amount_responded": convert_and_respect_annotation_metadata(
                    object_=amount_responded, annotation=Amount, direction="write"
                ),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[Attachment], direction="write"
                ),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "credit_scheme_identifier": credit_scheme_identifier,
                "description": description,
                "eligible_whitelist_id": eligible_whitelist_id,
                "event_id": event_id,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "mandate_identifier": mandate_identifier,
                "minimum_age": minimum_age,
                "monetary_account_id": monetary_account_id,
                "redirect_url": redirect_url,
                "request_reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=request_reference_split_the_bill,
                    annotation=typing.Sequence[RequestInquiryReference],
                    direction="write",
                ),
                "require_address": require_address,
                "status": status,
                "sub_type": sub_type,
                "time_expiry": time_expiry,
                "time_refund_requested": time_refund_requested,
                "time_refunded": time_refunded,
                "time_responded": time_responded,
                "type": type,
                "updated": updated,
                "user_refund_requested": convert_and_respect_annotation_metadata(
                    object_=user_refund_requested, annotation=LabelUser, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestResponseUpdate,
                    parse_obj_as(
                        type_=RequestResponseUpdate,
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
