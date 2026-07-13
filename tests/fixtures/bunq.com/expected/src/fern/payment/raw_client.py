

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
from ..types.attachment_monetary_account_payment import AttachmentMonetaryAccountPayment
from ..types.geolocation import Geolocation
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.master_card_payment_listing import MasterCardPaymentListing
from ..types.payment_auto_allocate_instance import PaymentAutoAllocateInstance
from ..types.payment_create import PaymentCreate
from ..types.payment_listing import PaymentListing
from ..types.payment_read import PaymentRead
from ..types.request_inquiry_reference import RequestInquiryReference


OMIT = typing.cast(typing.Any, ...)


class RawPaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_payment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[MasterCardPaymentListing]]:
        """
        MasterCard transaction view.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[MasterCardPaymentListing]]
            MasterCard transaction view.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MasterCardPaymentListing],
                    parse_obj_as(
                        type_=typing.List[MasterCardPaymentListing],
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

    def list_all_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PaymentListing]]:
        """
        Get a listing of all Payments performed on a given MonetaryAccount (incoming and outgoing).

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PaymentListing]]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentListing],
                    parse_obj_as(
                        type_=typing.List[PaymentListing],
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

    def create_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        allow_bunqto: typing.Optional[bool] = OMIT,
        amount: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]] = OMIT,
        balance_after_mutation: typing.Optional[Amount] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqto_expiry: typing.Optional[str] = OMIT,
        bunqto_share_url: typing.Optional[str] = OMIT,
        bunqto_status: typing.Optional[str] = OMIT,
        bunqto_sub_status: typing.Optional[str] = OMIT,
        bunqto_time_responded: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        payment_auto_allocate_instance: typing.Optional[PaymentAutoAllocateInstance] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentCreate]:
        """
        Create a new Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        address_billing : typing.Optional[Address]
            A billing Address provided with the Payment, currently unused.

        address_shipping : typing.Optional[Address]
            A shipping Address provided with the Payment, currently unused.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        allow_bunqto : typing.Optional[bool]
            Whether or not sending a bunq.to payment is allowed.

        amount : typing.Optional[Amount]
            The Amount transferred by the Payment. Will be negative for outgoing Payments and positive for incoming Payments (relative to the MonetaryAccount indicated by monetary_account_id).

        attachment : typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]]
            The Attachments attached to the Payment.

        balance_after_mutation : typing.Optional[Amount]
            The new balance of the monetary account after the mutation.

        batch_id : typing.Optional[int]
            The id of the PaymentBatch if this Payment was part of one.

        bunqto_expiry : typing.Optional[str]
            When bunq.to payment is about to expire.

        bunqto_share_url : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_status : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_sub_status : typing.Optional[str]
            The sub status of the bunq.to payment.

        bunqto_time_responded : typing.Optional[str]
            The timestamp of when the bunq.to payment was responded to.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        created : typing.Optional[str]
            The timestamp when the Payment was done.

        description : typing.Optional[str]
            The description for the Payment. Maximum 140 characters for Payments to external IBANs, 9000 characters for Payments to only other bunq MonetaryAccounts.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the Payment was done from.

        id : typing.Optional[int]
            The id of the created Payment.

        merchant_reference : typing.Optional[str]
            Optional data included with the Payment specific to the merchant.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the Payment was made to or from (depending on whether this is an incoming or outgoing Payment).

        payment_auto_allocate_instance : typing.Optional[PaymentAutoAllocateInstance]
            A reference to the PaymentAutoAllocateInstance if it exists.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        scheduled_id : typing.Optional[int]
            The id of the JobScheduled if the Payment was scheduled.

        sub_type : typing.Optional[str]
            The sub-type of the Payment, can be PAYMENT, WITHDRAWAL, REVERSAL, REQUEST, BILLING, SCT, SDD or NLO.

        type : typing.Optional[str]
            The type of Payment, can be BUNQ, EBA_SCT, EBA_SDD, IDEAL, SWIFT or FIS (card).

        updated : typing.Optional[str]
            The timestamp when the Payment was last updated (will be updated when chat messages are received).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentCreate]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id_)}/payment",
            method="POST",
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
                "allow_bunqto": allow_bunqto,
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[AttachmentMonetaryAccountPayment], direction="write"
                ),
                "balance_after_mutation": convert_and_respect_annotation_metadata(
                    object_=balance_after_mutation, annotation=Amount, direction="write"
                ),
                "batch_id": batch_id,
                "bunqto_expiry": bunqto_expiry,
                "bunqto_share_url": bunqto_share_url,
                "bunqto_status": bunqto_status,
                "bunqto_sub_status": bunqto_sub_status,
                "bunqto_time_responded": bunqto_time_responded,
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "merchant_reference": merchant_reference,
                "monetary_account_id": monetary_account_id,
                "payment_auto_allocate_instance": convert_and_respect_annotation_metadata(
                    object_=payment_auto_allocate_instance, annotation=PaymentAutoAllocateInstance, direction="write"
                ),
                "request_reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=request_reference_split_the_bill,
                    annotation=typing.Sequence[RequestInquiryReference],
                    direction="write",
                ),
                "scheduled_id": scheduled_id,
                "sub_type": sub_type,
                "type": type,
                "updated": updated,
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
                    PaymentCreate,
                    parse_obj_as(
                        type_=PaymentCreate,
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

    def read_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentRead]:
        """
        Get a specific previous Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentRead]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentRead,
                    parse_obj_as(
                        type_=PaymentRead,
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


class AsyncRawPaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_payment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[MasterCardPaymentListing]]:
        """
        MasterCard transaction view.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[MasterCardPaymentListing]]
            MasterCard transaction view.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/mastercard-action/{jsonable_encoder(mastercard_action_id)}/payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MasterCardPaymentListing],
                    parse_obj_as(
                        type_=typing.List[MasterCardPaymentListing],
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

    async def list_all_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PaymentListing]]:
        """
        Get a listing of all Payments performed on a given MonetaryAccount (incoming and outgoing).

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PaymentListing]]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentListing],
                    parse_obj_as(
                        type_=typing.List[PaymentListing],
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

    async def create_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        allow_bunqto: typing.Optional[bool] = OMIT,
        amount: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]] = OMIT,
        balance_after_mutation: typing.Optional[Amount] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqto_expiry: typing.Optional[str] = OMIT,
        bunqto_share_url: typing.Optional[str] = OMIT,
        bunqto_status: typing.Optional[str] = OMIT,
        bunqto_sub_status: typing.Optional[str] = OMIT,
        bunqto_time_responded: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        payment_auto_allocate_instance: typing.Optional[PaymentAutoAllocateInstance] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentCreate]:
        """
        Create a new Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        address_billing : typing.Optional[Address]
            A billing Address provided with the Payment, currently unused.

        address_shipping : typing.Optional[Address]
            A shipping Address provided with the Payment, currently unused.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        allow_bunqto : typing.Optional[bool]
            Whether or not sending a bunq.to payment is allowed.

        amount : typing.Optional[Amount]
            The Amount transferred by the Payment. Will be negative for outgoing Payments and positive for incoming Payments (relative to the MonetaryAccount indicated by monetary_account_id).

        attachment : typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]]
            The Attachments attached to the Payment.

        balance_after_mutation : typing.Optional[Amount]
            The new balance of the monetary account after the mutation.

        batch_id : typing.Optional[int]
            The id of the PaymentBatch if this Payment was part of one.

        bunqto_expiry : typing.Optional[str]
            When bunq.to payment is about to expire.

        bunqto_share_url : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_status : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_sub_status : typing.Optional[str]
            The sub status of the bunq.to payment.

        bunqto_time_responded : typing.Optional[str]
            The timestamp of when the bunq.to payment was responded to.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        created : typing.Optional[str]
            The timestamp when the Payment was done.

        description : typing.Optional[str]
            The description for the Payment. Maximum 140 characters for Payments to external IBANs, 9000 characters for Payments to only other bunq MonetaryAccounts.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the Payment was done from.

        id : typing.Optional[int]
            The id of the created Payment.

        merchant_reference : typing.Optional[str]
            Optional data included with the Payment specific to the merchant.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the Payment was made to or from (depending on whether this is an incoming or outgoing Payment).

        payment_auto_allocate_instance : typing.Optional[PaymentAutoAllocateInstance]
            A reference to the PaymentAutoAllocateInstance if it exists.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        scheduled_id : typing.Optional[int]
            The id of the JobScheduled if the Payment was scheduled.

        sub_type : typing.Optional[str]
            The sub-type of the Payment, can be PAYMENT, WITHDRAWAL, REVERSAL, REQUEST, BILLING, SCT, SDD or NLO.

        type : typing.Optional[str]
            The type of Payment, can be BUNQ, EBA_SCT, EBA_SDD, IDEAL, SWIFT or FIS (card).

        updated : typing.Optional[str]
            The timestamp when the Payment was last updated (will be updated when chat messages are received).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentCreate]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id_)}/payment",
            method="POST",
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
                "allow_bunqto": allow_bunqto,
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "attachment": convert_and_respect_annotation_metadata(
                    object_=attachment, annotation=typing.Sequence[AttachmentMonetaryAccountPayment], direction="write"
                ),
                "balance_after_mutation": convert_and_respect_annotation_metadata(
                    object_=balance_after_mutation, annotation=Amount, direction="write"
                ),
                "batch_id": batch_id,
                "bunqto_expiry": bunqto_expiry,
                "bunqto_share_url": bunqto_share_url,
                "bunqto_status": bunqto_status,
                "bunqto_sub_status": bunqto_sub_status,
                "bunqto_time_responded": bunqto_time_responded,
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "geolocation": convert_and_respect_annotation_metadata(
                    object_=geolocation, annotation=Geolocation, direction="write"
                ),
                "id": id,
                "merchant_reference": merchant_reference,
                "monetary_account_id": monetary_account_id,
                "payment_auto_allocate_instance": convert_and_respect_annotation_metadata(
                    object_=payment_auto_allocate_instance, annotation=PaymentAutoAllocateInstance, direction="write"
                ),
                "request_reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=request_reference_split_the_bill,
                    annotation=typing.Sequence[RequestInquiryReference],
                    direction="write",
                ),
                "scheduled_id": scheduled_id,
                "sub_type": sub_type,
                "type": type,
                "updated": updated,
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
                    PaymentCreate,
                    parse_obj_as(
                        type_=PaymentCreate,
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

    async def read_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentRead]:
        """
        Get a specific previous Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentRead]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentRead,
                    parse_obj_as(
                        type_=PaymentRead,
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
