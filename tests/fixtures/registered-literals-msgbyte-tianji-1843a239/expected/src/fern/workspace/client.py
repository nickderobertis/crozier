

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWorkspaceClient, RawWorkspaceClient
from .types.workspace_create_response import WorkspaceCreateResponse
from .types.workspace_get_service_count_response import WorkspaceGetServiceCountResponse
from .types.workspace_invite_request_role import WorkspaceInviteRequestRole
from .types.workspace_members_response_item import WorkspaceMembersResponseItem
from .types.workspace_rename_response import WorkspaceRenameResponse
from .types.workspace_switch_response import WorkspaceSwitchResponse
from .types.workspace_update_member_role_request_role import WorkspaceUpdateMemberRoleRequestRole
from .types.workspace_update_settings_response import WorkspaceUpdateSettingsResponse


OMIT = typing.cast(typing.Any, ...)


class WorkspaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkspaceClient
        """
        return self._raw_client

    def create(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> WorkspaceCreateResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.create(
            name="name",
        )
        """
        _response = self._raw_client.create(name=name, request_options=request_options)
        return _response.data

    def switch(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceSwitchResponse:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceSwitchResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.switch(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.switch(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def rename(
        self, *, workspace_id: str, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRenameResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRenameResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.rename(
            workspace_id="workspaceId",
            name="name",
        )
        """
        _response = self._raw_client.rename(workspace_id=workspace_id, name=name, request_options=request_options)
        return _response.data

    def delete(self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.delete(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.delete(workspace_id, request_options=request_options)
        return _response.data

    def members(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkspaceMembersResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkspaceMembersResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.members(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.members(workspace_id, request_options=request_options)
        return _response.data

    def updatesettings(
        self,
        workspace_id: str,
        *,
        settings: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceUpdateSettingsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        settings : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceUpdateSettingsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.updatesettings(
            workspace_id="workspaceId",
            settings={"key": "value"},
        )
        """
        _response = self._raw_client.updatesettings(workspace_id, settings=settings, request_options=request_options)
        return _response.data

    def invite(
        self,
        workspace_id: str,
        *,
        email_or_id: str,
        role: typing.Optional[WorkspaceInviteRequestRole] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        workspace_id : str

        email_or_id : str

        role : typing.Optional[WorkspaceInviteRequestRole]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.invite(
            workspace_id="workspaceId",
            email_or_id="emailOrId",
        )
        """
        _response = self._raw_client.invite(
            workspace_id, email_or_id=email_or_id, role=role, request_options=request_options
        )
        return _response.data

    def tick(
        self, workspace_id: str, *, target_user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Administrator kicks a user out of a workspace.

        Parameters
        ----------
        workspace_id : str

        target_user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.tick(
            workspace_id="workspaceId",
            target_user_id="targetUserId",
        )
        """
        _response = self._raw_client.tick(workspace_id, target_user_id=target_user_id, request_options=request_options)
        return _response.data

    def updatememberrole(
        self,
        workspace_id: str,
        *,
        user_id: str,
        role: WorkspaceUpdateMemberRoleRequestRole,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Update workspace member role

        Parameters
        ----------
        workspace_id : str

        user_id : str

        role : WorkspaceUpdateMemberRoleRequestRole

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern.workspace import WorkspaceUpdateMemberRoleRequestRole

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.updatememberrole(
            workspace_id="workspaceId",
            user_id="userId",
            role=WorkspaceUpdateMemberRoleRequestRole.OWNER,
        )
        """
        _response = self._raw_client.updatememberrole(
            workspace_id, user_id=user_id, role=role, request_options=request_options
        )
        return _response.data

    def getservicecount(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceGetServiceCountResponse:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceGetServiceCountResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.getservicecount(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.getservicecount(workspace_id, request_options=request_options)
        return _response.data

    def recheckpausestatus(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Manually trigger workspace pause status check based on usage limits

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.recheckpausestatus(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.recheckpausestatus(workspace_id, request_options=request_options)
        return _response.data


class AsyncWorkspaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkspaceClient
        """
        return self._raw_client

    async def create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceCreateResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(name=name, request_options=request_options)
        return _response.data

    async def switch(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceSwitchResponse:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceSwitchResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.switch(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.switch(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    async def rename(
        self, *, workspace_id: str, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRenameResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRenameResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.rename(
                workspace_id="workspaceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rename(workspace_id=workspace_id, name=name, request_options=request_options)
        return _response.data

    async def delete(self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.delete(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(workspace_id, request_options=request_options)
        return _response.data

    async def members(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkspaceMembersResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkspaceMembersResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.members(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.members(workspace_id, request_options=request_options)
        return _response.data

    async def updatesettings(
        self,
        workspace_id: str,
        *,
        settings: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceUpdateSettingsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        settings : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceUpdateSettingsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.updatesettings(
                workspace_id="workspaceId",
                settings={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatesettings(
            workspace_id, settings=settings, request_options=request_options
        )
        return _response.data

    async def invite(
        self,
        workspace_id: str,
        *,
        email_or_id: str,
        role: typing.Optional[WorkspaceInviteRequestRole] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        workspace_id : str

        email_or_id : str

        role : typing.Optional[WorkspaceInviteRequestRole]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.invite(
                workspace_id="workspaceId",
                email_or_id="emailOrId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invite(
            workspace_id, email_or_id=email_or_id, role=role, request_options=request_options
        )
        return _response.data

    async def tick(
        self, workspace_id: str, *, target_user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Administrator kicks a user out of a workspace.

        Parameters
        ----------
        workspace_id : str

        target_user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.tick(
                workspace_id="workspaceId",
                target_user_id="targetUserId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tick(
            workspace_id, target_user_id=target_user_id, request_options=request_options
        )
        return _response.data

    async def updatememberrole(
        self,
        workspace_id: str,
        *,
        user_id: str,
        role: WorkspaceUpdateMemberRoleRequestRole,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Update workspace member role

        Parameters
        ----------
        workspace_id : str

        user_id : str

        role : WorkspaceUpdateMemberRoleRequestRole

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern.workspace import WorkspaceUpdateMemberRoleRequestRole

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.updatememberrole(
                workspace_id="workspaceId",
                user_id="userId",
                role=WorkspaceUpdateMemberRoleRequestRole.OWNER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatememberrole(
            workspace_id, user_id=user_id, role=role, request_options=request_options
        )
        return _response.data

    async def getservicecount(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceGetServiceCountResponse:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceGetServiceCountResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.getservicecount(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getservicecount(workspace_id, request_options=request_options)
        return _response.data

    async def recheckpausestatus(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Manually trigger workspace pause status check based on usage limits

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.recheckpausestatus(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recheckpausestatus(workspace_id, request_options=request_options)
        return _response.data
