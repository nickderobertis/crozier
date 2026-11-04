

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access import Access
from ..types.confirmation import Confirmation
from ..types.users_me import UsersMe
from .raw_client import AsyncRawAuthClient, RawAuthClient


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def current_user_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersMe:
        """
        Data about the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersMe
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.current_user_data()
        """
        _response = self._raw_client.current_user_data(request_options=request_options)
        return _response.data

    def login(self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None) -> UsersMe:
        """
        Login

        Parameters
        ----------
        email : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersMe
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.login(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.login(email=email, password=password, request_options=request_options)
        return _response.data

    def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> Confirmation:
        """
        Logout

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Confirmation
            confirmed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.logout()
        """
        _response = self._raw_client.logout(request_options=request_options)
        return _response.data

    def refresh_jwt(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersMe:
        """
        Refresh the JWT token

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersMe
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.refresh_jwt()
        """
        _response = self._raw_client.refresh_jwt(request_options=request_options)
        return _response.data

    def unlock_account(self, *, email: str, request_options: typing.Optional[RequestOptions] = None) -> Confirmation:
        """
        Unlock account

        Parameters
        ----------
        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Confirmation
            confirmed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.unlock_account(
            email="email",
        )
        """
        _response = self._raw_client.unlock_account(email=email, request_options=request_options)
        return _response.data

    def current_users_resource_access(self, *, request_options: typing.Optional[RequestOptions] = None) -> Access:
        """
        Lists the user's access per resource

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Access
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.current_users_resource_access()
        """
        _response = self._raw_client.current_users_resource_access(request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def current_user_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersMe:
        """
        Data about the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersMe
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.current_user_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.current_user_data(request_options=request_options)
        return _response.data

    async def login(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersMe:
        """
        Login

        Parameters
        ----------
        email : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersMe
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.login(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login(email=email, password=password, request_options=request_options)
        return _response.data

    async def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> Confirmation:
        """
        Logout

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Confirmation
            confirmed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(request_options=request_options)
        return _response.data

    async def refresh_jwt(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersMe:
        """
        Refresh the JWT token

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersMe
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.refresh_jwt()


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_jwt(request_options=request_options)
        return _response.data

    async def unlock_account(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Confirmation:
        """
        Unlock account

        Parameters
        ----------
        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Confirmation
            confirmed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.unlock_account(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unlock_account(email=email, request_options=request_options)
        return _response.data

    async def current_users_resource_access(self, *, request_options: typing.Optional[RequestOptions] = None) -> Access:
        """
        Lists the user's access per resource

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Access
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.current_users_resource_access()


        asyncio.run(main())
        """
        _response = await self._raw_client.current_users_resource_access(request_options=request_options)
        return _response.data
