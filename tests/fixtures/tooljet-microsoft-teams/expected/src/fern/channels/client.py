

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.channel import Channel
from ..types.conversation_member_input import ConversationMemberInput
from .raw_client import AsyncRawChannelsClient, RawChannelsClient
from .types.create_channel_request_membership_type import CreateChannelRequestMembershipType
from .types.get_channel_request_expand import GetChannelRequestExpand
from .types.list_all_channels_response import ListAllChannelsResponse
from .types.list_channels_response import ListChannelsResponse


OMIT = typing.cast(typing.Any, ...)


class ChannelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelsClient
        """
        return self._raw_client

    def list_all_channels(
        self,
        team_id: str,
        *,
        filter: typing.Optional[str] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllChannelsResponse:
        """
        Get all channels across a team, including shared channels

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        filter : typing.Optional[str]
            OData filter query

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllChannelsResponse
            Successfully retrieved all channels

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.list_all_channels(
            team_id="team-id",
            filter="membershipType eq 'shared'",
        )
        """
        _response = self._raw_client.list_all_channels(
            team_id, filter=filter, top=top, skip=skip, request_options=request_options
        )
        return _response.data

    def list_channels(
        self,
        team_id: str,
        *,
        filter: typing.Optional[str] = None,
        select: typing.Optional[str] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChannelsResponse:
        """
        Retrieve the list of channels in a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        filter : typing.Optional[str]
            OData filter query

        select : typing.Optional[str]
            OData select query

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelsResponse
            Successfully retrieved channels

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.list_channels(
            team_id="team-id",
            filter="membershipType eq 'private'",
        )
        """
        _response = self._raw_client.list_channels(
            team_id, filter=filter, select=select, top=top, skip=skip, request_options=request_options
        )
        return _response.data

    def create_channel(
        self,
        team_id: str,
        *,
        display_name: str,
        odata_type: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        membership_type: typing.Optional[CreateChannelRequestMembershipType] = OMIT,
        members: typing.Optional[typing.Sequence[ConversationMemberInput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Channel:
        """
        Create a new channel in a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        display_name : str

        odata_type : typing.Optional[str]

        description : typing.Optional[str]

        membership_type : typing.Optional[CreateChannelRequestMembershipType]

        members : typing.Optional[typing.Sequence[ConversationMemberInput]]
            Required when creating a private channel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channel
            Channel created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.create_channel(
            team_id="team-id",
            display_name="displayName",
        )
        """
        _response = self._raw_client.create_channel(
            team_id,
            display_name=display_name,
            odata_type=odata_type,
            description=description,
            membership_type=membership_type,
            members=members,
            request_options=request_options,
        )
        return _response.data

    def get_channel(
        self,
        team_id: str,
        channel_id: str,
        *,
        select: typing.Optional[str] = None,
        expand: typing.Optional[GetChannelRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Channel:
        """
        Retrieve the properties and relationships of a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        select : typing.Optional[str]
            OData select query

        expand : typing.Optional[GetChannelRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channel
            Successfully retrieved channel

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.get_channel(
            team_id="team-id",
            channel_id="channel-id",
            select="summary",
        )
        """
        _response = self._raw_client.get_channel(
            team_id, channel_id, select=select, expand=expand, request_options=request_options
        )
        return _response.data

    def delete_channel(
        self, team_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

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
        client.channels.delete_channel(
            team_id="team-id",
            channel_id="channel-id",
        )
        """
        _response = self._raw_client.delete_channel(team_id, channel_id, request_options=request_options)
        return _response.data

    def update_channel(
        self,
        team_id: str,
        channel_id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the properties of a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        display_name : typing.Optional[str]

        description : typing.Optional[str]

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
        client.channels.update_channel(
            team_id="team-id",
            channel_id="channel-id",
        )
        """
        _response = self._raw_client.update_channel(
            team_id, channel_id, display_name=display_name, description=description, request_options=request_options
        )
        return _response.data

    def get_channel_from_all_channels(
        self, team_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Channel:
        """
        Get a channel from the list of all channels

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channel
            Successfully retrieved channel

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.get_channel_from_all_channels(
            team_id="team-id",
            channel_id="channel-id",
        )
        """
        _response = self._raw_client.get_channel_from_all_channels(team_id, channel_id, request_options=request_options)
        return _response.data


class AsyncChannelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelsClient
        """
        return self._raw_client

    async def list_all_channels(
        self,
        team_id: str,
        *,
        filter: typing.Optional[str] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllChannelsResponse:
        """
        Get all channels across a team, including shared channels

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        filter : typing.Optional[str]
            OData filter query

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllChannelsResponse
            Successfully retrieved all channels

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.list_all_channels(
                team_id="team-id",
                filter="membershipType eq 'shared'",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_channels(
            team_id, filter=filter, top=top, skip=skip, request_options=request_options
        )
        return _response.data

    async def list_channels(
        self,
        team_id: str,
        *,
        filter: typing.Optional[str] = None,
        select: typing.Optional[str] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChannelsResponse:
        """
        Retrieve the list of channels in a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        filter : typing.Optional[str]
            OData filter query

        select : typing.Optional[str]
            OData select query

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelsResponse
            Successfully retrieved channels

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.list_channels(
                team_id="team-id",
                filter="membershipType eq 'private'",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_channels(
            team_id, filter=filter, select=select, top=top, skip=skip, request_options=request_options
        )
        return _response.data

    async def create_channel(
        self,
        team_id: str,
        *,
        display_name: str,
        odata_type: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        membership_type: typing.Optional[CreateChannelRequestMembershipType] = OMIT,
        members: typing.Optional[typing.Sequence[ConversationMemberInput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Channel:
        """
        Create a new channel in a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        display_name : str

        odata_type : typing.Optional[str]

        description : typing.Optional[str]

        membership_type : typing.Optional[CreateChannelRequestMembershipType]

        members : typing.Optional[typing.Sequence[ConversationMemberInput]]
            Required when creating a private channel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channel
            Channel created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.create_channel(
                team_id="team-id",
                display_name="displayName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_channel(
            team_id,
            display_name=display_name,
            odata_type=odata_type,
            description=description,
            membership_type=membership_type,
            members=members,
            request_options=request_options,
        )
        return _response.data

    async def get_channel(
        self,
        team_id: str,
        channel_id: str,
        *,
        select: typing.Optional[str] = None,
        expand: typing.Optional[GetChannelRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Channel:
        """
        Retrieve the properties and relationships of a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        select : typing.Optional[str]
            OData select query

        expand : typing.Optional[GetChannelRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channel
            Successfully retrieved channel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.get_channel(
                team_id="team-id",
                channel_id="channel-id",
                select="summary",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_channel(
            team_id, channel_id, select=select, expand=expand, request_options=request_options
        )
        return _response.data

    async def delete_channel(
        self, team_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

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
            await client.channels.delete_channel(
                team_id="team-id",
                channel_id="channel-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_channel(team_id, channel_id, request_options=request_options)
        return _response.data

    async def update_channel(
        self,
        team_id: str,
        channel_id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the properties of a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        display_name : typing.Optional[str]

        description : typing.Optional[str]

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
            await client.channels.update_channel(
                team_id="team-id",
                channel_id="channel-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_channel(
            team_id, channel_id, display_name=display_name, description=description, request_options=request_options
        )
        return _response.data

    async def get_channel_from_all_channels(
        self, team_id: str, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Channel:
        """
        Get a channel from the list of all channels

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channel
            Successfully retrieved channel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.get_channel_from_all_channels(
                team_id="team-id",
                channel_id="channel-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_channel_from_all_channels(
            team_id, channel_id, request_options=request_options
        )
        return _response.data
