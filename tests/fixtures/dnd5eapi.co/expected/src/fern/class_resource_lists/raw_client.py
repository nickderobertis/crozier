

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from .types.get_api_classes_index_features_request_index import GetApiClassesIndexFeaturesRequestIndex
from .types.get_api_classes_index_proficiencies_request_index import GetApiClassesIndexProficienciesRequestIndex
from .types.get_api_classes_index_spells_request_index import GetApiClassesIndexSpellsRequestIndex
from .types.get_api_classes_index_subclasses_request_index import GetApiClassesIndexSubclassesRequestIndex
from pydantic import ValidationError


class RawClassResourceListsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_features_available_for_a_class(
        self, index: GetApiClassesIndexFeaturesRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexFeaturesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            List of features for the class.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/features",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_proficiencies_available_for_a_class(
        self,
        index: GetApiClassesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexProficienciesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            List of proficiencies for the class.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/proficiencies",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_spells_available_for_a_class(
        self, index: GetApiClassesIndexSpellsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellsRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/spells",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_subclasses_available_for_a_class(
        self,
        index: GetApiClassesIndexSubclassesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSubclassesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/subclasses",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawClassResourceListsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_features_available_for_a_class(
        self, index: GetApiClassesIndexFeaturesRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexFeaturesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            List of features for the class.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/features",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_proficiencies_available_for_a_class(
        self,
        index: GetApiClassesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexProficienciesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            List of proficiencies for the class.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/proficiencies",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_spells_available_for_a_class(
        self, index: GetApiClassesIndexSpellsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellsRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/spells",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_subclasses_available_for_a_class(
        self,
        index: GetApiClassesIndexSubclassesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSubclassesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/subclasses",
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
