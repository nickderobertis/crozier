

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorization_relations_bidder import AuthorizationRelationsBidder
from ..types.get_bidder_relation_members_endpoint_cursor_paged_result_of_output import (
    GetBidderRelationMembersEndpointCursorPagedResultOfOutput,
)
from .raw_client import AsyncRawBidderClient, RawBidderClient


OMIT = typing.cast(typing.Any, ...)


class BidderClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBidderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBidderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBidderClient
        """
        return self._raw_client

    def lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time(
        self,
        *,
        relation: typing.Optional[AuthorizationRelationsBidder] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBidderRelationMembersEndpointCursorPagedResultOfOutput:
        """
        Returns every relation unless relation narrows it. Follow nextCursor to page.

        Parameters
        ----------
        relation : typing.Optional[AuthorizationRelationsBidder]
            Optional relation to filter by.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBidderRelationMembersEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.bidder.lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time()
        """
        _response = self._raw_client.lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time(
            relation=relation, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    def grants_a_bidder_relation_to_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsBidder,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: re-granting an existing relation is a no-op.

        Parameters
        ----------
        customer : str
            The customer to grant the relation to.

        relation : AuthorizationRelationsBidder

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
        client.bidder.grants_a_bidder_relation_to_a_customer(
            customer="customer",
            relation="Admin",
        )
        """
        _response = self._raw_client.grants_a_bidder_relation_to_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data

    def revokes_a_bidder_relation_from_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsBidder,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: revoking a relation that was never granted is a no-op.

        Parameters
        ----------
        customer : str
            The customer to revoke the relation from.

        relation : AuthorizationRelationsBidder

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
        client.bidder.revokes_a_bidder_relation_from_a_customer(
            customer="customer",
            relation="Admin",
        )
        """
        _response = self._raw_client.revokes_a_bidder_relation_from_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data


class AsyncBidderClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBidderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBidderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBidderClient
        """
        return self._raw_client

    async def lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time(
        self,
        *,
        relation: typing.Optional[AuthorizationRelationsBidder] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBidderRelationMembersEndpointCursorPagedResultOfOutput:
        """
        Returns every relation unless relation narrows it. Follow nextCursor to page.

        Parameters
        ----------
        relation : typing.Optional[AuthorizationRelationsBidder]
            Optional relation to filter by.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBidderRelationMembersEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bidder.lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time(
            relation=relation, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def grants_a_bidder_relation_to_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsBidder,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: re-granting an existing relation is a no-op.

        Parameters
        ----------
        customer : str
            The customer to grant the relation to.

        relation : AuthorizationRelationsBidder

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
            await client.bidder.grants_a_bidder_relation_to_a_customer(
                customer="customer",
                relation="Admin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grants_a_bidder_relation_to_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data

    async def revokes_a_bidder_relation_from_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsBidder,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: revoking a relation that was never granted is a no-op.

        Parameters
        ----------
        customer : str
            The customer to revoke the relation from.

        relation : AuthorizationRelationsBidder

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
            await client.bidder.revokes_a_bidder_relation_from_a_customer(
                customer="customer",
                relation="Admin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revokes_a_bidder_relation_from_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data
