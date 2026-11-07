

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.totp_auth_link_response import TotpAuthLinkResponse
from ..types.two_factor_auth_settings import TwoFactorAuthSettings
from .raw_client import AsyncRawTwoFactorAuthV1Alpha1UcClient, RawTwoFactorAuthV1Alpha1UcClient


OMIT = typing.cast(typing.Any, ...)


class TwoFactorAuthV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTwoFactorAuthV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTwoFactorAuthV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTwoFactorAuthV1Alpha1UcClient
        """
        return self._raw_client

    def get_two_factor_authentication_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TwoFactorAuthSettings:
        """
        Get Two-factor authentication settings.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TwoFactorAuthSettings
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.two_factor_auth_v1alpha1uc.get_two_factor_authentication_settings()
        """
        _response = self._raw_client.get_two_factor_authentication_settings(request_options=request_options)
        return _response.data

    def disable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.two_factor_auth_v1alpha1uc.disable_two_factor(
            password="password",
        )
        """
        _response = self._raw_client.disable_two_factor(
            password=password, totp_code=totp_code, request_options=request_options
        )
        return _response.data

    def enable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.two_factor_auth_v1alpha1uc.enable_two_factor(
            password="password",
        )
        """
        _response = self._raw_client.enable_two_factor(
            password=password, totp_code=totp_code, request_options=request_options
        )
        return _response.data

    def configurer_totp(
        self,
        *,
        code: str,
        password: str,
        secret: str,
        current_totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.two_factor_auth_v1alpha1uc.configurer_totp(
            code="code",
            password="password",
            secret="secret",
        )
        """
        _response = self._raw_client.configurer_totp(
            code=code,
            password=password,
            secret=secret,
            current_totp_code=current_totp_code,
            request_options=request_options,
        )
        return _response.data

    def delete_totp(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.two_factor_auth_v1alpha1uc.delete_totp(
            password="password",
        )
        """
        _response = self._raw_client.delete_totp(
            password=password, totp_code=totp_code, request_options=request_options
        )
        return _response.data

    def get_totp_auth_link(self, *, request_options: typing.Optional[RequestOptions] = None) -> TotpAuthLinkResponse:
        """
        Get TOTP auth link, including secret

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TotpAuthLinkResponse
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.two_factor_auth_v1alpha1uc.get_totp_auth_link()
        """
        _response = self._raw_client.get_totp_auth_link(request_options=request_options)
        return _response.data


class AsyncTwoFactorAuthV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTwoFactorAuthV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTwoFactorAuthV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTwoFactorAuthV1Alpha1UcClient
        """
        return self._raw_client

    async def get_two_factor_authentication_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TwoFactorAuthSettings:
        """
        Get Two-factor authentication settings.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TwoFactorAuthSettings
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.two_factor_auth_v1alpha1uc.get_two_factor_authentication_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_two_factor_authentication_settings(request_options=request_options)
        return _response.data

    async def disable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.two_factor_auth_v1alpha1uc.disable_two_factor(
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_two_factor(
            password=password, totp_code=totp_code, request_options=request_options
        )
        return _response.data

    async def enable_two_factor(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.two_factor_auth_v1alpha1uc.enable_two_factor(
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_two_factor(
            password=password, totp_code=totp_code, request_options=request_options
        )
        return _response.data

    async def configurer_totp(
        self,
        *,
        code: str,
        password: str,
        secret: str,
        current_totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.two_factor_auth_v1alpha1uc.configurer_totp(
                code="code",
                password="password",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.configurer_totp(
            code=code,
            password=password,
            secret=secret,
            current_totp_code=current_totp_code,
            request_options=request_options,
        )
        return _response.data

    async def delete_totp(
        self,
        *,
        password: str,
        totp_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TwoFactorAuthSettings:
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
        TwoFactorAuthSettings
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.two_factor_auth_v1alpha1uc.delete_totp(
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_totp(
            password=password, totp_code=totp_code, request_options=request_options
        )
        return _response.data

    async def get_totp_auth_link(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TotpAuthLinkResponse:
        """
        Get TOTP auth link, including secret

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TotpAuthLinkResponse
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.two_factor_auth_v1alpha1uc.get_totp_auth_link()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_totp_auth_link(request_options=request_options)
        return _response.data
