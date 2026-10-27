

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.beacon import Beacon
from pydantic import ValidationError


class RawBeaconsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_beacon(
        self, beacon_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Beacon]:
        """
        Returns the beacon's lamp and its schedule. The lamp is lit at dusk.
        A beacon that was retired answers 404.

        Parameters
        ----------
        beacon_id : str
            The beacon's identifier, as #registered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Beacon]
            The beacon
        """
        _response = self._client_wrapper.httpx_client.request(
            f"beacons/{encode_path_param(beacon_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Beacon,
                    parse_obj_as(
                        type_=Beacon,
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


class AsyncRawBeaconsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_beacon(
        self, beacon_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Beacon]:
        """
        Returns the beacon's lamp and its schedule. The lamp is lit at dusk.
        A beacon that was retired answers 404.

        Parameters
        ----------
        beacon_id : str
            The beacon's identifier, as #registered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Beacon]
            The beacon
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"beacons/{encode_path_param(beacon_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Beacon,
                    parse_obj_as(
                        type_=Beacon,
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
