

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.users_email_delete_response import UsersEmailDeleteResponse
from ..types.users_get_response import UsersGetResponse
from ..types.users_post_response import UsersPostResponse
from .raw_client import AsyncRawUsersClient, RawUsersClient


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def list_all_dex_static_users_emails_only(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersGetResponse:
        """
        List all Dex static users (emails only)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_all_dex_static_users_emails_only()
        """
        _response = self._raw_client.list_all_dex_static_users_emails_only(request_options=request_options)
        return _response.data

    def create_a_new_dex_static_user(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersPostResponse:
        """
        Create a new Dex static user

        Parameters
        ----------
        email : str
            User email address

        password : str
            User password (minimum 8 characters)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersPostResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.create_a_new_dex_static_user(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.create_a_new_dex_static_user(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    def delete_a_dex_static_user_by_email(
        self, email: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersEmailDeleteResponse:
        """
        Delete a Dex static user by email

        Parameters
        ----------
        email : str
            User email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersEmailDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.delete_a_dex_static_user_by_email(
            email="email",
        )
        """
        _response = self._raw_client.delete_a_dex_static_user_by_email(email, request_options=request_options)
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def list_all_dex_static_users_emails_only(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersGetResponse:
        """
        List all Dex static users (emails only)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_all_dex_static_users_emails_only()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_dex_static_users_emails_only(request_options=request_options)
        return _response.data

    async def create_a_new_dex_static_user(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersPostResponse:
        """
        Create a new Dex static user

        Parameters
        ----------
        email : str
            User email address

        password : str
            User password (minimum 8 characters)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersPostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.create_a_new_dex_static_user(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_dex_static_user(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    async def delete_a_dex_static_user_by_email(
        self, email: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersEmailDeleteResponse:
        """
        Delete a Dex static user by email

        Parameters
        ----------
        email : str
            User email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersEmailDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.delete_a_dex_static_user_by_email(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_dex_static_user_by_email(email, request_options=request_options)
        return _response.data
