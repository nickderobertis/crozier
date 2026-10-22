

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.gateway_timeout_error import GatewayTimeoutError
from ..types.data_set import DataSet
from .types.get_datasets_dataset_name_details_item_id_response import GetDatasetsDatasetNameDetailsItemIdResponse
from .types.post_datasets_dataset_name_search_response import PostDatasetsDatasetNameSearchResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_available_data_sets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[DataSet]]:
        """
        Get the available data sets.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[DataSet]]
            Available data sets results
        """
        _response = self._client_wrapper.httpx_client.request(
            "datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DataSet],
                    parse_obj_as(
                        type_=typing.List[DataSet],
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

    def search_dataset(
        self,
        dataset_name: str,
        *,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[str] = OMIT,
        facets: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostDatasetsDatasetNameSearchResponse]:
        """
        Search in the index of the dataset.

        Parameters
        ----------
        dataset_name : str

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        query : typing.Optional[str]

        facets : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostDatasetsDatasetNameSearchResponse]
            Search results
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/search",
            method="POST",
            json={
                "offset": offset,
                "limit": limit,
                "query": query,
                "facets": facets,
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
                    PostDatasetsDatasetNameSearchResponse,
                    parse_obj_as(
                        type_=PostDatasetsDatasetNameSearchResponse,
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

    def get_item_details(
        self, dataset_name: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDatasetsDatasetNameDetailsItemIdResponse]:
        """
        Get the details for a specific item in the dataset.

        Parameters
        ----------
        dataset_name : str

        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDatasetsDatasetNameDetailsItemIdResponse]
            Item details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/details/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDatasetsDatasetNameDetailsItemIdResponse,
                    parse_obj_as(
                        type_=GetDatasetsDatasetNameDetailsItemIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
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


class AsyncRawDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_available_data_sets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[DataSet]]:
        """
        Get the available data sets.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[DataSet]]
            Available data sets results
        """
        _response = await self._client_wrapper.httpx_client.request(
            "datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DataSet],
                    parse_obj_as(
                        type_=typing.List[DataSet],
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

    async def search_dataset(
        self,
        dataset_name: str,
        *,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[str] = OMIT,
        facets: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostDatasetsDatasetNameSearchResponse]:
        """
        Search in the index of the dataset.

        Parameters
        ----------
        dataset_name : str

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        query : typing.Optional[str]

        facets : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostDatasetsDatasetNameSearchResponse]
            Search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/search",
            method="POST",
            json={
                "offset": offset,
                "limit": limit,
                "query": query,
                "facets": facets,
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
                    PostDatasetsDatasetNameSearchResponse,
                    parse_obj_as(
                        type_=PostDatasetsDatasetNameSearchResponse,
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

    async def get_item_details(
        self, dataset_name: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDatasetsDatasetNameDetailsItemIdResponse]:
        """
        Get the details for a specific item in the dataset.

        Parameters
        ----------
        dataset_name : str

        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDatasetsDatasetNameDetailsItemIdResponse]
            Item details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset_name)}/details/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDatasetsDatasetNameDetailsItemIdResponse,
                    parse_obj_as(
                        type_=GetDatasetsDatasetNameDetailsItemIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
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
