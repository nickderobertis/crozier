

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
from ..errors.not_found_error import NotFoundError
from ..types.author import Author
from ..types.author_asin import AuthorAsin
from ..types.author_description import AuthorDescription
from ..types.author_id import AuthorId
from ..types.author_image_path import AuthorImagePath
from ..types.author_name import AuthorName
from ..types.author_search_name import AuthorSearchName
from ..types.image_format import ImageFormat
from ..types.image_height import ImageHeight
from ..types.image_raw import ImageRaw
from ..types.image_url import ImageUrl
from ..types.image_width import ImageWidth
from ..types.region import Region
from .types.match_author_by_id_response import MatchAuthorByIdResponse
from .types.update_author_by_id_response import UpdateAuthorByIdResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_author_by_id(
        self,
        id: AuthorId,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Author]:
        """
        Get an author by ID. The author's books and series can be included in the response.

        Parameters
        ----------
        id : AuthorId
            Author ID

        include : typing.Optional[str]
            A comma separated list of what to include with the author. The options are `items` and `series`. `series` will only have an effect if `items` is included. For example, the value `items,series` will include both library items and series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Author]
            getAuthorById OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}",
            method="GET",
            params={
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Author,
                    parse_obj_as(
                        type_=Author,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_author_by_id(
        self, id: AuthorId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Delete an author by ID. This will remove the author from all books.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            deleteAuthorById OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_author_by_id(
        self,
        id: AuthorId,
        *,
        name: typing.Optional[AuthorName] = OMIT,
        description: typing.Optional[AuthorDescription] = OMIT,
        image_path: typing.Optional[AuthorImagePath] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateAuthorByIdResponse]:
        """
        Update an author by ID. The author's name and description can be updated. This endpoint will merge two authors if the new author name matches another author name in the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        name : typing.Optional[AuthorName]

        description : typing.Optional[AuthorDescription]

        image_path : typing.Optional[AuthorImagePath]

        asin : typing.Optional[AuthorAsin]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateAuthorByIdResponse]
            updateAuthorById OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "imagePath": image_path,
                "asin": asin,
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
                    UpdateAuthorByIdResponse,
                    parse_obj_as(
                        type_=UpdateAuthorByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Get an author image by author ID. The image will be returned in the requested format and size.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            getAuthorImageById OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"api/authors/{encode_path_param(id)}/image",
            method="GET",
            params={
                "token": token,
                "ts": ts,
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

    @contextlib.contextmanager
    def add_author_image_by_id(
        self,
        id: AuthorId,
        *,
        request: ImageUrl,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Add an author image to the server. The image will be downloaded from the provided URL and stored on the server.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request : ImageUrl

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            addAuthorImageById OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"api/authors/{encode_path_param(id)}/image",
            method="POST",
            params={
                "token": token,
                "ts": ts,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    def delete_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete an author image by author ID. This will remove the image from the server and the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}/image",
            method="DELETE",
            params={
                "token": token,
                "ts": ts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def update_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        width: typing.Optional[ImageWidth] = OMIT,
        height: typing.Optional[ImageHeight] = OMIT,
        format: typing.Optional[ImageFormat] = OMIT,
        raw: typing.Optional[ImageRaw] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Update an author image by author ID. The image will be resized if the width, height, or format is provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        width : typing.Optional[ImageWidth]

        height : typing.Optional[ImageHeight]

        format : typing.Optional[ImageFormat]

        raw : typing.Optional[ImageRaw]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            updateAuthorImageById OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"api/authors/{encode_path_param(id)}/image",
            method="PATCH",
            params={
                "token": token,
                "ts": ts,
            },
            json={
                "width": width,
                "height": height,
                "format": format,
                "raw": raw,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    def match_author_by_id(
        self,
        id: AuthorId,
        *,
        q: typing.Optional[AuthorSearchName] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MatchAuthorByIdResponse]:
        """
        Match the author against Audible using quick match. Quick match updates the author's description and image (if no image already existed) with information from audible. Either `asin` or `q` must be provided, with `asin` taking priority if both are provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        q : typing.Optional[AuthorSearchName]

        asin : typing.Optional[AuthorAsin]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MatchAuthorByIdResponse]
            matchAuthorById OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}/match",
            method="POST",
            json={
                "q": q,
                "asin": asin,
                "region": region,
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
                    MatchAuthorByIdResponse,
                    parse_obj_as(
                        type_=MatchAuthorByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAuthorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_author_by_id(
        self,
        id: AuthorId,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Author]:
        """
        Get an author by ID. The author's books and series can be included in the response.

        Parameters
        ----------
        id : AuthorId
            Author ID

        include : typing.Optional[str]
            A comma separated list of what to include with the author. The options are `items` and `series`. `series` will only have an effect if `items` is included. For example, the value `items,series` will include both library items and series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Author]
            getAuthorById OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}",
            method="GET",
            params={
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Author,
                    parse_obj_as(
                        type_=Author,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_author_by_id(
        self, id: AuthorId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Delete an author by ID. This will remove the author from all books.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            deleteAuthorById OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_author_by_id(
        self,
        id: AuthorId,
        *,
        name: typing.Optional[AuthorName] = OMIT,
        description: typing.Optional[AuthorDescription] = OMIT,
        image_path: typing.Optional[AuthorImagePath] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateAuthorByIdResponse]:
        """
        Update an author by ID. The author's name and description can be updated. This endpoint will merge two authors if the new author name matches another author name in the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        name : typing.Optional[AuthorName]

        description : typing.Optional[AuthorDescription]

        image_path : typing.Optional[AuthorImagePath]

        asin : typing.Optional[AuthorAsin]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateAuthorByIdResponse]
            updateAuthorById OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "imagePath": image_path,
                "asin": asin,
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
                    UpdateAuthorByIdResponse,
                    parse_obj_as(
                        type_=UpdateAuthorByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Get an author image by author ID. The image will be returned in the requested format and size.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            getAuthorImageById OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"api/authors/{encode_path_param(id)}/image",
            method="GET",
            params={
                "token": token,
                "ts": ts,
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

    @contextlib.asynccontextmanager
    async def add_author_image_by_id(
        self,
        id: AuthorId,
        *,
        request: ImageUrl,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Add an author image to the server. The image will be downloaded from the provided URL and stored on the server.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request : ImageUrl

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            addAuthorImageById OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"api/authors/{encode_path_param(id)}/image",
            method="POST",
            params={
                "token": token,
                "ts": ts,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    async def delete_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete an author image by author ID. This will remove the image from the server and the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}/image",
            method="DELETE",
            params={
                "token": token,
                "ts": ts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def update_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        width: typing.Optional[ImageWidth] = OMIT,
        height: typing.Optional[ImageHeight] = OMIT,
        format: typing.Optional[ImageFormat] = OMIT,
        raw: typing.Optional[ImageRaw] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Update an author image by author ID. The image will be resized if the width, height, or format is provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        width : typing.Optional[ImageWidth]

        height : typing.Optional[ImageHeight]

        format : typing.Optional[ImageFormat]

        raw : typing.Optional[ImageRaw]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            updateAuthorImageById OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"api/authors/{encode_path_param(id)}/image",
            method="PATCH",
            params={
                "token": token,
                "ts": ts,
            },
            json={
                "width": width,
                "height": height,
                "format": format,
                "raw": raw,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    async def match_author_by_id(
        self,
        id: AuthorId,
        *,
        q: typing.Optional[AuthorSearchName] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MatchAuthorByIdResponse]:
        """
        Match the author against Audible using quick match. Quick match updates the author's description and image (if no image already existed) with information from audible. Either `asin` or `q` must be provided, with `asin` taking priority if both are provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        q : typing.Optional[AuthorSearchName]

        asin : typing.Optional[AuthorAsin]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MatchAuthorByIdResponse]
            matchAuthorById OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/authors/{encode_path_param(id)}/match",
            method="POST",
            json={
                "q": q,
                "asin": asin,
                "region": region,
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
                    MatchAuthorByIdResponse,
                    parse_obj_as(
                        type_=MatchAuthorByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
