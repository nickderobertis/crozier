

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.list_entries_request_season import ListEntriesRequestSeason
from ..types.list_entries_request_since import ListEntriesRequestSince
from ..types.list_entries_request_until import ListEntriesRequestUntil
from .types.list_entries_request_tide import ListEntriesRequestTide
from pydantic import ValidationError


class RawEntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_entries(
        self,
        *,
        tide: ListEntriesRequestTide,
        since: typing.Optional[ListEntriesRequestSince] = None,
        until: typing.Optional[ListEntriesRequestUntil] = None,
        season: typing.Optional[ListEntriesRequestSeason] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        tide : ListEntriesRequestTide

        since : typing.Optional[ListEntriesRequestSince]

        until : typing.Optional[ListEntriesRequestUntil]

        season : typing.Optional[ListEntriesRequestSeason]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Entries.
        """
        _response = self._client_wrapper.httpx_client.request(
            "entries",
            method="GET",
            params={
                "since": convert_and_respect_annotation_metadata(
                    object_=since, annotation=ListEntriesRequestSince, direction="write"
                ),
                "until": convert_and_respect_annotation_metadata(
                    object_=until, annotation=ListEntriesRequestUntil, direction="write"
                ),
                "season": convert_and_respect_annotation_metadata(
                    object_=season, annotation=ListEntriesRequestSeason, direction="write"
                ),
                "tide": convert_and_respect_annotation_metadata(
                    object_=tide, annotation=ListEntriesRequestTide, direction="write"
                ),
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_entries(
        self,
        *,
        tide: ListEntriesRequestTide,
        since: typing.Optional[ListEntriesRequestSince] = None,
        until: typing.Optional[ListEntriesRequestUntil] = None,
        season: typing.Optional[ListEntriesRequestSeason] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        tide : ListEntriesRequestTide

        since : typing.Optional[ListEntriesRequestSince]

        until : typing.Optional[ListEntriesRequestUntil]

        season : typing.Optional[ListEntriesRequestSeason]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Entries.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entries",
            method="GET",
            params={
                "since": convert_and_respect_annotation_metadata(
                    object_=since, annotation=ListEntriesRequestSince, direction="write"
                ),
                "until": convert_and_respect_annotation_metadata(
                    object_=until, annotation=ListEntriesRequestUntil, direction="write"
                ),
                "season": convert_and_respect_annotation_metadata(
                    object_=season, annotation=ListEntriesRequestSeason, direction="write"
                ),
                "tide": convert_and_respect_annotation_metadata(
                    object_=tide, annotation=ListEntriesRequestTide, direction="write"
                ),
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
