

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.audit_entry import AuditEntry
from .raw_client import AsyncRawTrailClient, RawTrailClient


class TrailClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrailClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrailClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrailClient
        """
        return self._raw_client

    def export(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[AuditEntry]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AuditEntry]
            The audit trail.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client._audit._trail.export()
        """
        _response = self._raw_client.export(request_options=request_options)
        return _response.data


class AsyncTrailClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrailClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrailClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrailClient
        """
        return self._raw_client

    async def export(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[AuditEntry]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AuditEntry]
            The audit trail.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client._audit._trail.export()


        asyncio.run(main())
        """
        _response = await self._raw_client.export(request_options=request_options)
        return _response.data
