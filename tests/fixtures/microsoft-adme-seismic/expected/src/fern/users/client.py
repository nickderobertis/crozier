

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_roles import UserRoles
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.user_add_request_group import UserAddRequestGroup


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

    def user_list(
        self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.List[str]]:
        """
        <ul><li>List users in subproject's role-based authorization groups.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path, sd://tenant/sub-project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.List[str]]
            Retrieved sub-project users in admin, viewer, and editor groups successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.user_list(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.user_list(sdpath=sdpath, request_options=request_options)
        return _response.data

    def user_add(
        self,
        *,
        email: str,
        path: str,
        group: UserAddRequestGroup,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul><li>Add a user to a subproject default authorization group if it exists, otherwise, add the user to the first group.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        email : str
            Email address of the user. Note that this field is used as a principal identifer for entitlements-svc and be configured using the env variable USER_ID_CLAIM_FOR_ENTITLEMENTS_SVC in the Seismic DMS runtime.

        path : str
            Seismic store path in the format sd://tenant/subproject.

        group : UserAddRequestGroup
            Role to be assigned to the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.users import UserAddRequestGroup

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.user_add(
            email="test@slb.com",
            path="sd://slb/test_project",
            group=UserAddRequestGroup.EDITOR,
        )
        """
        _response = self._raw_client.user_add(email=email, path=path, group=group, request_options=request_options)
        return _response.data

    def user_rm(self, *, email: str, path: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        <ul><li>Remove a user from subproject default authorization groups if exists, otherwise, remove it from the first authorization group.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        email : str
            Email of the user to remove.

        path : str
            Path of the subproject.

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
        )
        client.users.user_rm(
            email="email",
            path="path",
        )
        """
        _response = self._raw_client.user_rm(email=email, path=path, request_options=request_options)
        return _response.data

    def user_roles(self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None) -> UserRoles:
        """
        <ul><li>Retrieve user role in all subprojects of the tenant.</li><li>Required roles: none/li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRoles
            Retrieved user roles in all subprojects of the tenant.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.user_roles(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.user_roles(sdpath=sdpath, request_options=request_options)
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

    async def user_list(
        self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.List[str]]:
        """
        <ul><li>List users in subproject's role-based authorization groups.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path, sd://tenant/sub-project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.List[str]]
            Retrieved sub-project users in admin, viewer, and editor groups successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.user_list(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_list(sdpath=sdpath, request_options=request_options)
        return _response.data

    async def user_add(
        self,
        *,
        email: str,
        path: str,
        group: UserAddRequestGroup,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul><li>Add a user to a subproject default authorization group if it exists, otherwise, add the user to the first group.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        email : str
            Email address of the user. Note that this field is used as a principal identifer for entitlements-svc and be configured using the env variable USER_ID_CLAIM_FOR_ENTITLEMENTS_SVC in the Seismic DMS runtime.

        path : str
            Seismic store path in the format sd://tenant/subproject.

        group : UserAddRequestGroup
            Role to be assigned to the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.users import UserAddRequestGroup

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.user_add(
                email="test@slb.com",
                path="sd://slb/test_project",
                group=UserAddRequestGroup.EDITOR,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_add(
            email=email, path=path, group=group, request_options=request_options
        )
        return _response.data

    async def user_rm(self, *, email: str, path: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        <ul><li>Remove a user from subproject default authorization groups if exists, otherwise, remove it from the first authorization group.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        email : str
            Email of the user to remove.

        path : str
            Path of the subproject.

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
        )


        async def main() -> None:
            await client.users.user_rm(
                email="email",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_rm(email=email, path=path, request_options=request_options)
        return _response.data

    async def user_roles(self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None) -> UserRoles:
        """
        <ul><li>Retrieve user role in all subprojects of the tenant.</li><li>Required roles: none/li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRoles
            Retrieved user roles in all subprojects of the tenant.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.user_roles(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_roles(sdpath=sdpath, request_options=request_options)
        return _response.data
