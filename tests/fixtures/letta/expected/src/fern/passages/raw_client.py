

import datetime as dt
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
from ..types.passage_search_result import PassageSearchResult
from .types.passage_search_request_tag_match_mode import PassageSearchRequestTagMatchMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPassagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_passages(
        self,
        *,
        query: str,
        agent_id: typing.Optional[str] = OMIT,
        archive_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tag_match_mode: typing.Optional[PassageSearchRequestTagMatchMode] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[PassageSearchResult]]:
        """
        Search passages across the organization with optional agent and archive filtering.
        Returns passages with relevance scores.

        This endpoint supports semantic search through passages:
        - If neither agent_id nor archive_id is provided, searches ALL passages in the organization
        - If agent_id is provided, searches passages across all archives attached to that agent
        - If archive_id is provided, searches passages within that specific archive
        - If both are provided, agent_id takes precedence

        Parameters
        ----------
        query : str
            Text query for semantic search

        agent_id : typing.Optional[str]
            Filter passages by agent ID

        archive_id : typing.Optional[str]
            Filter passages by archive ID

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to filter search results

        tag_match_mode : typing.Optional[PassageSearchRequestTagMatchMode]
            How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter results to passages created after this datetime

        end_date : typing.Optional[dt.datetime]
            Filter results to passages created before this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PassageSearchResult]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/passages/search",
            method="POST",
            json={
                "query": query,
                "agent_id": agent_id,
                "archive_id": archive_id,
                "tags": tags,
                "tag_match_mode": tag_match_mode,
                "limit": limit,
                "start_date": start_date,
                "end_date": end_date,
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
                    typing.List[PassageSearchResult],
                    parse_obj_as(
                        type_=typing.List[PassageSearchResult],
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


class AsyncRawPassagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_passages(
        self,
        *,
        query: str,
        agent_id: typing.Optional[str] = OMIT,
        archive_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tag_match_mode: typing.Optional[PassageSearchRequestTagMatchMode] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[PassageSearchResult]]:
        """
        Search passages across the organization with optional agent and archive filtering.
        Returns passages with relevance scores.

        This endpoint supports semantic search through passages:
        - If neither agent_id nor archive_id is provided, searches ALL passages in the organization
        - If agent_id is provided, searches passages across all archives attached to that agent
        - If archive_id is provided, searches passages within that specific archive
        - If both are provided, agent_id takes precedence

        Parameters
        ----------
        query : str
            Text query for semantic search

        agent_id : typing.Optional[str]
            Filter passages by agent ID

        archive_id : typing.Optional[str]
            Filter passages by archive ID

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to filter search results

        tag_match_mode : typing.Optional[PassageSearchRequestTagMatchMode]
            How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter results to passages created after this datetime

        end_date : typing.Optional[dt.datetime]
            Filter results to passages created before this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PassageSearchResult]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/passages/search",
            method="POST",
            json={
                "query": query,
                "agent_id": agent_id,
                "archive_id": archive_id,
                "tags": tags,
                "tag_match_mode": tag_match_mode,
                "limit": limit,
                "start_date": start_date,
                "end_date": end_date,
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
                    typing.List[PassageSearchResult],
                    parse_obj_as(
                        type_=typing.List[PassageSearchResult],
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
