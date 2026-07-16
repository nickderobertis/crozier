

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.obtain_token_response import ObtainTokenResponse
from ..types.renew_token_response import RenewTokenResponse
from ..types.revoke_token_response import RevokeTokenResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def renew_token(
        self,
        client_id: str,
        *,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RenewTokenResponse]:
        """
        `RenewToken` is deprecated. For information about refreshing OAuth access tokens, see
        [Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).


        Renews an OAuth access token before it expires.

        OAuth access tokens besides your application's personal access token expire after __30 days__.
        You can also renew expired tokens within __15 days__ of their expiration.
        You cannot renew an access token that has been expired for more than 15 days.
        Instead, the associated user must re-complete the OAuth flow from the beginning.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the Credentials
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        client_id : str
            Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).

        access_token : typing.Optional[str]
            The token you want to renew.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RenewTokenResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth2/clients/{encode_path_param(client_id)}/access-token/renew",
            method="POST",
            json={
                "access_token": access_token,
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
                    RenewTokenResponse,
                    parse_obj_as(
                        type_=RenewTokenResponse,
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

    def revoke_token(
        self,
        *,
        access_token: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        merchant_id: typing.Optional[str] = OMIT,
        revoke_only_access_token: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RevokeTokenResponse]:
        """
        Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this
        endpoint revokes all of them, regardless of which token you specify. When an
        OAuth access token is revoked, all of the active subscriptions associated
        with that OAuth token are canceled immediately.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the OAuth
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        access_token : typing.Optional[str]
            The access token of the merchant whose token you want to revoke.
            Do not provide a value for merchant_id if you provide this parameter.

        client_id : typing.Optional[str]
            The Square issued ID for your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        merchant_id : typing.Optional[str]
            The ID of the merchant whose token you want to revoke.
            Do not provide a value for access_token if you provide this parameter.

        revoke_only_access_token : typing.Optional[bool]
            If `true`, terminate the given single access token, but do not
            terminate the entire authorization.
            Default: `false`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RevokeTokenResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth2/revoke",
            method="POST",
            json={
                "access_token": access_token,
                "client_id": client_id,
                "merchant_id": merchant_id,
                "revoke_only_access_token": revoke_only_access_token,
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
                    RevokeTokenResponse,
                    parse_obj_as(
                        type_=RevokeTokenResponse,
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

    def obtain_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: str,
        code: typing.Optional[str] = OMIT,
        migration_token: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        short_lived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObtainTokenResponse]:
        """
        Returns an OAuth access token.

        The endpoint supports distinct methods of obtaining OAuth access tokens.
        Applications specify a method by adding the `grant_type` parameter
        in the request and also provide relevant information.

        __Note:__ Regardless of the method application specified,
        the endpoint always returns two items; an OAuth access token and
        a refresh token in the response.

        __OAuth tokens should only live on secure servers. Application clients
        should never interact directly with OAuth tokens__.

        Parameters
        ----------
        client_id : str
            The Square-issued ID of your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        client_secret : str
            The Square-issued application secret for your application, available
            from the [developer dashboard](https://developer.squareup.com/apps).

        grant_type : str
            Specifies the method to request an OAuth access token.
            Valid values are: `authorization_code`, `refresh_token`, and `migration_token`

        code : typing.Optional[str]
            The authorization code to exchange.
            This is required if `grant_type` is set to `authorization_code`, to indicate that
            the application wants to exchange an authorization code for an OAuth access token.

        migration_token : typing.Optional[str]
            Legacy OAuth access token obtained using a Connect API version prior
            to 2019-03-13. This parameter is required if `grant_type` is set to
            `migration_token` to indicate that the application wants to get a replacement
            OAuth access token. The response also returns a refresh token.
            For more information, see [Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).

        redirect_uri : typing.Optional[str]
            The redirect URL assigned in the [developer dashboard](https://developer.squareup.com/apps).

        refresh_token : typing.Optional[str]
            A valid refresh token for generating a new OAuth access token.
            A valid refresh token is required if `grant_type` is set to `refresh_token` , to indicate the application wants a replacement for an expired OAuth access token.

        scopes : typing.Optional[typing.Sequence[str]]
            A JSON list of strings representing the permissions the application is requesting.
            For example: "`["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"]`"
            The access token returned in the response is granted the permissions
            that comprise the intersection between the requested list of permissions, and those
            that belong to the provided refresh token.

        short_lived : typing.Optional[bool]
            A boolean indicating a request for a short-lived access token.
            The short-lived access token returned in the response will expire in 24 hours.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObtainTokenResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth2/token",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "grant_type": grant_type,
                "migration_token": migration_token,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
                "scopes": scopes,
                "short_lived": short_lived,
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
                    ObtainTokenResponse,
                    parse_obj_as(
                        type_=ObtainTokenResponse,
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


class AsyncRawOAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def renew_token(
        self,
        client_id: str,
        *,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RenewTokenResponse]:
        """
        `RenewToken` is deprecated. For information about refreshing OAuth access tokens, see
        [Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).


        Renews an OAuth access token before it expires.

        OAuth access tokens besides your application's personal access token expire after __30 days__.
        You can also renew expired tokens within __15 days__ of their expiration.
        You cannot renew an access token that has been expired for more than 15 days.
        Instead, the associated user must re-complete the OAuth flow from the beginning.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the Credentials
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        client_id : str
            Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).

        access_token : typing.Optional[str]
            The token you want to renew.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RenewTokenResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth2/clients/{encode_path_param(client_id)}/access-token/renew",
            method="POST",
            json={
                "access_token": access_token,
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
                    RenewTokenResponse,
                    parse_obj_as(
                        type_=RenewTokenResponse,
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

    async def revoke_token(
        self,
        *,
        access_token: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        merchant_id: typing.Optional[str] = OMIT,
        revoke_only_access_token: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RevokeTokenResponse]:
        """
        Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this
        endpoint revokes all of them, regardless of which token you specify. When an
        OAuth access token is revoked, all of the active subscriptions associated
        with that OAuth token are canceled immediately.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the OAuth
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        access_token : typing.Optional[str]
            The access token of the merchant whose token you want to revoke.
            Do not provide a value for merchant_id if you provide this parameter.

        client_id : typing.Optional[str]
            The Square issued ID for your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        merchant_id : typing.Optional[str]
            The ID of the merchant whose token you want to revoke.
            Do not provide a value for access_token if you provide this parameter.

        revoke_only_access_token : typing.Optional[bool]
            If `true`, terminate the given single access token, but do not
            terminate the entire authorization.
            Default: `false`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RevokeTokenResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth2/revoke",
            method="POST",
            json={
                "access_token": access_token,
                "client_id": client_id,
                "merchant_id": merchant_id,
                "revoke_only_access_token": revoke_only_access_token,
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
                    RevokeTokenResponse,
                    parse_obj_as(
                        type_=RevokeTokenResponse,
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

    async def obtain_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: str,
        code: typing.Optional[str] = OMIT,
        migration_token: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        short_lived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObtainTokenResponse]:
        """
        Returns an OAuth access token.

        The endpoint supports distinct methods of obtaining OAuth access tokens.
        Applications specify a method by adding the `grant_type` parameter
        in the request and also provide relevant information.

        __Note:__ Regardless of the method application specified,
        the endpoint always returns two items; an OAuth access token and
        a refresh token in the response.

        __OAuth tokens should only live on secure servers. Application clients
        should never interact directly with OAuth tokens__.

        Parameters
        ----------
        client_id : str
            The Square-issued ID of your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        client_secret : str
            The Square-issued application secret for your application, available
            from the [developer dashboard](https://developer.squareup.com/apps).

        grant_type : str
            Specifies the method to request an OAuth access token.
            Valid values are: `authorization_code`, `refresh_token`, and `migration_token`

        code : typing.Optional[str]
            The authorization code to exchange.
            This is required if `grant_type` is set to `authorization_code`, to indicate that
            the application wants to exchange an authorization code for an OAuth access token.

        migration_token : typing.Optional[str]
            Legacy OAuth access token obtained using a Connect API version prior
            to 2019-03-13. This parameter is required if `grant_type` is set to
            `migration_token` to indicate that the application wants to get a replacement
            OAuth access token. The response also returns a refresh token.
            For more information, see [Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).

        redirect_uri : typing.Optional[str]
            The redirect URL assigned in the [developer dashboard](https://developer.squareup.com/apps).

        refresh_token : typing.Optional[str]
            A valid refresh token for generating a new OAuth access token.
            A valid refresh token is required if `grant_type` is set to `refresh_token` , to indicate the application wants a replacement for an expired OAuth access token.

        scopes : typing.Optional[typing.Sequence[str]]
            A JSON list of strings representing the permissions the application is requesting.
            For example: "`["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"]`"
            The access token returned in the response is granted the permissions
            that comprise the intersection between the requested list of permissions, and those
            that belong to the provided refresh token.

        short_lived : typing.Optional[bool]
            A boolean indicating a request for a short-lived access token.
            The short-lived access token returned in the response will expire in 24 hours.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObtainTokenResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth2/token",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "grant_type": grant_type,
                "migration_token": migration_token,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
                "scopes": scopes,
                "short_lived": short_lived,
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
                    ObtainTokenResponse,
                    parse_obj_as(
                        type_=ObtainTokenResponse,
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
