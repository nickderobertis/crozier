

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.analysis_snapshot_entry import AnalysisSnapshotEntry
from ..types.api_error_response import ApiErrorResponse
from ..types.create_analysis_snapshot_response import CreateAnalysisSnapshotResponse
from ..types.get_analysis_snapshot_response import GetAnalysisSnapshotResponse
from ..types.json_value import JsonValue
from ..types.list_analysis_snapshots_response import ListAnalysisSnapshotsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAnalysisSnapshotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_analysis_snapshots(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAnalysisSnapshotsResponse]:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAnalysisSnapshotsResponse]
            List analysis snapshots
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/games/{encode_path_param(game_id)}/analysis-snapshots",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAnalysisSnapshotsResponse,
                    parse_obj_as(
                        type_=ListAnalysisSnapshotsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def create_analysis_snapshot(
        self,
        game_id: str,
        *,
        line_moves: typing.Sequence[str],
        entries: typing.Sequence[AnalysisSnapshotEntry],
        label: typing.Optional[str] = OMIT,
        analysis_settings: typing.Optional[JsonValue] = OMIT,
        metadata: typing.Optional[JsonValue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAnalysisSnapshotResponse]:
        """
        Parameters
        ----------
        game_id : str

        line_moves : typing.Sequence[str]

        entries : typing.Sequence[AnalysisSnapshotEntry]

        label : typing.Optional[str]

        analysis_settings : typing.Optional[JsonValue]

        metadata : typing.Optional[JsonValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAnalysisSnapshotResponse]
            Created analysis snapshot
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/games/{encode_path_param(game_id)}/analysis-snapshots",
            method="POST",
            json={
                "label": label,
                "lineMoves": line_moves,
                "analysisSettings": convert_and_respect_annotation_metadata(
                    object_=analysis_settings, annotation=typing.Optional[JsonValue], direction="write"
                ),
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=typing.Optional[JsonValue], direction="write"
                ),
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[AnalysisSnapshotEntry], direction="write"
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
                    CreateAnalysisSnapshotResponse,
                    parse_obj_as(
                        type_=CreateAnalysisSnapshotResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def get_analysis_snapshot(
        self, game_id: str, snapshot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAnalysisSnapshotResponse]:
        """
        Parameters
        ----------
        game_id : str

        snapshot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAnalysisSnapshotResponse]
            Get analysis snapshot
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/games/{encode_path_param(game_id)}/analysis-snapshots/{encode_path_param(snapshot_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAnalysisSnapshotResponse,
                    parse_obj_as(
                        type_=GetAnalysisSnapshotResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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


class AsyncRawAnalysisSnapshotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_analysis_snapshots(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAnalysisSnapshotsResponse]:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAnalysisSnapshotsResponse]
            List analysis snapshots
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/games/{encode_path_param(game_id)}/analysis-snapshots",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAnalysisSnapshotsResponse,
                    parse_obj_as(
                        type_=ListAnalysisSnapshotsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def create_analysis_snapshot(
        self,
        game_id: str,
        *,
        line_moves: typing.Sequence[str],
        entries: typing.Sequence[AnalysisSnapshotEntry],
        label: typing.Optional[str] = OMIT,
        analysis_settings: typing.Optional[JsonValue] = OMIT,
        metadata: typing.Optional[JsonValue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAnalysisSnapshotResponse]:
        """
        Parameters
        ----------
        game_id : str

        line_moves : typing.Sequence[str]

        entries : typing.Sequence[AnalysisSnapshotEntry]

        label : typing.Optional[str]

        analysis_settings : typing.Optional[JsonValue]

        metadata : typing.Optional[JsonValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAnalysisSnapshotResponse]
            Created analysis snapshot
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/games/{encode_path_param(game_id)}/analysis-snapshots",
            method="POST",
            json={
                "label": label,
                "lineMoves": line_moves,
                "analysisSettings": convert_and_respect_annotation_metadata(
                    object_=analysis_settings, annotation=typing.Optional[JsonValue], direction="write"
                ),
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=typing.Optional[JsonValue], direction="write"
                ),
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[AnalysisSnapshotEntry], direction="write"
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
                    CreateAnalysisSnapshotResponse,
                    parse_obj_as(
                        type_=CreateAnalysisSnapshotResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def get_analysis_snapshot(
        self, game_id: str, snapshot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAnalysisSnapshotResponse]:
        """
        Parameters
        ----------
        game_id : str

        snapshot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAnalysisSnapshotResponse]
            Get analysis snapshot
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/games/{encode_path_param(game_id)}/analysis-snapshots/{encode_path_param(snapshot_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAnalysisSnapshotResponse,
                    parse_obj_as(
                        type_=GetAnalysisSnapshotResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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
