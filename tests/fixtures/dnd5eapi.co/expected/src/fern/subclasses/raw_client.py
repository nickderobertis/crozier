

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.subclass import Subclass
from ..types.subclass_level import SubclassLevel
from ..types.subclass_level_resource import SubclassLevelResource
from .types.get_api_subclasses_index_features_request_index import GetApiSubclassesIndexFeaturesRequestIndex
from .types.get_api_subclasses_index_levels_request_index import GetApiSubclassesIndexLevelsRequestIndex
from .types.get_api_subclasses_index_levels_subclass_level_features_request_index import (
    GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
)
from .types.get_api_subclasses_index_levels_subclass_level_request_index import (
    GetApiSubclassesIndexLevelsSubclassLevelRequestIndex,
)
from .types.get_api_subclasses_index_request_index import GetApiSubclassesIndexRequestIndex


class RawSubclassesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_subclass_by_index(
        self, index: GetApiSubclassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Subclass]:
        """
        Subclasses reflect the different paths a class may take as levels are gained.

        Parameters
        ----------
        index : GetApiSubclassesIndexRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Subclass]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Subclass,
                    parse_obj_as(
                        type_=Subclass,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_features_available_for_a_subclass(
        self,
        index: GetApiSubclassesIndexFeaturesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexFeaturesRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            List of features for the subclass.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/features",
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

    def get_all_level_resources_for_a_subclass(
        self, index: GetApiSubclassesIndexLevelsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[SubclassLevelResource]]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SubclassLevelResource]]
            List of level resource for the subclass.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/levels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SubclassLevelResource],
                    parse_obj_as(
                        type_=typing.List[SubclassLevelResource],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_level_resources_for_a_subclass_and_level(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubclassLevel]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubclassLevel]
            Level resource for the subclass and level.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/levels/{jsonable_encoder(subclass_level)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubclassLevel,
                    parse_obj_as(
                        type_=SubclassLevel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_features_of_the_requested_spell_level_available_to_the_class(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            List of features for the subclass and level.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/levels/{jsonable_encoder(subclass_level)}/features",
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


class AsyncRawSubclassesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_subclass_by_index(
        self, index: GetApiSubclassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Subclass]:
        """
        Subclasses reflect the different paths a class may take as levels are gained.

        Parameters
        ----------
        index : GetApiSubclassesIndexRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Subclass]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Subclass,
                    parse_obj_as(
                        type_=Subclass,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_features_available_for_a_subclass(
        self,
        index: GetApiSubclassesIndexFeaturesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexFeaturesRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            List of features for the subclass.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/features",
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

    async def get_all_level_resources_for_a_subclass(
        self, index: GetApiSubclassesIndexLevelsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[SubclassLevelResource]]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SubclassLevelResource]]
            List of level resource for the subclass.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/levels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SubclassLevelResource],
                    parse_obj_as(
                        type_=typing.List[SubclassLevelResource],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_level_resources_for_a_subclass_and_level(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubclassLevel]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubclassLevel]
            Level resource for the subclass and level.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/levels/{jsonable_encoder(subclass_level)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubclassLevel,
                    parse_obj_as(
                        type_=SubclassLevel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_features_of_the_requested_spell_level_available_to_the_class(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            List of features for the subclass and level.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/subclasses/{jsonable_encoder(index)}/levels/{jsonable_encoder(subclass_level)}/features",
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
