

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.codeable_concept_bulk_search_result import CodeableConceptBulkSearchResult
from ..types.codeable_concept_entry import CodeableConceptEntry
from ..types.codeable_concept_search_result import CodeableConceptSearchResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCodeableConceptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_codeable_concepts(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        value_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CodeableConceptSearchResult]:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        value_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain value sets (specified via url)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CodeableConceptSearchResult]
            Ok, return the page of results
        """
        _response = self._client_wrapper.httpx_client.request(
            "codeable-concept/entry/search",
            method="GET",
            params={
                "searchterm": searchterm,
                "value-sets": ",".join(map(str, value_sets))
                if isinstance(value_sets, (list, tuple, set))
                else value_sets,
                "page-size": page_size,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CodeableConceptSearchResult,
                    parse_obj_as(
                        type_=CodeableConceptSearchResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def bulk_search_codeable_concepts(
        self,
        *,
        value_set: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CodeableConceptBulkSearchResult]:
        """
        Parameters
        ----------
        value_set : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CodeableConceptBulkSearchResult]
            Ok, return a list with found codes and a list with codes that were not found
        """
        _response = self._client_wrapper.httpx_client.request(
            "codeable-concept/entry/bulk-search",
            method="POST",
            json={
                "valueSet": value_set,
                "searchterms": searchterms,
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
                    CodeableConceptBulkSearchResult,
                    parse_obj_as(
                        type_=CodeableConceptBulkSearchResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def get_codeable_concepts_by_code(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CodeableConceptEntry]:
        """
        Parameters
        ----------
        ids : str
            The ids (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CodeableConceptEntry]
            Ok, return the codeable concept
        """
        _response = self._client_wrapper.httpx_client.request(
            "codeable-concept/entry",
            method="GET",
            params={
                "ids": ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CodeableConceptEntry,
                    parse_obj_as(
                        type_=CodeableConceptEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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


class AsyncRawCodeableConceptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_codeable_concepts(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        value_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CodeableConceptSearchResult]:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        value_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain value sets (specified via url)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CodeableConceptSearchResult]
            Ok, return the page of results
        """
        _response = await self._client_wrapper.httpx_client.request(
            "codeable-concept/entry/search",
            method="GET",
            params={
                "searchterm": searchterm,
                "value-sets": ",".join(map(str, value_sets))
                if isinstance(value_sets, (list, tuple, set))
                else value_sets,
                "page-size": page_size,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CodeableConceptSearchResult,
                    parse_obj_as(
                        type_=CodeableConceptSearchResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def bulk_search_codeable_concepts(
        self,
        *,
        value_set: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CodeableConceptBulkSearchResult]:
        """
        Parameters
        ----------
        value_set : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CodeableConceptBulkSearchResult]
            Ok, return a list with found codes and a list with codes that were not found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "codeable-concept/entry/bulk-search",
            method="POST",
            json={
                "valueSet": value_set,
                "searchterms": searchterms,
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
                    CodeableConceptBulkSearchResult,
                    parse_obj_as(
                        type_=CodeableConceptBulkSearchResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def get_codeable_concepts_by_code(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CodeableConceptEntry]:
        """
        Parameters
        ----------
        ids : str
            The ids (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CodeableConceptEntry]
            Ok, return the codeable concept
        """
        _response = await self._client_wrapper.httpx_client.request(
            "codeable-concept/entry",
            method="GET",
            params={
                "ids": ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CodeableConceptEntry,
                    parse_obj_as(
                        type_=CodeableConceptEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
