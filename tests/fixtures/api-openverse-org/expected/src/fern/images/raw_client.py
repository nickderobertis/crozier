

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
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.image import Image
from ..types.paginated_image_results import PaginatedImageResults
from ..types.report_request_reason import ReportRequestReason
from ..types.source_stats import SourceStats
from .types.get_image_oembed_response import GetImageOembedResponse
from .types.search_images_request_aspect_ratio import SearchImagesRequestAspectRatio
from .types.search_images_request_category import SearchImagesRequestCategory
from .types.search_images_request_size import SearchImagesRequestSize
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawImagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_images(
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
        aspect_ratio: typing.Optional[SearchImagesRequestAspectRatio] = None,
        size: typing.Optional[SearchImagesRequestSize] = None,
        category: typing.Optional[SearchImagesRequestCategory] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedImageResults]:
        """
        Search for openly-licensed images with extensive filtering options.

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

        aspect_ratio : typing.Optional[SearchImagesRequestAspectRatio]
            Filter by aspect ratio

        size : typing.Optional[SearchImagesRequestSize]
            Filter by image size

        category : typing.Optional[SearchImagesRequestCategory]
            Filter by image category

        extension : typing.Optional[str]
            Filter by file extension

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedImageResults]
            Successful image search results
        """
        _response = self._client_wrapper.httpx_client.request(
            "images",
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
                "aspect_ratio": aspect_ratio,
                "size": size,
                "category": category,
                "extension": extension,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedImageResults,
                    parse_obj_as(
                        type_=PaginatedImageResults,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def get_image(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Image]:
        """
        Retrieve detailed information about a specific image by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Image]
            Image details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Image,
                    parse_obj_as(
                        type_=Image,
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

    def get_related_images(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PaginatedImageResults]:
        """
        Find images related to a specified image.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedImageResults]
            Related images
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{encode_path_param(identifier)}/related",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedImageResults,
                    parse_obj_as(
                        type_=PaginatedImageResults,
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

    def report_image(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Report an image for issues such as DMCA violations, mature content, or other concerns.

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
            f"images/{encode_path_param(identifier)}/report",
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
    def get_image_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Retrieve a thumbnail proxy for the specified image.

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
            f"images/{encode_path_param(identifier)}/thumb",
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

    def get_image_oembed(
        self, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetImageOembedResponse]:
        """
        Retrieve oEmbed structured data for embedding an image.

        Parameters
        ----------
        url : str
            The URL of the image to retrieve oEmbed data for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetImageOembedResponse]
            oEmbed response
        """
        _response = self._client_wrapper.httpx_client.request(
            "images/oembed",
            method="GET",
            params={
                "url": url,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetImageOembedResponse,
                    parse_obj_as(
                        type_=GetImageOembedResponse,
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

    def get_image_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[SourceStats]]:
        """
        List all content sources for images and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SourceStats]]
            Image source statistics
        """
        _response = self._client_wrapper.httpx_client.request(
            "images/stats",
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


class AsyncRawImagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_images(
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
        aspect_ratio: typing.Optional[SearchImagesRequestAspectRatio] = None,
        size: typing.Optional[SearchImagesRequestSize] = None,
        category: typing.Optional[SearchImagesRequestCategory] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedImageResults]:
        """
        Search for openly-licensed images with extensive filtering options.

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

        aspect_ratio : typing.Optional[SearchImagesRequestAspectRatio]
            Filter by aspect ratio

        size : typing.Optional[SearchImagesRequestSize]
            Filter by image size

        category : typing.Optional[SearchImagesRequestCategory]
            Filter by image category

        extension : typing.Optional[str]
            Filter by file extension

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedImageResults]
            Successful image search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images",
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
                "aspect_ratio": aspect_ratio,
                "size": size,
                "category": category,
                "extension": extension,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedImageResults,
                    parse_obj_as(
                        type_=PaginatedImageResults,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def get_image(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Image]:
        """
        Retrieve detailed information about a specific image by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Image]
            Image details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Image,
                    parse_obj_as(
                        type_=Image,
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

    async def get_related_images(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PaginatedImageResults]:
        """
        Find images related to a specified image.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedImageResults]
            Related images
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{encode_path_param(identifier)}/related",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedImageResults,
                    parse_obj_as(
                        type_=PaginatedImageResults,
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

    async def report_image(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Report an image for issues such as DMCA violations, mature content, or other concerns.

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
            f"images/{encode_path_param(identifier)}/report",
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
    async def get_image_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Retrieve a thumbnail proxy for the specified image.

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
            f"images/{encode_path_param(identifier)}/thumb",
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

    async def get_image_oembed(
        self, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetImageOembedResponse]:
        """
        Retrieve oEmbed structured data for embedding an image.

        Parameters
        ----------
        url : str
            The URL of the image to retrieve oEmbed data for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetImageOembedResponse]
            oEmbed response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images/oembed",
            method="GET",
            params={
                "url": url,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetImageOembedResponse,
                    parse_obj_as(
                        type_=GetImageOembedResponse,
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

    async def get_image_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[SourceStats]]:
        """
        List all content sources for images and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SourceStats]]
            Image source statistics
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images/stats",
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
