

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from .types.get_chains_chain_id_events_response import GetChainsChainIdEventsResponse
from pydantic import ValidationError


class RawChangelogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[str] = None,
        symbol: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdEventsResponse]:
        """
        Public. Without `since`/`cursor`: newest first, with `kinds` (every kind the daemon can emit) and `nextCursor`. With `since` or `cursor` (an ISO instant, use the previous `nextCursor`): only newer rows, oldest first, so a consumer catches up without gaps; a `since` or `cursor` that does not parse is a 400, never a silent restart from now. `kind` matches exactly or by prefix (`registry.`, `multiplier.`) and `symbol` narrows to one token, on the newest-first read only: the cursor read returns every kind, and a consumer following a cursor filters on `kind` itself. `limit` up to 500. When the changelog is empty, `nextCursor` is the epoch, which passed back yields every event from the first.

        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[str]

        symbol : typing.Optional[str]

        since : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]
            An opaque position, `${observedAt}|${id}`, as returned in `nextCursor`. Pass it back verbatim; a bare ISO instant is also accepted.

        limit : typing.Optional[int]
            A malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdEventsResponse]
            Events
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/events",
            method="GET",
            params={
                "kind": kind,
                "symbol": symbol,
                "since": serialize_datetime(since) if since is not None else None,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdEventsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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

    def the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
        self,
        chain_id: int,
        *,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        chain_id : int

        since : typing.Optional[str]
            An ISO instant or a cursor `${observedAt}|${id}`; the Last-Event-ID header takes precedence. Without either the stream starts at now.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/events/stream",
            method="GET",
            params={
                "since": since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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


class AsyncRawChangelogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[str] = None,
        symbol: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdEventsResponse]:
        """
        Public. Without `since`/`cursor`: newest first, with `kinds` (every kind the daemon can emit) and `nextCursor`. With `since` or `cursor` (an ISO instant, use the previous `nextCursor`): only newer rows, oldest first, so a consumer catches up without gaps; a `since` or `cursor` that does not parse is a 400, never a silent restart from now. `kind` matches exactly or by prefix (`registry.`, `multiplier.`) and `symbol` narrows to one token, on the newest-first read only: the cursor read returns every kind, and a consumer following a cursor filters on `kind` itself. `limit` up to 500. When the changelog is empty, `nextCursor` is the epoch, which passed back yields every event from the first.

        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[str]

        symbol : typing.Optional[str]

        since : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]
            An opaque position, `${observedAt}|${id}`, as returned in `nextCursor`. Pass it back verbatim; a bare ISO instant is also accepted.

        limit : typing.Optional[int]
            A malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdEventsResponse]
            Events
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/events",
            method="GET",
            params={
                "kind": kind,
                "symbol": symbol,
                "since": serialize_datetime(since) if since is not None else None,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdEventsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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

    async def the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
        self,
        chain_id: int,
        *,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        chain_id : int

        since : typing.Optional[str]
            An ISO instant or a cursor `${observedAt}|${id}`; the Last-Event-ID header takes precedence. Without either the stream starts at now.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/events/stream",
            method="GET",
            params={
                "since": since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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
