

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.namespace_diagnostics import NamespaceDiagnostics
from .raw_client import AsyncRawDiagnosticsClient, RawDiagnosticsClient


class DiagnosticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDiagnosticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDiagnosticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDiagnosticsClient
        """
        return self._raw_client

    def retrieve(
        self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamespaceDiagnostics:
        """
        Returns namespace state together with the current manifest and visible WAL tail.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceDiagnostics
            Namespace diagnostics

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
        client.maintenance.diagnostics.retrieve(
            namespace_id="namespace_id",
        )
        """
        _response = self._raw_client.retrieve(namespace_id, request_options=request_options)
        return _response.data


class AsyncDiagnosticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDiagnosticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDiagnosticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDiagnosticsClient
        """
        return self._raw_client

    async def retrieve(
        self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamespaceDiagnostics:
        """
        Returns namespace state together with the current manifest and visible WAL tail.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceDiagnostics
            Namespace diagnostics

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
            await client.maintenance.diagnostics.retrieve(
                namespace_id="namespace_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(namespace_id, request_options=request_options)
        return _response.data
