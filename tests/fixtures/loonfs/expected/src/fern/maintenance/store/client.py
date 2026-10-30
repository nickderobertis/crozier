

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.store_probe_request import StoreProbeRequest
from ...types.store_probe_response import StoreProbeResponse
from .raw_client import AsyncRawStoreClient, RawStoreClient


OMIT = typing.cast(typing.Any, ...)


class StoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStoreClient
        """
        return self._raw_client

    def probe(
        self, *, request: StoreProbeRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> StoreProbeResponse:
        """
        Checks that the configured object store supports the create-if-absent, compare-and-swap, visibility, listing, and ranged-read behavior that LoonFS depends on, and reports the result of each check. The probe runs only when a client calls this route, because it writes and deletes objects. It writes them all under a scratch prefix that isn't a durable object family, and its last check deletes them and confirms that the prefix is empty. If the store fails a check, the response is still 200, and it reports that check as `failed`. If the store declares that it doesn't support an optional capability, the response reports that check as `unsupported`, which isn't a failure. The probe doesn't control whether the deployment can serve presigned direct uploads. The endpoint allowlist controls that, because the probe tests only the server's own requests and never a presigned capability issued to a client.

        Parameters
        ----------
        request : StoreProbeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoreProbeResponse
            The probe completed, and the body reports each check's outcome

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.maintenance.store.probe(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.probe(request=request, request_options=request_options)
        return _response.data


class AsyncStoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStoreClient
        """
        return self._raw_client

    async def probe(
        self, *, request: StoreProbeRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> StoreProbeResponse:
        """
        Checks that the configured object store supports the create-if-absent, compare-and-swap, visibility, listing, and ranged-read behavior that LoonFS depends on, and reports the result of each check. The probe runs only when a client calls this route, because it writes and deletes objects. It writes them all under a scratch prefix that isn't a durable object family, and its last check deletes them and confirms that the prefix is empty. If the store fails a check, the response is still 200, and it reports that check as `failed`. If the store declares that it doesn't support an optional capability, the response reports that check as `unsupported`, which isn't a failure. The probe doesn't control whether the deployment can serve presigned direct uploads. The endpoint allowlist controls that, because the probe tests only the server's own requests and never a presigned capability issued to a client.

        Parameters
        ----------
        request : StoreProbeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoreProbeResponse
            The probe completed, and the body reports each check's outcome

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.maintenance.store.probe(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.probe(request=request, request_options=request_options)
        return _response.data
