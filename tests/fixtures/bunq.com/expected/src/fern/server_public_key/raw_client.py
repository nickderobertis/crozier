

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.installation_server_public_key_listing import InstallationServerPublicKeyListing


class RawServerPublicKeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_server_public_key_for_installation(
        self, installation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[InstallationServerPublicKeyListing]]:
        """
        Show the ServerPublicKey for this Installation.

        Parameters
        ----------
        installation_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[InstallationServerPublicKeyListing]]
            Using /installation/_/server-public-key you can request the ServerPublicKey again. This is done by referring to the id of the Installation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"installation/{jsonable_encoder(installation_id)}/server-public-key",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InstallationServerPublicKeyListing],
                    parse_obj_as(
                        type_=typing.List[InstallationServerPublicKeyListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawServerPublicKeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_server_public_key_for_installation(
        self, installation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[InstallationServerPublicKeyListing]]:
        """
        Show the ServerPublicKey for this Installation.

        Parameters
        ----------
        installation_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[InstallationServerPublicKeyListing]]
            Using /installation/_/server-public-key you can request the ServerPublicKey again. This is done by referring to the id of the Installation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"installation/{jsonable_encoder(installation_id)}/server-public-key",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InstallationServerPublicKeyListing],
                    parse_obj_as(
                        type_=typing.List[InstallationServerPublicKeyListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
