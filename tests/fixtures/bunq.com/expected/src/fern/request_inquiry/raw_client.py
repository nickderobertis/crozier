

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.address import Address
from ..types.amount import Amount
from ..types.bunq_id import BunqId
from ..types.geolocation import Geolocation
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.label_user import LabelUser
from ..types.request_inquiry_create import RequestInquiryCreate
from ..types.request_inquiry_listing import RequestInquiryListing
from ..types.request_inquiry_read import RequestInquiryRead
from ..types.request_inquiry_update import RequestInquiryUpdate
from ..types.request_reference_split_the_bill_anchor_object import RequestReferenceSplitTheBillAnchorObject
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRequestInquiryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_request_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RequestInquiryListing]]:
        """
        Get all payment requests for a user's monetary account. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RequestInquiryListing]]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestInquiryListing],
                    parse_obj_as(
                        type_=typing.List[RequestInquiryListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestInquiryCreate]:
        """
        Create a new payment request.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInquiryCreate]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/request-inquiry",
            method="POST",
            json={
                "address_billing": convert_and_respect_annotation_metadata(
                    object_=address_billing, annotation=Address, direction="write"
                ),
                "address_shipping": convert_and_respect_annotation_metadata(
                    object_=address_shipping, annotation=Address, direction="write"
                ),
                "allow_amount_higher": allow_amount_higher,
                "allow_amount_lower": allow_amount_lower,
                "allow_bunqme": allow_bunqme,
                "amount_inquired": convert_and_respect_annotation_metadata(
                    object_=amount_inquired, annotation=Amount, direction="write"
                ),
                "amount_responded": convert_and_respect_annotation_metadata(
                    object_=amount_responded, annotation=Amount, direction="write"
                ),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[BunqId], direction="write"
                ),
                "batch_id": batch_id,
                "bunqme_share_url": bunqme_share_url,
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "event_id": event_id,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "merchant_reference": merchant_reference,
                "minimum_age": minimum_age,
                "monetary_account_id": monetary_account_id,
                "redirect_url": redirect_url,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "require_address": require_address,
                "scheduled_id": scheduled_id,
                "status": status,
                "time_expiry": time_expiry,
                "time_responded": time_responded,
                "updated": updated,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
                ),
                "want_tip": want_tip,
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
                    RequestInquiryCreate,
                    parse_obj_as(
                        type_=RequestInquiryCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestInquiryRead]:
        """
        Get the details of a specific payment request, including its status. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInquiryRead]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInquiryRead,
                    parse_obj_as(
                        type_=RequestInquiryRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestInquiryUpdate]:
        """
        Revoke a request for payment, by updating the status to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInquiryUpdate]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/request-inquiry/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_billing": convert_and_respect_annotation_metadata(
                    object_=address_billing, annotation=Address, direction="write"
                ),
                "address_shipping": convert_and_respect_annotation_metadata(
                    object_=address_shipping, annotation=Address, direction="write"
                ),
                "allow_amount_higher": allow_amount_higher,
                "allow_amount_lower": allow_amount_lower,
                "allow_bunqme": allow_bunqme,
                "amount_inquired": convert_and_respect_annotation_metadata(
                    object_=amount_inquired, annotation=Amount, direction="write"
                ),
                "amount_responded": convert_and_respect_annotation_metadata(
                    object_=amount_responded, annotation=Amount, direction="write"
                ),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[BunqId], direction="write"
                ),
                "batch_id": batch_id,
                "bunqme_share_url": bunqme_share_url,
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "event_id": event_id,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "merchant_reference": merchant_reference,
                "minimum_age": minimum_age,
                "monetary_account_id": monetary_account_id,
                "redirect_url": redirect_url,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "require_address": require_address,
                "scheduled_id": scheduled_id,
                "status": status,
                "time_expiry": time_expiry,
                "time_responded": time_responded,
                "updated": updated,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
                ),
                "want_tip": want_tip,
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
                    RequestInquiryUpdate,
                    parse_obj_as(
                        type_=RequestInquiryUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawRequestInquiryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_request_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RequestInquiryListing]]:
        """
        Get all payment requests for a user's monetary account. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RequestInquiryListing]]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestInquiryListing],
                    parse_obj_as(
                        type_=typing.List[RequestInquiryListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestInquiryCreate]:
        """
        Create a new payment request.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInquiryCreate]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/request-inquiry",
            method="POST",
            json={
                "address_billing": convert_and_respect_annotation_metadata(
                    object_=address_billing, annotation=Address, direction="write"
                ),
                "address_shipping": convert_and_respect_annotation_metadata(
                    object_=address_shipping, annotation=Address, direction="write"
                ),
                "allow_amount_higher": allow_amount_higher,
                "allow_amount_lower": allow_amount_lower,
                "allow_bunqme": allow_bunqme,
                "amount_inquired": convert_and_respect_annotation_metadata(
                    object_=amount_inquired, annotation=Amount, direction="write"
                ),
                "amount_responded": convert_and_respect_annotation_metadata(
                    object_=amount_responded, annotation=Amount, direction="write"
                ),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[BunqId], direction="write"
                ),
                "batch_id": batch_id,
                "bunqme_share_url": bunqme_share_url,
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "event_id": event_id,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "merchant_reference": merchant_reference,
                "minimum_age": minimum_age,
                "monetary_account_id": monetary_account_id,
                "redirect_url": redirect_url,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "require_address": require_address,
                "scheduled_id": scheduled_id,
                "status": status,
                "time_expiry": time_expiry,
                "time_responded": time_responded,
                "updated": updated,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
                ),
                "want_tip": want_tip,
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
                    RequestInquiryCreate,
                    parse_obj_as(
                        type_=RequestInquiryCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestInquiryRead]:
        """
        Get the details of a specific payment request, including its status. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInquiryRead]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/request-inquiry/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInquiryRead,
                    parse_obj_as(
                        type_=RequestInquiryRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestInquiryUpdate]:
        """
        Revoke a request for payment, by updating the status to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInquiryUpdate]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/request-inquiry/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_billing": convert_and_respect_annotation_metadata(
                    object_=address_billing, annotation=Address, direction="write"
                ),
                "address_shipping": convert_and_respect_annotation_metadata(
                    object_=address_shipping, annotation=Address, direction="write"
                ),
                "allow_amount_higher": allow_amount_higher,
                "allow_amount_lower": allow_amount_lower,
                "allow_bunqme": allow_bunqme,
                "amount_inquired": convert_and_respect_annotation_metadata(
                    object_=amount_inquired, annotation=Amount, direction="write"
                ),
                "amount_responded": convert_and_respect_annotation_metadata(
                    object_=amount_responded, annotation=Amount, direction="write"
                ),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[BunqId], direction="write"
                ),
                "batch_id": batch_id,
                "bunqme_share_url": bunqme_share_url,
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "event_id": event_id,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "merchant_reference": merchant_reference,
                "minimum_age": minimum_age,
                "monetary_account_id": monetary_account_id,
                "redirect_url": redirect_url,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "require_address": require_address,
                "scheduled_id": scheduled_id,
                "status": status,
                "time_expiry": time_expiry,
                "time_responded": time_responded,
                "updated": updated,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
                ),
                "want_tip": want_tip,
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
                    RequestInquiryUpdate,
                    parse_obj_as(
                        type_=RequestInquiryUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
