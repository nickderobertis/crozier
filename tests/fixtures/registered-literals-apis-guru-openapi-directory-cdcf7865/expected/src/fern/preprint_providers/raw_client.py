

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.preprint_provider_detail_response import PreprintProviderDetailResponse
from .types.preprint_provider_licenses_list_response import PreprintProviderLicensesListResponse
from .types.preprint_provider_list_response import PreprintProviderListResponse
from .types.preprint_provider_taxonomies_list_response import PreprintProviderTaxonomiesListResponse
from .types.preprint_providers_preprints_list_response_item import PreprintProvidersPreprintsListResponseItem
from pydantic import ValidationError


class RawPreprintProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def preprint_provider_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreprintProviderListResponse]:
        """

        A paginated list of all preprint providers. The returned preprint providers are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprint providers that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/?filter[id]=osf.

        Preprint Providers may be filtered by their `id`, `name`,  and `description`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreprintProviderListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "preprint_providers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderListResponse,
                    parse_obj_as(
                        type_=PreprintProviderListResponse,
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

    def preprint_provider_detail(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreprintProviderDetailResponse]:
        """
        Retrieves the details of a preprint provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint provider, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Acceptable Subjects Structure
        Each preprint provider specifies acceptable subjects.
        `subjects_acceptable` is an array found in `attributes`.
        Subjects consist of general parent subjects (e.g., Engineering), more specific child subjects (e.g., Aerospace Engineering), and even more specific grandchild subjects (e.g., Aerodynamics and Fluid Mechanics). Subjects can only be nested 3 deep.


            "subjects_acceptable": [
                [
                    [
                        # Parent Subject:
                        # Architecture
                        "584240d954be81056ceca9e5",

                        # Child Subject:
                        # Architectural Engineering
                        "584240da54be81056cecac87"
                    ],
                    # Include all Architectural Engineering's children:
                    true
                ],
                [
                    [
                        # Parent Subject:
                        # Engineering
                        "584240da54be81056cecaca9",

                        # Child Subject:
                        # Aerospace Engineering
                        "584240db54be81056cecacd6",

                        # Grandchild Subject:
                        # Aerodynamics and Fluid Mechanics
                        "584240da54be81056cecaa74"
                    ],
                    # All nestings 3 deep must be false
                    false
                ]
            ]

        The above structure would allow Architecture, Architectural Engineering, all of Architectural Engineering's children, Engineering, Aerospace Engineering, and Aerodynamics and Fluid Mechanics.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreprintProviderDetailResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderDetailResponse,
                    parse_obj_as(
                        type_=PreprintProviderDetailResponse,
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

    def preprint_provider_licenses_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreprintProviderLicensesListResponse]:
        """

        A paginated list of the licenses allowed by a preprint provider.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreprintProviderLicensesListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/licenses/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderLicensesListResponse,
                    parse_obj_as(
                        type_=PreprintProviderLicensesListResponse,
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

    def preprints_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PreprintProvidersPreprintsListResponseItem]]:
        """

        A paginated list of preprints from the specified preprint provider. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary with keys that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/osf/preprints/?filter[is_published]=true.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PreprintProvidersPreprintsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/preprints/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintProvidersPreprintsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintProvidersPreprintsListResponseItem],
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

    def preprint_provider_taxonomies_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreprintProviderTaxonomiesListResponse]:
        """

        A paginated list of the taxonomies for a preprint provider. The returned preprint providers taxonomies are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreprintProviderTaxonomiesListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/taxonomies/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderTaxonomiesListResponse,
                    parse_obj_as(
                        type_=PreprintProviderTaxonomiesListResponse,
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


class AsyncRawPreprintProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def preprint_provider_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreprintProviderListResponse]:
        """

        A paginated list of all preprint providers. The returned preprint providers are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprint providers that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/?filter[id]=osf.

        Preprint Providers may be filtered by their `id`, `name`,  and `description`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreprintProviderListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "preprint_providers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderListResponse,
                    parse_obj_as(
                        type_=PreprintProviderListResponse,
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

    async def preprint_provider_detail(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreprintProviderDetailResponse]:
        """
        Retrieves the details of a preprint provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint provider, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Acceptable Subjects Structure
        Each preprint provider specifies acceptable subjects.
        `subjects_acceptable` is an array found in `attributes`.
        Subjects consist of general parent subjects (e.g., Engineering), more specific child subjects (e.g., Aerospace Engineering), and even more specific grandchild subjects (e.g., Aerodynamics and Fluid Mechanics). Subjects can only be nested 3 deep.


            "subjects_acceptable": [
                [
                    [
                        # Parent Subject:
                        # Architecture
                        "584240d954be81056ceca9e5",

                        # Child Subject:
                        # Architectural Engineering
                        "584240da54be81056cecac87"
                    ],
                    # Include all Architectural Engineering's children:
                    true
                ],
                [
                    [
                        # Parent Subject:
                        # Engineering
                        "584240da54be81056cecaca9",

                        # Child Subject:
                        # Aerospace Engineering
                        "584240db54be81056cecacd6",

                        # Grandchild Subject:
                        # Aerodynamics and Fluid Mechanics
                        "584240da54be81056cecaa74"
                    ],
                    # All nestings 3 deep must be false
                    false
                ]
            ]

        The above structure would allow Architecture, Architectural Engineering, all of Architectural Engineering's children, Engineering, Aerospace Engineering, and Aerodynamics and Fluid Mechanics.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreprintProviderDetailResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderDetailResponse,
                    parse_obj_as(
                        type_=PreprintProviderDetailResponse,
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

    async def preprint_provider_licenses_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreprintProviderLicensesListResponse]:
        """

        A paginated list of the licenses allowed by a preprint provider.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreprintProviderLicensesListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/licenses/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderLicensesListResponse,
                    parse_obj_as(
                        type_=PreprintProviderLicensesListResponse,
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

    async def preprints_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PreprintProvidersPreprintsListResponseItem]]:
        """

        A paginated list of preprints from the specified preprint provider. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary with keys that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/osf/preprints/?filter[is_published]=true.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PreprintProvidersPreprintsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/preprints/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PreprintProvidersPreprintsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[PreprintProvidersPreprintsListResponseItem],
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

    async def preprint_provider_taxonomies_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreprintProviderTaxonomiesListResponse]:
        """

        A paginated list of the taxonomies for a preprint provider. The returned preprint providers taxonomies are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreprintProviderTaxonomiesListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"preprint_providers/{encode_path_param(preprint_provider_id)}/taxonomies/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreprintProviderTaxonomiesListResponse,
                    parse_obj_as(
                        type_=PreprintProviderTaxonomiesListResponse,
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
