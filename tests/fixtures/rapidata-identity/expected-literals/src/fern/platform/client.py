

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorization_relations_platform import AuthorizationRelationsPlatform
from ..types.get_platform_relation_members_endpoint_cursor_paged_result_of_output import (
    GetPlatformRelationMembersEndpointCursorPagedResultOfOutput,
)
from .raw_client import AsyncRawPlatformClient, RawPlatformClient


OMIT = typing.cast(typing.Any, ...)


class PlatformClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlatformClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlatformClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlatformClient
        """
        return self._raw_client

    def lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time(
        self,
        *,
        relation: typing.Optional[AuthorizationRelationsPlatform] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPlatformRelationMembersEndpointCursorPagedResultOfOutput:
        """
        Returns every relation unless relation narrows it. Follow nextCursor to page.

        Parameters
        ----------
        relation : typing.Optional[AuthorizationRelationsPlatform]
            Optional relation to filter by.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPlatformRelationMembersEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.platform.lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time()
        """
        _response = self._raw_client.lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time(
            relation=relation, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    def grants_a_platform_relation_to_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsPlatform,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: re-granting an existing relation is a no-op.

        Parameters
        ----------
        customer : str
            The customer to grant the relation to.

        relation : AuthorizationRelationsPlatform

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
        client.platform.grants_a_platform_relation_to_a_customer(
            customer="customer",
            relation="Admin",
        )
        """
        _response = self._raw_client.grants_a_platform_relation_to_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data

    def revokes_a_platform_relation_from_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsPlatform,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: revoking a relation that was never granted is a no-op.

        Parameters
        ----------
        customer : str
            The customer to revoke the relation from.

        relation : AuthorizationRelationsPlatform

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
        client.platform.revokes_a_platform_relation_from_a_customer(
            customer="customer",
            relation="Admin",
        )
        """
        _response = self._raw_client.revokes_a_platform_relation_from_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data


class AsyncPlatformClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlatformClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlatformClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlatformClient
        """
        return self._raw_client

    async def lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time(
        self,
        *,
        relation: typing.Optional[AuthorizationRelationsPlatform] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPlatformRelationMembersEndpointCursorPagedResultOfOutput:
        """
        Returns every relation unless relation narrows it. Follow nextCursor to page.

        Parameters
        ----------
        relation : typing.Optional[AuthorizationRelationsPlatform]
            Optional relation to filter by.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPlatformRelationMembersEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.platform.lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time(
            relation=relation, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def grants_a_platform_relation_to_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsPlatform,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: re-granting an existing relation is a no-op.

        Parameters
        ----------
        customer : str
            The customer to grant the relation to.

        relation : AuthorizationRelationsPlatform

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
            await client.platform.grants_a_platform_relation_to_a_customer(
                customer="customer",
                relation="Admin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grants_a_platform_relation_to_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data

    async def revokes_a_platform_relation_from_a_customer(
        self,
        *,
        customer: str,
        relation: AuthorizationRelationsPlatform,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: revoking a relation that was never granted is a no-op.

        Parameters
        ----------
        customer : str
            The customer to revoke the relation from.

        relation : AuthorizationRelationsPlatform

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
            await client.platform.revokes_a_platform_relation_from_a_customer(
                customer="customer",
                relation="Admin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revokes_a_platform_relation_from_a_customer(
            customer=customer, relation=relation, request_options=request_options
        )
        return _response.data
