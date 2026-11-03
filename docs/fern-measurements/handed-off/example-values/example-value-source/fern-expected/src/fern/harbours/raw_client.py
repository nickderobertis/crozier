

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_berth_response import GetBerthResponse
from pydantic import ValidationError


class RawHarboursClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_berth(
        self, harbour_slug: str, berth_ref: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBerthResponse]:
        """
        Path parameters beside one declaring an empty schema.

        Parameters
        ----------
        harbour_slug : str

        berth_ref : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBerthResponse]
            The berth
        """
        _response = self._client_wrapper.httpx_client.request(
            f"harbours/{encode_path_param(harbour_slug)}/berths/{encode_path_param(berth_ref)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBerthResponse,
                    parse_obj_as(
                        type_=GetBerthResponse,
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


class AsyncRawHarboursClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_berth(
        self, harbour_slug: str, berth_ref: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBerthResponse]:
        """
        Path parameters beside one declaring an empty schema.

        Parameters
        ----------
        harbour_slug : str

        berth_ref : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBerthResponse]
            The berth
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"harbours/{encode_path_param(harbour_slug)}/berths/{encode_path_param(berth_ref)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBerthResponse,
                    parse_obj_as(
                        type_=GetBerthResponse,
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
