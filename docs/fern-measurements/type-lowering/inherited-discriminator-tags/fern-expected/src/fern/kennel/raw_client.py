

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.pet import Pet
from .types.list_tasks_response_item import ListTasksResponseItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawKennelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_pet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        species: typing.Optional[str] = OMIT,
        breed: typing.Optional[str] = OMIT,
        size: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pet]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        age : typing.Optional[int]

        species : typing.Optional[str]

        breed : typing.Optional[str]

        size : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pet]
            Added.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pets",
            method="POST",
            json={
                "name": name,
                "age": age,
                "species": species,
                "breed": breed,
                "size": size,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pet,
                    parse_obj_as(
                        type_=Pet,
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

    def list_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ListTasksResponseItem]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListTasksResponseItem]]
            The tasks.
        """
        _response = self._client_wrapper.httpx_client.request(
            "tasks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListTasksResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListTasksResponseItem],
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


class AsyncRawKennelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_pet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        species: typing.Optional[str] = OMIT,
        breed: typing.Optional[str] = OMIT,
        size: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pet]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        age : typing.Optional[int]

        species : typing.Optional[str]

        breed : typing.Optional[str]

        size : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pet]
            Added.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pets",
            method="POST",
            json={
                "name": name,
                "age": age,
                "species": species,
                "breed": breed,
                "size": size,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pet,
                    parse_obj_as(
                        type_=Pet,
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

    async def list_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ListTasksResponseItem]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListTasksResponseItem]]
            The tasks.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tasks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListTasksResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListTasksResponseItem],
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
