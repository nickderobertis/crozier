

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.totp_auth_link_response import TotpAuthLinkResponse
from ..types.two_factor_auth_settings import TwoFactorAuthSettings
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTwoFactorAuthV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_two_factor_authentication_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TwoFactorAuthSettings]:
        """
        Get Two-factor authentication settings.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    def disable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TwoFactorAuthSettings]:
        """
        Disable Two-factor authentication

        Parameters
        ----------
        password : str
            Current password of the authenticated user.

        totp_code : typing.Optional[str]
            Current TOTP code, required when TOTP has already been configured.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/settings/disabled",
            method="PUT",
            json={
                "password": password,
                "totpCode": totp_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    def enable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TwoFactorAuthSettings]:
        """
        Enable Two-factor authentication

        Parameters
        ----------
        password : str
            Current password of the authenticated user.

        totp_code : typing.Optional[str]
            Current TOTP code, required when TOTP has already been configured.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/settings/enabled",
            method="PUT",
            json={
                "password": password,
                "totpCode": totp_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    def configurer_totp(
        self,
        *,
        code: str,
        password: str,
        secret: str,
        current_totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TwoFactorAuthSettings]:
        """
        Configure a TOTP

        Parameters
        ----------
        code : str
            TOTP code generated from the new secret.

        password : str
            Current password of the authenticated user.

        secret : str
            Raw TOTP secret returned by the auth-link endpoint.

        current_totp_code : typing.Optional[str]
            Current TOTP code, required when replacing an existing TOTP authenticator.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/totp",
            method="POST",
            json={
                "code": code,
                "currentTotpCode": current_totp_code,
                "password": password,
                "secret": secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    def delete_totp(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TwoFactorAuthSettings]:
        """
        Delete the current user's configured TOTP authenticator after password verification.

        Parameters
        ----------
        password : str
            Current password of the authenticated user.

        totp_code : typing.Optional[str]
            Current TOTP code, required when TOTP has already been configured.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/totp/-",
            method="DELETE",
            json={
                "password": password,
                "totpCode": totp_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    def get_totp_auth_link(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TotpAuthLinkResponse]:
        """
        Get TOTP auth link, including secret

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TotpAuthLinkResponse]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/totp/auth-link",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TotpAuthLinkResponse,
                    parse_obj_as(
                        type_=TotpAuthLinkResponse,
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


class AsyncRawTwoFactorAuthV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_two_factor_authentication_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TwoFactorAuthSettings]:
        """
        Get Two-factor authentication settings.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    async def disable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TwoFactorAuthSettings]:
        """
        Disable Two-factor authentication

        Parameters
        ----------
        password : str
            Current password of the authenticated user.

        totp_code : typing.Optional[str]
            Current TOTP code, required when TOTP has already been configured.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/settings/disabled",
            method="PUT",
            json={
                "password": password,
                "totpCode": totp_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    async def enable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TwoFactorAuthSettings]:
        """
        Enable Two-factor authentication

        Parameters
        ----------
        password : str
            Current password of the authenticated user.

        totp_code : typing.Optional[str]
            Current TOTP code, required when TOTP has already been configured.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/settings/enabled",
            method="PUT",
            json={
                "password": password,
                "totpCode": totp_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    async def configurer_totp(
        self,
        *,
        code: str,
        password: str,
        secret: str,
        current_totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TwoFactorAuthSettings]:
        """
        Configure a TOTP

        Parameters
        ----------
        code : str
            TOTP code generated from the new secret.

        password : str
            Current password of the authenticated user.

        secret : str
            Raw TOTP secret returned by the auth-link endpoint.

        current_totp_code : typing.Optional[str]
            Current TOTP code, required when replacing an existing TOTP authenticator.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/totp",
            method="POST",
            json={
                "code": code,
                "currentTotpCode": current_totp_code,
                "password": password,
                "secret": secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    async def delete_totp(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TwoFactorAuthSettings]:
        """
        Delete the current user's configured TOTP authenticator after password verification.

        Parameters
        ----------
        password : str
            Current password of the authenticated user.

        totp_code : typing.Optional[str]
            Current TOTP code, required when TOTP has already been configured.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TwoFactorAuthSettings]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/totp/-",
            method="DELETE",
            json={
                "password": password,
                "totpCode": totp_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TwoFactorAuthSettings,
                    parse_obj_as(
                        type_=TwoFactorAuthSettings,
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

    async def get_totp_auth_link(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TotpAuthLinkResponse]:
        """
        Get TOTP auth link, including secret

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TotpAuthLinkResponse]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.security.halo.run/v1alpha1/authentications/two-factor/totp/auth-link",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TotpAuthLinkResponse,
                    parse_obj_as(
                        type_=TotpAuthLinkResponse,
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
