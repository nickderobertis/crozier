

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_models_user_role_change import ApiModelsUserRoleChange
from ..types.api_paged_response_api_models_role import ApiPagedResponseApiModelsRole
from ..types.api_paged_response_api_models_user import ApiPagedResponseApiModelsUser
from ..types.api_paged_response_api_models_user_effective_permission import (
    ApiPagedResponseApiModelsUserEffectivePermission,
)
from .raw_client import AsyncRawUserpermissionsClient, RawUserpermissionsClient


OMIT = typing.cast(typing.Any, ...)


class UserpermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserpermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserpermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserpermissionsClient
        """
        return self._raw_client

    def getusers(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The Role's ID

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsUser
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.userpermissions.getusers(
            id=1,
        )
        """
        _response = self._raw_client.getusers(id, limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def put(
        self,
        id: int,
        *,
        request: typing.Sequence[ApiModelsUserRoleChange],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        request : typing.Sequence[ApiModelsUserRoleChange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import ApiModelsUserRoleChange, ApiModelsUserRoleChangeAction, FernApi

        client = FernApi()
        client.userpermissions.put(
            id=1,
            request=[
                ApiModelsUserRoleChange(
                    action=ApiModelsUserRoleChangeAction.GRANT,
                    name="Name",
                )
            ],
        )
        """
        _response = self._raw_client.put(id, request=request, request_options=request_options)
        return _response.data

    def getpermissions(
        self,
        id: int,
        *,
        permission: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsUserEffectivePermission:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        permission : typing.Optional[str]
            Filter by permission name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsUserEffectivePermission
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.userpermissions.getpermissions(
            id=1,
        )
        """
        _response = self._raw_client.getpermissions(
            id, permission=permission, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def getcurrentuserroles(
        self,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

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
        client.userpermissions.getcurrentuserroles()
        """
        _response = self._raw_client.getcurrentuserroles(
            role=role, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def getroles(
        self,
        id: int,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

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
        client.userpermissions.getroles(
            id=1,
        )
        """
        _response = self._raw_client.getroles(
            id, role=role, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data


class AsyncUserpermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserpermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserpermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserpermissionsClient
        """
        return self._raw_client

    async def getusers(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The Role's ID

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsUser
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.userpermissions.getusers(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getusers(id, limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def put(
        self,
        id: int,
        *,
        request: typing.Sequence[ApiModelsUserRoleChange],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        request : typing.Sequence[ApiModelsUserRoleChange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            ApiModelsUserRoleChange,
            ApiModelsUserRoleChangeAction,
            AsyncFernApi,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.userpermissions.put(
                id=1,
                request=[
                    ApiModelsUserRoleChange(
                        action=ApiModelsUserRoleChangeAction.GRANT,
                        name="Name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(id, request=request, request_options=request_options)
        return _response.data

    async def getpermissions(
        self,
        id: int,
        *,
        permission: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsUserEffectivePermission:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        permission : typing.Optional[str]
            Filter by permission name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsUserEffectivePermission
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.userpermissions.getpermissions(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpermissions(
            id, permission=permission, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def getcurrentuserroles(
        self,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

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
            await client.userpermissions.getcurrentuserroles()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcurrentuserroles(
            role=role, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def getroles(
        self,
        id: int,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsRole:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

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
            await client.userpermissions.getroles(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getroles(
            id, role=role, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
