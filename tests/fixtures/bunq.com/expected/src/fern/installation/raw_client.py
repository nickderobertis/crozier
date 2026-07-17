

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
from ..types.installation_create import InstallationCreate
from ..types.installation_listing import InstallationListing
from ..types.installation_read import InstallationRead
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInstallationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_installation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[InstallationListing]]:
        """
        You must have an active session to make this call. This call returns the Id of the the Installation you are using in your session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[InstallationListing]]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.
        """
        _response = self._client_wrapper.httpx_client.request(
            "installation",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InstallationListing],
                    parse_obj_as(
                        type_=typing.List[InstallationListing],
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

    def create_installation(
        self, *, client_public_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InstallationCreate]:
        """
        This is the only API call that does not require you to use the "X-Bunq-Client-Authentication" and "X-Bunq-Client-Signature" headers.
         You provide the server with the public part of the key pair that you are going to use to create the value of the signature header for all future API calls. The server creates an installation for you. Store the Installation Token and ServerPublicKey from the response. This token is used in the "X-Bunq-Client-Authentication" header for the creation of a DeviceServer and SessionServer.

        Parameters
        ----------
        client_public_key : str
            Your public key. This is the public part of the key pair that you are going to use to create value of the "X-Bunq-Client-Signature" header for all future API calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InstallationCreate]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.
        """
        _response = self._client_wrapper.httpx_client.request(
            "installation",
            method="POST",
            json={
                "client_public_key": client_public_key,
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
                    InstallationCreate,
                    parse_obj_as(
                        type_=InstallationCreate,
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

    def read_installation(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InstallationRead]:
        """
        You must have an active session to make this call. This call is used to check whether the Id you provide is the Id of your current installation or not.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InstallationRead]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"installation/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InstallationRead,
                    parse_obj_as(
                        type_=InstallationRead,
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


class AsyncRawInstallationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_installation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[InstallationListing]]:
        """
        You must have an active session to make this call. This call returns the Id of the the Installation you are using in your session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[InstallationListing]]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "installation",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InstallationListing],
                    parse_obj_as(
                        type_=typing.List[InstallationListing],
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

    async def create_installation(
        self, *, client_public_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InstallationCreate]:
        """
        This is the only API call that does not require you to use the "X-Bunq-Client-Authentication" and "X-Bunq-Client-Signature" headers.
         You provide the server with the public part of the key pair that you are going to use to create the value of the signature header for all future API calls. The server creates an installation for you. Store the Installation Token and ServerPublicKey from the response. This token is used in the "X-Bunq-Client-Authentication" header for the creation of a DeviceServer and SessionServer.

        Parameters
        ----------
        client_public_key : str
            Your public key. This is the public part of the key pair that you are going to use to create value of the "X-Bunq-Client-Signature" header for all future API calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InstallationCreate]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "installation",
            method="POST",
            json={
                "client_public_key": client_public_key,
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
                    InstallationCreate,
                    parse_obj_as(
                        type_=InstallationCreate,
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

    async def read_installation(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InstallationRead]:
        """
        You must have an active session to make this call. This call is used to check whether the Id you provide is the Id of your current installation or not.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InstallationRead]
            Installation is used to tell the server about the public key of your key pair. The server uses this key to verify your subsequent calls, which need to be signed with your own private key. Additionally, you can use the token you get from an Installation to authenticate the registration of a new device.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"installation/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InstallationRead,
                    parse_obj_as(
                        type_=InstallationRead,
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
