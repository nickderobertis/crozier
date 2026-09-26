

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.gateway_timeout_error import GatewayTimeoutError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_model import ErrorModel
from ..types.refund_item import RefundItem
from ..types.tax_cloud_address import TaxCloudAddress
from ..types.tax_cloud_cart import TaxCloudCart
from ..types.tax_cloud_cart_item_with_tax import TaxCloudCartItemWithTax
from ..types.tax_cloud_cert_list_response import TaxCloudCertListResponse
from ..types.tax_cloud_cert_response import TaxCloudCertResponse
from ..types.tax_cloud_currency import TaxCloudCurrency
from ..types.tax_cloud_discounts import TaxCloudDiscounts
from ..types.tax_cloud_exempt_state import TaxCloudExemptState
from ..types.tax_cloud_exemption import TaxCloudExemption
from ..types.tax_cloud_order_response import TaxCloudOrderResponse
from ..types.tax_cloud_refund_response import TaxCloudRefundResponse
from .types.merchant_cart_calculate_response import MerchantCartCalculateResponse
from .types.merchant_cert_create_request_customer_business_type import MerchantCertCreateRequestCustomerBusinessType
from .types.merchant_cert_create_request_reason import MerchantCertCreateRequestReason
from .types.merchant_cert_list_request_sort_by import MerchantCertListRequestSortBy
from .types.merchant_order_create_from_cart_request_kind import MerchantOrderCreateFromCartRequestKind
from .types.merchant_order_create_request_kind import MerchantOrderCreateRequestKind
from .types.merchant_order_get_request_expand import MerchantOrderGetRequestExpand
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMerchantTaxCloudClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def merchant_cart_calculate(
        self,
        *,
        items: typing.Sequence[TaxCloudCart],
        merchant_id: str,
        transaction_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MerchantCartCalculateResponse]:
        """
        Calculates sales tax for one or more carts on behalf of a merchant. The request contract is the same for both merchant management modes, so a caller does not have to know which mode a merchant is in. TaxCloud-managed merchant: the request is forwarded to TaxCloud (POST /connections/{connectionId}/carts) using the merchant's stored credentials and TaxCloud's response is returned verbatim; capture the returned cartId with /merchant/order/create-from-cart to record the sale. Self-managed merchant: the cart is calculated in-process by the Ziptax rate engine, US destinations only, and nothing is persisted - the returned cartId correlates the response with the request and cannot be captured as an order, and the other stateful /merchant endpoints return 403. Self-managed calculation rejects (rather than ignores) fields it cannot honour: discounts, exemption, deliveredBySeller, productId, and any currency other than USD. A value that asks for nothing is accepted, so a caller that always emits the TaxCloud shape is not refused: deliveredBySeller false, and an exemption claiming no exemption ({} or {"isExempt": false}). TIC vocabulary also differs: self-managed carts use Ziptax TICs, where 10001 is shipping and 11000 is handling, and TaxCloud's shipping TICs 11010-11015 and the Colorado retail delivery fee TIC 11098 are rejected with 400 because they cannot be mapped onto the in-process shipping and handling treatment. A self-managed interstate cart whose destination address cannot be resolved returns 422 rather than being sourced at its origin, which would quote another state's rate. A self-managed request may contain at most 2500 line items summed across all carts; a larger batch is rejected with 400 before any cart is calculated. Calculation has no lasting side effect in either mode and is safe to retry.

        Parameters
        ----------
        items : typing.Sequence[TaxCloudCart]
            The carts to calculate tax for. Most integrations send a single cart; up to 100 carts may be calculated in one call.

        merchant_id : str
            UUID of the merchant whose TaxCloud connection is used. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        transaction_date : typing.Optional[dt.datetime]
            RFC3339 datetime the carts are calculated for. Defaults to the current time when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MerchantCartCalculateResponse]
            Calculated carts. For a TaxCloud-managed merchant this is TaxCloud's response relayed verbatim; for a self-managed merchant it is the Ziptax calculation, which has no connectionId, exemption, or deliveredBySeller.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/cart/calculate",
            method="POST",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[TaxCloudCart], direction="write"
                ),
                "merchantId": merchant_id,
                "transactionDate": transaction_date,
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
                    MerchantCartCalculateResponse,
                    parse_obj_as(
                        type_=MerchantCartCalculateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_cert_create(
        self,
        *,
        address: TaxCloudAddress,
        customer_business_type: MerchantCertCreateRequestCustomerBusinessType,
        customer_id: str,
        customer_name: str,
        merchant_id: str,
        reason: MerchantCertCreateRequestReason,
        reason_description: str,
        states: typing.Sequence[TaxCloudExemptState],
        customer_business_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaxCloudCertResponse]:
        """
        Creates an exemption certificate for one of the merchant's customers. The request is forwarded to TaxCloud POST /connections/{connectionId}/exemption-certificates using the merchant's stored credentials and TaxCloud's response is returned verbatim. Reference the returned certificateId as exemptionId on carts and orders to apply the exemption. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        address : TaxCloudAddress
            Address of the exempt customer.

        customer_business_type : MerchantCertCreateRequestCustomerBusinessType
            The type of business the customer is.

        customer_id : str
            Your identifier for the exempt customer. Carts and orders submitted with this customerId can use the certificate.

        customer_name : str
            Name of the customer or organization the certificate is issued to.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        reason : MerchantCertCreateRequestReason
            The reason the customer is exempt from sales tax.

        reason_description : str
            Short free-text elaboration of the exemption reason (maximum 20 characters).

        states : typing.Sequence[TaxCloudExemptState]
            The states the certificate is valid in, each as a two-letter abbreviation object.

        customer_business_description : typing.Optional[str]
            Free-text description of the business. Provide when customerBusinessType is Other.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudCertResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/cert/create",
            method="POST",
            json={
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=TaxCloudAddress, direction="write"
                ),
                "customerBusinessDescription": customer_business_description,
                "customerBusinessType": customer_business_type,
                "customerId": customer_id,
                "customerName": customer_name,
                "merchantId": merchant_id,
                "reason": reason,
                "reasonDescription": reason_description,
                "states": convert_and_respect_annotation_metadata(
                    object_=states, annotation=typing.Sequence[TaxCloudExemptState], direction="write"
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
                    TaxCloudCertResponse,
                    parse_obj_as(
                        type_=TaxCloudCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_cert_delete(
        self, *, certificate_id: str, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Deletes (disables) an exemption certificate so it can no longer be applied to new transactions. The request is forwarded to TaxCloud DELETE /connections/{connectionId}/exemption-certificates/{certificateId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        certificate_id : str
            The certificateId returned when the exemption certificate was created.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/cert/delete",
            method="POST",
            json={
                "certificateId": certificate_id,
                "merchantId": merchant_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_cert_get(
        self, *, certificate_id: str, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TaxCloudCertResponse]:
        """
        Retrieves a single exemption certificate. The request is forwarded to TaxCloud GET /connections/{connectionId}/exemption-certificates/{certificateId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        certificate_id : str
            The certificateId returned when the exemption certificate was created.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudCertResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/cert/get",
            method="POST",
            json={
                "certificateId": certificate_id,
                "merchantId": merchant_id,
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
                    TaxCloudCertResponse,
                    parse_obj_as(
                        type_=TaxCloudCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_cert_list(
        self,
        *,
        merchant_id: str,
        ascending: typing.Optional[bool] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[MerchantCertListRequestSortBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaxCloudCertListResponse]:
        """
        Lists the merchant's exemption certificates with cursor-based pagination. The request is forwarded to TaxCloud GET /exemption-certificates, scoped to the merchant's connection, with the optional filter fields mapped onto the query string; TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        ascending : typing.Optional[bool]
            Whether to sort results in ascending order. Defaults to false (descending).

        cursor : typing.Optional[str]
            Opaque pagination cursor from the nextCursor field of a previous response. Omit to start at the first page.

        customer_id : typing.Optional[str]
            Filter results to certificates belonging to this customerId.

        disabled : typing.Optional[bool]
            Set true to list disabled (revoked) certificates instead of active ones. Defaults to false.

        limit : typing.Optional[int]
            Maximum number of certificates to return per page. Defaults to 20; maximum 100.

        sort_by : typing.Optional[MerchantCertListRequestSortBy]
            The field to sort results by: 'createdDate' or 'id'. Defaults to 'id'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudCertListResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/cert/list",
            method="POST",
            json={
                "ascending": ascending,
                "cursor": cursor,
                "customerId": customer_id,
                "disabled": disabled,
                "limit": limit,
                "merchantId": merchant_id,
                "sortBy": sort_by,
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
                    TaxCloudCertListResponse,
                    parse_obj_as(
                        type_=TaxCloudCertListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_order_create(
        self,
        *,
        completed_date: dt.datetime,
        currency: TaxCloudCurrency,
        customer_id: str,
        destination: TaxCloudAddress,
        line_items: typing.Sequence[TaxCloudCartItemWithTax],
        merchant_id: str,
        order_id: str,
        origin: TaxCloudAddress,
        transaction_date: dt.datetime,
        batch_id: typing.Optional[str] = OMIT,
        channel: typing.Optional[str] = OMIT,
        delivered_by_seller: typing.Optional[bool] = OMIT,
        discounts: typing.Optional[TaxCloudDiscounts] = OMIT,
        exclude_from_filing: typing.Optional[bool] = OMIT,
        exemption: typing.Optional[TaxCloudExemption] = OMIT,
        kind: typing.Optional[MerchantOrderCreateRequestKind] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaxCloudOrderResponse]:
        """
        Records an order directly, without a prior cart calculation; the tax amounts on each line item are the amounts your checkout collected. The request is forwarded to TaxCloud POST /connections/{connectionId}/orders using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        completed_date : dt.datetime
            RFC3339 datetime the order was shipped on, which created the tax liability.

        currency : TaxCloudCurrency
            The currency the line-item prices and tax amounts are denominated in.

        customer_id : str
            Your identifier for the customer in your own system. Used to match exemption certificates and order history.

        destination : TaxCloudAddress
            The ship-to (destination) address of the sale.

        line_items : typing.Sequence[TaxCloudCartItemWithTax]
            The items on the order, each including the tax rate and amount that was collected.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order in your own system. Used later with /merchant/order/get, /merchant/order/update, and /merchant/refund/create.

        origin : TaxCloudAddress
            The ship-from (origin) address of the sale.

        transaction_date : dt.datetime
            RFC3339 datetime the order was purchased on.

        batch_id : typing.Optional[str]
            Optional batch ID for grouping related orders.

        channel : typing.Optional[str]
            The sales channel the order came from. Pass one of amazon, ebay, or walmart to exclude marketplace-collected tax from filing.

        delivered_by_seller : typing.Optional[bool]
            Whether the seller delivers the order directly (own vehicles) rather than via common carrier. Affects taxability of delivery charges in some states.

        discounts : typing.Optional[TaxCloudDiscounts]
            Optional line-item and order-level discounts to apply. If omitted, prices are used as is.

        exclude_from_filing : typing.Optional[bool]
            Whether to exclude the order from tax filing.

        exemption : typing.Optional[TaxCloudExemption]
            Optional exemption information for the customer.

        kind : typing.Optional[MerchantOrderCreateRequestKind]
            The kind of order: 'order' for a sale (default) or 'credit' for a credit order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/order/create",
            method="POST",
            json={
                "batchId": batch_id,
                "channel": channel,
                "completedDate": completed_date,
                "currency": convert_and_respect_annotation_metadata(
                    object_=currency, annotation=TaxCloudCurrency, direction="write"
                ),
                "customerId": customer_id,
                "deliveredBySeller": delivered_by_seller,
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=TaxCloudAddress, direction="write"
                ),
                "discounts": convert_and_respect_annotation_metadata(
                    object_=discounts, annotation=TaxCloudDiscounts, direction="write"
                ),
                "excludeFromFiling": exclude_from_filing,
                "exemption": convert_and_respect_annotation_metadata(
                    object_=exemption, annotation=TaxCloudExemption, direction="write"
                ),
                "kind": kind,
                "lineItems": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[TaxCloudCartItemWithTax], direction="write"
                ),
                "merchantId": merchant_id,
                "orderId": order_id,
                "origin": convert_and_respect_annotation_metadata(
                    object_=origin, annotation=TaxCloudAddress, direction="write"
                ),
                "transactionDate": transaction_date,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_order_create_from_cart(
        self,
        *,
        cart_id: str,
        merchant_id: str,
        order_id: str,
        completed: typing.Optional[bool] = OMIT,
        completed_date: typing.Optional[dt.datetime] = OMIT,
        kind: typing.Optional[MerchantOrderCreateFromCartRequestKind] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaxCloudOrderResponse]:
        """
        Captures a cart previously calculated with /merchant/cart/calculate as a recorded order. The request is forwarded to TaxCloud POST /connections/{connectionId}/carts/orders using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        cart_id : str
            The cartId returned by (or supplied to) /merchant/cart/calculate identifying the calculated cart to convert into an order.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the resulting order in your own system. Used later with /merchant/order/get, /merchant/order/update, and /merchant/refund/create.

        completed : typing.Optional[bool]
            Whether the order has shipped, creating a tax liability. Defaults to false. Ignored when completedDate is provided.

        completed_date : typing.Optional[dt.datetime]
            RFC3339 datetime the order was shipped on, which created the tax liability. Takes precedence over the completed field when provided.

        kind : typing.Optional[MerchantOrderCreateFromCartRequestKind]
            The kind of order to create: 'order' for a sale (default) or 'credit' for a credit order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/order/create-from-cart",
            method="POST",
            json={
                "cartId": cart_id,
                "completed": completed,
                "completedDate": completed_date,
                "kind": kind,
                "merchantId": merchant_id,
                "orderId": order_id,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_order_get(
        self,
        *,
        merchant_id: str,
        order_id: str,
        expand: typing.Optional[MerchantOrderGetRequestExpand] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaxCloudOrderResponse]:
        """
        Retrieves a recorded order. The request is forwarded to TaxCloud GET /connections/{connectionId}/orders/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order to retrieve, as supplied when the order was created.

        expand : typing.Optional[MerchantOrderGetRequestExpand]
            Set to 'refunds' to include the order's refunds in the response. Forwarded to TaxCloud as a query parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/order/get",
            method="POST",
            json={
                "expand": expand,
                "merchantId": merchant_id,
                "orderId": order_id,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_order_update(
        self,
        *,
        merchant_id: str,
        order_id: str,
        completed_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaxCloudOrderResponse]:
        """
        Modifies a recorded order; currently the completedDate can be set to mark the order shipped, creating the tax liability. The request is forwarded to TaxCloud PATCH /connections/{connectionId}/orders/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Updates overwrite the fields you send, so do not retry them blindly. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order to update, as supplied when the order was created. Consumed for routing and not forwarded in the update payload.

        completed_date : typing.Optional[dt.datetime]
            RFC3339 datetime the order was shipped on, which creates the tax liability.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/order/update",
            method="POST",
            json={
                "completedDate": completed_date,
                "merchantId": merchant_id,
                "orderId": order_id,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def merchant_refund_create(
        self,
        *,
        merchant_id: str,
        order_id: str,
        batch_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[RefundItem]] = OMIT,
        returned_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaxCloudRefundResponse]:
        """
        Refunds all or part of a recorded order. The request is forwarded to TaxCloud POST /connections/{connectionId}/orders/refunds/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Refund prices and tax amounts are calculated automatically from the order; when the order had discounts, refunds use the discounted prices actually paid. Do not retry refunds blindly - a duplicate submission records a duplicate refund. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order to refund, as supplied when the order was created. Consumed for routing and not forwarded in the refund payload.

        batch_id : typing.Optional[str]
            Optional batch ID for grouping related refunds.

        items : typing.Optional[typing.Sequence[RefundItem]]
            The line items and quantities to refund. Omit (or send an empty array) to refund the entire order.

        returned_date : typing.Optional[dt.datetime]
            Include only if this return amends a previously filed sales tax return; providing it triggers an Amended Sales Tax Return. Not typically recommended.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaxCloudRefundResponse]
            TaxCloud response relayed verbatim.
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/refund/create",
            method="POST",
            json={
                "batchId": batch_id,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Optional[typing.Sequence[RefundItem]], direction="write"
                ),
                "merchantId": merchant_id,
                "orderId": order_id,
                "returnedDate": returned_date,
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
                    TaxCloudRefundResponse,
                    parse_obj_as(
                        type_=TaxCloudRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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


class AsyncRawMerchantTaxCloudClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def merchant_cart_calculate(
        self,
        *,
        items: typing.Sequence[TaxCloudCart],
        merchant_id: str,
        transaction_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MerchantCartCalculateResponse]:
        """
        Calculates sales tax for one or more carts on behalf of a merchant. The request contract is the same for both merchant management modes, so a caller does not have to know which mode a merchant is in. TaxCloud-managed merchant: the request is forwarded to TaxCloud (POST /connections/{connectionId}/carts) using the merchant's stored credentials and TaxCloud's response is returned verbatim; capture the returned cartId with /merchant/order/create-from-cart to record the sale. Self-managed merchant: the cart is calculated in-process by the Ziptax rate engine, US destinations only, and nothing is persisted - the returned cartId correlates the response with the request and cannot be captured as an order, and the other stateful /merchant endpoints return 403. Self-managed calculation rejects (rather than ignores) fields it cannot honour: discounts, exemption, deliveredBySeller, productId, and any currency other than USD. A value that asks for nothing is accepted, so a caller that always emits the TaxCloud shape is not refused: deliveredBySeller false, and an exemption claiming no exemption ({} or {"isExempt": false}). TIC vocabulary also differs: self-managed carts use Ziptax TICs, where 10001 is shipping and 11000 is handling, and TaxCloud's shipping TICs 11010-11015 and the Colorado retail delivery fee TIC 11098 are rejected with 400 because they cannot be mapped onto the in-process shipping and handling treatment. A self-managed interstate cart whose destination address cannot be resolved returns 422 rather than being sourced at its origin, which would quote another state's rate. A self-managed request may contain at most 2500 line items summed across all carts; a larger batch is rejected with 400 before any cart is calculated. Calculation has no lasting side effect in either mode and is safe to retry.

        Parameters
        ----------
        items : typing.Sequence[TaxCloudCart]
            The carts to calculate tax for. Most integrations send a single cart; up to 100 carts may be calculated in one call.

        merchant_id : str
            UUID of the merchant whose TaxCloud connection is used. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        transaction_date : typing.Optional[dt.datetime]
            RFC3339 datetime the carts are calculated for. Defaults to the current time when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MerchantCartCalculateResponse]
            Calculated carts. For a TaxCloud-managed merchant this is TaxCloud's response relayed verbatim; for a self-managed merchant it is the Ziptax calculation, which has no connectionId, exemption, or deliveredBySeller.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/cart/calculate",
            method="POST",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[TaxCloudCart], direction="write"
                ),
                "merchantId": merchant_id,
                "transactionDate": transaction_date,
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
                    MerchantCartCalculateResponse,
                    parse_obj_as(
                        type_=MerchantCartCalculateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_cert_create(
        self,
        *,
        address: TaxCloudAddress,
        customer_business_type: MerchantCertCreateRequestCustomerBusinessType,
        customer_id: str,
        customer_name: str,
        merchant_id: str,
        reason: MerchantCertCreateRequestReason,
        reason_description: str,
        states: typing.Sequence[TaxCloudExemptState],
        customer_business_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaxCloudCertResponse]:
        """
        Creates an exemption certificate for one of the merchant's customers. The request is forwarded to TaxCloud POST /connections/{connectionId}/exemption-certificates using the merchant's stored credentials and TaxCloud's response is returned verbatim. Reference the returned certificateId as exemptionId on carts and orders to apply the exemption. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        address : TaxCloudAddress
            Address of the exempt customer.

        customer_business_type : MerchantCertCreateRequestCustomerBusinessType
            The type of business the customer is.

        customer_id : str
            Your identifier for the exempt customer. Carts and orders submitted with this customerId can use the certificate.

        customer_name : str
            Name of the customer or organization the certificate is issued to.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        reason : MerchantCertCreateRequestReason
            The reason the customer is exempt from sales tax.

        reason_description : str
            Short free-text elaboration of the exemption reason (maximum 20 characters).

        states : typing.Sequence[TaxCloudExemptState]
            The states the certificate is valid in, each as a two-letter abbreviation object.

        customer_business_description : typing.Optional[str]
            Free-text description of the business. Provide when customerBusinessType is Other.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudCertResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/cert/create",
            method="POST",
            json={
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=TaxCloudAddress, direction="write"
                ),
                "customerBusinessDescription": customer_business_description,
                "customerBusinessType": customer_business_type,
                "customerId": customer_id,
                "customerName": customer_name,
                "merchantId": merchant_id,
                "reason": reason,
                "reasonDescription": reason_description,
                "states": convert_and_respect_annotation_metadata(
                    object_=states, annotation=typing.Sequence[TaxCloudExemptState], direction="write"
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
                    TaxCloudCertResponse,
                    parse_obj_as(
                        type_=TaxCloudCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_cert_delete(
        self, *, certificate_id: str, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Deletes (disables) an exemption certificate so it can no longer be applied to new transactions. The request is forwarded to TaxCloud DELETE /connections/{connectionId}/exemption-certificates/{certificateId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        certificate_id : str
            The certificateId returned when the exemption certificate was created.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/cert/delete",
            method="POST",
            json={
                "certificateId": certificate_id,
                "merchantId": merchant_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_cert_get(
        self, *, certificate_id: str, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TaxCloudCertResponse]:
        """
        Retrieves a single exemption certificate. The request is forwarded to TaxCloud GET /connections/{connectionId}/exemption-certificates/{certificateId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        certificate_id : str
            The certificateId returned when the exemption certificate was created.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudCertResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/cert/get",
            method="POST",
            json={
                "certificateId": certificate_id,
                "merchantId": merchant_id,
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
                    TaxCloudCertResponse,
                    parse_obj_as(
                        type_=TaxCloudCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_cert_list(
        self,
        *,
        merchant_id: str,
        ascending: typing.Optional[bool] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[MerchantCertListRequestSortBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaxCloudCertListResponse]:
        """
        Lists the merchant's exemption certificates with cursor-based pagination. The request is forwarded to TaxCloud GET /exemption-certificates, scoped to the merchant's connection, with the optional filter fields mapped onto the query string; TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        ascending : typing.Optional[bool]
            Whether to sort results in ascending order. Defaults to false (descending).

        cursor : typing.Optional[str]
            Opaque pagination cursor from the nextCursor field of a previous response. Omit to start at the first page.

        customer_id : typing.Optional[str]
            Filter results to certificates belonging to this customerId.

        disabled : typing.Optional[bool]
            Set true to list disabled (revoked) certificates instead of active ones. Defaults to false.

        limit : typing.Optional[int]
            Maximum number of certificates to return per page. Defaults to 20; maximum 100.

        sort_by : typing.Optional[MerchantCertListRequestSortBy]
            The field to sort results by: 'createdDate' or 'id'. Defaults to 'id'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudCertListResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/cert/list",
            method="POST",
            json={
                "ascending": ascending,
                "cursor": cursor,
                "customerId": customer_id,
                "disabled": disabled,
                "limit": limit,
                "merchantId": merchant_id,
                "sortBy": sort_by,
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
                    TaxCloudCertListResponse,
                    parse_obj_as(
                        type_=TaxCloudCertListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_order_create(
        self,
        *,
        completed_date: dt.datetime,
        currency: TaxCloudCurrency,
        customer_id: str,
        destination: TaxCloudAddress,
        line_items: typing.Sequence[TaxCloudCartItemWithTax],
        merchant_id: str,
        order_id: str,
        origin: TaxCloudAddress,
        transaction_date: dt.datetime,
        batch_id: typing.Optional[str] = OMIT,
        channel: typing.Optional[str] = OMIT,
        delivered_by_seller: typing.Optional[bool] = OMIT,
        discounts: typing.Optional[TaxCloudDiscounts] = OMIT,
        exclude_from_filing: typing.Optional[bool] = OMIT,
        exemption: typing.Optional[TaxCloudExemption] = OMIT,
        kind: typing.Optional[MerchantOrderCreateRequestKind] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaxCloudOrderResponse]:
        """
        Records an order directly, without a prior cart calculation; the tax amounts on each line item are the amounts your checkout collected. The request is forwarded to TaxCloud POST /connections/{connectionId}/orders using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        completed_date : dt.datetime
            RFC3339 datetime the order was shipped on, which created the tax liability.

        currency : TaxCloudCurrency
            The currency the line-item prices and tax amounts are denominated in.

        customer_id : str
            Your identifier for the customer in your own system. Used to match exemption certificates and order history.

        destination : TaxCloudAddress
            The ship-to (destination) address of the sale.

        line_items : typing.Sequence[TaxCloudCartItemWithTax]
            The items on the order, each including the tax rate and amount that was collected.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order in your own system. Used later with /merchant/order/get, /merchant/order/update, and /merchant/refund/create.

        origin : TaxCloudAddress
            The ship-from (origin) address of the sale.

        transaction_date : dt.datetime
            RFC3339 datetime the order was purchased on.

        batch_id : typing.Optional[str]
            Optional batch ID for grouping related orders.

        channel : typing.Optional[str]
            The sales channel the order came from. Pass one of amazon, ebay, or walmart to exclude marketplace-collected tax from filing.

        delivered_by_seller : typing.Optional[bool]
            Whether the seller delivers the order directly (own vehicles) rather than via common carrier. Affects taxability of delivery charges in some states.

        discounts : typing.Optional[TaxCloudDiscounts]
            Optional line-item and order-level discounts to apply. If omitted, prices are used as is.

        exclude_from_filing : typing.Optional[bool]
            Whether to exclude the order from tax filing.

        exemption : typing.Optional[TaxCloudExemption]
            Optional exemption information for the customer.

        kind : typing.Optional[MerchantOrderCreateRequestKind]
            The kind of order: 'order' for a sale (default) or 'credit' for a credit order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/order/create",
            method="POST",
            json={
                "batchId": batch_id,
                "channel": channel,
                "completedDate": completed_date,
                "currency": convert_and_respect_annotation_metadata(
                    object_=currency, annotation=TaxCloudCurrency, direction="write"
                ),
                "customerId": customer_id,
                "deliveredBySeller": delivered_by_seller,
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=TaxCloudAddress, direction="write"
                ),
                "discounts": convert_and_respect_annotation_metadata(
                    object_=discounts, annotation=TaxCloudDiscounts, direction="write"
                ),
                "excludeFromFiling": exclude_from_filing,
                "exemption": convert_and_respect_annotation_metadata(
                    object_=exemption, annotation=TaxCloudExemption, direction="write"
                ),
                "kind": kind,
                "lineItems": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[TaxCloudCartItemWithTax], direction="write"
                ),
                "merchantId": merchant_id,
                "orderId": order_id,
                "origin": convert_and_respect_annotation_metadata(
                    object_=origin, annotation=TaxCloudAddress, direction="write"
                ),
                "transactionDate": transaction_date,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_order_create_from_cart(
        self,
        *,
        cart_id: str,
        merchant_id: str,
        order_id: str,
        completed: typing.Optional[bool] = OMIT,
        completed_date: typing.Optional[dt.datetime] = OMIT,
        kind: typing.Optional[MerchantOrderCreateFromCartRequestKind] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaxCloudOrderResponse]:
        """
        Captures a cart previously calculated with /merchant/cart/calculate as a recorded order. The request is forwarded to TaxCloud POST /connections/{connectionId}/carts/orders using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        cart_id : str
            The cartId returned by (or supplied to) /merchant/cart/calculate identifying the calculated cart to convert into an order.

        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the resulting order in your own system. Used later with /merchant/order/get, /merchant/order/update, and /merchant/refund/create.

        completed : typing.Optional[bool]
            Whether the order has shipped, creating a tax liability. Defaults to false. Ignored when completedDate is provided.

        completed_date : typing.Optional[dt.datetime]
            RFC3339 datetime the order was shipped on, which created the tax liability. Takes precedence over the completed field when provided.

        kind : typing.Optional[MerchantOrderCreateFromCartRequestKind]
            The kind of order to create: 'order' for a sale (default) or 'credit' for a credit order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/order/create-from-cart",
            method="POST",
            json={
                "cartId": cart_id,
                "completed": completed,
                "completedDate": completed_date,
                "kind": kind,
                "merchantId": merchant_id,
                "orderId": order_id,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_order_get(
        self,
        *,
        merchant_id: str,
        order_id: str,
        expand: typing.Optional[MerchantOrderGetRequestExpand] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaxCloudOrderResponse]:
        """
        Retrieves a recorded order. The request is forwarded to TaxCloud GET /connections/{connectionId}/orders/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order to retrieve, as supplied when the order was created.

        expand : typing.Optional[MerchantOrderGetRequestExpand]
            Set to 'refunds' to include the order's refunds in the response. Forwarded to TaxCloud as a query parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/order/get",
            method="POST",
            json={
                "expand": expand,
                "merchantId": merchant_id,
                "orderId": order_id,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_order_update(
        self,
        *,
        merchant_id: str,
        order_id: str,
        completed_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaxCloudOrderResponse]:
        """
        Modifies a recorded order; currently the completedDate can be set to mark the order shipped, creating the tax liability. The request is forwarded to TaxCloud PATCH /connections/{connectionId}/orders/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Updates overwrite the fields you send, so do not retry them blindly. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order to update, as supplied when the order was created. Consumed for routing and not forwarded in the update payload.

        completed_date : typing.Optional[dt.datetime]
            RFC3339 datetime the order was shipped on, which creates the tax liability.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudOrderResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/order/update",
            method="POST",
            json={
                "completedDate": completed_date,
                "merchantId": merchant_id,
                "orderId": order_id,
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
                    TaxCloudOrderResponse,
                    parse_obj_as(
                        type_=TaxCloudOrderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def merchant_refund_create(
        self,
        *,
        merchant_id: str,
        order_id: str,
        batch_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[RefundItem]] = OMIT,
        returned_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaxCloudRefundResponse]:
        """
        Refunds all or part of a recorded order. The request is forwarded to TaxCloud POST /connections/{connectionId}/orders/refunds/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Refund prices and tax amounts are calculated automatically from the order; when the order had discounts, refunds use the discounted prices actually paid. Do not retry refunds blindly - a duplicate submission records a duplicate refund. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.

        order_id : str
            Your identifier for the order to refund, as supplied when the order was created. Consumed for routing and not forwarded in the refund payload.

        batch_id : typing.Optional[str]
            Optional batch ID for grouping related refunds.

        items : typing.Optional[typing.Sequence[RefundItem]]
            The line items and quantities to refund. Omit (or send an empty array) to refund the entire order.

        returned_date : typing.Optional[dt.datetime]
            Include only if this return amends a previously filed sales tax return; providing it triggers an Amended Sales Tax Return. Not typically recommended.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaxCloudRefundResponse]
            TaxCloud response relayed verbatim.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/refund/create",
            method="POST",
            json={
                "batchId": batch_id,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Optional[typing.Sequence[RefundItem]], direction="write"
                ),
                "merchantId": merchant_id,
                "orderId": order_id,
                "returnedDate": returned_date,
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
                    TaxCloudRefundResponse,
                    parse_obj_as(
                        type_=TaxCloudRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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
