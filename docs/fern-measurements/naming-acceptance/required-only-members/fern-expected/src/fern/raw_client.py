

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.shelf import Shelf
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_packet(
        self,
        *,
        name: str,
        label: typing.Optional[str] = OMIT,
        bin_id: typing.Optional[str] = OMIT,
        grower: typing.Optional[str] = OMIT,
        vault_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Shelf]:
        """
        Parameters
        ----------
        name : str

        label : typing.Optional[str]

        bin_id : typing.Optional[str]

        grower : typing.Optional[str]

        vault_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Shelf]
            The packet
        """
        _response = self._client_wrapper.httpx_client.request(
            "packets",
            method="POST",
            json={
                "label": label,
                "name": name,
                "binId": bin_id,
                "grower": grower,
                "vaultId": vault_id,
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
                    Shelf,
                    parse_obj_as(
                        type_=Shelf,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_packet(
        self,
        *,
        name: str,
        label: typing.Optional[str] = OMIT,
        bin_id: typing.Optional[str] = OMIT,
        grower: typing.Optional[str] = OMIT,
        vault_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Shelf]:
        """
        Parameters
        ----------
        name : str

        label : typing.Optional[str]

        bin_id : typing.Optional[str]

        grower : typing.Optional[str]

        vault_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Shelf]
            The packet
        """
        _response = await self._client_wrapper.httpx_client.request(
            "packets",
            method="POST",
            json={
                "label": label,
                "name": name,
                "binId": bin_id,
                "grower": grower,
                "vaultId": vault_id,
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
                    Shelf,
                    parse_obj_as(
                        type_=Shelf,
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
