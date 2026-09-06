

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_models_authenticated_user import ApiModelsAuthenticatedUser
from .types.api_models_credentials_bearer_action import ApiModelsCredentialsBearerAction
from .types.api_models_credentials_mac_action import ApiModelsCredentialsMacAction
from .types.api_models_token_options_bearer_action import ApiModelsTokenOptionsBearerAction
from .types.api_models_token_options_mac_action import ApiModelsTokenOptionsMacAction
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def putmanagetokens(
        self,
        user_id: int,
        *,
        bearer_action: typing.Optional[ApiModelsTokenOptionsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsTokenOptionsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        user_id : int

        bearer_action : typing.Optional[ApiModelsTokenOptionsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsTokenOptionsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthenticatedUsers/{encode_path_param(user_id)}/Tokens",
            method="PUT",
            json={
                "BearerAction": bearer_action,
                "MACAction": mac_action,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def default(
        self,
        *,
        password: str,
        username: str,
        bearer_action: typing.Optional[ApiModelsCredentialsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsCredentialsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiModelsAuthenticatedUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        password : str
            A secret word or phrase that must be used to gain admission

        username : str
            A unique ID a user needs to login with

        bearer_action : typing.Optional[ApiModelsCredentialsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsCredentialsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiModelsAuthenticatedUser]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Authentication",
            method="POST",
            json={
                "BearerAction": bearer_action,
                "MACAction": mac_action,
                "password": password,
                "username": username,
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
                    ApiModelsAuthenticatedUser,
                    parse_obj_as(
                        type_=ApiModelsAuthenticatedUser,
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

    def isalive(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Authentication/IsAlive",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def requestpasswordreset(
        self, *, parameter_name: str, url: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        parameter_name : str
            The query string parameter name to use for supplying the password reset token

        url : str
            The URL to direct the user to reset the password.

        username : str
            The username to reset the password for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Authentication/RequestPasswordReset",
            method="POST",
            json={
                "ParameterName": parameter_name,
                "Url": url,
                "Username": username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def resetpasword(
        self, *, new_password: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        new_password : str
            The new password

        token : str
            The password reset token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Authentication/ResetPasword",
            method="POST",
            json={
                "NewPassword": new_password,
                "Token": token,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def putmanagetokens(
        self,
        user_id: int,
        *,
        bearer_action: typing.Optional[ApiModelsTokenOptionsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsTokenOptionsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        user_id : int

        bearer_action : typing.Optional[ApiModelsTokenOptionsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsTokenOptionsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthenticatedUsers/{encode_path_param(user_id)}/Tokens",
            method="PUT",
            json={
                "BearerAction": bearer_action,
                "MACAction": mac_action,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def default(
        self,
        *,
        password: str,
        username: str,
        bearer_action: typing.Optional[ApiModelsCredentialsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsCredentialsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiModelsAuthenticatedUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        password : str
            A secret word or phrase that must be used to gain admission

        username : str
            A unique ID a user needs to login with

        bearer_action : typing.Optional[ApiModelsCredentialsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsCredentialsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiModelsAuthenticatedUser]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Authentication",
            method="POST",
            json={
                "BearerAction": bearer_action,
                "MACAction": mac_action,
                "password": password,
                "username": username,
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
                    ApiModelsAuthenticatedUser,
                    parse_obj_as(
                        type_=ApiModelsAuthenticatedUser,
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

    async def isalive(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Authentication/IsAlive",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def requestpasswordreset(
        self, *, parameter_name: str, url: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        parameter_name : str
            The query string parameter name to use for supplying the password reset token

        url : str
            The URL to direct the user to reset the password.

        username : str
            The username to reset the password for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Authentication/RequestPasswordReset",
            method="POST",
            json={
                "ParameterName": parameter_name,
                "Url": url,
                "Username": username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def resetpasword(
        self, *, new_password: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        new_password : str
            The new password

        token : str
            The password reset token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Authentication/ResetPasword",
            method="POST",
            json={
                "NewPassword": new_password,
                "Token": token,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
