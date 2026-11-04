

import contextlib
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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.precondition_failed_error import PreconditionFailedError
from ..errors.range_not_satisfiable_error import RangeNotSatisfiableError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.casting_devices import CastingDevices
from ..types.casting_relay import CastingRelay
from ..types.cursor import Cursor
from ..types.drive_statistics import DriveStatistics
from ..types.e_tag import ETag
from ..types.error_envelope import ErrorEnvelope
from ..types.file_bulk_result import FileBulkResult
from ..types.file_category import FileCategory
from ..types.file_category_statistics import FileCategoryStatistics
from ..types.file_entry import FileEntry
from ..types.file_kind import FileKind
from ..types.file_list_scope import FileListScope
from ..types.file_search_type import FileSearchType
from ..types.file_sort import FileSort
from ..types.file_status import FileStatus
from ..types.file_view_state import FileViewState
from ..types.media_tracks import MediaTracks
from ..types.name_conflict_policy import NameConflictPolicy
from ..types.playback_diagnostics import PlaybackDiagnostics
from ..types.playback_session import PlaybackSession
from ..types.sort_order import SortOrder
from ..types.uuid_ import Uuid
from ..types.viewer_kind import ViewerKind
from .types.casting_start_mode import CastingStartMode
from .types.control_casting_device_request_command import ControlCastingDeviceRequestCommand
from .types.download_file_legacy_request_download import DownloadFileLegacyRequestDownload
from .types.download_file_request_download import DownloadFileRequestDownload
from .types.list_files_response import ListFilesResponse
from .types.stream_playback_request_download import StreamPlaybackRequestDownload
from .types.stream_playback_request_mode import StreamPlaybackRequestMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_playback(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PlaybackSession]:
        """
        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PlaybackSession]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/playback",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaybackSession,
                    parse_obj_as(
                        type_=PlaybackSession,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.contextmanager
    def stream_playback(
        self,
        *,
        ticket: str,
        mode: typing.Optional[StreamPlaybackRequestMode] = None,
        start: typing.Optional[float] = None,
        audio: typing.Optional[int] = None,
        video: typing.Optional[int] = None,
        subtitle: typing.Optional[int] = None,
        download: typing.Optional[StreamPlaybackRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        ticket : str

        mode : typing.Optional[StreamPlaybackRequestMode]

        start : typing.Optional[float]

        audio : typing.Optional[int]

        video : typing.Optional[int]

        subtitle : typing.Optional[int]

        download : typing.Optional[StreamPlaybackRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The request has succeeded.
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/playback",
            method="GET",
            params={
                "ticket": ticket,
                "mode": mode,
                "start": start,
                "audio": audio,
                "video": video,
                "subtitle": subtitle,
                "download": download,
            },
            headers={
                "Range": str(range) if range is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def get_playback_diagnostics(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PlaybackDiagnostics]:
        """
        Owner-session-only, bounded in-memory statistics for one playback ticket. No Telegram credentials, internal addresses or ticket values are included. The edge merges authorized primary and secondary snapshots.

        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PlaybackDiagnostics]
            Current server counters, recent streams and bot identities.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/playback/diagnostics",
            method="GET",
            params={
                "ticket": ticket,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaybackDiagnostics,
                    parse_obj_as(
                        type_=PlaybackDiagnostics,
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

    def get_playback_tracks(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MediaTracks]:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MediaTracks]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/playback/tracks",
            method="GET",
            params={
                "ticket": ticket,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MediaTracks,
                    parse_obj_as(
                        type_=MediaTracks,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.contextmanager
    def get_playback_subtitles(
        self,
        *,
        ticket: str,
        track: int,
        start: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        ticket : str

        track : int

        start : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The request has succeeded.
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/playback/subtitles",
            method="GET",
            params={
                "ticket": ticket,
                "track": track,
                "start": start,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def create_casting_relay(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CastingRelay]:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CastingRelay]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/casting/relay",
            method="POST",
            json={
                "ticket": ticket,
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
                    CastingRelay,
                    parse_obj_as(
                        type_=CastingRelay,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def list_casting_devices(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CastingDevices]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CastingDevices]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/casting/devices",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CastingDevices,
                    parse_obj_as(
                        type_=CastingDevices,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def play_on_casting_device(
        self,
        device_id: str,
        *,
        ticket: str,
        server_url: str,
        mode: CastingStartMode,
        start: typing.Optional[float] = OMIT,
        audio: typing.Optional[int] = OMIT,
        subtitle: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        device_id : str

        ticket : str

        server_url : str

        mode : CastingStartMode

        start : typing.Optional[float]

        audio : typing.Optional[int]

        subtitle : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/casting/devices/{encode_path_param(device_id)}/play",
            method="POST",
            json={
                "ticket": ticket,
                "serverUrl": server_url,
                "mode": mode,
                "start": start,
                "audio": audio,
                "subtitle": subtitle,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def control_casting_device(
        self,
        device_id: str,
        *,
        command: ControlCastingDeviceRequestCommand,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        device_id : str

        command : ControlCastingDeviceRequestCommand

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/casting/devices/{encode_path_param(device_id)}/control",
            method="POST",
            json={
                "command": command,
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
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def list_files(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        scope: typing.Optional[FileListScope] = None,
        parent_id: typing.Optional[Uuid] = None,
        path: typing.Optional[str] = None,
        kind: typing.Optional[FileKind] = None,
        status: typing.Optional[FileStatus] = None,
        search: typing.Optional[str] = None,
        search_type: typing.Optional[FileSearchType] = None,
        category: typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]] = None,
        updated_after: typing.Optional[dt.datetime] = None,
        updated_before: typing.Optional[dt.datetime] = None,
        sort: typing.Optional[FileSort] = None,
        order: typing.Optional[SortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListFilesResponse]:
        """
        List one folder or search within the authenticated user's drive.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        scope : typing.Optional[FileListScope]

        parent_id : typing.Optional[Uuid]

        path : typing.Optional[str]
            Resolve the listing root relative to the user's drive root.

        kind : typing.Optional[FileKind]

        status : typing.Optional[FileStatus]

        search : typing.Optional[str]
            File-name search. Text search is case-insensitive; regex uses PostgreSQL-compatible regular expressions.

        search_type : typing.Optional[FileSearchType]

        category : typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]]

        updated_after : typing.Optional[dt.datetime]

        updated_before : typing.Optional[dt.datetime]

        sort : typing.Optional[FileSort]

        order : typing.Optional[SortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListFilesResponse]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "scope": scope,
                "parentId": parent_id,
                "path": path,
                "kind": kind,
                "status": status,
                "search": search,
                "searchType": search_type,
                "category": ",".join(map(str, category)) if isinstance(category, (list, tuple, set)) else category,
                "updatedAfter": serialize_datetime(updated_after) if updated_after is not None else None,
                "updatedBefore": serialize_datetime(updated_before) if updated_before is not None else None,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFilesResponse,
                    parse_obj_as(
                        type_=ListFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def get_file(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileEntry]:
        """
        Return file or folder metadata.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def trash_file(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Move a file or folder to trash.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def update_file(
        self,
        file_id: Uuid,
        *,
        if_match: typing.Optional[ETag] = None,
        name: typing.Optional[str] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileEntry]:
        """
        Rename a file/folder or update its modification time.

        Parameters
        ----------
        file_id : Uuid

        if_match : typing.Optional[ETag]

        name : typing.Optional[str]

        mod_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}",
            method="PATCH",
            json={
                "name": name,
                "modTime": mod_time,
            },
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def move_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        if_match: typing.Optional[ETag] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileEntry]:
        """
        Move a file or folder using metadata only.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        if_match : typing.Optional[ETag]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/move",
            method="POST",
            json={
                "parentId": parent_id,
                "conflictPolicy": conflict_policy,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def copy_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        parent_id: typing.Optional[Uuid] = OMIT,
        name: typing.Optional[str] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileEntry]:
        """
        Copy a file or folder to another destination.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        parent_id : typing.Optional[Uuid]

        name : typing.Optional[str]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileEntry]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/copy",
            method="POST",
            json={
                "parentId": parent_id,
                "name": name,
                "conflictPolicy": conflict_policy,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def restore_file(
        self, file_id: Uuid, *, idempotency_key: Uuid, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileEntry]:
        """
        Restore a trashed file or folder.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/restore",
            method="POST",
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def purge_file(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Permanently delete a trashed file or folder from the catalog.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/purge",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def clean_trash(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Move every trashed file and folder owned by the authenticated user to deletion pending.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files/trash",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.contextmanager
    def download_file(
        self,
        file_id: Uuid,
        file_name: str,
        *,
        download: typing.Optional[DownloadFileRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Stream complete or partial file content. The filename path segment gives command-line clients a useful output name.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

        download : typing.Optional[DownloadFileRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The request has succeeded.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/files/{encode_path_param(file_id)}/content/{encode_path_param(file_name)}",
            method="GET",
            params={
                "download": download,
            },
            headers={
                "Range": str(range) if range is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def head_file(
        self, file_id: Uuid, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Return content metadata without streaming the file.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/content/{encode_path_param(file_name)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.contextmanager
    def download_file_legacy(
        self,
        file_id: Uuid,
        *,
        download: typing.Optional[DownloadFileLegacyRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Stream file content using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

        download : typing.Optional[DownloadFileLegacyRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The request has succeeded.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/files/{encode_path_param(file_id)}/content",
            method="GET",
            params={
                "download": download,
            },
            headers={
                "Range": str(range) if range is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def head_file_legacy(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Return file metadata using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/content",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def get_file_view_state(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[FileViewState]]:
        """
        Return the authenticated user's synchronized viewer state for a file.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[FileViewState]]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/view-state",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[FileViewState],
                    parse_obj_as(
                        type_=typing.Optional[FileViewState],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def put_file_view_state(
        self,
        file_id: Uuid,
        *,
        kind: ViewerKind,
        position: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        preferences: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        bookmarks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileViewState]:
        """
        Create or replace the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

        kind : ViewerKind

        position : typing.Optional[typing.Dict[str, typing.Any]]

        preferences : typing.Optional[typing.Dict[str, typing.Any]]

        bookmarks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileViewState]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/view-state",
            method="PUT",
            json={
                "kind": kind,
                "position": position,
                "preferences": preferences,
                "bookmarks": bookmarks,
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
                    FileViewState,
                    parse_obj_as(
                        type_=FileViewState,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def delete_file_view_state(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Clear the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/view-state",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def bulk_move_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileBulkResult]:
        """
        Transactionally move multiple files or folders.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileBulkResult]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files/bulk/move",
            method="POST",
            json={
                "fileIds": file_ids,
                "parentId": parent_id,
                "conflictPolicy": conflict_policy,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileBulkResult,
                    parse_obj_as(
                        type_=FileBulkResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def bulk_spam_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileBulkResult]:
        """
        Quarantine owned files and folders and revoke their sharing.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileBulkResult]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files/bulk/spam",
            method="POST",
            json={
                "fileIds": file_ids,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileBulkResult,
                    parse_obj_as(
                        type_=FileBulkResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def bulk_trash_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileBulkResult]:
        """
        Transactionally move multiple files or folders to trash.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileBulkResult]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files/bulk/trash",
            method="POST",
            json={
                "fileIds": file_ids,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileBulkResult,
                    parse_obj_as(
                        type_=FileBulkResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def get_file_category_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[FileCategoryStatistics]]:
        """
        Aggregate active file counts and bytes by category.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FileCategoryStatistics]]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files/statistics/categories",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileCategoryStatistics],
                    parse_obj_as(
                        type_=typing.List[FileCategoryStatistics],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def get_drive_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DriveStatistics]:
        """
        Aggregate drive-level counters for the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DriveStatistics]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files/statistics/drive",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DriveStatistics,
                    parse_obj_as(
                        type_=DriveStatistics,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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


class AsyncRawFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_playback(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PlaybackSession]:
        """
        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PlaybackSession]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/playback",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaybackSession,
                    parse_obj_as(
                        type_=PlaybackSession,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.asynccontextmanager
    async def stream_playback(
        self,
        *,
        ticket: str,
        mode: typing.Optional[StreamPlaybackRequestMode] = None,
        start: typing.Optional[float] = None,
        audio: typing.Optional[int] = None,
        video: typing.Optional[int] = None,
        subtitle: typing.Optional[int] = None,
        download: typing.Optional[StreamPlaybackRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        ticket : str

        mode : typing.Optional[StreamPlaybackRequestMode]

        start : typing.Optional[float]

        audio : typing.Optional[int]

        video : typing.Optional[int]

        subtitle : typing.Optional[int]

        download : typing.Optional[StreamPlaybackRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The request has succeeded.
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/playback",
            method="GET",
            params={
                "ticket": ticket,
                "mode": mode,
                "start": start,
                "audio": audio,
                "video": video,
                "subtitle": subtitle,
                "download": download,
            },
            headers={
                "Range": str(range) if range is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def get_playback_diagnostics(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PlaybackDiagnostics]:
        """
        Owner-session-only, bounded in-memory statistics for one playback ticket. No Telegram credentials, internal addresses or ticket values are included. The edge merges authorized primary and secondary snapshots.

        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PlaybackDiagnostics]
            Current server counters, recent streams and bot identities.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/playback/diagnostics",
            method="GET",
            params={
                "ticket": ticket,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaybackDiagnostics,
                    parse_obj_as(
                        type_=PlaybackDiagnostics,
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

    async def get_playback_tracks(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MediaTracks]:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MediaTracks]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/playback/tracks",
            method="GET",
            params={
                "ticket": ticket,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MediaTracks,
                    parse_obj_as(
                        type_=MediaTracks,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.asynccontextmanager
    async def get_playback_subtitles(
        self,
        *,
        ticket: str,
        track: int,
        start: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        ticket : str

        track : int

        start : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The request has succeeded.
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/playback/subtitles",
            method="GET",
            params={
                "ticket": ticket,
                "track": track,
                "start": start,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def create_casting_relay(
        self, *, ticket: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CastingRelay]:
        """
        Parameters
        ----------
        ticket : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CastingRelay]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/casting/relay",
            method="POST",
            json={
                "ticket": ticket,
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
                    CastingRelay,
                    parse_obj_as(
                        type_=CastingRelay,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def list_casting_devices(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CastingDevices]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CastingDevices]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/casting/devices",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CastingDevices,
                    parse_obj_as(
                        type_=CastingDevices,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def play_on_casting_device(
        self,
        device_id: str,
        *,
        ticket: str,
        server_url: str,
        mode: CastingStartMode,
        start: typing.Optional[float] = OMIT,
        audio: typing.Optional[int] = OMIT,
        subtitle: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        device_id : str

        ticket : str

        server_url : str

        mode : CastingStartMode

        start : typing.Optional[float]

        audio : typing.Optional[int]

        subtitle : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/casting/devices/{encode_path_param(device_id)}/play",
            method="POST",
            json={
                "ticket": ticket,
                "serverUrl": server_url,
                "mode": mode,
                "start": start,
                "audio": audio,
                "subtitle": subtitle,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def control_casting_device(
        self,
        device_id: str,
        *,
        command: ControlCastingDeviceRequestCommand,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        device_id : str

        command : ControlCastingDeviceRequestCommand

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/casting/devices/{encode_path_param(device_id)}/control",
            method="POST",
            json={
                "command": command,
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
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def list_files(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        scope: typing.Optional[FileListScope] = None,
        parent_id: typing.Optional[Uuid] = None,
        path: typing.Optional[str] = None,
        kind: typing.Optional[FileKind] = None,
        status: typing.Optional[FileStatus] = None,
        search: typing.Optional[str] = None,
        search_type: typing.Optional[FileSearchType] = None,
        category: typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]] = None,
        updated_after: typing.Optional[dt.datetime] = None,
        updated_before: typing.Optional[dt.datetime] = None,
        sort: typing.Optional[FileSort] = None,
        order: typing.Optional[SortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListFilesResponse]:
        """
        List one folder or search within the authenticated user's drive.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        scope : typing.Optional[FileListScope]

        parent_id : typing.Optional[Uuid]

        path : typing.Optional[str]
            Resolve the listing root relative to the user's drive root.

        kind : typing.Optional[FileKind]

        status : typing.Optional[FileStatus]

        search : typing.Optional[str]
            File-name search. Text search is case-insensitive; regex uses PostgreSQL-compatible regular expressions.

        search_type : typing.Optional[FileSearchType]

        category : typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]]

        updated_after : typing.Optional[dt.datetime]

        updated_before : typing.Optional[dt.datetime]

        sort : typing.Optional[FileSort]

        order : typing.Optional[SortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListFilesResponse]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "scope": scope,
                "parentId": parent_id,
                "path": path,
                "kind": kind,
                "status": status,
                "search": search,
                "searchType": search_type,
                "category": ",".join(map(str, category)) if isinstance(category, (list, tuple, set)) else category,
                "updatedAfter": serialize_datetime(updated_after) if updated_after is not None else None,
                "updatedBefore": serialize_datetime(updated_before) if updated_before is not None else None,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFilesResponse,
                    parse_obj_as(
                        type_=ListFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def get_file(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileEntry]:
        """
        Return file or folder metadata.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def trash_file(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Move a file or folder to trash.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def update_file(
        self,
        file_id: Uuid,
        *,
        if_match: typing.Optional[ETag] = None,
        name: typing.Optional[str] = OMIT,
        mod_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileEntry]:
        """
        Rename a file/folder or update its modification time.

        Parameters
        ----------
        file_id : Uuid

        if_match : typing.Optional[ETag]

        name : typing.Optional[str]

        mod_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}",
            method="PATCH",
            json={
                "name": name,
                "modTime": mod_time,
            },
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def move_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        if_match: typing.Optional[ETag] = None,
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileEntry]:
        """
        Move a file or folder using metadata only.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        if_match : typing.Optional[ETag]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/move",
            method="POST",
            json={
                "parentId": parent_id,
                "conflictPolicy": conflict_policy,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 412:
                raise PreconditionFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def copy_file(
        self,
        file_id: Uuid,
        *,
        idempotency_key: Uuid,
        parent_id: typing.Optional[Uuid] = OMIT,
        name: typing.Optional[str] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileEntry]:
        """
        Copy a file or folder to another destination.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        parent_id : typing.Optional[Uuid]

        name : typing.Optional[str]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileEntry]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/copy",
            method="POST",
            json={
                "parentId": parent_id,
                "name": name,
                "conflictPolicy": conflict_policy,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def restore_file(
        self, file_id: Uuid, *, idempotency_key: Uuid, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileEntry]:
        """
        Restore a trashed file or folder.

        Parameters
        ----------
        file_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/restore",
            method="POST",
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def purge_file(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Permanently delete a trashed file or folder from the catalog.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/purge",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def clean_trash(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        Move every trashed file and folder owned by the authenticated user to deletion pending.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files/trash",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.asynccontextmanager
    async def download_file(
        self,
        file_id: Uuid,
        file_name: str,
        *,
        download: typing.Optional[DownloadFileRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Stream complete or partial file content. The filename path segment gives command-line clients a useful output name.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

        download : typing.Optional[DownloadFileRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The request has succeeded.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/files/{encode_path_param(file_id)}/content/{encode_path_param(file_name)}",
            method="GET",
            params={
                "download": download,
            },
            headers={
                "Range": str(range) if range is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def head_file(
        self, file_id: Uuid, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Return content metadata without streaming the file.

        Parameters
        ----------
        file_id : Uuid

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/content/{encode_path_param(file_name)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    @contextlib.asynccontextmanager
    async def download_file_legacy(
        self,
        file_id: Uuid,
        *,
        download: typing.Optional[DownloadFileLegacyRequestDownload] = None,
        range: typing.Optional[str] = None,
        if_none_match: typing.Optional[ETag] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Stream file content using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

        download : typing.Optional[DownloadFileLegacyRequestDownload]
            Force a browser download instead of inline display.

        range : typing.Optional[str]

        if_none_match : typing.Optional[ETag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The request has succeeded.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/files/{encode_path_param(file_id)}/content",
            method="GET",
            params={
                "download": download,
            },
            headers={
                "Range": str(range) if range is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorEnvelope,
                                parse_obj_as(
                                    type_=ErrorEnvelope,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def head_file_legacy(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Return file metadata using the legacy URL without a filename segment.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/content",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def get_file_view_state(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[FileViewState]]:
        """
        Return the authenticated user's synchronized viewer state for a file.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[FileViewState]]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/view-state",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[FileViewState],
                    parse_obj_as(
                        type_=typing.Optional[FileViewState],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def put_file_view_state(
        self,
        file_id: Uuid,
        *,
        kind: ViewerKind,
        position: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        preferences: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        bookmarks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileViewState]:
        """
        Create or replace the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

        kind : ViewerKind

        position : typing.Optional[typing.Dict[str, typing.Any]]

        preferences : typing.Optional[typing.Dict[str, typing.Any]]

        bookmarks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileViewState]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/view-state",
            method="PUT",
            json={
                "kind": kind,
                "position": position,
                "preferences": preferences,
                "bookmarks": bookmarks,
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
                    FileViewState,
                    parse_obj_as(
                        type_=FileViewState,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def delete_file_view_state(
        self, file_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Clear the authenticated user's synchronized viewer state.

        Parameters
        ----------
        file_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{encode_path_param(file_id)}/view-state",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def bulk_move_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        parent_id: typing.Optional[Uuid] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileBulkResult]:
        """
        Transactionally move multiple files or folders.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        parent_id : typing.Optional[Uuid]

        conflict_policy : typing.Optional[NameConflictPolicy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileBulkResult]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files/bulk/move",
            method="POST",
            json={
                "fileIds": file_ids,
                "parentId": parent_id,
                "conflictPolicy": conflict_policy,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileBulkResult,
                    parse_obj_as(
                        type_=FileBulkResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def bulk_spam_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileBulkResult]:
        """
        Quarantine owned files and folders and revoke their sharing.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileBulkResult]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files/bulk/spam",
            method="POST",
            json={
                "fileIds": file_ids,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileBulkResult,
                    parse_obj_as(
                        type_=FileBulkResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def bulk_trash_files(
        self,
        *,
        idempotency_key: Uuid,
        file_ids: typing.Sequence[Uuid],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileBulkResult]:
        """
        Transactionally move multiple files or folders to trash.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        file_ids : typing.Sequence[Uuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileBulkResult]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files/bulk/trash",
            method="POST",
            json={
                "fileIds": file_ids,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileBulkResult,
                    parse_obj_as(
                        type_=FileBulkResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def get_file_category_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[FileCategoryStatistics]]:
        """
        Aggregate active file counts and bytes by category.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FileCategoryStatistics]]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files/statistics/categories",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileCategoryStatistics],
                    parse_obj_as(
                        type_=typing.List[FileCategoryStatistics],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def get_drive_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DriveStatistics]:
        """
        Aggregate drive-level counters for the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DriveStatistics]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files/statistics/drive",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DriveStatistics,
                    parse_obj_as(
                        type_=DriveStatistics,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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
