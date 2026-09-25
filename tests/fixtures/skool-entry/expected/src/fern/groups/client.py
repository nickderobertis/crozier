

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.group import Group
from .raw_client import AsyncRawGroupsClient, RawGroupsClient


class GroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroupsClient
        """
        return self._raw_client

    def list_groups(
        self, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Group]:
        """
        Retrieve a list of Skool groups/communities the authenticated user has access to.

        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            List of groups

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groups.list_groups(
            session_id="session_id",
        )
        """
        _response = self._raw_client.list_groups(session_id=session_id, request_options=request_options)
        return _response.data

    def get_group(
        self, group_slug: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Retrieve details of a specific Skool group/community.

        Parameters
        ----------
        group_slug : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Group details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groups.get_group(
            group_slug="group_slug",
            session_id="session_id",
        )
        """
        _response = self._raw_client.get_group(group_slug, session_id=session_id, request_options=request_options)
        return _response.data


class AsyncGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroupsClient
        """
        return self._raw_client

    async def list_groups(
        self, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Group]:
        """
        Retrieve a list of Skool groups/communities the authenticated user has access to.

        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            List of groups

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groups.list_groups(
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_groups(session_id=session_id, request_options=request_options)
        return _response.data

    async def get_group(
        self, group_slug: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Retrieve details of a specific Skool group/community.

        Parameters
        ----------
        group_slug : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Group details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groups.get_group(
                group_slug="group_slug",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group(group_slug, session_id=session_id, request_options=request_options)
        return _response.data
