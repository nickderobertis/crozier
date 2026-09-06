

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_models_role import ApiModelsRole
from ..types.api_models_role_permission_change import ApiModelsRolePermissionChange
from ..types.api_paged_response_api_models_permission import ApiPagedResponseApiModelsPermission
from ..types.api_paged_response_api_models_role import ApiPagedResponseApiModelsRole
from .raw_client import AsyncRawRolesClient, RawRolesClient


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

    def getroles(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        permission_id: typing.Optional[int] = None,
        permission_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        name : typing.Optional[str]
            Optional. Finds a role with the given name.

        permission_id : typing.Optional[int]

        permission_name : typing.Optional[str]
            Optional. Filters roles by whether they contain the provided permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsRole
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.roles.getroles()
        """
        _response = self._raw_client.getroles(
            limit=limit,
            offset=offset,
            name=name,
            permission_id=permission_id,
            permission_name=permission_name,
            request_options=request_options,
        )
        return _response.data

    def postrole(
        self,
        *,
        description: str,
        name: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            Role description

        name : str
            The name of the role. Must be alpha-numeric strings separated by a period (.).

        id : typing.Optional[int]
            The role's identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.roles.postrole(
            description="Description",
            name="Name",
        )
        """
        _response = self._raw_client.postrole(
            description=description, name=name, id=id, request_options=request_options
        )
        return _response.data

    def getrole(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The role's id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsRole
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.roles.getrole(
            id=1,
        )
        """
        _response = self._raw_client.getrole(id, request_options=request_options)
        return _response.data

    def putrole(
        self,
        id_: int,
        *,
        description: str,
        name: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The role's id

        description : str
            Role description

        name : str
            The name of the role. Must be alpha-numeric strings separated by a period (.).

        id : typing.Optional[int]
            The role's identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.roles.putrole(
            id_=1,
            description="Description",
            name="Name",
        )
        """
        _response = self._raw_client.putrole(
            id_, description=description, name=name, id=id, request_options=request_options
        )
        return _response.data

    def deleterole(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The role's id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.roles.deleterole(
            id=1,
        )
        """
        _response = self._raw_client.deleterole(id, request_options=request_options)
        return _response.data

    def getrolepermissions(
        self,
        id: int,
        *,
        name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsPermission:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the Role

        name : typing.Optional[str]
            Filter by permission name. Optional.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsPermission
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.roles.getrolepermissions(
            id=1,
        )
        """
        _response = self._raw_client.getrolepermissions(
            id, name=name, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def putrolepermissions(
        self,
        id: int,
        *,
        request: typing.Sequence[ApiModelsRolePermissionChange],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the Role

        request : typing.Sequence[ApiModelsRolePermissionChange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            ApiModelsRolePermissionChange,
            ApiModelsRolePermissionChangeAction,
            FernApi,
        )

        client = FernApi()
        client.roles.putrolepermissions(
            id=1,
            request=[
                ApiModelsRolePermissionChange(
                    action=ApiModelsRolePermissionChangeAction.GRANT,
                    permission="Permission",
                )
            ],
        )
        """
        _response = self._raw_client.putrolepermissions(id, request=request, request_options=request_options)
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

    async def getroles(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        permission_id: typing.Optional[int] = None,
        permission_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        name : typing.Optional[str]
            Optional. Finds a role with the given name.

        permission_id : typing.Optional[int]

        permission_name : typing.Optional[str]
            Optional. Filters roles by whether they contain the provided permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsRole
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.roles.getroles()


        asyncio.run(main())
        """
        _response = await self._raw_client.getroles(
            limit=limit,
            offset=offset,
            name=name,
            permission_id=permission_id,
            permission_name=permission_name,
            request_options=request_options,
        )
        return _response.data

    async def postrole(
        self,
        *,
        description: str,
        name: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            Role description

        name : str
            The name of the role. Must be alpha-numeric strings separated by a period (.).

        id : typing.Optional[int]
            The role's identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.roles.postrole(
                description="Description",
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postrole(
            description=description, name=name, id=id, request_options=request_options
        )
        return _response.data

    async def getrole(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The role's id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsRole
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.roles.getrole(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrole(id, request_options=request_options)
        return _response.data

    async def putrole(
        self,
        id_: int,
        *,
        description: str,
        name: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The role's id

        description : str
            Role description

        name : str
            The name of the role. Must be alpha-numeric strings separated by a period (.).

        id : typing.Optional[int]
            The role's identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.roles.putrole(
                id_=1,
                description="Description",
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putrole(
            id_, description=description, name=name, id=id, request_options=request_options
        )
        return _response.data

    async def deleterole(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The role's id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.roles.deleterole(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleterole(id, request_options=request_options)
        return _response.data

    async def getrolepermissions(
        self,
        id: int,
        *,
        name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsPermission:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the Role

        name : typing.Optional[str]
            Filter by permission name. Optional.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsPermission
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.roles.getrolepermissions(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrolepermissions(
            id, name=name, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def putrolepermissions(
        self,
        id: int,
        *,
        request: typing.Sequence[ApiModelsRolePermissionChange],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the Role

        request : typing.Sequence[ApiModelsRolePermissionChange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            ApiModelsRolePermissionChange,
            ApiModelsRolePermissionChangeAction,
            AsyncFernApi,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.roles.putrolepermissions(
                id=1,
                request=[
                    ApiModelsRolePermissionChange(
                        action=ApiModelsRolePermissionChangeAction.GRANT,
                        permission="Permission",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putrolepermissions(id, request=request, request_options=request_options)
        return _response.data
