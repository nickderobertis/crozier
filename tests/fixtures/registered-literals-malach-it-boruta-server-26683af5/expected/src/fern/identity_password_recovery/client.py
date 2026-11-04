

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityPasswordRecoveryClient, RawIdentityPasswordRecoveryClient


OMIT = typing.cast(typing.Any, ...)


class IdentityPasswordRecoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityPasswordRecoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityPasswordRecoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityPasswordRecoveryClient
        """
        return self._raw_client

    def display_the_password_reset_request_form(
        self, *, request: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_password_recovery.display_the_password_reset_request_form()
        """
        _response = self._raw_client.display_the_password_reset_request_form(
            request=request, request_options=request_options
        )
        return _response.data

    def request_password_reset_instructions(
        self,
        *,
        user_email: str,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_email : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

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
        )
        client.identity_password_recovery.request_password_reset_instructions(
            user_email="user[email]",
        )
        """
        _response = self._raw_client.request_password_reset_instructions(
            user_email=user_email, request=request, request_options=request_options
        )
        return _response.data

    def display_the_password_reset_form(
        self,
        token: str,
        *,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        token : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_password_recovery.display_the_password_reset_form(
            token="token",
        )
        """
        _response = self._raw_client.display_the_password_reset_form(
            token, request=request, request_options=request_options
        )
        return _response.data

    def reset_a_password(
        self,
        token: str,
        *,
        user_password: str,
        user_password_confirmation: str,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        token : str

        user_password : str

        user_password_confirmation : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_password_recovery.reset_a_password(
            token="token",
            user_password="user[password]",
            user_password_confirmation="user[password_confirmation]",
        )
        """
        _response = self._raw_client.reset_a_password(
            token,
            user_password=user_password,
            user_password_confirmation=user_password_confirmation,
            request=request,
            request_options=request_options,
        )
        return _response.data


class AsyncIdentityPasswordRecoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityPasswordRecoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityPasswordRecoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityPasswordRecoveryClient
        """
        return self._raw_client

    async def display_the_password_reset_request_form(
        self, *, request: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_password_recovery.display_the_password_reset_request_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_the_password_reset_request_form(
            request=request, request_options=request_options
        )
        return _response.data

    async def request_password_reset_instructions(
        self,
        *,
        user_email: str,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_email : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

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
        )


        async def main() -> None:
            await client.identity_password_recovery.request_password_reset_instructions(
                user_email="user[email]",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_password_reset_instructions(
            user_email=user_email, request=request, request_options=request_options
        )
        return _response.data

    async def display_the_password_reset_form(
        self,
        token: str,
        *,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        token : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_password_recovery.display_the_password_reset_form(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.display_the_password_reset_form(
            token, request=request, request_options=request_options
        )
        return _response.data

    async def reset_a_password(
        self,
        token: str,
        *,
        user_password: str,
        user_password_confirmation: str,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        token : str

        user_password : str

        user_password_confirmation : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_password_recovery.reset_a_password(
                token="token",
                user_password="user[password]",
                user_password_confirmation="user[password_confirmation]",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_a_password(
            token,
            user_password=user_password,
            user_password_confirmation=user_password_confirmation,
            request=request,
            request_options=request_options,
        )
        return _response.data
