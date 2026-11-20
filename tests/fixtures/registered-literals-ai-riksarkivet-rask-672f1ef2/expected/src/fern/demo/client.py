

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.demo_datasets import DemoDatasets
from .raw_client import AsyncRawDemoClient, RawDemoClient


class DemoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDemoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDemoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDemoClient
        """
        return self._raw_client

    def demo_datasets(self, *, request_options: typing.Optional[RequestOptions] = None) -> DemoDatasets:
        """
        The medallion datasets as they currently exist on S3 — schema per Lance version + rows.

        GOVERNED (audit: this endpoint reads real medallion schemas/row-counts + gold's lineage JSONB from S3
        with the SERVICE root credentials, so it must not disclose a dataset the caller cannot see). Every
        other lineage read gates on ``can_get_metadata``; this does the same via the shared batch filter —
        ONE ``batch_check`` over the layout, not a per-dataset round-trip loop (F-LIN-13). The ladder is
        unchanged: 401 unauthenticated / 503 FGA unwired propagate; a denied dataset is dropped, not fatal.
        FGA off → pass-through (the dev demo).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DemoDatasets
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.demo.demo_datasets()
        """
        _response = self._raw_client.demo_datasets(request_options=request_options)
        return _response.data


class AsyncDemoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDemoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDemoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDemoClient
        """
        return self._raw_client

    async def demo_datasets(self, *, request_options: typing.Optional[RequestOptions] = None) -> DemoDatasets:
        """
        The medallion datasets as they currently exist on S3 — schema per Lance version + rows.

        GOVERNED (audit: this endpoint reads real medallion schemas/row-counts + gold's lineage JSONB from S3
        with the SERVICE root credentials, so it must not disclose a dataset the caller cannot see). Every
        other lineage read gates on ``can_get_metadata``; this does the same via the shared batch filter —
        ONE ``batch_check`` over the layout, not a per-dataset round-trip loop (F-LIN-13). The ladder is
        unchanged: 401 unauthenticated / 503 FGA unwired propagate; a denied dataset is dropped, not fatal.
        FGA off → pass-through (the dev demo).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DemoDatasets
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.demo.demo_datasets()


        asyncio.run(main())
        """
        _response = await self._raw_client.demo_datasets(request_options=request_options)
        return _response.data
