

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.book_name import BookName
from ..types.protoform_conformance_v1book import ProtoformConformanceV1Book
from ..types.protoform_conformance_v1list_books_response import ProtoformConformanceV1ListBooksResponse
from ..types.publisher_name import PublisherName
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLibraryRpcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def protoform_conformance_v1library_service_list_books(
        self,
        *,
        parent: PublisherName,
        page_size: typing.Optional[int] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProtoformConformanceV1ListBooksResponse]:
        """
        Parameters
        ----------
        parent : PublisherName

        page_size : typing.Optional[int]

        page_token : typing.Optional[str]

        filter : typing.Optional[str]
            Case-insensitive title or ISBN substring.

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProtoformConformanceV1ListBooksResponse]
            Books in the temporary library
        """
        _response = self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/ListBooks",
            method="POST",
            json={
                "parent": parent,
                "pageSize": page_size,
                "pageToken": page_token,
                "filter": filter,
                "orderBy": order_by,
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
                    ProtoformConformanceV1ListBooksResponse,
                    parse_obj_as(
                        type_=ProtoformConformanceV1ListBooksResponse,
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

    def protoform_conformance_v1library_service_get_book(
        self, *, name: BookName, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProtoformConformanceV1Book]:
        """
        Parameters
        ----------
        name : BookName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProtoformConformanceV1Book]
            The requested book
        """
        _response = self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/GetBook",
            method="POST",
            json={
                "name": name,
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
                    ProtoformConformanceV1Book,
                    parse_obj_as(
                        type_=ProtoformConformanceV1Book,
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

    def protoform_conformance_v1library_service_create_book(
        self,
        *,
        parent: PublisherName,
        book: ProtoformConformanceV1Book,
        book_id: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProtoformConformanceV1Book]:
        """
        Parameters
        ----------
        parent : PublisherName

        book : ProtoformConformanceV1Book

        book_id : str

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProtoformConformanceV1Book]
            The created book
        """
        _response = self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/CreateBook",
            method="POST",
            json={
                "parent": parent,
                "book": convert_and_respect_annotation_metadata(
                    object_=book, annotation=ProtoformConformanceV1Book, direction="write"
                ),
                "bookId": book_id,
                "requestId": request_id,
                "validateOnly": validate_only,
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
                    ProtoformConformanceV1Book,
                    parse_obj_as(
                        type_=ProtoformConformanceV1Book,
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

    def protoform_conformance_v1library_service_update_book(
        self,
        *,
        book: ProtoformConformanceV1Book,
        update_mask: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        allow_missing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProtoformConformanceV1Book]:
        """
        Parameters
        ----------
        book : ProtoformConformanceV1Book

        update_mask : str
            Protobuf JSON FieldMask, such as displayName,note.

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        allow_missing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProtoformConformanceV1Book]
            The updated book with a new etag
        """
        _response = self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/UpdateBook",
            method="POST",
            json={
                "book": convert_and_respect_annotation_metadata(
                    object_=book, annotation=ProtoformConformanceV1Book, direction="write"
                ),
                "updateMask": update_mask,
                "requestId": request_id,
                "validateOnly": validate_only,
                "allowMissing": allow_missing,
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
                    ProtoformConformanceV1Book,
                    parse_obj_as(
                        type_=ProtoformConformanceV1Book,
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

    def protoform_conformance_v1library_service_delete_book(
        self,
        *,
        name: BookName,
        request_id: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a book by resource name and etag. The server validates optimistic concurrency, returns a structured Connect error when the version is stale, and responds with an empty protobuf message after successful deletion.

        Parameters
        ----------
        name : BookName

        request_id : typing.Optional[str]

        etag : typing.Optional[str]
            Last observed book etag.

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Empty protobuf response
        """
        _response = self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/DeleteBook",
            method="POST",
            json={
                "name": name,
                "requestId": request_id,
                "etag": etag,
                "validateOnly": validate_only,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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


class AsyncRawLibraryRpcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def protoform_conformance_v1library_service_list_books(
        self,
        *,
        parent: PublisherName,
        page_size: typing.Optional[int] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProtoformConformanceV1ListBooksResponse]:
        """
        Parameters
        ----------
        parent : PublisherName

        page_size : typing.Optional[int]

        page_token : typing.Optional[str]

        filter : typing.Optional[str]
            Case-insensitive title or ISBN substring.

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProtoformConformanceV1ListBooksResponse]
            Books in the temporary library
        """
        _response = await self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/ListBooks",
            method="POST",
            json={
                "parent": parent,
                "pageSize": page_size,
                "pageToken": page_token,
                "filter": filter,
                "orderBy": order_by,
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
                    ProtoformConformanceV1ListBooksResponse,
                    parse_obj_as(
                        type_=ProtoformConformanceV1ListBooksResponse,
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

    async def protoform_conformance_v1library_service_get_book(
        self, *, name: BookName, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProtoformConformanceV1Book]:
        """
        Parameters
        ----------
        name : BookName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProtoformConformanceV1Book]
            The requested book
        """
        _response = await self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/GetBook",
            method="POST",
            json={
                "name": name,
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
                    ProtoformConformanceV1Book,
                    parse_obj_as(
                        type_=ProtoformConformanceV1Book,
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

    async def protoform_conformance_v1library_service_create_book(
        self,
        *,
        parent: PublisherName,
        book: ProtoformConformanceV1Book,
        book_id: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProtoformConformanceV1Book]:
        """
        Parameters
        ----------
        parent : PublisherName

        book : ProtoformConformanceV1Book

        book_id : str

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProtoformConformanceV1Book]
            The created book
        """
        _response = await self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/CreateBook",
            method="POST",
            json={
                "parent": parent,
                "book": convert_and_respect_annotation_metadata(
                    object_=book, annotation=ProtoformConformanceV1Book, direction="write"
                ),
                "bookId": book_id,
                "requestId": request_id,
                "validateOnly": validate_only,
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
                    ProtoformConformanceV1Book,
                    parse_obj_as(
                        type_=ProtoformConformanceV1Book,
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

    async def protoform_conformance_v1library_service_update_book(
        self,
        *,
        book: ProtoformConformanceV1Book,
        update_mask: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        allow_missing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProtoformConformanceV1Book]:
        """
        Parameters
        ----------
        book : ProtoformConformanceV1Book

        update_mask : str
            Protobuf JSON FieldMask, such as displayName,note.

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        allow_missing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProtoformConformanceV1Book]
            The updated book with a new etag
        """
        _response = await self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/UpdateBook",
            method="POST",
            json={
                "book": convert_and_respect_annotation_metadata(
                    object_=book, annotation=ProtoformConformanceV1Book, direction="write"
                ),
                "updateMask": update_mask,
                "requestId": request_id,
                "validateOnly": validate_only,
                "allowMissing": allow_missing,
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
                    ProtoformConformanceV1Book,
                    parse_obj_as(
                        type_=ProtoformConformanceV1Book,
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

    async def protoform_conformance_v1library_service_delete_book(
        self,
        *,
        name: BookName,
        request_id: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a book by resource name and etag. The server validates optimistic concurrency, returns a structured Connect error when the version is stale, and responds with an empty protobuf message after successful deletion.

        Parameters
        ----------
        name : BookName

        request_id : typing.Optional[str]

        etag : typing.Optional[str]
            Last observed book etag.

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Empty protobuf response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "protoform.conformance.v1.LibraryService/DeleteBook",
            method="POST",
            json={
                "name": name,
                "requestId": request_id,
                "etag": etag,
                "validateOnly": validate_only,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
