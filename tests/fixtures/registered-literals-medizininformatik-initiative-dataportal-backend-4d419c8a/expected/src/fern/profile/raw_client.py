

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
from ..types.profile_entry import ProfileEntry
from ..types.profile_filter import ProfileFilter
from ..types.profile_search_result import ProfileSearchResult
from .types.get_filter_request_target_filter import GetFilterRequestTargetFilter
from pydantic import ValidationError


class RawProfileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_profiles(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProfileSearchResult]:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProfileSearchResult]
            Ok, return the page of results. Only selectable profiles are returned.
        """
        _response = self._client_wrapper.httpx_client.request(
            "profile/entry/search",
            method="GET",
            params={
                "searchterm": searchterm,
                "modules": ",".join(map(str, modules)) if isinstance(modules, (list, tuple, set)) else modules,
                "categories": ",".join(map(str, categories))
                if isinstance(categories, (list, tuple, set))
                else categories,
                "resource-types": ",".join(map(str, resource_types))
                if isinstance(resource_types, (list, tuple, set))
                else resource_types,
                "page-size": page_size,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileSearchResult,
                    parse_obj_as(
                        type_=ProfileSearchResult,
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

    def get_profile_list_details_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProfileEntry]:
        """
        Parameters
        ----------
        id : str
            The id of the profile entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProfileEntry]
            Entry found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profile/entry/{encode_path_param(id)}/list-details",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileEntry,
                    parse_obj_as(
                        type_=ProfileEntry,
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

    def get_filter(
        self,
        *,
        target_filter: typing.Optional[GetFilterRequestTargetFilter] = None,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ProfileFilter]]:
        """
        Can optionally be filtered to only get the filter of one target category, depending on the selections of the other categories and/or a searchterm

        Parameters
        ----------
        target_filter : typing.Optional[GetFilterRequestTargetFilter]
            The requested filter category. Only if this is set, the further filters for searchterm, modules, categories and resource-types are considered. If it is empty or null, ALL filters are returned unfiltered.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ProfileFilter]]
            Ok, return the list of available filters
        """
        _response = self._client_wrapper.httpx_client.request(
            "profile/search/filter",
            method="GET",
            params={
                "target-filter": target_filter,
                "searchterm": searchterm,
                "modules": ",".join(map(str, modules)) if isinstance(modules, (list, tuple, set)) else modules,
                "categories": ",".join(map(str, categories))
                if isinstance(categories, (list, tuple, set))
                else categories,
                "resource-types": ",".join(map(str, resource_types))
                if isinstance(resource_types, (list, tuple, set))
                else resource_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProfileFilter],
                    parse_obj_as(
                        type_=typing.List[ProfileFilter],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawProfileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_profiles(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProfileSearchResult]:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProfileSearchResult]
            Ok, return the page of results. Only selectable profiles are returned.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "profile/entry/search",
            method="GET",
            params={
                "searchterm": searchterm,
                "modules": ",".join(map(str, modules)) if isinstance(modules, (list, tuple, set)) else modules,
                "categories": ",".join(map(str, categories))
                if isinstance(categories, (list, tuple, set))
                else categories,
                "resource-types": ",".join(map(str, resource_types))
                if isinstance(resource_types, (list, tuple, set))
                else resource_types,
                "page-size": page_size,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileSearchResult,
                    parse_obj_as(
                        type_=ProfileSearchResult,
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

    async def get_profile_list_details_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProfileEntry]:
        """
        Parameters
        ----------
        id : str
            The id of the profile entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProfileEntry]
            Entry found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profile/entry/{encode_path_param(id)}/list-details",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileEntry,
                    parse_obj_as(
                        type_=ProfileEntry,
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

    async def get_filter(
        self,
        *,
        target_filter: typing.Optional[GetFilterRequestTargetFilter] = None,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ProfileFilter]]:
        """
        Can optionally be filtered to only get the filter of one target category, depending on the selections of the other categories and/or a searchterm

        Parameters
        ----------
        target_filter : typing.Optional[GetFilterRequestTargetFilter]
            The requested filter category. Only if this is set, the further filters for searchterm, modules, categories and resource-types are considered. If it is empty or null, ALL filters are returned unfiltered.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ProfileFilter]]
            Ok, return the list of available filters
        """
        _response = await self._client_wrapper.httpx_client.request(
            "profile/search/filter",
            method="GET",
            params={
                "target-filter": target_filter,
                "searchterm": searchterm,
                "modules": ",".join(map(str, modules)) if isinstance(modules, (list, tuple, set)) else modules,
                "categories": ",".join(map(str, categories))
                if isinstance(categories, (list, tuple, set))
                else categories,
                "resource-types": ",".join(map(str, resource_types))
                if isinstance(resource_types, (list, tuple, set))
                else resource_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProfileFilter],
                    parse_obj_as(
                        type_=typing.List[ProfileFilter],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
