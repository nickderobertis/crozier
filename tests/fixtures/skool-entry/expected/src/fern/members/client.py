

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.member import Member
from .raw_client import AsyncRawMembersClient, RawMembersClient


class MembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMembersClient
        """
        return self._raw_client

    def list_members(
        self,
        group_slug: str,
        *,
        session_id: str,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Member]:
        """
        Retrieve a list of members in a Skool group.

        Parameters
        ----------
        group_slug : str

        session_id : str

        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Member]
            List of members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.members.list_members(
            group_slug="group_slug",
            session_id="session_id",
        )
        """
        _response = self._raw_client.list_members(
            group_slug, session_id=session_id, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    def get_member(
        self,
        group_slug: str,
        member_id: str,
        *,
        session_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Member:
        """
        Retrieve details of a specific member in a group.

        Parameters
        ----------
        group_slug : str

        member_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Member details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.members.get_member(
            group_slug="group_slug",
            member_id="member_id",
            session_id="session_id",
        )
        """
        _response = self._raw_client.get_member(
            group_slug, member_id, session_id=session_id, request_options=request_options
        )
        return _response.data


class AsyncMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMembersClient
        """
        return self._raw_client

    async def list_members(
        self,
        group_slug: str,
        *,
        session_id: str,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Member]:
        """
        Retrieve a list of members in a Skool group.

        Parameters
        ----------
        group_slug : str

        session_id : str

        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Member]
            List of members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.members.list_members(
                group_slug="group_slug",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_members(
            group_slug, session_id=session_id, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_member(
        self,
        group_slug: str,
        member_id: str,
        *,
        session_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Member:
        """
        Retrieve details of a specific member in a group.

        Parameters
        ----------
        group_slug : str

        member_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Member details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.members.get_member(
                group_slug="group_slug",
                member_id="member_id",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_member(
            group_slug, member_id, session_id=session_id, request_options=request_options
        )
        return _response.data
