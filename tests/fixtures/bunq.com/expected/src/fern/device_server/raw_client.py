

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.device_server_create import DeviceServerCreate
from ..types.device_server_listing import DeviceServerListing
from ..types.device_server_read import DeviceServerRead
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDeviceServerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_device_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[DeviceServerListing]]:
        """
        Get a collection of all the DeviceServers you have created.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[DeviceServerListing]]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.
        """
        _response = self._client_wrapper.httpx_client.request(
            "device-server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DeviceServerListing],
                    parse_obj_as(
                        type_=typing.List[DeviceServerListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_device_server(
        self,
        *,
        description: str,
        secret: str,
        permitted_ips: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeviceServerCreate]:
        """
        Create a new DeviceServer providing the installation token in the header and signing the request with the private part of the key you used to create the installation. The API Key that you are using will be bound to the IP address of the DeviceServer which you have created.<br/><br/>Using a Wildcard API Key gives you the freedom to make API calls even if the IP address has changed after the POST device-server.<br/><br/>Find out more at this link <a href="https:/bunq.com/en/apikey-dynamic-ip" target="_blank">https:/bunq.com/en/apikey-dynamic-ip</a>.

        Parameters
        ----------
        description : str
            The description of the DeviceServer. This is only for your own reference when reading the DeviceServer again.

        secret : str
            The API key. You can request an API key in the bunq app.

        permitted_ips : typing.Optional[typing.Sequence[str]]
            An array of IPs (v4 or v6) this DeviceServer will be able to do calls from. These will be linked to the API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeviceServerCreate]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.
        """
        _response = self._client_wrapper.httpx_client.request(
            "device-server",
            method="POST",
            json={
                "description": description,
                "permitted_ips": permitted_ips,
                "secret": secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceServerCreate,
                    parse_obj_as(
                        type_=DeviceServerCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_device_server(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeviceServerRead]:
        """
        Get one of your DeviceServers.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeviceServerRead]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"device-server/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceServerRead,
                    parse_obj_as(
                        type_=DeviceServerRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDeviceServerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_device_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[DeviceServerListing]]:
        """
        Get a collection of all the DeviceServers you have created.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[DeviceServerListing]]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "device-server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DeviceServerListing],
                    parse_obj_as(
                        type_=typing.List[DeviceServerListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_device_server(
        self,
        *,
        description: str,
        secret: str,
        permitted_ips: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeviceServerCreate]:
        """
        Create a new DeviceServer providing the installation token in the header and signing the request with the private part of the key you used to create the installation. The API Key that you are using will be bound to the IP address of the DeviceServer which you have created.<br/><br/>Using a Wildcard API Key gives you the freedom to make API calls even if the IP address has changed after the POST device-server.<br/><br/>Find out more at this link <a href="https:/bunq.com/en/apikey-dynamic-ip" target="_blank">https:/bunq.com/en/apikey-dynamic-ip</a>.

        Parameters
        ----------
        description : str
            The description of the DeviceServer. This is only for your own reference when reading the DeviceServer again.

        secret : str
            The API key. You can request an API key in the bunq app.

        permitted_ips : typing.Optional[typing.Sequence[str]]
            An array of IPs (v4 or v6) this DeviceServer will be able to do calls from. These will be linked to the API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeviceServerCreate]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "device-server",
            method="POST",
            json={
                "description": description,
                "permitted_ips": permitted_ips,
                "secret": secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceServerCreate,
                    parse_obj_as(
                        type_=DeviceServerCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_device_server(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeviceServerRead]:
        """
        Get one of your DeviceServers.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeviceServerRead]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"device-server/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceServerRead,
                    parse_obj_as(
                        type_=DeviceServerRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
