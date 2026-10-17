

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.realtime_config_response_output import RealtimeConfigResponseOutput
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRealtimeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1get_realtime_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RealtimeConfigResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RealtimeConfigResponseOutput]
            Gets project's realtime configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/config/realtime",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RealtimeConfigResponseOutput,
                    parse_obj_as(
                        type_=RealtimeConfigResponseOutput,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def v1update_realtime_config(
        self,
        ref: str,
        *,
        private_only: typing.Optional[bool] = OMIT,
        connection_pool: typing.Optional[int] = OMIT,
        postgres_changes_pool: typing.Optional[int] = OMIT,
        max_concurrent_users: typing.Optional[int] = OMIT,
        max_events_per_second: typing.Optional[int] = OMIT,
        max_bytes_per_second: typing.Optional[int] = OMIT,
        max_channels_per_client: typing.Optional[int] = OMIT,
        max_joins_per_second: typing.Optional[int] = OMIT,
        max_presence_events_per_second: typing.Optional[int] = OMIT,
        max_payload_size_in_kb: typing.Optional[int] = OMIT,
        suspend: typing.Optional[bool] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        private_only : typing.Optional[bool]
            Whether to only allow private channels

        connection_pool : typing.Optional[int]
            Sets connection pool size for Realtime Authorization

        postgres_changes_pool : typing.Optional[int]
            Sets connection pool size used to create Postgres Changes subscriptions

        max_concurrent_users : typing.Optional[int]
            Sets maximum number of concurrent users rate limit

        max_events_per_second : typing.Optional[int]
            Sets maximum number of events per second rate per channel limit

        max_bytes_per_second : typing.Optional[int]
            Sets maximum number of bytes per second rate per channel limit

        max_channels_per_client : typing.Optional[int]
            Sets maximum number of channels per client rate limit

        max_joins_per_second : typing.Optional[int]
            Sets maximum number of joins per second rate limit

        max_presence_events_per_second : typing.Optional[int]
            Sets maximum number of presence events per second rate limit

        max_payload_size_in_kb : typing.Optional[int]
            Sets maximum number of payload size in KB rate limit

        suspend : typing.Optional[bool]
            Disables the Realtime service for this project when true. Set to false to re-enable it.

        presence_enabled : typing.Optional[bool]
            Whether to enable presence

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/config/realtime",
            method="PATCH",
            json={
                "private_only": private_only,
                "connection_pool": connection_pool,
                "postgres_changes_pool": postgres_changes_pool,
                "max_concurrent_users": max_concurrent_users,
                "max_events_per_second": max_events_per_second,
                "max_bytes_per_second": max_bytes_per_second,
                "max_channels_per_client": max_channels_per_client,
                "max_joins_per_second": max_joins_per_second,
                "max_presence_events_per_second": max_presence_events_per_second,
                "max_payload_size_in_kb": max_payload_size_in_kb,
                "suspend": suspend,
                "presence_enabled": presence_enabled,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def v1shutdown_realtime(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/config/realtime/shutdown",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawRealtimeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1get_realtime_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RealtimeConfigResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RealtimeConfigResponseOutput]
            Gets project's realtime configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/config/realtime",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RealtimeConfigResponseOutput,
                    parse_obj_as(
                        type_=RealtimeConfigResponseOutput,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def v1update_realtime_config(
        self,
        ref: str,
        *,
        private_only: typing.Optional[bool] = OMIT,
        connection_pool: typing.Optional[int] = OMIT,
        postgres_changes_pool: typing.Optional[int] = OMIT,
        max_concurrent_users: typing.Optional[int] = OMIT,
        max_events_per_second: typing.Optional[int] = OMIT,
        max_bytes_per_second: typing.Optional[int] = OMIT,
        max_channels_per_client: typing.Optional[int] = OMIT,
        max_joins_per_second: typing.Optional[int] = OMIT,
        max_presence_events_per_second: typing.Optional[int] = OMIT,
        max_payload_size_in_kb: typing.Optional[int] = OMIT,
        suspend: typing.Optional[bool] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        private_only : typing.Optional[bool]
            Whether to only allow private channels

        connection_pool : typing.Optional[int]
            Sets connection pool size for Realtime Authorization

        postgres_changes_pool : typing.Optional[int]
            Sets connection pool size used to create Postgres Changes subscriptions

        max_concurrent_users : typing.Optional[int]
            Sets maximum number of concurrent users rate limit

        max_events_per_second : typing.Optional[int]
            Sets maximum number of events per second rate per channel limit

        max_bytes_per_second : typing.Optional[int]
            Sets maximum number of bytes per second rate per channel limit

        max_channels_per_client : typing.Optional[int]
            Sets maximum number of channels per client rate limit

        max_joins_per_second : typing.Optional[int]
            Sets maximum number of joins per second rate limit

        max_presence_events_per_second : typing.Optional[int]
            Sets maximum number of presence events per second rate limit

        max_payload_size_in_kb : typing.Optional[int]
            Sets maximum number of payload size in KB rate limit

        suspend : typing.Optional[bool]
            Disables the Realtime service for this project when true. Set to false to re-enable it.

        presence_enabled : typing.Optional[bool]
            Whether to enable presence

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/config/realtime",
            method="PATCH",
            json={
                "private_only": private_only,
                "connection_pool": connection_pool,
                "postgres_changes_pool": postgres_changes_pool,
                "max_concurrent_users": max_concurrent_users,
                "max_events_per_second": max_events_per_second,
                "max_bytes_per_second": max_bytes_per_second,
                "max_channels_per_client": max_channels_per_client,
                "max_joins_per_second": max_joins_per_second,
                "max_presence_events_per_second": max_presence_events_per_second,
                "max_payload_size_in_kb": max_payload_size_in_kb,
                "suspend": suspend,
                "presence_enabled": presence_enabled,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def v1shutdown_realtime(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/config/realtime/shutdown",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
