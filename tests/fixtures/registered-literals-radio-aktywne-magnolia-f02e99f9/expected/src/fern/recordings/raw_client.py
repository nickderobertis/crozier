

import contextlib
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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.delete_request_event import DeleteRequestEvent
from ..types.delete_request_start import DeleteRequestStart
from ..types.download_request_event import DownloadRequestEvent
from ..types.download_request_start import DownloadRequestStart
from ..types.head_download_request_event import HeadDownloadRequestEvent
from ..types.head_download_request_start import HeadDownloadRequestStart
from ..types.list_request_event import ListRequestEvent
from ..types.list_response_results import ListResponseResults
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.upload_request_event import UploadRequestEvent
from ..types.upload_request_start import UploadRequestStart
from .types.recordings_event_list_request_after import RecordingsEventListRequestAfter
from .types.recordings_event_list_request_before import RecordingsEventListRequestBefore
from .types.recordings_event_list_request_limit import RecordingsEventListRequestLimit
from .types.recordings_event_list_request_offset import RecordingsEventListRequestOffset
from .types.recordings_event_list_request_order import RecordingsEventListRequestOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRecordingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def recordings_event_start_download(
        self,
        event: DownloadRequestEvent,
        start: DownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Download a recording.

        Parameters
        ----------
        event : DownloadRequestEvent

        start : DownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Stream Response
        """
        with self._client_wrapper.httpx_client.stream(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="GET",
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

    def recordings_event_start_upload(
        self,
        event: UploadRequestEvent,
        start: UploadRequestStart,
        *,
        request: bytes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Upload a recording.

        Parameters
        ----------
        event : UploadRequestEvent

        start : UploadRequestStart
            Datetime without timezone.

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="PUT",
            json=request,
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
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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

    def recordings_event_start_delete(
        self,
        event: DeleteRequestEvent,
        start: DeleteRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete a recording.

        Parameters
        ----------
        event : DeleteRequestEvent

        start : DeleteRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="DELETE",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def recordings_event_start_headdownload(
        self,
        event: HeadDownloadRequestEvent,
        start: HeadDownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Download recording headers.

        Parameters
        ----------
        event : HeadDownloadRequestEvent

        start : HeadDownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="HEAD",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def recordings_event_list(
        self,
        event: ListRequestEvent,
        *,
        after: typing.Optional[RecordingsEventListRequestAfter] = None,
        before: typing.Optional[RecordingsEventListRequestBefore] = None,
        limit: typing.Optional[RecordingsEventListRequestLimit] = None,
        offset: typing.Optional[RecordingsEventListRequestOffset] = None,
        order: typing.Optional[RecordingsEventListRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseResults]:
        """
        List recordings.

        Parameters
        ----------
        event : ListRequestEvent

        after : typing.Optional[RecordingsEventListRequestAfter]
            Only list recordings after this datetime (in event timezone).

        before : typing.Optional[RecordingsEventListRequestBefore]
            Only list recordings before this datetime (in event timezone).

        limit : typing.Optional[RecordingsEventListRequestLimit]
            Maximum number of recordings to return. Default is 10.

        offset : typing.Optional[RecordingsEventListRequestOffset]
            Number of recordings to skip.

        order : typing.Optional[RecordingsEventListRequestOrder]
            Order to apply to the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseResults]
            Request fulfilled, document follows
        """
        _response = self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}",
            method="GET",
            params={
                "after": convert_and_respect_annotation_metadata(
                    object_=after, annotation=typing.Optional[RecordingsEventListRequestAfter], direction="write"
                ),
                "before": convert_and_respect_annotation_metadata(
                    object_=before, annotation=typing.Optional[RecordingsEventListRequestBefore], direction="write"
                ),
                "limit": limit,
                "offset": offset,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseResults,
                    parse_obj_as(
                        type_=ListResponseResults,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawRecordingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def recordings_event_start_download(
        self,
        event: DownloadRequestEvent,
        start: DownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Download a recording.

        Parameters
        ----------
        event : DownloadRequestEvent

        start : DownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Stream Response
        """
        async with self._client_wrapper.httpx_client.stream(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="GET",
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

    async def recordings_event_start_upload(
        self,
        event: UploadRequestEvent,
        start: UploadRequestStart,
        *,
        request: bytes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Upload a recording.

        Parameters
        ----------
        event : UploadRequestEvent

        start : UploadRequestStart
            Datetime without timezone.

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="PUT",
            json=request,
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
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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

    async def recordings_event_start_delete(
        self,
        event: DeleteRequestEvent,
        start: DeleteRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete a recording.

        Parameters
        ----------
        event : DeleteRequestEvent

        start : DeleteRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="DELETE",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def recordings_event_start_headdownload(
        self,
        event: HeadDownloadRequestEvent,
        start: HeadDownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Download recording headers.

        Parameters
        ----------
        event : HeadDownloadRequestEvent

        start : HeadDownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}/{encode_path_param(start)}",
            method="HEAD",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def recordings_event_list(
        self,
        event: ListRequestEvent,
        *,
        after: typing.Optional[RecordingsEventListRequestAfter] = None,
        before: typing.Optional[RecordingsEventListRequestBefore] = None,
        limit: typing.Optional[RecordingsEventListRequestLimit] = None,
        offset: typing.Optional[RecordingsEventListRequestOffset] = None,
        order: typing.Optional[RecordingsEventListRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseResults]:
        """
        List recordings.

        Parameters
        ----------
        event : ListRequestEvent

        after : typing.Optional[RecordingsEventListRequestAfter]
            Only list recordings after this datetime (in event timezone).

        before : typing.Optional[RecordingsEventListRequestBefore]
            Only list recordings before this datetime (in event timezone).

        limit : typing.Optional[RecordingsEventListRequestLimit]
            Maximum number of recordings to return. Default is 10.

        offset : typing.Optional[RecordingsEventListRequestOffset]
            Number of recordings to skip.

        order : typing.Optional[RecordingsEventListRequestOrder]
            Order to apply to the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseResults]
            Request fulfilled, document follows
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"recordings/{encode_path_param(event)}",
            method="GET",
            params={
                "after": convert_and_respect_annotation_metadata(
                    object_=after, annotation=typing.Optional[RecordingsEventListRequestAfter], direction="write"
                ),
                "before": convert_and_respect_annotation_metadata(
                    object_=before, annotation=typing.Optional[RecordingsEventListRequestBefore], direction="write"
                ),
                "limit": limit,
                "offset": offset,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseResults,
                    parse_obj_as(
                        type_=ListResponseResults,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
