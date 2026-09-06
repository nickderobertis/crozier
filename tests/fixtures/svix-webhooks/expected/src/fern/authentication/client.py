

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_portal_access_out import AppPortalAccessOut
from ..types.application_in import ApplicationIn
from .raw_client import AsyncRawAuthenticationClient, RawAuthenticationClient


OMIT = typing.cast(typing.Any, ...)


class AuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticationClient
        """
        return self._raw_client

    def v1authentication_app_portal_access(
        self,
        app_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        application: typing.Optional[ApplicationIn] = OMIT,
        feature_flags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppPortalAccessOut:
        """
        Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

        Parameters
        ----------
        app_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        application : typing.Optional[ApplicationIn]
            Optionally creates a new application alongside the message.

            If the application id or uid that is used in the path already exists, this argument is ignored.

        feature_flags : typing.Optional[typing.Sequence[str]]
            The set of feature flags the created token will have access to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPortalAccessOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authentication.v1authentication_app_portal_access(
            app_id="unique-app-identifier",
        )
        """
        _response = self._raw_client.v1authentication_app_portal_access(
            app_id,
            idempotency_key=idempotency_key,
            application=application,
            feature_flags=feature_flags,
            request_options=request_options,
        )
        return _response.data

    def logout_api_v1auth_logout_post(
        self, *, idempotency_key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """

        Logout an app token.

        Trying to log out other tokens will fail.

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authentication.logout_api_v1auth_logout_post()
        """
        _response = self._raw_client.logout_api_v1auth_logout_post(
            idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data


class AsyncAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticationClient
        """
        return self._raw_client

    async def v1authentication_app_portal_access(
        self,
        app_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        application: typing.Optional[ApplicationIn] = OMIT,
        feature_flags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppPortalAccessOut:
        """
        Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

        Parameters
        ----------
        app_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        application : typing.Optional[ApplicationIn]
            Optionally creates a new application alongside the message.

            If the application id or uid that is used in the path already exists, this argument is ignored.

        feature_flags : typing.Optional[typing.Sequence[str]]
            The set of feature flags the created token will have access to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPortalAccessOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authentication.v1authentication_app_portal_access(
                app_id="unique-app-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1authentication_app_portal_access(
            app_id,
            idempotency_key=idempotency_key,
            application=application,
            feature_flags=feature_flags,
            request_options=request_options,
        )
        return _response.data

    async def logout_api_v1auth_logout_post(
        self, *, idempotency_key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """

        Logout an app token.

        Trying to log out other tokens will fail.

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authentication.logout_api_v1auth_logout_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout_api_v1auth_logout_post(
            idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data
