

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.channel import Channel
from ..types.knocker_id import KnockerId
from ..types.media import Media
from ..types.member_action import MemberAction
from ..types.member_id import MemberId
from ..types.member_id_inviting import MemberIdInviting
from ..types.user_id import UserId
from .raw_client import AsyncRawMemberClient, RawMemberClient
from .types.create_member_response import CreateMemberResponse
from .types.get_member_response import GetMemberResponse
from .types.get_members_response_item import GetMembersResponseItem
from .types.update_member_response import UpdateMemberResponse


OMIT = typing.cast(typing.Any, ...)


class MemberClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMemberClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMemberClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMemberClient
        """
        return self._raw_client

    def get_members(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetMembersResponseItem]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/members](/api/conversation.v2#get-members).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetMembersResponseItem]
            Members List Object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.member.get_members(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
        )
        """
        _response = self._raw_client.get_members(conversation_id, request_options=request_options)
        return _response.data

    def create_member(
        self,
        conversation_id: str,
        *,
        channel: Channel,
        user_id: UserId,
        action: typing.Optional[MemberAction] = OMIT,
        knocking_id: typing.Optional[KnockerId] = OMIT,
        media: typing.Optional[Media] = OMIT,
        member_id: typing.Optional[MemberId] = OMIT,
        member_id_inviting: typing.Optional[MemberIdInviting] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMemberResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        channel : Channel

        user_id : UserId

        action : typing.Optional[MemberAction]

        knocking_id : typing.Optional[KnockerId]

        media : typing.Optional[Media]

        member_id : typing.Optional[MemberId]

        member_id_inviting : typing.Optional[MemberIdInviting]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMemberResponse
            Create or invite Member in invite state

        Examples
        --------
        from fern import Channel, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.member.create_member(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            channel=Channel(),
            user_id="USR-63f61863-4a51-4f6b-86e1-46edebio0391",
        )
        """
        _response = self._raw_client.create_member(
            conversation_id,
            channel=channel,
            user_id=user_id,
            action=action,
            knocking_id=knocking_id,
            media=media,
            member_id=member_id,
            member_id_inviting=member_id_inviting,
            request_options=request_options,
        )
        return _response.data

    def get_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMemberResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMemberResponse
            Retrieve member payload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.member.get_member(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            member_id="member_id",
        )
        """
        _response = self._raw_client.get_member(conversation_id, member_id, request_options=request_options)
        return _response.data

    def update_member(
        self,
        conversation_id: str,
        member_id: str,
        *,
        action: typing.Optional[MemberAction] = OMIT,
        channel: typing.Optional[Channel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMemberResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        action : typing.Optional[MemberAction]

        channel : typing.Optional[Channel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMemberResponse
            Member retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.member.update_member(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            member_id="member_id",
        )
        """
        _response = self._raw_client.update_member(
            conversation_id, member_id, action=action, channel=channel, request_options=request_options
        )
        return _response.data

    def delete_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.member.delete_member(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            member_id="member_id",
        )
        """
        _response = self._raw_client.delete_member(conversation_id, member_id, request_options=request_options)
        return _response.data


class AsyncMemberClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMemberClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMemberClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMemberClient
        """
        return self._raw_client

    async def get_members(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetMembersResponseItem]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/members](/api/conversation.v2#get-members).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetMembersResponseItem]
            Members List Object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.member.get_members(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_members(conversation_id, request_options=request_options)
        return _response.data

    async def create_member(
        self,
        conversation_id: str,
        *,
        channel: Channel,
        user_id: UserId,
        action: typing.Optional[MemberAction] = OMIT,
        knocking_id: typing.Optional[KnockerId] = OMIT,
        media: typing.Optional[Media] = OMIT,
        member_id: typing.Optional[MemberId] = OMIT,
        member_id_inviting: typing.Optional[MemberIdInviting] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMemberResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        channel : Channel

        user_id : UserId

        action : typing.Optional[MemberAction]

        knocking_id : typing.Optional[KnockerId]

        media : typing.Optional[Media]

        member_id : typing.Optional[MemberId]

        member_id_inviting : typing.Optional[MemberIdInviting]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMemberResponse
            Create or invite Member in invite state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Channel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.member.create_member(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                channel=Channel(),
                user_id="USR-63f61863-4a51-4f6b-86e1-46edebio0391",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_member(
            conversation_id,
            channel=channel,
            user_id=user_id,
            action=action,
            knocking_id=knocking_id,
            media=media,
            member_id=member_id,
            member_id_inviting=member_id_inviting,
            request_options=request_options,
        )
        return _response.data

    async def get_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMemberResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMemberResponse
            Retrieve member payload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.member.get_member(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                member_id="member_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_member(conversation_id, member_id, request_options=request_options)
        return _response.data

    async def update_member(
        self,
        conversation_id: str,
        member_id: str,
        *,
        action: typing.Optional[MemberAction] = OMIT,
        channel: typing.Optional[Channel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMemberResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        action : typing.Optional[MemberAction]

        channel : typing.Optional[Channel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMemberResponse
            Member retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.member.update_member(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                member_id="member_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_member(
            conversation_id, member_id, action=action, channel=channel, request_options=request_options
        )
        return _response.data

    async def delete_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.member.delete_member(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                member_id="member_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_member(conversation_id, member_id, request_options=request_options)
        return _response.data
