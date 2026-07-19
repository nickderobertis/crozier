

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from .types.list_tags_request_order import ListTagsRequestOrder
from .types.list_tags_request_order_by import ListTagsRequestOrderBy
from pydantic import ValidationError


class RawTagClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tags(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListTagsRequestOrder] = None,
        order_by: typing.Optional[ListTagsRequestOrderBy] = None,
        query_text: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Get the list of all tags (from agents and blocks) that have been created.

        Parameters
        ----------
        before : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come before this tag in the specified sort order

        after : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come after this tag in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tags to return

        order : typing.Optional[ListTagsRequestOrder]
            Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse alphabetical order

        order_by : typing.Optional[ListTagsRequestOrderBy]
            Field to sort by

        query_text : typing.Optional[str]
            Filter tags by text search. Deprecated, please use name field instead

        name : typing.Optional[str]
            Filter tags by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tags/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "query_text": query_text,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawTagClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tags(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListTagsRequestOrder] = None,
        order_by: typing.Optional[ListTagsRequestOrderBy] = None,
        query_text: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Get the list of all tags (from agents and blocks) that have been created.

        Parameters
        ----------
        before : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come before this tag in the specified sort order

        after : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come after this tag in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tags to return

        order : typing.Optional[ListTagsRequestOrder]
            Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse alphabetical order

        order_by : typing.Optional[ListTagsRequestOrderBy]
            Field to sort by

        query_text : typing.Optional[str]
            Filter tags by text search. Deprecated, please use name field instead

        name : typing.Optional[str]
            Filter tags by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tags/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "query_text": query_text,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
