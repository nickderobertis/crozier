

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_ecosystem_response import GetEcosystemResponse


class RawEcosystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ecosystems_one(
        self, ecosystem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEcosystemResponse]:
        """
        Get ecosystem

        Parameters
        ----------
        ecosystem_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEcosystemResponse]
            Ecosystems
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ecosystems/{jsonable_encoder(ecosystem_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEcosystemResponse,
                    parse_obj_as(
                        type_=GetEcosystemResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEcosystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ecosystems_one(
        self, ecosystem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEcosystemResponse]:
        """
        Get ecosystem

        Parameters
        ----------
        ecosystem_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEcosystemResponse]
            Ecosystems
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ecosystems/{jsonable_encoder(ecosystem_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEcosystemResponse,
                    parse_obj_as(
                        type_=GetEcosystemResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
