

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ticket_get_user_response import TicketGetUserResponse
from ..types.ticket_get_users_response import TicketGetUsersResponse
from .raw_client import AsyncRawTicketUserClient, RawTicketUserClient


class TicketUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTicketUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTicketUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTicketUserClient
        """
        return self._raw_client

    def ticket_user_get_user(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TicketGetUserResponse:
        """
        Get details of a user

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetUserResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_user.ticket_user_get_user(
            id="id",
        )
        """
        _response = self._raw_client.ticket_user_get_user(id, fields=fields, request_options=request_options)
        return _response.data

    def ticket_user_get_users(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetUsersResponse:
        """
        Get all the users

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetUsersResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_user.ticket_user_get_users()
        """
        _response = self._raw_client.ticket_user_get_users(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data


class AsyncTicketUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTicketUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTicketUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTicketUserClient
        """
        return self._raw_client

    async def ticket_user_get_user(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TicketGetUserResponse:
        """
        Get details of a user

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetUserResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_user.ticket_user_get_user(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_user_get_user(id, fields=fields, request_options=request_options)
        return _response.data

    async def ticket_user_get_users(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetUsersResponse:
        """
        Get all the users

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetUsersResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_user.ticket_user_get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_user_get_users(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data
