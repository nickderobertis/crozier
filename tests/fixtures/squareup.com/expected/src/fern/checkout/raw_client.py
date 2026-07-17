

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
from ..types.address import Address
from ..types.charge_request_additional_recipient import ChargeRequestAdditionalRecipient
from ..types.create_checkout_response import CreateCheckoutResponse
from ..types.create_order_request import CreateOrderRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCheckoutClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_checkout(
        self,
        location_id: str,
        *,
        idempotency_key: str,
        order: CreateOrderRequest,
        additional_recipients: typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]] = OMIT,
        ask_for_shipping_address: typing.Optional[bool] = OMIT,
        merchant_support_email: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        pre_populate_buyer_email: typing.Optional[str] = OMIT,
        pre_populate_shipping_address: typing.Optional[Address] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCheckoutResponse]:
        """
        Links a `checkoutId` to a `checkout_page_url` that customers are
        directed to in order to provide their payment information using a
        payment processing workflow hosted on connect.squareup.com.

        Parameters
        ----------
        location_id : str
            The ID of the business location to associate the checkout with.

        idempotency_key : str
            A unique string that identifies this checkout among others you have created. It can be
            any valid string but must be unique for every order sent to Square Checkout for a given location ID.

            The idempotency key is used to avoid processing the same order more than once. If you are
            unsure whether a particular checkout was created successfully, you can attempt it again with
            the same idempotency key and all the same other parameters without worrying about creating duplicates.

            You should use a random number/string generator native to the language
            you are working in to generate strings for your idempotency keys.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        order : CreateOrderRequest

        additional_recipients : typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]]
            The basic primitive of a multi-party transaction. The value is optional.
            The transaction facilitated by you can be split from here.

            If you provide this value, the `amount_money` value in your `additional_recipients` field
            cannot be more than 90% of the `total_money` calculated by Square for your order.
            The `location_id` must be a valid seller location where the checkout is occurring.

            This field requires `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

            This field is currently not supported in the Square Sandbox.

        ask_for_shipping_address : typing.Optional[bool]
            If `true`, Square Checkout collects shipping information on your behalf and stores
            that information with the transaction information in the Square Seller Dashboard.

            Default: `false`.

        merchant_support_email : typing.Optional[str]
            The email address to display on the Square Checkout confirmation page
            and confirmation email that the buyer can use to contact the seller.

            If this value is not set, the confirmation page and email display the
            primary email address associated with the seller's Square account.

            Default: none; only exists if explicitly set.

        note : typing.Optional[str]
            An optional note to associate with the `checkout` object.

            This value cannot exceed 60 characters.

        pre_populate_buyer_email : typing.Optional[str]
            If provided, the buyer's email is prepopulated on the checkout page
            as an editable text field.

            Default: none; only exists if explicitly set.

        pre_populate_shipping_address : typing.Optional[Address]

        redirect_url : typing.Optional[str]
            The URL to redirect to after the checkout is completed with `checkoutId`,
            `transactionId`, and `referenceId` appended as URL parameters. For example,
            if the provided redirect URL is `http://www.example.com/order-complete`, a
            successful transaction redirects the customer to:

            <pre><code>http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx</code></pre>

            If you do not provide a redirect URL, Square Checkout displays an order
            confirmation page on your behalf; however, it is strongly recommended that
            you provide a redirect URL so you can verify the transaction results and
            finalize the order through your existing/normal confirmation workflow.

            Default: none; only exists if explicitly set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCheckoutResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/checkouts",
            method="POST",
            json={
                "additional_recipients": convert_and_respect_annotation_metadata(
                    object_=additional_recipients,
                    annotation=typing.Sequence[ChargeRequestAdditionalRecipient],
                    direction="write",
                ),
                "ask_for_shipping_address": ask_for_shipping_address,
                "idempotency_key": idempotency_key,
                "merchant_support_email": merchant_support_email,
                "note": note,
                "order": convert_and_respect_annotation_metadata(
                    object_=order, annotation=CreateOrderRequest, direction="write"
                ),
                "pre_populate_buyer_email": pre_populate_buyer_email,
                "pre_populate_shipping_address": convert_and_respect_annotation_metadata(
                    object_=pre_populate_shipping_address, annotation=Address, direction="write"
                ),
                "redirect_url": redirect_url,
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
                    CreateCheckoutResponse,
                    parse_obj_as(
                        type_=CreateCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCheckoutClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_checkout(
        self,
        location_id: str,
        *,
        idempotency_key: str,
        order: CreateOrderRequest,
        additional_recipients: typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]] = OMIT,
        ask_for_shipping_address: typing.Optional[bool] = OMIT,
        merchant_support_email: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        pre_populate_buyer_email: typing.Optional[str] = OMIT,
        pre_populate_shipping_address: typing.Optional[Address] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCheckoutResponse]:
        """
        Links a `checkoutId` to a `checkout_page_url` that customers are
        directed to in order to provide their payment information using a
        payment processing workflow hosted on connect.squareup.com.

        Parameters
        ----------
        location_id : str
            The ID of the business location to associate the checkout with.

        idempotency_key : str
            A unique string that identifies this checkout among others you have created. It can be
            any valid string but must be unique for every order sent to Square Checkout for a given location ID.

            The idempotency key is used to avoid processing the same order more than once. If you are
            unsure whether a particular checkout was created successfully, you can attempt it again with
            the same idempotency key and all the same other parameters without worrying about creating duplicates.

            You should use a random number/string generator native to the language
            you are working in to generate strings for your idempotency keys.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        order : CreateOrderRequest

        additional_recipients : typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]]
            The basic primitive of a multi-party transaction. The value is optional.
            The transaction facilitated by you can be split from here.

            If you provide this value, the `amount_money` value in your `additional_recipients` field
            cannot be more than 90% of the `total_money` calculated by Square for your order.
            The `location_id` must be a valid seller location where the checkout is occurring.

            This field requires `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

            This field is currently not supported in the Square Sandbox.

        ask_for_shipping_address : typing.Optional[bool]
            If `true`, Square Checkout collects shipping information on your behalf and stores
            that information with the transaction information in the Square Seller Dashboard.

            Default: `false`.

        merchant_support_email : typing.Optional[str]
            The email address to display on the Square Checkout confirmation page
            and confirmation email that the buyer can use to contact the seller.

            If this value is not set, the confirmation page and email display the
            primary email address associated with the seller's Square account.

            Default: none; only exists if explicitly set.

        note : typing.Optional[str]
            An optional note to associate with the `checkout` object.

            This value cannot exceed 60 characters.

        pre_populate_buyer_email : typing.Optional[str]
            If provided, the buyer's email is prepopulated on the checkout page
            as an editable text field.

            Default: none; only exists if explicitly set.

        pre_populate_shipping_address : typing.Optional[Address]

        redirect_url : typing.Optional[str]
            The URL to redirect to after the checkout is completed with `checkoutId`,
            `transactionId`, and `referenceId` appended as URL parameters. For example,
            if the provided redirect URL is `http://www.example.com/order-complete`, a
            successful transaction redirects the customer to:

            <pre><code>http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx</code></pre>

            If you do not provide a redirect URL, Square Checkout displays an order
            confirmation page on your behalf; however, it is strongly recommended that
            you provide a redirect URL so you can verify the transaction results and
            finalize the order through your existing/normal confirmation workflow.

            Default: none; only exists if explicitly set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCheckoutResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/checkouts",
            method="POST",
            json={
                "additional_recipients": convert_and_respect_annotation_metadata(
                    object_=additional_recipients,
                    annotation=typing.Sequence[ChargeRequestAdditionalRecipient],
                    direction="write",
                ),
                "ask_for_shipping_address": ask_for_shipping_address,
                "idempotency_key": idempotency_key,
                "merchant_support_email": merchant_support_email,
                "note": note,
                "order": convert_and_respect_annotation_metadata(
                    object_=order, annotation=CreateOrderRequest, direction="write"
                ),
                "pre_populate_buyer_email": pre_populate_buyer_email,
                "pre_populate_shipping_address": convert_and_respect_annotation_metadata(
                    object_=pre_populate_shipping_address, annotation=Address, direction="write"
                ),
                "redirect_url": redirect_url,
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
                    CreateCheckoutResponse,
                    parse_obj_as(
                        type_=CreateCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
