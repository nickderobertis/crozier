

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
from ..types.book_dto import BookDto
from ..types.page_book_dto import PageBookDto
from ..types.validation_error_response import ValidationErrorResponse
from .types.get_books_by_read_list_id_request_media_status_item import GetBooksByReadListIdRequestMediaStatusItem
from .types.get_books_by_read_list_id_request_read_status_item import GetBooksByReadListIdRequestReadStatusItem
from pydantic import ValidationError


class RawReadlistBooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_books_by_read_list_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        read_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]
            ]
        ] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        media_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]
            ]
        ] = None,
        deleted: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageBookDto]:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        read_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        media_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]]]

        deleted : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageBookDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/readlists/{encode_path_param(id)}/books",
            method="GET",
            params={
                "library_id": library_id,
                "read_status": read_status,
                "tag": tag,
                "media_status": media_status,
                "deleted": deleted,
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageBookDto,
                    parse_obj_as(
                        type_=PageBookDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def get_book_sibling_next_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BookDto]:
        """
        Parameters
        ----------
        id : str

        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BookDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/readlists/{encode_path_param(id)}/books/{encode_path_param(book_id)}/next",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BookDto,
                    parse_obj_as(
                        type_=BookDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def get_book_sibling_previous_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BookDto]:
        """
        Parameters
        ----------
        id : str

        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BookDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/readlists/{encode_path_param(id)}/books/{encode_path_param(book_id)}/previous",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BookDto,
                    parse_obj_as(
                        type_=BookDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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


class AsyncRawReadlistBooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_books_by_read_list_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        read_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]
            ]
        ] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        media_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]
            ]
        ] = None,
        deleted: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageBookDto]:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        read_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        media_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]]]

        deleted : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageBookDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/readlists/{encode_path_param(id)}/books",
            method="GET",
            params={
                "library_id": library_id,
                "read_status": read_status,
                "tag": tag,
                "media_status": media_status,
                "deleted": deleted,
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageBookDto,
                    parse_obj_as(
                        type_=PageBookDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def get_book_sibling_next_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BookDto]:
        """
        Parameters
        ----------
        id : str

        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BookDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/readlists/{encode_path_param(id)}/books/{encode_path_param(book_id)}/next",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BookDto,
                    parse_obj_as(
                        type_=BookDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def get_book_sibling_previous_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BookDto]:
        """
        Parameters
        ----------
        id : str

        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BookDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/readlists/{encode_path_param(id)}/books/{encode_path_param(book_id)}/previous",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BookDto,
                    parse_obj_as(
                        type_=BookDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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
