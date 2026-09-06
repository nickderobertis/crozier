

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.audio import Audio
from ..types.error import Error
from ..types.paginated_audio_results import PaginatedAudioResults
from ..types.report_request_reason import ReportRequestReason
from ..types.source_stats import SourceStats
from .types.get_audio_waveform_response import GetAudioWaveformResponse
from .types.search_audio_request_category import SearchAudioRequestCategory
from .types.search_audio_request_length import SearchAudioRequestLength
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAudioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_audio(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        license_type: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        excluded_source: typing.Optional[str] = None,
        creator: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        mature: typing.Optional[bool] = None,
        filter_dead: typing.Optional[bool] = None,
        category: typing.Optional[SearchAudioRequestCategory] = None,
        length: typing.Optional[SearchAudioRequestLength] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedAudioResults]:
        """
        Search for openly-licensed audio files with filtering and pagination.

        Parameters
        ----------
        q : typing.Optional[str]
            Full-text search query (max 200 characters)

        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of results per page

        license : typing.Optional[str]
            Filter by license type (comma-separated)

        license_type : typing.Optional[str]
            Filter by license category (commercial, modification)

        source : typing.Optional[str]
            Filter by content source

        excluded_source : typing.Optional[str]
            Exclude content from specific sources

        creator : typing.Optional[str]
            Filter by creator name

        tags : typing.Optional[str]
            Filter by tags

        title : typing.Optional[str]
            Filter by title

        mature : typing.Optional[bool]
            Include mature/sensitive content

        filter_dead : typing.Optional[bool]
            Filter out dead/broken links

        category : typing.Optional[SearchAudioRequestCategory]
            Filter by audio category

        length : typing.Optional[SearchAudioRequestLength]
            Filter by audio duration

        extension : typing.Optional[str]
            Filter by file extension (e.g., mp3, ogg, flac)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedAudioResults]
            Successful audio search results
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio",
            method="GET",
            params={
                "q": q,
                "page": page,
                "page_size": page_size,
                "license": license,
                "license_type": license_type,
                "source": source,
                "excluded_source": excluded_source,
                "creator": creator,
                "tags": tags,
                "title": title,
                "mature": mature,
                "filter_dead": filter_dead,
                "category": category,
                "length": length,
                "extension": extension,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedAudioResults,
                    parse_obj_as(
                        type_=PaginatedAudioResults,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_audio(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Audio]:
        """
        Retrieve detailed information about a specific audio file by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Audio]
            Audio details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Audio,
                    parse_obj_as(
                        type_=Audio,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_related_audio(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PaginatedAudioResults]:
        """
        Find audio files related to a specified audio.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedAudioResults]
            Related audio
        """
        _response = self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}/related",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedAudioResults,
                    parse_obj_as(
                        type_=PaginatedAudioResults,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def report_audio(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Report an audio file for issues such as DMCA violations or mature content.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        reason : ReportRequestReason
            Reason for the report

        description : typing.Optional[str]
            Additional details about the report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}/report",
            method="POST",
            json={
                "reason": reason,
                "description": description,
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
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    def get_audio_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Retrieve a thumbnail for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Thumbnail image
        """
        with self._client_wrapper.httpx_client.stream(
            f"audio/{encode_path_param(identifier)}/thumb",
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
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

    def get_audio_waveform(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAudioWaveformResponse]:
        """
        Retrieve waveform peak data for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAudioWaveformResponse]
            Waveform data
        """
        _response = self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}/waveform",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudioWaveformResponse,
                    parse_obj_as(
                        type_=GetAudioWaveformResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_audio_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[SourceStats]]:
        """
        List all content sources for audio and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SourceStats]]
            Audio source statistics
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio/stats",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SourceStats],
                    parse_obj_as(
                        type_=typing.List[SourceStats],
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


class AsyncRawAudioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_audio(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        license_type: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        excluded_source: typing.Optional[str] = None,
        creator: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        mature: typing.Optional[bool] = None,
        filter_dead: typing.Optional[bool] = None,
        category: typing.Optional[SearchAudioRequestCategory] = None,
        length: typing.Optional[SearchAudioRequestLength] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedAudioResults]:
        """
        Search for openly-licensed audio files with filtering and pagination.

        Parameters
        ----------
        q : typing.Optional[str]
            Full-text search query (max 200 characters)

        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of results per page

        license : typing.Optional[str]
            Filter by license type (comma-separated)

        license_type : typing.Optional[str]
            Filter by license category (commercial, modification)

        source : typing.Optional[str]
            Filter by content source

        excluded_source : typing.Optional[str]
            Exclude content from specific sources

        creator : typing.Optional[str]
            Filter by creator name

        tags : typing.Optional[str]
            Filter by tags

        title : typing.Optional[str]
            Filter by title

        mature : typing.Optional[bool]
            Include mature/sensitive content

        filter_dead : typing.Optional[bool]
            Filter out dead/broken links

        category : typing.Optional[SearchAudioRequestCategory]
            Filter by audio category

        length : typing.Optional[SearchAudioRequestLength]
            Filter by audio duration

        extension : typing.Optional[str]
            Filter by file extension (e.g., mp3, ogg, flac)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedAudioResults]
            Successful audio search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio",
            method="GET",
            params={
                "q": q,
                "page": page,
                "page_size": page_size,
                "license": license,
                "license_type": license_type,
                "source": source,
                "excluded_source": excluded_source,
                "creator": creator,
                "tags": tags,
                "title": title,
                "mature": mature,
                "filter_dead": filter_dead,
                "category": category,
                "length": length,
                "extension": extension,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedAudioResults,
                    parse_obj_as(
                        type_=PaginatedAudioResults,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_audio(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Audio]:
        """
        Retrieve detailed information about a specific audio file by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Audio]
            Audio details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Audio,
                    parse_obj_as(
                        type_=Audio,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_related_audio(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PaginatedAudioResults]:
        """
        Find audio files related to a specified audio.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedAudioResults]
            Related audio
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}/related",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedAudioResults,
                    parse_obj_as(
                        type_=PaginatedAudioResults,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def report_audio(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Report an audio file for issues such as DMCA violations or mature content.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        reason : ReportRequestReason
            Reason for the report

        description : typing.Optional[str]
            Additional details about the report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}/report",
            method="POST",
            json={
                "reason": reason,
                "description": description,
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
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    async def get_audio_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Retrieve a thumbnail for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Thumbnail image
        """
        async with self._client_wrapper.httpx_client.stream(
            f"audio/{encode_path_param(identifier)}/thumb",
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
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

    async def get_audio_waveform(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAudioWaveformResponse]:
        """
        Retrieve waveform peak data for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAudioWaveformResponse]
            Waveform data
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"audio/{encode_path_param(identifier)}/waveform",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudioWaveformResponse,
                    parse_obj_as(
                        type_=GetAudioWaveformResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_audio_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[SourceStats]]:
        """
        List all content sources for audio and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SourceStats]]
            Audio source statistics
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio/stats",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SourceStats],
                    parse_obj_as(
                        type_=typing.List[SourceStats],
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
