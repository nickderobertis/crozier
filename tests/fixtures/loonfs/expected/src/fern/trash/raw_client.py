

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import encode_path_param
from ..core.pagination import AsyncPager, SyncPager
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.gone_error import GoneError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.list_trash_response import ListTrashResponse
from ..types.read_consistency import ReadConsistency
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from ..types.trash_entry import TrashEntry
from pydantic import ValidationError


class RawTrashClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[TrashEntry, ListTrashResponse]:
        """
        Returns the namespace's recoverable deletions, oldest first. A deletion leaves the list when it's undeleted, or when the namespace's writer expires it after the retention floor reaches its `deletion_seq`. Each entry includes the inode ID and deletion sequence that an undelete needs, and the directory binding that the delete removed.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[TrashEntry, ListTrashResponse]
            Recoverable deletions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/trash",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListTrashResponse,
                    parse_obj_as(
                        type_=ListTrashResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.entries
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    namespace_id,
                    limit=limit,
                    cursor=_parsed_next,
                    consistency=consistency,
                    max_staleness_ms=max_staleness_ms,
                    request_options=request_options,
                )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
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


class AsyncRawTrashClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[TrashEntry, ListTrashResponse]:
        """
        Returns the namespace's recoverable deletions, oldest first. A deletion leaves the list when it's undeleted, or when the namespace's writer expires it after the retention floor reaches its `deletion_seq`. Each entry includes the inode ID and deletion sequence that an undelete needs, and the directory binding that the delete removed.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[TrashEntry, ListTrashResponse]
            Recoverable deletions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/trash",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListTrashResponse,
                    parse_obj_as(
                        type_=ListTrashResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.entries
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""

                async def _get_next():
                    return await self.list(
                        namespace_id,
                        limit=limit,
                        cursor=_parsed_next,
                        consistency=consistency,
                        max_staleness_ms=max_staleness_ms,
                        request_options=request_options,
                    )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
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
