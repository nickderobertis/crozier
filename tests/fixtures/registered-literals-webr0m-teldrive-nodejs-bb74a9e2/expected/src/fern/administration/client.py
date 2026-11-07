

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.admin_user_summary import AdminUserSummary
from ..types.user_role import UserRole
from .raw_client import AsyncRawAdministrationClient, RawAdministrationClient


OMIT = typing.cast(typing.Any, ...)


class AdministrationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdministrationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdministrationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdministrationClient
        """
        return self._raw_client

    def list_admin_users(
        self, *, search: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AdminUserSummary]:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AdminUserSummary]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.administration.list_admin_users()
        """
        _response = self._raw_client.list_admin_users(search=search, request_options=request_options)
        return _response.data

    def update_admin_user(
        self,
        user_id: int,
        *,
        role: typing.Optional[UserRole] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminUserSummary:
        """
        Parameters
        ----------
        user_id : int

        role : typing.Optional[UserRole]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminUserSummary
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.administration.update_admin_user(
            user_id=1000000,
        )
        """
        _response = self._raw_client.update_admin_user(
            user_id, role=role, disabled=disabled, request_options=request_options
        )
        return _response.data

    def revoke_admin_user_access(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.administration.revoke_admin_user_access(
            user_id=1000000,
        )
        """
        _response = self._raw_client.revoke_admin_user_access(user_id, request_options=request_options)
        return _response.data


class AsyncAdministrationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdministrationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdministrationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdministrationClient
        """
        return self._raw_client

    async def list_admin_users(
        self, *, search: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AdminUserSummary]:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AdminUserSummary]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.administration.list_admin_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_admin_users(search=search, request_options=request_options)
        return _response.data

    async def update_admin_user(
        self,
        user_id: int,
        *,
        role: typing.Optional[UserRole] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminUserSummary:
        """
        Parameters
        ----------
        user_id : int

        role : typing.Optional[UserRole]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminUserSummary
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.administration.update_admin_user(
                user_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_admin_user(
            user_id, role=role, disabled=disabled, request_options=request_options
        )
        return _response.data

    async def revoke_admin_user_access(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_id : int

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.administration.revoke_admin_user_access(
                user_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_admin_user_access(user_id, request_options=request_options)
        return _response.data
