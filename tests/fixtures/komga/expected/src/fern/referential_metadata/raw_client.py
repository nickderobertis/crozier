

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.page_author_dto import PageAuthorDto
from ..types.page_integer import PageInteger
from ..types.page_string import PageString
from ..types.validation_error_response import ValidationErrorResponse
from .types.get_tags_request_include import GetTagsRequestInclude
from pydantic import ValidationError


class RawReferentialMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_age_ratings(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageInteger]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageInteger]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/age-ratings",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageInteger,
                    parse_obj_as(
                        type_=PageInteger,
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

    def get_authors(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageAuthorDto]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageAuthorDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/authors",
            method="GET",
            params={
                "search": search,
                "role": role,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageAuthorDto,
                    parse_obj_as(
                        type_=PageAuthorDto,
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

    def get_authors_names(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/authors/names",
            method="GET",
            params={
                "search": search,
                "role": role,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    def get_authors_roles(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/authors/roles",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    def get_genres(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/genres",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    def get_languages(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/languages",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    def get_publishers(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/publishers",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    def get_series_release_years(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/series/release-years",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    def get_sharing_labels(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/sharing-labels",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    def get_tags(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include: typing.Optional[GetTagsRequestInclude] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        include : typing.Optional[GetTagsRequestInclude]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tags",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "include": include,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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


class AsyncRawReferentialMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_age_ratings(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageInteger]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageInteger]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/age-ratings",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageInteger,
                    parse_obj_as(
                        type_=PageInteger,
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

    async def get_authors(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageAuthorDto]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageAuthorDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/authors",
            method="GET",
            params={
                "search": search,
                "role": role,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageAuthorDto,
                    parse_obj_as(
                        type_=PageAuthorDto,
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

    async def get_authors_names(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/authors/names",
            method="GET",
            params={
                "search": search,
                "role": role,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    async def get_authors_roles(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/authors/roles",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    async def get_genres(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/genres",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    async def get_languages(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/languages",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    async def get_publishers(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/publishers",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    async def get_series_release_years(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/series/release-years",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    async def get_sharing_labels(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/sharing-labels",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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

    async def get_tags(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include: typing.Optional[GetTagsRequestInclude] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageString]:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        include : typing.Optional[GetTagsRequestInclude]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tags",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
                "readlist_id": readlist_id,
                "include": include,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageString,
                    parse_obj_as(
                        type_=PageString,
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
