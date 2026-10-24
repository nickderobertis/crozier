

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorization_relations_external_app import AuthorizationRelationsExternalApp
from ..types.external_app_id import ExternalAppId
from ..types.get_external_app_relation_members_endpoint_cursor_paged_result_of_output import (
    GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput,
)
from .raw_client import AsyncRawExternalAppsClient, RawExternalAppsClient


OMIT = typing.cast(typing.Any, ...)


class ExternalAppsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExternalAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExternalAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExternalAppsClient
        """
        return self._raw_client

    def lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time(
        self,
        *,
        app: ExternalAppId,
        relation: typing.Optional[AuthorizationRelationsExternalApp] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput:
        """
        app is required: each app is a separate object in the graph, so there is no combined
         listing. Returns every relation unless relation narrows it. Follow nextCursor to page.

        Parameters
        ----------
        app : ExternalAppId
            The app whose members to list.

        relation : typing.Optional[AuthorizationRelationsExternalApp]
            Optional relation to filter by.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.external_apps.lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time(
            app="ArgoCd",
        )
        """
        _response = self._raw_client.lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time(
            app=app, relation=relation, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    def grants_an_external_app_relation_to_a_customer(
        self,
        *,
        customer: str,
        app: ExternalAppId,
        relation: AuthorizationRelationsExternalApp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: re-granting an existing relation is a no-op. The app must be one of the known
         values — an unrecognised app is rejected rather than written, since a grant against an object
         nothing reads would look like access was granted while conferring nothing.

        Parameters
        ----------
        customer : str
            The customer to grant the relation to.

        app : ExternalAppId

        relation : AuthorizationRelationsExternalApp

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
        client.external_apps.grants_an_external_app_relation_to_a_customer(
            customer="customer",
            app="ArgoCd",
            relation="Admin",
        )
        """
        _response = self._raw_client.grants_an_external_app_relation_to_a_customer(
            customer=customer, app=app, relation=relation, request_options=request_options
        )
        return _response.data

    def revokes_an_external_app_relation_from_a_customer(
        self,
        *,
        customer: str,
        app: ExternalAppId,
        relation: AuthorizationRelationsExternalApp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: revoking a relation that was never granted is a no-op.

        Parameters
        ----------
        customer : str
            The customer to revoke the relation from.

        app : ExternalAppId

        relation : AuthorizationRelationsExternalApp

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
        client.external_apps.revokes_an_external_app_relation_from_a_customer(
            customer="customer",
            app="ArgoCd",
            relation="Admin",
        )
        """
        _response = self._raw_client.revokes_an_external_app_relation_from_a_customer(
            customer=customer, app=app, relation=relation, request_options=request_options
        )
        return _response.data


class AsyncExternalAppsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExternalAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExternalAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExternalAppsClient
        """
        return self._raw_client

    async def lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time(
        self,
        *,
        app: ExternalAppId,
        relation: typing.Optional[AuthorizationRelationsExternalApp] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput:
        """
        app is required: each app is a separate object in the graph, so there is no combined
         listing. Returns every relation unless relation narrows it. Follow nextCursor to page.

        Parameters
        ----------
        app : ExternalAppId
            The app whose members to list.

        relation : typing.Optional[AuthorizationRelationsExternalApp]
            Optional relation to filter by.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.external_apps.lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time(
                app="ArgoCd",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time(
            app=app, relation=relation, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def grants_an_external_app_relation_to_a_customer(
        self,
        *,
        customer: str,
        app: ExternalAppId,
        relation: AuthorizationRelationsExternalApp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: re-granting an existing relation is a no-op. The app must be one of the known
         values — an unrecognised app is rejected rather than written, since a grant against an object
         nothing reads would look like access was granted while conferring nothing.

        Parameters
        ----------
        customer : str
            The customer to grant the relation to.

        app : ExternalAppId

        relation : AuthorizationRelationsExternalApp

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
            await client.external_apps.grants_an_external_app_relation_to_a_customer(
                customer="customer",
                app="ArgoCd",
                relation="Admin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grants_an_external_app_relation_to_a_customer(
            customer=customer, app=app, relation=relation, request_options=request_options
        )
        return _response.data

    async def revokes_an_external_app_relation_from_a_customer(
        self,
        *,
        customer: str,
        app: ExternalAppId,
        relation: AuthorizationRelationsExternalApp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Idempotent: revoking a relation that was never granted is a no-op.

        Parameters
        ----------
        customer : str
            The customer to revoke the relation from.

        app : ExternalAppId

        relation : AuthorizationRelationsExternalApp

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
            await client.external_apps.revokes_an_external_app_relation_from_a_customer(
                customer="customer",
                app="ArgoCd",
                relation="Admin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revokes_an_external_app_relation_from_a_customer(
            customer=customer, app=app, relation=relation, request_options=request_options
        )
        return _response.data
