

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentitySessionsClient, RawIdentitySessionsClient


OMIT = typing.cast(typing.Any, ...)


class IdentitySessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentitySessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentitySessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentitySessionsClient
        """
        return self._raw_client

    def display_the_login_form(
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
        client.identity_sessions.display_the_login_form()
        """
        _response = self._raw_client.display_the_login_form(request=request, request_options=request_options)
        return _response.data

    def authenticate_a_user(
        self,
        *,
        user_email: str,
        user_password: str,
        request: typing.Optional[str] = None,
        user_remember_me: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_email : str

        user_password : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        user_remember_me : typing.Optional[bool]

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
        client.identity_sessions.authenticate_a_user(
            user_email="user[email]",
            user_password="user[password]",
        )
        """
        _response = self._raw_client.authenticate_a_user(
            user_email=user_email,
            user_password=user_password,
            request=request,
            user_remember_me=user_remember_me,
            request_options=request_options,
        )
        return _response.data

    def log_out_the_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.identity_sessions.log_out_the_current_user()
        """
        _response = self._raw_client.log_out_the_current_user(request_options=request_options)
        return _response.data

    def choose_an_active_user_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
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
        client.identity_sessions.choose_an_active_user_session()
        """
        _response = self._raw_client.choose_an_active_user_session(request_options=request_options)
        return _response.data


class AsyncIdentitySessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentitySessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentitySessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentitySessionsClient
        """
        return self._raw_client

    async def display_the_login_form(
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
            await client.identity_sessions.display_the_login_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_the_login_form(request=request, request_options=request_options)
        return _response.data

    async def authenticate_a_user(
        self,
        *,
        user_email: str,
        user_password: str,
        request: typing.Optional[str] = None,
        user_remember_me: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_email : str

        user_password : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        user_remember_me : typing.Optional[bool]

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
            await client.identity_sessions.authenticate_a_user(
                user_email="user[email]",
                user_password="user[password]",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authenticate_a_user(
            user_email=user_email,
            user_password=user_password,
            request=request,
            user_remember_me=user_remember_me,
            request_options=request_options,
        )
        return _response.data

    async def log_out_the_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.identity_sessions.log_out_the_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.log_out_the_current_user(request_options=request_options)
        return _response.data

    async def choose_an_active_user_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
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
            await client.identity_sessions.choose_an_active_user_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.choose_an_active_user_session(request_options=request_options)
        return _response.data
