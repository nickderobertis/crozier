

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.spell import Spell


class RawSpellsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_list_of_spells_with_optional_filtering(
        self,
        *,
        level: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        school: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        level : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            The level or levels to filter on.

        school : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The magic school or schools to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/spells",
            method="GET",
            params={
                "level": level,
                "school": school,
            },
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

    def get_a_spell_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Spell]:
        """
        Parameters
        ----------
        index : str
            The `index` of the `Spell` to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `spells`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Spell]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/spells/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Spell,
                    parse_obj_as(
                        type_=Spell,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSpellsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_list_of_spells_with_optional_filtering(
        self,
        *,
        level: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        school: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Parameters
        ----------
        level : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            The level or levels to filter on.

        school : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The magic school or schools to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/spells",
            method="GET",
            params={
                "level": level,
                "school": school,
            },
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

    async def get_a_spell_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Spell]:
        """
        Parameters
        ----------
        index : str
            The `index` of the `Spell` to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `spells`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Spell]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/spells/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Spell,
                    parse_obj_as(
                        type_=Spell,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
