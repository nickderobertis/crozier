

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.subrace import Subrace
from .types.get_api_subraces_index_proficiencies_request_index import GetApiSubracesIndexProficienciesRequestIndex
from .types.get_api_subraces_index_request_index import GetApiSubracesIndexRequestIndex
from .types.get_api_subraces_index_traits_request_index import GetApiSubracesIndexTraitsRequestIndex


class RawSubracesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_subrace_by_index(
        self, index: GetApiSubracesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Subrace]:
        """
        Subraces reflect the different varieties of a certain parent race.

        Parameters
        ----------
        index : GetApiSubracesIndexRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Subrace]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subraces/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Subrace,
                    parse_obj_as(
                        type_=Subrace,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_proficiences_available_for_a_subrace(
        self,
        index: GetApiSubracesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexProficienciesRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            List of proficiences for the subrace.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subraces/{jsonable_encoder(index)}/proficiencies",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_traits_available_for_a_subrace(
        self, index: GetApiSubracesIndexTraitsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexTraitsRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            List of traits for the subrace.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subraces/{jsonable_encoder(index)}/traits",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSubracesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_subrace_by_index(
        self, index: GetApiSubracesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Subrace]:
        """
        Subraces reflect the different varieties of a certain parent race.

        Parameters
        ----------
        index : GetApiSubracesIndexRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Subrace]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subraces/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Subrace,
                    parse_obj_as(
                        type_=Subrace,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_proficiences_available_for_a_subrace(
        self,
        index: GetApiSubracesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexProficienciesRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            List of proficiences for the subrace.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subraces/{jsonable_encoder(index)}/proficiencies",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_traits_available_for_a_subrace(
        self, index: GetApiSubracesIndexTraitsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexTraitsRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            List of traits for the subrace.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subraces/{jsonable_encoder(index)}/traits",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
