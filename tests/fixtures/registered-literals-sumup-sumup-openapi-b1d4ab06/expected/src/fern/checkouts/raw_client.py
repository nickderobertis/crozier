

import datetime as dt
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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.card import Card
from ..types.checkout import Checkout
from ..types.checkout_success import CheckoutSuccess
from ..types.currency import Currency
from ..types.hosted_checkout import HostedCheckout
from ..types.mandate_payload import MandatePayload
from ..types.personal_details import PersonalDetails
from .types.checkout_create_request_purpose import CheckoutCreateRequestPurpose
from .types.get_payment_methods_response import GetPaymentMethodsResponse
from .types.process_checkout_payment_type import ProcessCheckoutPaymentType
from .types.process_checkout_response import ProcessCheckoutResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCheckoutsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_payment_methods(
        self,
        merchant_code: str,
        *,
        amount: typing.Optional[float] = None,
        currency: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPaymentMethodsResponse]:
        """
        Get payment methods available for the given merchant to use with a checkout.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        amount : typing.Optional[float]
            The amount for which the payment methods should be eligible, in major units.

        currency : typing.Optional[str]
            The currency for which the payment methods should be eligible.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPaymentMethodsResponse]
            Available payment methods
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/payment-methods",
            method="GET",
            params={
                "amount": amount,
                "currency": currency,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPaymentMethodsResponse,
                    parse_obj_as(
                        type_=GetPaymentMethodsResponse,
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

    def list_checkouts(
        self,
        *,
        checkout_reference: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CheckoutSuccess]]:
        """
        Lists created checkout resources according to the applied `checkout_reference`.

        Parameters
        ----------
        checkout_reference : typing.Optional[str]
            Filters the list of checkout resources by the unique reference of the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CheckoutSuccess]]
            Returns a list of checkout resources.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/checkouts",
            method="GET",
            params={
                "checkout_reference": checkout_reference,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CheckoutSuccess],
                    parse_obj_as(
                        type_=typing.List[CheckoutSuccess],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def create_checkout(
        self,
        *,
        checkout_reference: str,
        amount: float,
        currency: Currency,
        merchant_code: str,
        description: typing.Optional[str] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        purpose: typing.Optional[CheckoutCreateRequestPurpose] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        hosted_checkout: typing.Optional[HostedCheckout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Checkout]:
        """
        Creates a payment checkout for the specified merchant, amount, and currency. Supply a `checkout_reference` to identify the payment attempt in your own systems. Creating a checkout does not charge a payment instrument.

        Set `hosted_checkout.enabled` to `true` to receive a [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) URL where the customer can complete the payment.
        Use `redirect_url` for redirect-based payment and 3DS flows. If `return_url` is provided, SumUp sends processing updates to that backend callback URL.

        Complete the payment through [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) or the [Payment Widget](https://developer.sumup.com/online-payments/checkouts/card-widget).

        Parameters
        ----------
        checkout_reference : str
            Merchant-defined reference for the new checkout. It should be unique enough for you to identify the payment attempt in your own systems.

        amount : float
            Amount to be charged to the payer, expressed in major units.

        currency : Currency

        merchant_code : str
            Short unique identifier for the merchant that should receive the payment.

        description : typing.Optional[str]
            Short merchant-defined description shown in SumUp tools and reporting for easier identification of the checkout.

        return_url : typing.Optional[str]
            Optional backend callback URL used by SumUp to notify your platform about processing updates for the checkout.

        customer_id : typing.Optional[str]
            Merchant-scoped customer identifier. Required when setting up recurring payments and useful when the checkout should be linked to a returning payer.

        purpose : typing.Optional[CheckoutCreateRequestPurpose]
            Business purpose of the checkout. Use `CHECKOUT` for a standard payment and `SETUP_RECURRING_PAYMENT` when collecting consent and payment details for future recurring charges.

        valid_until : typing.Optional[dt.datetime]
            Optional expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable. If omitted, the checkout does not have an explicit expiry time.

        redirect_url : typing.Optional[str]
            URL where the payer should be sent after a redirect-based payment or SCA flow completes. This is required for [APMs](https://developer.sumup.com/online-payments/apm/introduction) and recommended for card checkouts that may require [3DS](https://developer.sumup.com/online-payments/features/3ds). If it is omitted, the [Payment Widget](https://developer.sumup.com/online-payments/checkouts) can render the challenge in an iframe instead of using a full-page redirect.

        hosted_checkout : typing.Optional[HostedCheckout]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Checkout]
            Returns the created checkout resource.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/checkouts",
            method="POST",
            json={
                "checkout_reference": checkout_reference,
                "amount": amount,
                "currency": currency,
                "merchant_code": merchant_code,
                "description": description,
                "return_url": return_url,
                "customer_id": customer_id,
                "purpose": purpose,
                "valid_until": valid_until,
                "redirect_url": redirect_url,
                "hosted_checkout": convert_and_respect_annotation_metadata(
                    object_=hosted_checkout, annotation=HostedCheckout, direction="write"
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
                    Checkout,
                    parse_obj_as(
                        type_=Checkout,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckoutSuccess]:
        """
        Retrieves an identified checkout resource. Use this request after processing a checkout to confirm its status and inform the end user respectively.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckoutSuccess]
            Returns the requested checkout resource.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckoutSuccess,
                    parse_obj_as(
                        type_=CheckoutSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def process_checkout(
        self,
        checkout_id: str,
        *,
        payment_type: ProcessCheckoutPaymentType,
        installments: typing.Optional[int] = OMIT,
        mandate: typing.Optional[MandatePayload] = OMIT,
        card: typing.Optional[Card] = OMIT,
        google_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        apple_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        token: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcessCheckoutResponse]:
        """
        :::caution[PCI DSS compliance required]
        When you submit raw card details directly to the Checkout API, your systems store, process, or transmit cardholder data and are therefore subject to applicable [PCI DSS requirements](https://www.pcisecuritystandards.org/document_library/). You should only use this integration if your environment is appropriately PCI DSS compliant.
        :::

        Processing a checkout will attempt to charge the provided payment instrument for the amount of the specified checkout resource initiated in the `Create a checkout` endpoint.

        Follow this request with `Retrieve a checkout` to confirm its status.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        payment_type : ProcessCheckoutPaymentType
            Payment method used for this processing attempt. It determines which additional request fields are required.

        installments : typing.Optional[int]
            Number of installments for deferred payments. Available only to merchant users in Brazil.

        mandate : typing.Optional[MandatePayload]

        card : typing.Optional[Card]

        google_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw `PaymentData` object received from Google Pay. Send the Google Pay response payload as-is.

        apple_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw payment token object received from Apple Pay. Send the Apple Pay response payload as-is.

        token : typing.Optional[str]
            Saved-card token to use instead of raw card details when processing with a previously stored payment instrument.

        customer_id : typing.Optional[str]
            Customer identifier associated with the saved payment instrument. Required when `token` is provided.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProcessCheckoutResponse]
            Returns the checkout resource after a processing attempt.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="PUT",
            json={
                "payment_type": payment_type,
                "installments": installments,
                "mandate": convert_and_respect_annotation_metadata(
                    object_=mandate, annotation=MandatePayload, direction="write"
                ),
                "card": convert_and_respect_annotation_metadata(object_=card, annotation=Card, direction="write"),
                "google_pay": google_pay,
                "apple_pay": apple_pay,
                "token": token,
                "customer_id": customer_id,
                "personal_details": convert_and_respect_annotation_metadata(
                    object_=personal_details, annotation=PersonalDetails, direction="write"
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
                    ProcessCheckoutResponse,
                    parse_obj_as(
                        type_=ProcessCheckoutResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    def deactivate_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Checkout]:
        """
        Deactivates an identified checkout resource. If the checkout has already been processed it can not be deactivated.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Checkout]
            Returns the checkout object after successful deactivation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Checkout,
                    parse_obj_as(
                        type_=Checkout,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    def update_checkout(
        self,
        checkout_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        description: typing.Optional[str] = OMIT,
        checkout_reference: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Checkout]:
        """
        Updates the amount, currency, description, reference, expiration, or customer associated with an existing checkout. Only the supplied fields are updated.

        This request changes the checkout details; it does not charge a payment instrument. Process the checkout separately to attempt a payment.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        amount : typing.Optional[float]
            Updated amount to be charged to the payer, expressed in major units.

        currency : typing.Optional[Currency]

        description : typing.Optional[str]
            Updated short merchant-defined description shown in SumUp tools and reporting.

        checkout_reference : typing.Optional[str]
            Updated merchant-defined reference for the checkout.

        valid_until : typing.Optional[dt.datetime]
            Updated expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable.

        customer_id : typing.Optional[str]
            Updated merchant-scoped customer identifier associated with the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Checkout]
            Returns the updated checkout resource.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="PATCH",
            json={
                "amount": amount,
                "currency": currency,
                "description": description,
                "checkout_reference": checkout_reference,
                "valid_until": valid_until,
                "customer_id": customer_id,
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
                    Checkout,
                    parse_obj_as(
                        type_=Checkout,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def create_apple_pay_session(
        self, checkout_id: str, *, context: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Creates an Apple Pay merchant session for the specified checkout.

        Use this endpoint after the customer selects Apple Pay and before calling
        `ApplePaySession.completeMerchantValidation(...)` in the browser.
        SumUp validates the merchant session request and returns the Apple Pay
        session object that your frontend should pass to Apple's JavaScript API.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        context : str
            the context to create this apple pay session.

        target : str
            The target url to create this apple pay session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful request. Returns the Apple Pay merchant session object
            that should be forwarded to the Apple Pay JS SDK to complete merchant
            validation and continue the payment flow.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.2/checkouts/{encode_path_param(checkout_id)}/apple-pay-session",
            method="PUT",
            json={
                "context": context,
                "target": target,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawCheckoutsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_payment_methods(
        self,
        merchant_code: str,
        *,
        amount: typing.Optional[float] = None,
        currency: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPaymentMethodsResponse]:
        """
        Get payment methods available for the given merchant to use with a checkout.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        amount : typing.Optional[float]
            The amount for which the payment methods should be eligible, in major units.

        currency : typing.Optional[str]
            The currency for which the payment methods should be eligible.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPaymentMethodsResponse]
            Available payment methods
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/payment-methods",
            method="GET",
            params={
                "amount": amount,
                "currency": currency,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPaymentMethodsResponse,
                    parse_obj_as(
                        type_=GetPaymentMethodsResponse,
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

    async def list_checkouts(
        self,
        *,
        checkout_reference: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CheckoutSuccess]]:
        """
        Lists created checkout resources according to the applied `checkout_reference`.

        Parameters
        ----------
        checkout_reference : typing.Optional[str]
            Filters the list of checkout resources by the unique reference of the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CheckoutSuccess]]
            Returns a list of checkout resources.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/checkouts",
            method="GET",
            params={
                "checkout_reference": checkout_reference,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CheckoutSuccess],
                    parse_obj_as(
                        type_=typing.List[CheckoutSuccess],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def create_checkout(
        self,
        *,
        checkout_reference: str,
        amount: float,
        currency: Currency,
        merchant_code: str,
        description: typing.Optional[str] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        purpose: typing.Optional[CheckoutCreateRequestPurpose] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        hosted_checkout: typing.Optional[HostedCheckout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Checkout]:
        """
        Creates a payment checkout for the specified merchant, amount, and currency. Supply a `checkout_reference` to identify the payment attempt in your own systems. Creating a checkout does not charge a payment instrument.

        Set `hosted_checkout.enabled` to `true` to receive a [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) URL where the customer can complete the payment.
        Use `redirect_url` for redirect-based payment and 3DS flows. If `return_url` is provided, SumUp sends processing updates to that backend callback URL.

        Complete the payment through [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) or the [Payment Widget](https://developer.sumup.com/online-payments/checkouts/card-widget).

        Parameters
        ----------
        checkout_reference : str
            Merchant-defined reference for the new checkout. It should be unique enough for you to identify the payment attempt in your own systems.

        amount : float
            Amount to be charged to the payer, expressed in major units.

        currency : Currency

        merchant_code : str
            Short unique identifier for the merchant that should receive the payment.

        description : typing.Optional[str]
            Short merchant-defined description shown in SumUp tools and reporting for easier identification of the checkout.

        return_url : typing.Optional[str]
            Optional backend callback URL used by SumUp to notify your platform about processing updates for the checkout.

        customer_id : typing.Optional[str]
            Merchant-scoped customer identifier. Required when setting up recurring payments and useful when the checkout should be linked to a returning payer.

        purpose : typing.Optional[CheckoutCreateRequestPurpose]
            Business purpose of the checkout. Use `CHECKOUT` for a standard payment and `SETUP_RECURRING_PAYMENT` when collecting consent and payment details for future recurring charges.

        valid_until : typing.Optional[dt.datetime]
            Optional expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable. If omitted, the checkout does not have an explicit expiry time.

        redirect_url : typing.Optional[str]
            URL where the payer should be sent after a redirect-based payment or SCA flow completes. This is required for [APMs](https://developer.sumup.com/online-payments/apm/introduction) and recommended for card checkouts that may require [3DS](https://developer.sumup.com/online-payments/features/3ds). If it is omitted, the [Payment Widget](https://developer.sumup.com/online-payments/checkouts) can render the challenge in an iframe instead of using a full-page redirect.

        hosted_checkout : typing.Optional[HostedCheckout]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Checkout]
            Returns the created checkout resource.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/checkouts",
            method="POST",
            json={
                "checkout_reference": checkout_reference,
                "amount": amount,
                "currency": currency,
                "merchant_code": merchant_code,
                "description": description,
                "return_url": return_url,
                "customer_id": customer_id,
                "purpose": purpose,
                "valid_until": valid_until,
                "redirect_url": redirect_url,
                "hosted_checkout": convert_and_respect_annotation_metadata(
                    object_=hosted_checkout, annotation=HostedCheckout, direction="write"
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
                    Checkout,
                    parse_obj_as(
                        type_=Checkout,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckoutSuccess]:
        """
        Retrieves an identified checkout resource. Use this request after processing a checkout to confirm its status and inform the end user respectively.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckoutSuccess]
            Returns the requested checkout resource.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckoutSuccess,
                    parse_obj_as(
                        type_=CheckoutSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def process_checkout(
        self,
        checkout_id: str,
        *,
        payment_type: ProcessCheckoutPaymentType,
        installments: typing.Optional[int] = OMIT,
        mandate: typing.Optional[MandatePayload] = OMIT,
        card: typing.Optional[Card] = OMIT,
        google_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        apple_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        token: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProcessCheckoutResponse]:
        """
        :::caution[PCI DSS compliance required]
        When you submit raw card details directly to the Checkout API, your systems store, process, or transmit cardholder data and are therefore subject to applicable [PCI DSS requirements](https://www.pcisecuritystandards.org/document_library/). You should only use this integration if your environment is appropriately PCI DSS compliant.
        :::

        Processing a checkout will attempt to charge the provided payment instrument for the amount of the specified checkout resource initiated in the `Create a checkout` endpoint.

        Follow this request with `Retrieve a checkout` to confirm its status.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        payment_type : ProcessCheckoutPaymentType
            Payment method used for this processing attempt. It determines which additional request fields are required.

        installments : typing.Optional[int]
            Number of installments for deferred payments. Available only to merchant users in Brazil.

        mandate : typing.Optional[MandatePayload]

        card : typing.Optional[Card]

        google_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw `PaymentData` object received from Google Pay. Send the Google Pay response payload as-is.

        apple_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw payment token object received from Apple Pay. Send the Apple Pay response payload as-is.

        token : typing.Optional[str]
            Saved-card token to use instead of raw card details when processing with a previously stored payment instrument.

        customer_id : typing.Optional[str]
            Customer identifier associated with the saved payment instrument. Required when `token` is provided.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProcessCheckoutResponse]
            Returns the checkout resource after a processing attempt.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="PUT",
            json={
                "payment_type": payment_type,
                "installments": installments,
                "mandate": convert_and_respect_annotation_metadata(
                    object_=mandate, annotation=MandatePayload, direction="write"
                ),
                "card": convert_and_respect_annotation_metadata(object_=card, annotation=Card, direction="write"),
                "google_pay": google_pay,
                "apple_pay": apple_pay,
                "token": token,
                "customer_id": customer_id,
                "personal_details": convert_and_respect_annotation_metadata(
                    object_=personal_details, annotation=PersonalDetails, direction="write"
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
                    ProcessCheckoutResponse,
                    parse_obj_as(
                        type_=ProcessCheckoutResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    async def deactivate_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Checkout]:
        """
        Deactivates an identified checkout resource. If the checkout has already been processed it can not be deactivated.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Checkout]
            Returns the checkout object after successful deactivation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Checkout,
                    parse_obj_as(
                        type_=Checkout,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    async def update_checkout(
        self,
        checkout_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        description: typing.Optional[str] = OMIT,
        checkout_reference: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Checkout]:
        """
        Updates the amount, currency, description, reference, expiration, or customer associated with an existing checkout. Only the supplied fields are updated.

        This request changes the checkout details; it does not charge a payment instrument. Process the checkout separately to attempt a payment.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        amount : typing.Optional[float]
            Updated amount to be charged to the payer, expressed in major units.

        currency : typing.Optional[Currency]

        description : typing.Optional[str]
            Updated short merchant-defined description shown in SumUp tools and reporting.

        checkout_reference : typing.Optional[str]
            Updated merchant-defined reference for the checkout.

        valid_until : typing.Optional[dt.datetime]
            Updated expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable.

        customer_id : typing.Optional[str]
            Updated merchant-scoped customer identifier associated with the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Checkout]
            Returns the updated checkout resource.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/checkouts/{encode_path_param(checkout_id)}",
            method="PATCH",
            json={
                "amount": amount,
                "currency": currency,
                "description": description,
                "checkout_reference": checkout_reference,
                "valid_until": valid_until,
                "customer_id": customer_id,
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
                    Checkout,
                    parse_obj_as(
                        type_=Checkout,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def create_apple_pay_session(
        self, checkout_id: str, *, context: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Creates an Apple Pay merchant session for the specified checkout.

        Use this endpoint after the customer selects Apple Pay and before calling
        `ApplePaySession.completeMerchantValidation(...)` in the browser.
        SumUp validates the merchant session request and returns the Apple Pay
        session object that your frontend should pass to Apple's JavaScript API.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        context : str
            the context to create this apple pay session.

        target : str
            The target url to create this apple pay session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful request. Returns the Apple Pay merchant session object
            that should be forwarded to the Apple Pay JS SDK to complete merchant
            validation and continue the payment flow.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.2/checkouts/{encode_path_param(checkout_id)}/apple-pay-session",
            method="PUT",
            json={
                "context": context,
                "target": target,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 404:
                raise NotFoundError(
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
