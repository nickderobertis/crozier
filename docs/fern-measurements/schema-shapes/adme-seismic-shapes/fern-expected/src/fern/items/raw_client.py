

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.items_create_request_data import ItemsCreateRequestData
from .types.items_create_request_info import ItemsCreateRequestInfo
from .types.items_create_request_meta_item import ItemsCreateRequestMetaItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        info: ItemsCreateRequestInfo,
        created: typing.Optional[dt.datetime] = OMIT,
        meta: typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]] = OMIT,
        data: typing.Optional[ItemsCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        info : ItemsCreateRequestInfo

        created : typing.Optional[dt.datetime]

        meta : typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]]

        data : typing.Optional[ItemsCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "items",
            method="POST",
            json={
                "info": convert_and_respect_annotation_metadata(
                    object_=info, annotation=ItemsCreateRequestInfo, direction="write"
                ),
                "created": created,
                "meta": convert_and_respect_annotation_metadata(
                    object_=meta, annotation=typing.Sequence[ItemsCreateRequestMetaItem], direction="write"
                ),
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ItemsCreateRequestData, direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        info: ItemsCreateRequestInfo,
        created: typing.Optional[dt.datetime] = OMIT,
        meta: typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]] = OMIT,
        data: typing.Optional[ItemsCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        info : ItemsCreateRequestInfo

        created : typing.Optional[dt.datetime]

        meta : typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]]

        data : typing.Optional[ItemsCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "items",
            method="POST",
            json={
                "info": convert_and_respect_annotation_metadata(
                    object_=info, annotation=ItemsCreateRequestInfo, direction="write"
                ),
                "created": created,
                "meta": convert_and_respect_annotation_metadata(
                    object_=meta, annotation=typing.Sequence[ItemsCreateRequestMetaItem], direction="write"
                ),
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ItemsCreateRequestData, direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
