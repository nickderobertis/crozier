

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.gone_error import GoneError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.change_seq import ChangeSeq
from ..types.error_response import ErrorResponse
from ..types.list_changes_response import ListChangesResponse
from ..types.pin_id import PinId
from ..types.read_consistency import ReadConsistency
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from pydantic import ValidationError


class RawChangesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        namespace_id: str,
        *,
        after_seq: ChangeSeq,
        limit: typing.Optional[int] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListChangesResponse]:
        """
        Returns committed changes after a sequence. A snapshot limits the feed to its captured sequence.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        after_seq : ChangeSeq
            The sequence after which to return committed changes.

        limit : typing.Optional[int]
            The maximum page size.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the feed from. The feed ends at the sequence that the snapshot captured.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListChangesResponse]
            Committed changes
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/changes",
            method="GET",
            params={
                "after_seq": after_seq,
                "limit": limit,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChangesResponse,
                    parse_obj_as(
                        type_=ListChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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


class AsyncRawChangesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        namespace_id: str,
        *,
        after_seq: ChangeSeq,
        limit: typing.Optional[int] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListChangesResponse]:
        """
        Returns committed changes after a sequence. A snapshot limits the feed to its captured sequence.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        after_seq : ChangeSeq
            The sequence after which to return committed changes.

        limit : typing.Optional[int]
            The maximum page size.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the feed from. The feed ends at the sequence that the snapshot captured.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListChangesResponse]
            Committed changes
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/changes",
            method="GET",
            params={
                "after_seq": after_seq,
                "limit": limit,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChangesResponse,
                    parse_obj_as(
                        type_=ListChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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
