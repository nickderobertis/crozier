

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.criteria_profile_data import CriteriaProfileData
from ..types.elastic_search_bulk_result import ElasticSearchBulkResult
from ..types.elastic_search_result import ElasticSearchResult
from ..types.elastic_search_result_entry import ElasticSearchResultEntry
from ..types.filter import Filter
from ..types.relations_entry import RelationsEntry
from ..types.terminology_systems import TerminologySystems
from ..types.ui_profile_list import UiProfileList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTerminologyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_filters(
        self,
        *,
        target_filter: typing.Optional[str] = None,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Filter]]:
        """
        Can optionally be filtered to only get the filters of one category, depending on the selections of other categories

        Parameters
        ----------
        target_filter : typing.Optional[str]
            The requested filter category. Only if this is set, the further filters for contexts, kds-modules and terminologies are considered. If it is empty or null, ALL entries are returned.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Filter]]
            Ok, return the list of available filters
        """
        _response = self._client_wrapper.httpx_client.request(
            "terminology/search/filter",
            method="GET",
            params={
                "target-filter": target_filter,
                "searchterm": searchterm,
                "contexts": ",".join(map(str, contexts)) if isinstance(contexts, (list, tuple, set)) else contexts,
                "terminologies": ",".join(map(str, terminologies))
                if isinstance(terminologies, (list, tuple, set))
                else terminologies,
                "kds-modules": ",".join(map(str, kds_modules))
                if isinstance(kds_modules, (list, tuple, set))
                else kds_modules,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Filter],
                    parse_obj_as(
                        type_=typing.List[Filter],
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

    def get_terminology_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TerminologySystems]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TerminologySystems]
            System mapping file found and readable
        """
        _response = self._client_wrapper.httpx_client.request(
            "terminology/systems",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TerminologySystems,
                    parse_obj_as(
                        type_=TerminologySystems,
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

    def search_entry(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        criteria_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        availability: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ElasticSearchResult]:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        criteria_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain criteria sets (specified via url)

        availability : typing.Optional[bool]
            Limit the search to available items? (Maybe better invert this one to make this the default?)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ElasticSearchResult]
            Ok, return the list of results for the search
        """
        _response = self._client_wrapper.httpx_client.request(
            "terminology/entry/search",
            method="GET",
            params={
                "searchterm": searchterm,
                "contexts": ",".join(map(str, contexts)) if isinstance(contexts, (list, tuple, set)) else contexts,
                "terminologies": ",".join(map(str, terminologies))
                if isinstance(terminologies, (list, tuple, set))
                else terminologies,
                "kds-modules": ",".join(map(str, kds_modules))
                if isinstance(kds_modules, (list, tuple, set))
                else kds_modules,
                "criteria-sets": ",".join(map(str, criteria_sets))
                if isinstance(criteria_sets, (list, tuple, set))
                else criteria_sets,
                "availability": availability,
                "page-size": page_size,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElasticSearchResult,
                    parse_obj_as(
                        type_=ElasticSearchResult,
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

    def bulk_search_entry(
        self,
        *,
        terminology: str,
        context: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ElasticSearchBulkResult]:
        """
        Parameters
        ----------
        terminology : str

        context : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ElasticSearchBulkResult]
            Ok, return the list of results for the search
        """
        _response = self._client_wrapper.httpx_client.request(
            "terminology/entry/bulk-search",
            method="POST",
            json={
                "terminology": terminology,
                "context": context,
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
                    ElasticSearchBulkResult,
                    parse_obj_as(
                        type_=ElasticSearchBulkResult,
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

    def get_entry_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RelationsEntry]:
        """
        Parameters
        ----------
        id : str
            The id (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RelationsEntry]
            Entry found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"terminology/entry/{encode_path_param(id)}/relations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RelationsEntry,
                    parse_obj_as(
                        type_=RelationsEntry,
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

    def get_entries_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ElasticSearchResultEntry]:
        """
        This should be in the getEntryById call, but for better distinction between the return values it is listed separately here

        Parameters
        ----------
        id : str
            The ids (contextualized termcode hash) of the entries that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ElasticSearchResultEntry]
            Entry found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"terminology/entry/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElasticSearchResultEntry,
                    parse_obj_as(
                        type_=ElasticSearchResultEntry,
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

    def get_entries_by_ids_with_detail(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[CriteriaProfileData]]:
        """
        This should return all the information needed to build criteria in the frontend.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (contextualized termcode hashes) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CriteriaProfileData]]
            Entries found. May contain empty entries if some were not found.
        """
        _response = self._client_wrapper.httpx_client.request(
            "terminology/criteria-profile-data",
            method="GET",
            params={
                "ids": ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CriteriaProfileData],
                    parse_obj_as(
                        type_=typing.List[CriteriaProfileData],
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

    def get_ui_profiles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UiProfileList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UiProfileList]
            Get all UiProfiles
        """
        _response = self._client_wrapper.httpx_client.request(
            "terminology/ui-profile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UiProfileList,
                    parse_obj_as(
                        type_=UiProfileList,
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


class AsyncRawTerminologyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_filters(
        self,
        *,
        target_filter: typing.Optional[str] = None,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Filter]]:
        """
        Can optionally be filtered to only get the filters of one category, depending on the selections of other categories

        Parameters
        ----------
        target_filter : typing.Optional[str]
            The requested filter category. Only if this is set, the further filters for contexts, kds-modules and terminologies are considered. If it is empty or null, ALL entries are returned.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Filter]]
            Ok, return the list of available filters
        """
        _response = await self._client_wrapper.httpx_client.request(
            "terminology/search/filter",
            method="GET",
            params={
                "target-filter": target_filter,
                "searchterm": searchterm,
                "contexts": ",".join(map(str, contexts)) if isinstance(contexts, (list, tuple, set)) else contexts,
                "terminologies": ",".join(map(str, terminologies))
                if isinstance(terminologies, (list, tuple, set))
                else terminologies,
                "kds-modules": ",".join(map(str, kds_modules))
                if isinstance(kds_modules, (list, tuple, set))
                else kds_modules,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Filter],
                    parse_obj_as(
                        type_=typing.List[Filter],
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

    async def get_terminology_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TerminologySystems]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TerminologySystems]
            System mapping file found and readable
        """
        _response = await self._client_wrapper.httpx_client.request(
            "terminology/systems",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TerminologySystems,
                    parse_obj_as(
                        type_=TerminologySystems,
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

    async def search_entry(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        criteria_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        availability: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ElasticSearchResult]:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        criteria_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain criteria sets (specified via url)

        availability : typing.Optional[bool]
            Limit the search to available items? (Maybe better invert this one to make this the default?)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ElasticSearchResult]
            Ok, return the list of results for the search
        """
        _response = await self._client_wrapper.httpx_client.request(
            "terminology/entry/search",
            method="GET",
            params={
                "searchterm": searchterm,
                "contexts": ",".join(map(str, contexts)) if isinstance(contexts, (list, tuple, set)) else contexts,
                "terminologies": ",".join(map(str, terminologies))
                if isinstance(terminologies, (list, tuple, set))
                else terminologies,
                "kds-modules": ",".join(map(str, kds_modules))
                if isinstance(kds_modules, (list, tuple, set))
                else kds_modules,
                "criteria-sets": ",".join(map(str, criteria_sets))
                if isinstance(criteria_sets, (list, tuple, set))
                else criteria_sets,
                "availability": availability,
                "page-size": page_size,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElasticSearchResult,
                    parse_obj_as(
                        type_=ElasticSearchResult,
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

    async def bulk_search_entry(
        self,
        *,
        terminology: str,
        context: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ElasticSearchBulkResult]:
        """
        Parameters
        ----------
        terminology : str

        context : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ElasticSearchBulkResult]
            Ok, return the list of results for the search
        """
        _response = await self._client_wrapper.httpx_client.request(
            "terminology/entry/bulk-search",
            method="POST",
            json={
                "terminology": terminology,
                "context": context,
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
                    ElasticSearchBulkResult,
                    parse_obj_as(
                        type_=ElasticSearchBulkResult,
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

    async def get_entry_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RelationsEntry]:
        """
        Parameters
        ----------
        id : str
            The id (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RelationsEntry]
            Entry found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"terminology/entry/{encode_path_param(id)}/relations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RelationsEntry,
                    parse_obj_as(
                        type_=RelationsEntry,
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

    async def get_entries_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ElasticSearchResultEntry]:
        """
        This should be in the getEntryById call, but for better distinction between the return values it is listed separately here

        Parameters
        ----------
        id : str
            The ids (contextualized termcode hash) of the entries that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ElasticSearchResultEntry]
            Entry found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"terminology/entry/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElasticSearchResultEntry,
                    parse_obj_as(
                        type_=ElasticSearchResultEntry,
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

    async def get_entries_by_ids_with_detail(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[CriteriaProfileData]]:
        """
        This should return all the information needed to build criteria in the frontend.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (contextualized termcode hashes) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CriteriaProfileData]]
            Entries found. May contain empty entries if some were not found.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "terminology/criteria-profile-data",
            method="GET",
            params={
                "ids": ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CriteriaProfileData],
                    parse_obj_as(
                        type_=typing.List[CriteriaProfileData],
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

    async def get_ui_profiles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UiProfileList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UiProfileList]
            Get all UiProfiles
        """
        _response = await self._client_wrapper.httpx_client.request(
            "terminology/ui-profile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UiProfileList,
                    parse_obj_as(
                        type_=UiProfileList,
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
