

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.delivery import Delivery
from .types.delivery_condition import DeliveryCondition
from .types.dispatch import Dispatch
from .types.notice import Notice
from .types.notice_condition import NoticeCondition
from .types.routing_hint import RoutingHint
from .types.spare_basket import SpareBasket
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_dispatch(
        self,
        *,
        hint: typing.Optional[RoutingHint] = OMIT,
        basket: typing.Optional[SpareBasket] = OMIT,
        delivery: typing.Optional[Delivery] = OMIT,
        delivery_condition: typing.Optional[DeliveryCondition] = OMIT,
        notice: typing.Optional[Notice] = OMIT,
        notice_condition: typing.Optional[NoticeCondition] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dispatch]:
        """
        Parameters
        ----------
        hint : typing.Optional[RoutingHint]

        basket : typing.Optional[SpareBasket]

        delivery : typing.Optional[Delivery]

        delivery_condition : typing.Optional[DeliveryCondition]

        notice : typing.Optional[Notice]

        notice_condition : typing.Optional[NoticeCondition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dispatch]
            Dispatch recorded
        """
        _response = self._client_wrapper.httpx_client.request(
            "dispatches",
            method="POST",
            json={
                "hint": convert_and_respect_annotation_metadata(
                    object_=hint, annotation=RoutingHint, direction="write"
                ),
                "basket": convert_and_respect_annotation_metadata(
                    object_=basket, annotation=typing.Optional[SpareBasket], direction="write"
                ),
                "delivery": convert_and_respect_annotation_metadata(
                    object_=delivery, annotation=Delivery, direction="write"
                ),
                "delivery_condition": convert_and_respect_annotation_metadata(
                    object_=delivery_condition, annotation=DeliveryCondition, direction="write"
                ),
                "notice": convert_and_respect_annotation_metadata(object_=notice, annotation=Notice, direction="write"),
                "notice_condition": convert_and_respect_annotation_metadata(
                    object_=notice_condition, annotation=NoticeCondition, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_dispatch(
        self,
        *,
        hint: typing.Optional[RoutingHint] = OMIT,
        basket: typing.Optional[SpareBasket] = OMIT,
        delivery: typing.Optional[Delivery] = OMIT,
        delivery_condition: typing.Optional[DeliveryCondition] = OMIT,
        notice: typing.Optional[Notice] = OMIT,
        notice_condition: typing.Optional[NoticeCondition] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dispatch]:
        """
        Parameters
        ----------
        hint : typing.Optional[RoutingHint]

        basket : typing.Optional[SpareBasket]

        delivery : typing.Optional[Delivery]

        delivery_condition : typing.Optional[DeliveryCondition]

        notice : typing.Optional[Notice]

        notice_condition : typing.Optional[NoticeCondition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dispatch]
            Dispatch recorded
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dispatches",
            method="POST",
            json={
                "hint": convert_and_respect_annotation_metadata(
                    object_=hint, annotation=RoutingHint, direction="write"
                ),
                "basket": convert_and_respect_annotation_metadata(
                    object_=basket, annotation=typing.Optional[SpareBasket], direction="write"
                ),
                "delivery": convert_and_respect_annotation_metadata(
                    object_=delivery, annotation=Delivery, direction="write"
                ),
                "delivery_condition": convert_and_respect_annotation_metadata(
                    object_=delivery_condition, annotation=DeliveryCondition, direction="write"
                ),
                "notice": convert_and_respect_annotation_metadata(object_=notice, annotation=Notice, direction="write"),
                "notice_condition": convert_and_respect_annotation_metadata(
                    object_=notice_condition, annotation=NoticeCondition, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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
