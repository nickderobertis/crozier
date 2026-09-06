

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.role import Role
from .raw_client import AsyncRawRolesClient, RawRolesClient
from .types.get_roles_request_order import GetRolesRequestOrder


OMIT = typing.cast(typing.Any, ...)


class RolesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRolesClient
        """
        return self._raw_client

    def get_roles(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetRolesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Role]:
        """
        Returns an array with one or more roles

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetRolesRequestOrder]
            Ordering groups by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Role]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.roles.get_roles()
        """
        _response = self._raw_client.get_roles(offset=offset, limit=limit, order=order, request_options=request_options)
        return _response.data

    def add_role(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Adds a new role

        Parameters
        ----------
        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.roles.add_role()
        """
        _response = self._raw_client.add_role(
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    def get_role_by_name(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Returns the role with the given name if it exists.

        Parameters
        ----------
        name : str
            role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.roles.get_role_by_name(
            name="name",
        )
        """
        _response = self._raw_client.get_role_by_name(name, request_options=request_options)
        return _response.data

    def update_role(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing role

        Parameters
        ----------
        name_ : str
            role name

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.roles.update_role(
            name_="name",
        )
        """
        _response = self._raw_client.update_role(
            name_,
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    def delete_role(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing role. A role referenced by users or admins cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.roles.delete_role(
            name="name",
        )
        """
        _response = self._raw_client.delete_role(name, request_options=request_options)
        return _response.data


class AsyncRolesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRolesClient
        """
        return self._raw_client

    async def get_roles(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetRolesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Role]:
        """
        Returns an array with one or more roles

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetRolesRequestOrder]
            Ordering groups by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Role]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.roles.get_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_roles(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_role(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Adds a new role

        Parameters
        ----------
        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.roles.add_role()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_role(
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    async def get_role_by_name(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Returns the role with the given name if it exists.

        Parameters
        ----------
        name : str
            role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.roles.get_role_by_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_role_by_name(name, request_options=request_options)
        return _response.data

    async def update_role(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing role

        Parameters
        ----------
        name_ : str
            role name

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.roles.update_role(
                name_="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_role(
            name_,
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    async def delete_role(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing role. A role referenced by users or admins cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            role name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.roles.delete_role(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_role(name, request_options=request_options)
        return _response.data
