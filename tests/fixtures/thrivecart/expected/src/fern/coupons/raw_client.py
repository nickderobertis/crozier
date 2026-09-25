

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from .types.create_coupon_request_discount_type import CreateCouponRequestDiscountType
from .types.create_coupon_response import CreateCouponResponse
from .types.list_coupons_response import ListCouponsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCouponsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_coupons(
        self, *, product_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListCouponsResponse]:
        """
        Get a list of coupons for the account.

        Parameters
        ----------
        product_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCouponsResponse]
            List of coupons
        """
        _response = self._client_wrapper.httpx_client.request(
            "coupons",
            method="POST",
            json={
                "product_id": product_id,
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
                    ListCouponsResponse,
                    parse_obj_as(
                        type_=ListCouponsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_coupon(
        self,
        *,
        code: str,
        product_id: int,
        discount_type: typing.Optional[CreateCouponRequestDiscountType] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        uses_limit: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCouponResponse]:
        """
        Create a new discount coupon.

        Parameters
        ----------
        code : str
            Coupon code

        product_id : int

        discount_type : typing.Optional[CreateCouponRequestDiscountType]

        discount_amount : typing.Optional[float]

        uses_limit : typing.Optional[int]

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCouponResponse]
            Coupon created
        """
        _response = self._client_wrapper.httpx_client.request(
            "coupons/create",
            method="POST",
            json={
                "code": code,
                "product_id": product_id,
                "discount_type": discount_type,
                "discount_amount": discount_amount,
                "uses_limit": uses_limit,
                "expires_at": expires_at,
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
                    CreateCouponResponse,
                    parse_obj_as(
                        type_=CreateCouponResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCouponsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_coupons(
        self, *, product_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListCouponsResponse]:
        """
        Get a list of coupons for the account.

        Parameters
        ----------
        product_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCouponsResponse]
            List of coupons
        """
        _response = await self._client_wrapper.httpx_client.request(
            "coupons",
            method="POST",
            json={
                "product_id": product_id,
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
                    ListCouponsResponse,
                    parse_obj_as(
                        type_=ListCouponsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_coupon(
        self,
        *,
        code: str,
        product_id: int,
        discount_type: typing.Optional[CreateCouponRequestDiscountType] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        uses_limit: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCouponResponse]:
        """
        Create a new discount coupon.

        Parameters
        ----------
        code : str
            Coupon code

        product_id : int

        discount_type : typing.Optional[CreateCouponRequestDiscountType]

        discount_amount : typing.Optional[float]

        uses_limit : typing.Optional[int]

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCouponResponse]
            Coupon created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "coupons/create",
            method="POST",
            json={
                "code": code,
                "product_id": product_id,
                "discount_type": discount_type,
                "discount_amount": discount_amount,
                "uses_limit": uses_limit,
                "expires_at": expires_at,
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
                    CreateCouponResponse,
                    parse_obj_as(
                        type_=CreateCouponResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
