

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.facet_result import FacetResult
from .types.get_datasets_dataset_name_facets_response_item import GetDatasetsDatasetNameFacetsResponseItem
from .types.post_datasets_dataset_name_facet_request_facets_value import PostDatasetsDatasetNameFacetRequestFacetsValue
from .types.post_datasets_dataset_name_facet_request_sort import PostDatasetsDatasetNameFacetRequestSort
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFacetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_facets(
        self, dataset_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetDatasetsDatasetNameFacetsResponseItem]]:
        """
        Get the facets used in this dataset.

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetDatasetsDatasetNameFacetsResponseItem]]
            Facets
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/facets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetDatasetsDatasetNameFacetsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetDatasetsDatasetNameFacetsResponseItem],
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

    def get_facet_options(
        self,
        dataset_name: str,
        *,
        name: typing.Optional[str] = OMIT,
        amount: typing.Optional[int] = OMIT,
        filter: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        sort: typing.Optional[PostDatasetsDatasetNameFacetRequestSort] = OMIT,
        facets: typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FacetResult]]:
        """
        Get the available options for a specific facet.

        Parameters
        ----------
        dataset_name : str

        name : typing.Optional[str]
            The Facet for which to get options

        amount : typing.Optional[int]
            How many results to retrieve

        filter : typing.Optional[str]
            String to filter results on. For searching in the list of facet options.

        query : typing.Optional[str]
            Text query used for filtering search results (not facet options). Used to make sure the counts reflect the actual search results.

        sort : typing.Optional[PostDatasetsDatasetNameFacetRequestSort]

        facets : typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FacetResult]]
            Facet results
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/facet",
            method="POST",
            json={
                "name": name,
                "amount": amount,
                "filter": filter,
                "query": query,
                "sort": sort,
                "facets": convert_and_respect_annotation_metadata(
                    object_=facets,
                    annotation=typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue],
                    direction="write",
                ),
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
                    typing.List[FacetResult],
                    parse_obj_as(
                        type_=typing.List[FacetResult],
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


class AsyncRawFacetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_facets(
        self, dataset_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetDatasetsDatasetNameFacetsResponseItem]]:
        """
        Get the facets used in this dataset.

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetDatasetsDatasetNameFacetsResponseItem]]
            Facets
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/facets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetDatasetsDatasetNameFacetsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetDatasetsDatasetNameFacetsResponseItem],
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

    async def get_facet_options(
        self,
        dataset_name: str,
        *,
        name: typing.Optional[str] = OMIT,
        amount: typing.Optional[int] = OMIT,
        filter: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        sort: typing.Optional[PostDatasetsDatasetNameFacetRequestSort] = OMIT,
        facets: typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FacetResult]]:
        """
        Get the available options for a specific facet.

        Parameters
        ----------
        dataset_name : str

        name : typing.Optional[str]
            The Facet for which to get options

        amount : typing.Optional[int]
            How many results to retrieve

        filter : typing.Optional[str]
            String to filter results on. For searching in the list of facet options.

        query : typing.Optional[str]
            Text query used for filtering search results (not facet options). Used to make sure the counts reflect the actual search results.

        sort : typing.Optional[PostDatasetsDatasetNameFacetRequestSort]

        facets : typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FacetResult]]
            Facet results
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/facet",
            method="POST",
            json={
                "name": name,
                "amount": amount,
                "filter": filter,
                "query": query,
                "sort": sort,
                "facets": convert_and_respect_annotation_metadata(
                    object_=facets,
                    annotation=typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue],
                    direction="write",
                ),
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
                    typing.List[FacetResult],
                    parse_obj_as(
                        type_=typing.List[FacetResult],
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
