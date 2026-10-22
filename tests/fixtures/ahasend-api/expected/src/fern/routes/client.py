

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.created_route import CreatedRoute
from ..types.paginated_routes_response import PaginatedRoutesResponse
from ..types.route import Route
from ..types.success_response import SuccessResponse
from .raw_client import AsyncRawRoutesClient, RawRoutesClient


OMIT = typing.cast(typing.Any, ...)


class RoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoutesClient
        """
        return self._raw_client

    def get_routes(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRoutesResponse:
        """
        Returns a list of routes for the account. A domain-scoped key must
        provide the matching `domain` query parameter; the global read role can
        list without that filter.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Domain to filter routes by. Required when using a domain-scoped routes:read:{domain} API key.

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedRoutesResponse
            List of routes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.routes.get_routes(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_routes(
            account_id, domain=domain, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    def create_route(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        recipient: str,
        idempotency_key: typing.Optional[str] = None,
        attachments: typing.Optional[bool] = OMIT,
        headers: typing.Optional[bool] = OMIT,
        group_by_message_id: typing.Optional[bool] = OMIT,
        strip_replies: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedRoute:
        """
        Creates a new route for inbound email routing. Authorization uses the
        domain in `recipient`: the global write role or its matching
        domain-specific write role is sufficient.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Route name

        url : str
            Webhook URL for the route

        recipient : str
            Recipient filter

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        attachments : typing.Optional[bool]
            Whether to include attachments in webhooks

        headers : typing.Optional[bool]
            Whether to include headers in webhooks

        group_by_message_id : typing.Optional[bool]
            Whether to group by message ID

        strip_replies : typing.Optional[bool]
            Whether to strip reply content

        enabled : typing.Optional[bool]
            Whether the route is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedRoute
            Route created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.routes.create_route(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            name="Support Route",
            url="https://example.com/webhook",
            recipient="support@example.com",
            enabled=True,
        )
        """
        _response = self._raw_client.create_route(
            account_id,
            name=name,
            url=url,
            recipient=recipient,
            idempotency_key=idempotency_key,
            attachments=attachments,
            headers=headers,
            group_by_message_id=group_by_message_id,
            strip_replies=strip_replies,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_route(
        self, account_id: str, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Route:
        """
        Returns a specific route by ID. Access requires the global read role or
        a read role matching the route's recipient domain.

        Parameters
        ----------
        account_id : str
            Account ID

        route_id : str
            Route ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Route
            Route details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.routes.get_route(
            account_id="account_id",
            route_id="route_id",
        )
        """
        _response = self._raw_client.get_route(account_id, route_id, request_options=request_options)
        return _response.data

    def update_route(
        self,
        account_id: str,
        route_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        recipient: typing.Optional[str] = OMIT,
        attachments: typing.Optional[bool] = OMIT,
        headers: typing.Optional[bool] = OMIT,
        group_by_message_id: typing.Optional[bool] = OMIT,
        strip_replies: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Route:
        """
        Updates an existing route. A domain-scoped key must authorize the
        existing recipient domain and, when `recipient` changes, the new domain;
        `routes:write:all` satisfies both checks.

        Parameters
        ----------
        account_id : str
            Account ID

        route_id : str
            Route ID

        name : typing.Optional[str]
            Route name

        url : typing.Optional[str]
            Webhook URL for the route

        recipient : typing.Optional[str]
            Recipient filter

        attachments : typing.Optional[bool]
            Whether to include attachments in webhooks

        headers : typing.Optional[bool]
            Whether to include headers in webhooks

        group_by_message_id : typing.Optional[bool]
            Whether to group by message ID

        strip_replies : typing.Optional[bool]
            Whether to strip reply content

        enabled : typing.Optional[bool]
            Whether the route is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Route
            Route updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.routes.update_route(
            account_id="account_id",
            route_id="route_id",
            name="Updated Support Route",
            enabled=False,
        )
        """
        _response = self._raw_client.update_route(
            account_id,
            route_id,
            name=name,
            url=url,
            recipient=recipient,
            attachments=attachments,
            headers=headers,
            group_by_message_id=group_by_message_id,
            strip_replies=strip_replies,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def delete_route(
        self, account_id: str, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes a route. Access requires the global delete role or a delete role
        matching the route's recipient domain.

        Parameters
        ----------
        account_id : str
            Account ID

        route_id : str
            Route ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Route deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.routes.delete_route(
            account_id="account_id",
            route_id="route_id",
        )
        """
        _response = self._raw_client.delete_route(account_id, route_id, request_options=request_options)
        return _response.data


class AsyncRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoutesClient
        """
        return self._raw_client

    async def get_routes(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRoutesResponse:
        """
        Returns a list of routes for the account. A domain-scoped key must
        provide the matching `domain` query parameter; the global read role can
        list without that filter.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Domain to filter routes by. Required when using a domain-scoped routes:read:{domain} API key.

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedRoutesResponse
            List of routes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.routes.get_routes(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_routes(
            account_id, domain=domain, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def create_route(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        recipient: str,
        idempotency_key: typing.Optional[str] = None,
        attachments: typing.Optional[bool] = OMIT,
        headers: typing.Optional[bool] = OMIT,
        group_by_message_id: typing.Optional[bool] = OMIT,
        strip_replies: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedRoute:
        """
        Creates a new route for inbound email routing. Authorization uses the
        domain in `recipient`: the global write role or its matching
        domain-specific write role is sufficient.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Route name

        url : str
            Webhook URL for the route

        recipient : str
            Recipient filter

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        attachments : typing.Optional[bool]
            Whether to include attachments in webhooks

        headers : typing.Optional[bool]
            Whether to include headers in webhooks

        group_by_message_id : typing.Optional[bool]
            Whether to group by message ID

        strip_replies : typing.Optional[bool]
            Whether to strip reply content

        enabled : typing.Optional[bool]
            Whether the route is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedRoute
            Route created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.routes.create_route(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                name="Support Route",
                url="https://example.com/webhook",
                recipient="support@example.com",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_route(
            account_id,
            name=name,
            url=url,
            recipient=recipient,
            idempotency_key=idempotency_key,
            attachments=attachments,
            headers=headers,
            group_by_message_id=group_by_message_id,
            strip_replies=strip_replies,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_route(
        self, account_id: str, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Route:
        """
        Returns a specific route by ID. Access requires the global read role or
        a read role matching the route's recipient domain.

        Parameters
        ----------
        account_id : str
            Account ID

        route_id : str
            Route ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Route
            Route details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.routes.get_route(
                account_id="account_id",
                route_id="route_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_route(account_id, route_id, request_options=request_options)
        return _response.data

    async def update_route(
        self,
        account_id: str,
        route_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        recipient: typing.Optional[str] = OMIT,
        attachments: typing.Optional[bool] = OMIT,
        headers: typing.Optional[bool] = OMIT,
        group_by_message_id: typing.Optional[bool] = OMIT,
        strip_replies: typing.Optional[bool] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Route:
        """
        Updates an existing route. A domain-scoped key must authorize the
        existing recipient domain and, when `recipient` changes, the new domain;
        `routes:write:all` satisfies both checks.

        Parameters
        ----------
        account_id : str
            Account ID

        route_id : str
            Route ID

        name : typing.Optional[str]
            Route name

        url : typing.Optional[str]
            Webhook URL for the route

        recipient : typing.Optional[str]
            Recipient filter

        attachments : typing.Optional[bool]
            Whether to include attachments in webhooks

        headers : typing.Optional[bool]
            Whether to include headers in webhooks

        group_by_message_id : typing.Optional[bool]
            Whether to group by message ID

        strip_replies : typing.Optional[bool]
            Whether to strip reply content

        enabled : typing.Optional[bool]
            Whether the route is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Route
            Route updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.routes.update_route(
                account_id="account_id",
                route_id="route_id",
                name="Updated Support Route",
                enabled=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_route(
            account_id,
            route_id,
            name=name,
            url=url,
            recipient=recipient,
            attachments=attachments,
            headers=headers,
            group_by_message_id=group_by_message_id,
            strip_replies=strip_replies,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def delete_route(
        self, account_id: str, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes a route. Access requires the global delete role or a delete role
        matching the route's recipient domain.

        Parameters
        ----------
        account_id : str
            Account ID

        route_id : str
            Route ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Route deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.routes.delete_route(
                account_id="account_id",
                route_id="route_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_route(account_id, route_id, request_options=request_options)
        return _response.data
