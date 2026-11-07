

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
from ..errors.client_request_error import ClientRequestError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.server_error import ServerError
from ..types.affiliate_attribution import AffiliateAttribution
from ..types.authentication_result import AuthenticationResult
from ..types.buyer import Buyer
from ..types.checkout_session import CheckoutSession
from ..types.checkout_session_with_order import CheckoutSessionWithOrder
from ..types.error import Error
from ..types.fulfillment_details import FulfillmentDetails
from ..types.intent_trace import IntentTrace
from ..types.item import Item
from ..types.payment_data import PaymentData
from ..types.selected_fulfillment_option import SelectedFulfillmentOption
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCheckoutSessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_checkout_session(
        self,
        *,
        items: typing.Sequence[Item],
        buyer: typing.Optional[Buyer] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckoutSession]:
        """
        Initializes a new checkout session from items and (optionally) buyer and fulfillment info.
        MUST return 201 with a rich, authoritative cart state.

        Agents MAY include `affiliate_attribution` with `touchpoint: "first"` to record first-touch attribution.
        This enables multi-touch attribution models where networks can capture both first and last touch.

        Parameters
        ----------
        items : typing.Sequence[Item]

        buyer : typing.Optional[Buyer]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckoutSession]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "checkout_sessions",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "fulfillment_details": convert_and_respect_annotation_metadata(
                    object_=fulfillment_details, annotation=FulfillmentDetails, direction="write"
                ),
                "affiliate_attribution": convert_and_respect_annotation_metadata(
                    object_=affiliate_attribution, annotation=AffiliateAttribution, direction="write"
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
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if 400 <= _response.status_code < 500:
                raise ClientRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            if 500 <= _response.status_code < 600:
                raise ServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_checkout_session(
        self, checkout_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckoutSession]:
        """
        Returns the latest authoritative state for the checkout session.

        Parameters
        ----------
        checkout_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckoutSession]
            Current session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def update_checkout_session(
        self,
        checkout_session_id: str,
        *,
        buyer: typing.Optional[Buyer] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        selected_fulfillment_options: typing.Optional[typing.Sequence[SelectedFulfillmentOption]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckoutSession]:
        """
        Applies changes (items, fulfillment address, fulfillment option) and returns an updated authoritative cart state.

        Parameters
        ----------
        checkout_session_id : str

        buyer : typing.Optional[Buyer]

        items : typing.Optional[typing.Sequence[Item]]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        selected_fulfillment_options : typing.Optional[typing.Sequence[SelectedFulfillmentOption]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckoutSession]
            Updated session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "fulfillment_details": convert_and_respect_annotation_metadata(
                    object_=fulfillment_details, annotation=FulfillmentDetails, direction="write"
                ),
                "selected_fulfillment_options": convert_and_respect_annotation_metadata(
                    object_=selected_fulfillment_options,
                    annotation=typing.Sequence[SelectedFulfillmentOption],
                    direction="write",
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
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if 400 <= _response.status_code < 500:
                raise ClientRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            if 500 <= _response.status_code < 600:
                raise ServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def complete_checkout_session(
        self,
        checkout_session_id: str,
        *,
        payment_data: PaymentData,
        buyer: typing.Optional[Buyer] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        authentication_result: typing.Optional[AuthenticationResult] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckoutSessionWithOrder]:
        """
        Finalizes the checkout by applying a payment method. MUST create an order and return completed state on success.

        Agents MAY include `affiliate_attribution` to ensure the merchant receives final attribution context.
        Attribution is stored alongside the resulting order but not returned in the response.

        Parameters
        ----------
        checkout_session_id : str

        payment_data : PaymentData

        buyer : typing.Optional[Buyer]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        authentication_result : typing.Optional[AuthenticationResult]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckoutSessionWithOrder]
            Completed session with order
        """
        _response = self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}/complete",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "payment_data": convert_and_respect_annotation_metadata(
                    object_=payment_data, annotation=PaymentData, direction="write"
                ),
                "affiliate_attribution": convert_and_respect_annotation_metadata(
                    object_=affiliate_attribution, annotation=AffiliateAttribution, direction="write"
                ),
                "authentication_result": convert_and_respect_annotation_metadata(
                    object_=authentication_result, annotation=AuthenticationResult, direction="write"
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
                    CheckoutSessionWithOrder,
                    parse_obj_as(
                        type_=CheckoutSessionWithOrder,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if 400 <= _response.status_code < 500:
                raise ClientRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            if 500 <= _response.status_code < 600:
                raise ServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_checkout_session(
        self,
        checkout_session_id: str,
        *,
        intent_trace: typing.Optional[IntentTrace] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckoutSession]:
        """
        Cancels a session if not already completed or canceled.
        Agents MAY include an intent_trace to communicate why the session is being abandoned.

        Parameters
        ----------
        checkout_session_id : str

        intent_trace : typing.Optional[IntentTrace]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckoutSession]
            Canceled session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}/cancel",
            method="POST",
            json={
                "intent_trace": convert_and_respect_annotation_metadata(
                    object_=intent_trace, annotation=IntentTrace, direction="write"
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
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawCheckoutSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_checkout_session(
        self,
        *,
        items: typing.Sequence[Item],
        buyer: typing.Optional[Buyer] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckoutSession]:
        """
        Initializes a new checkout session from items and (optionally) buyer and fulfillment info.
        MUST return 201 with a rich, authoritative cart state.

        Agents MAY include `affiliate_attribution` with `touchpoint: "first"` to record first-touch attribution.
        This enables multi-touch attribution models where networks can capture both first and last touch.

        Parameters
        ----------
        items : typing.Sequence[Item]

        buyer : typing.Optional[Buyer]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckoutSession]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "checkout_sessions",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "fulfillment_details": convert_and_respect_annotation_metadata(
                    object_=fulfillment_details, annotation=FulfillmentDetails, direction="write"
                ),
                "affiliate_attribution": convert_and_respect_annotation_metadata(
                    object_=affiliate_attribution, annotation=AffiliateAttribution, direction="write"
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
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if 400 <= _response.status_code < 500:
                raise ClientRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            if 500 <= _response.status_code < 600:
                raise ServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_checkout_session(
        self, checkout_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckoutSession]:
        """
        Returns the latest authoritative state for the checkout session.

        Parameters
        ----------
        checkout_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckoutSession]
            Current session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def update_checkout_session(
        self,
        checkout_session_id: str,
        *,
        buyer: typing.Optional[Buyer] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        selected_fulfillment_options: typing.Optional[typing.Sequence[SelectedFulfillmentOption]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckoutSession]:
        """
        Applies changes (items, fulfillment address, fulfillment option) and returns an updated authoritative cart state.

        Parameters
        ----------
        checkout_session_id : str

        buyer : typing.Optional[Buyer]

        items : typing.Optional[typing.Sequence[Item]]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        selected_fulfillment_options : typing.Optional[typing.Sequence[SelectedFulfillmentOption]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckoutSession]
            Updated session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "fulfillment_details": convert_and_respect_annotation_metadata(
                    object_=fulfillment_details, annotation=FulfillmentDetails, direction="write"
                ),
                "selected_fulfillment_options": convert_and_respect_annotation_metadata(
                    object_=selected_fulfillment_options,
                    annotation=typing.Sequence[SelectedFulfillmentOption],
                    direction="write",
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
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if 400 <= _response.status_code < 500:
                raise ClientRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            if 500 <= _response.status_code < 600:
                raise ServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def complete_checkout_session(
        self,
        checkout_session_id: str,
        *,
        payment_data: PaymentData,
        buyer: typing.Optional[Buyer] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        authentication_result: typing.Optional[AuthenticationResult] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckoutSessionWithOrder]:
        """
        Finalizes the checkout by applying a payment method. MUST create an order and return completed state on success.

        Agents MAY include `affiliate_attribution` to ensure the merchant receives final attribution context.
        Attribution is stored alongside the resulting order but not returned in the response.

        Parameters
        ----------
        checkout_session_id : str

        payment_data : PaymentData

        buyer : typing.Optional[Buyer]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        authentication_result : typing.Optional[AuthenticationResult]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckoutSessionWithOrder]
            Completed session with order
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}/complete",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "payment_data": convert_and_respect_annotation_metadata(
                    object_=payment_data, annotation=PaymentData, direction="write"
                ),
                "affiliate_attribution": convert_and_respect_annotation_metadata(
                    object_=affiliate_attribution, annotation=AffiliateAttribution, direction="write"
                ),
                "authentication_result": convert_and_respect_annotation_metadata(
                    object_=authentication_result, annotation=AuthenticationResult, direction="write"
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
                    CheckoutSessionWithOrder,
                    parse_obj_as(
                        type_=CheckoutSessionWithOrder,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if 400 <= _response.status_code < 500:
                raise ClientRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            if 500 <= _response.status_code < 600:
                raise ServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                    status_code=_response.status_code,
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_checkout_session(
        self,
        checkout_session_id: str,
        *,
        intent_trace: typing.Optional[IntentTrace] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckoutSession]:
        """
        Cancels a session if not already completed or canceled.
        Agents MAY include an intent_trace to communicate why the session is being abandoned.

        Parameters
        ----------
        checkout_session_id : str

        intent_trace : typing.Optional[IntentTrace]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckoutSession]
            Canceled session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"checkout_sessions/{encode_path_param(checkout_session_id)}/cancel",
            method="POST",
            json={
                "intent_trace": convert_and_respect_annotation_metadata(
                    object_=intent_trace, annotation=IntentTrace, direction="write"
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
                    CheckoutSession,
                    parse_obj_as(
                        type_=CheckoutSession,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
