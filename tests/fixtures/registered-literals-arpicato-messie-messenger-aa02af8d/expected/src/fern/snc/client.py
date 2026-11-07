

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.created_group import CreatedGroup
from ..types.resolved_identifier import ResolvedIdentifier
from ..types.user_login_id import UserLoginId
from .raw_client import AsyncRawSncClient, RawSncClient
from .types.create_dm_response import CreateDmResponse
from .types.get_contacts_response import GetContactsResponse
from .types.group_create_params_avatar import GroupCreateParamsAvatar
from .types.group_create_params_disappear import GroupCreateParamsDisappear
from .types.group_create_params_name import GroupCreateParamsName
from .types.group_create_params_topic import GroupCreateParamsTopic
from .types.search_users_response import SearchUsersResponse


OMIT = typing.cast(typing.Any, ...)


class SncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSncClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSncClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSncClient
        """
        return self._raw_client

    def get_contacts(
        self, *, login_id: typing.Optional[UserLoginId] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContactsResponse:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactsResponse
            Contact list fetched successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.snc.get_contacts(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        """
        _response = self._raw_client.get_contacts(login_id=login_id, request_options=request_options)
        return _response.data

    def search_users(
        self,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchUsersResponse:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        query : typing.Optional[str]
            The search query to send to the remote network

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchUsersResponse
            Search completed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.snc.search_users(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        """
        _response = self._raw_client.search_users(login_id=login_id, query=query, request_options=request_options)
        return _response.data

    def resolve_identifier(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolvedIdentifier:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolvedIdentifier
            Identifier resolved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.snc.resolve_identifier(
            identifier="username",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        """
        _response = self._raw_client.resolve_identifier(identifier, login_id=login_id, request_options=request_options)
        return _response.data

    def create_dm(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDmResponse:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDmResponse
            Identifier resolved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.snc.create_dm(
            identifier="username",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        """
        _response = self._raw_client.create_dm(identifier, login_id=login_id, request_options=request_options)
        return _response.data

    def create_group(
        self,
        type_path_param: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        type: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        participants: typing.Optional[typing.Sequence[str]] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[GroupCreateParamsName] = OMIT,
        avatar: typing.Optional[GroupCreateParamsAvatar] = OMIT,
        topic: typing.Optional[GroupCreateParamsTopic] = OMIT,
        disappear: typing.Optional[GroupCreateParamsDisappear] = OMIT,
        room_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedGroup:
        """
        Parameters
        ----------
        type_path_param : str

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        type : typing.Optional[str]
            The type of group to create.

        username : typing.Optional[str]
            The public username for the created group.

        participants : typing.Optional[typing.Sequence[str]]
            The users to add to the group initially.

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[GroupCreateParamsName]
            The `m.room.name` event content for the room.

        avatar : typing.Optional[GroupCreateParamsAvatar]
            The `m.room.avatar` event content for the room.

        topic : typing.Optional[GroupCreateParamsTopic]
            The `m.room.topic` event content for the room.

        disappear : typing.Optional[GroupCreateParamsDisappear]
            The `com.beeper.disappearing_timer` event content for the room.

        room_id : typing.Optional[str]
            An existing Matrix room ID to bridge to.
            The other parameters must be already in sync with the room state when using this parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedGroup
            Identifier resolved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.snc.create_group(
            type_path_param="type",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        """
        _response = self._raw_client.create_group(
            type_path_param,
            login_id=login_id,
            type=type,
            username=username,
            participants=participants,
            parent=parent,
            name=name,
            avatar=avatar,
            topic=topic,
            disappear=disappear,
            room_id=room_id,
            request_options=request_options,
        )
        return _response.data


class AsyncSncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSncClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSncClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSncClient
        """
        return self._raw_client

    async def get_contacts(
        self, *, login_id: typing.Optional[UserLoginId] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContactsResponse:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactsResponse
            Contact list fetched successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snc.get_contacts(
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contacts(login_id=login_id, request_options=request_options)
        return _response.data

    async def search_users(
        self,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchUsersResponse:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        query : typing.Optional[str]
            The search query to send to the remote network

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchUsersResponse
            Search completed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snc.search_users(
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_users(login_id=login_id, query=query, request_options=request_options)
        return _response.data

    async def resolve_identifier(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolvedIdentifier:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolvedIdentifier
            Identifier resolved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snc.resolve_identifier(
                identifier="username",
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_identifier(
            identifier, login_id=login_id, request_options=request_options
        )
        return _response.data

    async def create_dm(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDmResponse:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDmResponse
            Identifier resolved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snc.create_dm(
                identifier="username",
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dm(identifier, login_id=login_id, request_options=request_options)
        return _response.data

    async def create_group(
        self,
        type_path_param: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        type: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        participants: typing.Optional[typing.Sequence[str]] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[GroupCreateParamsName] = OMIT,
        avatar: typing.Optional[GroupCreateParamsAvatar] = OMIT,
        topic: typing.Optional[GroupCreateParamsTopic] = OMIT,
        disappear: typing.Optional[GroupCreateParamsDisappear] = OMIT,
        room_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedGroup:
        """
        Parameters
        ----------
        type_path_param : str

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        type : typing.Optional[str]
            The type of group to create.

        username : typing.Optional[str]
            The public username for the created group.

        participants : typing.Optional[typing.Sequence[str]]
            The users to add to the group initially.

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[GroupCreateParamsName]
            The `m.room.name` event content for the room.

        avatar : typing.Optional[GroupCreateParamsAvatar]
            The `m.room.avatar` event content for the room.

        topic : typing.Optional[GroupCreateParamsTopic]
            The `m.room.topic` event content for the room.

        disappear : typing.Optional[GroupCreateParamsDisappear]
            The `com.beeper.disappearing_timer` event content for the room.

        room_id : typing.Optional[str]
            An existing Matrix room ID to bridge to.
            The other parameters must be already in sync with the room state when using this parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedGroup
            Identifier resolved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snc.create_group(
                type_path_param="type",
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_group(
            type_path_param,
            login_id=login_id,
            type=type,
            username=username,
            participants=participants,
            parent=parent,
            name=name,
            avatar=avatar,
            topic=topic,
            disappear=disappear,
            room_id=room_id,
            request_options=request_options,
        )
        return _response.data
