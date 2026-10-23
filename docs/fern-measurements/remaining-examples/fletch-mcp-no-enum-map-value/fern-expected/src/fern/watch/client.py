

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWatchClient, RawWatchClient
from .types.delete_watchers_id_response import DeleteWatchersIdResponse
from .types.delete_webhooks_id_response import DeleteWebhooksIdResponse
from .types.get_watchers_id_response import GetWatchersIdResponse
from .types.get_watchers_id_runs_response import GetWatchersIdRunsResponse
from .types.get_watchers_response import GetWatchersResponse
from .types.get_webhooks_response import GetWebhooksResponse
from .types.patch_watchers_id_response import PatchWatchersIdResponse
from .types.patch_webhooks_id_response import PatchWebhooksIdResponse
from .types.post_watchers_request_kind import PostWatchersRequestKind
from .types.post_watchers_response import PostWatchersResponse
from .types.post_webhooks_id_test_response import PostWebhooksIdTestResponse
from .types.post_webhooks_response import PostWebhooksResponse


OMIT = typing.cast(typing.Any, ...)


class WatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWatchClient
        """
        return self._raw_client

    def list_this_accounts_watchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatchersResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatchersResponse
            Watchers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.list_this_accounts_watchers()
        """
        _response = self._raw_client.list_this_accounts_watchers(request_options=request_options)
        return _response.data

    def create_a_watcher(
        self,
        *,
        idempotency_key: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = OMIT,
        threshold: typing.Optional[str] = OMIT,
        kind: typing.Optional[PostWatchersRequestKind] = OMIT,
        lookalikes_only: typing.Optional[bool] = OMIT,
        wallet: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        webhook_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWatchersResponse:
        """
        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            Repeat a POST with the same key to get the same watcher back instead of creating another.

        asset_id : typing.Optional[str]
            Required for large_transfer, wallet_activity and token_event; omitted for registry_event.

        threshold : typing.Optional[str]
            Required for large_transfer (positive) and wallet_activity ("0" means every transfer); ignored by registry_event, token_event and new_pool.

        kind : typing.Optional[PostWatchersRequestKind]

        lookalikes_only : typing.Optional[bool]
            new_pool only: alert only on a pool whose token borrows a listed ticker or name. Off by default.

        wallet : typing.Optional[str]
            Required when kind is wallet_activity — a 0x-prefixed 40-character hex address.

        name : typing.Optional[str]

        project_id : typing.Optional[str]

        webhook_id : typing.Optional[str]
            Deliver this watcher to a registered webhook endpoint instead of Telegram.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWatchersResponse
            Idempotency-Key replay: the existing watcher

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.create_a_watcher()
        """
        _response = self._raw_client.create_a_watcher(
            idempotency_key=idempotency_key,
            asset_id=asset_id,
            threshold=threshold,
            kind=kind,
            lookalikes_only=lookalikes_only,
            wallet=wallet,
            name=name,
            project_id=project_id,
            webhook_id=webhook_id,
            request_options=request_options,
        )
        return _response.data

    def get_one_watcher(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatchersIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatchersIdResponse
            The watcher

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.get_one_watcher(
            id="id",
        )
        """
        _response = self._raw_client.get_one_watcher(id, request_options=request_options)
        return _response.data

    def delete_a_watcher(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWatchersIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWatchersIdResponse
            Deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.delete_a_watcher(
            id="id",
        )
        """
        _response = self._raw_client.delete_a_watcher(id, request_options=request_options)
        return _response.data

    def pause_resume_or_re_point_a_watcher(
        self,
        id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        webhook_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchWatchersIdResponse:
        """
        Parameters
        ----------
        id : str

        enabled : typing.Optional[bool]

        webhook_id : typing.Optional[str]
            Re-point this watcher: an endpoint id delivers there, null goes back to Telegram. The endpoint must be yours and enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWatchersIdResponse
            Updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.pause_resume_or_re_point_a_watcher(
            id="id",
        )
        """
        _response = self._raw_client.pause_resume_or_re_point_a_watcher(
            id, enabled=enabled, webhook_id=webhook_id, request_options=request_options
        )
        return _response.data

    def a_watchers_delivery_history(
        self, id: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatchersIdRunsResponse:
        """
        Parameters
        ----------
        id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatchersIdRunsResponse
            Deliveries, newest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.a_watchers_delivery_history(
            id="id",
        )
        """
        _response = self._raw_client.a_watchers_delivery_history(id, limit=limit, request_options=request_options)
        return _response.data

    def list_this_accounts_webhook_endpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhooksResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Endpoints, oldest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.list_this_accounts_webhook_endpoints()
        """
        _response = self._raw_client.list_this_accounts_webhook_endpoints(request_options=request_options)
        return _response.data

    def register_a_webhook_endpoint(
        self, *, url: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PostWebhooksResponse:
        """
        Returns the signing secret once. Every delivery carries X-Fletch-Signature: t=<unix>,v1=<hex hmac-sha256 over "<t>.<body>"> and X-Fletch-Event.

        Parameters
        ----------
        url : str
            An https:// URL on a public host.

        name : typing.Optional[str]
            Defaults to the URL's host.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWebhooksResponse
            Created, with the secret shown once

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.register_a_webhook_endpoint(
            url="https://example.com/fletch",
        )
        """
        _response = self._raw_client.register_a_webhook_endpoint(url=url, name=name, request_options=request_options)
        return _response.data

    def delete_an_endpoint(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhooksIdResponse:
        """
        Watchers delivering to it are paused; the response says how many.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhooksIdResponse
            Deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.delete_an_endpoint(
            id="id",
        )
        """
        _response = self._raw_client.delete_an_endpoint(id, request_options=request_options)
        return _response.data

    def enable_disable_or_rotate_the_secret_of_an_endpoint(
        self,
        id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        rotate_secret: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchWebhooksIdResponse:
        """
        Parameters
        ----------
        id : str

        enabled : typing.Optional[bool]

        rotate_secret : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWebhooksIdResponse
            The endpoint; a rotation includes the new secret once

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.enable_disable_or_rotate_the_secret_of_an_endpoint(
            id="id",
        )
        """
        _response = self._raw_client.enable_disable_or_rotate_the_secret_of_an_endpoint(
            id, enabled=enabled, rotate_secret=rotate_secret, request_options=request_options
        )
        return _response.data

    def send_a_signed_ping_to_an_endpoint_now(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostWebhooksIdTestResponse:
        """
        Always HTTP 200: the endpoint's own answer is in the body as ok, status and error. Sent directly rather than through the delivery outbox, so a failure is not retried.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWebhooksIdTestResponse
            What the endpoint answered

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watch.send_a_signed_ping_to_an_endpoint_now(
            id="id",
        )
        """
        _response = self._raw_client.send_a_signed_ping_to_an_endpoint_now(id, request_options=request_options)
        return _response.data


class AsyncWatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWatchClient
        """
        return self._raw_client

    async def list_this_accounts_watchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatchersResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatchersResponse
            Watchers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.list_this_accounts_watchers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_this_accounts_watchers(request_options=request_options)
        return _response.data

    async def create_a_watcher(
        self,
        *,
        idempotency_key: typing.Optional[str] = None,
        asset_id: typing.Optional[str] = OMIT,
        threshold: typing.Optional[str] = OMIT,
        kind: typing.Optional[PostWatchersRequestKind] = OMIT,
        lookalikes_only: typing.Optional[bool] = OMIT,
        wallet: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        webhook_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWatchersResponse:
        """
        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            Repeat a POST with the same key to get the same watcher back instead of creating another.

        asset_id : typing.Optional[str]
            Required for large_transfer, wallet_activity and token_event; omitted for registry_event.

        threshold : typing.Optional[str]
            Required for large_transfer (positive) and wallet_activity ("0" means every transfer); ignored by registry_event, token_event and new_pool.

        kind : typing.Optional[PostWatchersRequestKind]

        lookalikes_only : typing.Optional[bool]
            new_pool only: alert only on a pool whose token borrows a listed ticker or name. Off by default.

        wallet : typing.Optional[str]
            Required when kind is wallet_activity — a 0x-prefixed 40-character hex address.

        name : typing.Optional[str]

        project_id : typing.Optional[str]

        webhook_id : typing.Optional[str]
            Deliver this watcher to a registered webhook endpoint instead of Telegram.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWatchersResponse
            Idempotency-Key replay: the existing watcher

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.create_a_watcher()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_watcher(
            idempotency_key=idempotency_key,
            asset_id=asset_id,
            threshold=threshold,
            kind=kind,
            lookalikes_only=lookalikes_only,
            wallet=wallet,
            name=name,
            project_id=project_id,
            webhook_id=webhook_id,
            request_options=request_options,
        )
        return _response.data

    async def get_one_watcher(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatchersIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatchersIdResponse
            The watcher

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.get_one_watcher(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_one_watcher(id, request_options=request_options)
        return _response.data

    async def delete_a_watcher(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWatchersIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWatchersIdResponse
            Deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.delete_a_watcher(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_watcher(id, request_options=request_options)
        return _response.data

    async def pause_resume_or_re_point_a_watcher(
        self,
        id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        webhook_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchWatchersIdResponse:
        """
        Parameters
        ----------
        id : str

        enabled : typing.Optional[bool]

        webhook_id : typing.Optional[str]
            Re-point this watcher: an endpoint id delivers there, null goes back to Telegram. The endpoint must be yours and enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWatchersIdResponse
            Updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.pause_resume_or_re_point_a_watcher(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pause_resume_or_re_point_a_watcher(
            id, enabled=enabled, webhook_id=webhook_id, request_options=request_options
        )
        return _response.data

    async def a_watchers_delivery_history(
        self, id: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatchersIdRunsResponse:
        """
        Parameters
        ----------
        id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatchersIdRunsResponse
            Deliveries, newest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.a_watchers_delivery_history(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.a_watchers_delivery_history(id, limit=limit, request_options=request_options)
        return _response.data

    async def list_this_accounts_webhook_endpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhooksResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Endpoints, oldest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.list_this_accounts_webhook_endpoints()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_this_accounts_webhook_endpoints(request_options=request_options)
        return _response.data

    async def register_a_webhook_endpoint(
        self, *, url: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PostWebhooksResponse:
        """
        Returns the signing secret once. Every delivery carries X-Fletch-Signature: t=<unix>,v1=<hex hmac-sha256 over "<t>.<body>"> and X-Fletch-Event.

        Parameters
        ----------
        url : str
            An https:// URL on a public host.

        name : typing.Optional[str]
            Defaults to the URL's host.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWebhooksResponse
            Created, with the secret shown once

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.register_a_webhook_endpoint(
                url="https://example.com/fletch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_webhook_endpoint(
            url=url, name=name, request_options=request_options
        )
        return _response.data

    async def delete_an_endpoint(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhooksIdResponse:
        """
        Watchers delivering to it are paused; the response says how many.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhooksIdResponse
            Deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.delete_an_endpoint(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_an_endpoint(id, request_options=request_options)
        return _response.data

    async def enable_disable_or_rotate_the_secret_of_an_endpoint(
        self,
        id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        rotate_secret: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchWebhooksIdResponse:
        """
        Parameters
        ----------
        id : str

        enabled : typing.Optional[bool]

        rotate_secret : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWebhooksIdResponse
            The endpoint; a rotation includes the new secret once

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.enable_disable_or_rotate_the_secret_of_an_endpoint(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_disable_or_rotate_the_secret_of_an_endpoint(
            id, enabled=enabled, rotate_secret=rotate_secret, request_options=request_options
        )
        return _response.data

    async def send_a_signed_ping_to_an_endpoint_now(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostWebhooksIdTestResponse:
        """
        Always HTTP 200: the endpoint's own answer is in the body as ok, status and error. Sent directly rather than through the delivery outbox, so a failure is not retried.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWebhooksIdTestResponse
            What the endpoint answered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watch.send_a_signed_ping_to_an_endpoint_now(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_a_signed_ping_to_an_endpoint_now(id, request_options=request_options)
        return _response.data
