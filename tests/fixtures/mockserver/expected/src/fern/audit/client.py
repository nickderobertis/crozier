

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuditClient, RawAuditClient
from .types.get_mockserver_audit_response_item import GetMockserverAuditResponseItem


class AuditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuditClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuditClient
        """
        return self._raw_client

    def retrieve_the_control_plane_audit_log(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetMockserverAuditResponseItem]:
        """
        Returns the most-recent control-plane audit entries (one per authorised control-plane mutation, newest first). Off by default — enable with controlPlaneAuditEnabled. Each entry records redacted, structural metadata only (method, control-plane path with query string dropped, logical operation, source address, best-effort principal, outcome); it never contains request headers or bodies.

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent audit entries to return (default 200, capped at 1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetMockserverAuditResponseItem]
            audit entries returned (newest first)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.audit.retrieve_the_control_plane_audit_log()
        """
        _response = self._raw_client.retrieve_the_control_plane_audit_log(limit=limit, request_options=request_options)
        return _response.data


class AsyncAuditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuditClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuditClient
        """
        return self._raw_client

    async def retrieve_the_control_plane_audit_log(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetMockserverAuditResponseItem]:
        """
        Returns the most-recent control-plane audit entries (one per authorised control-plane mutation, newest first). Off by default — enable with controlPlaneAuditEnabled. Each entry records redacted, structural metadata only (method, control-plane path with query string dropped, logical operation, source address, best-effort principal, outcome); it never contains request headers or bodies.

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent audit entries to return (default 200, capped at 1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetMockserverAuditResponseItem]
            audit entries returned (newest first)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.audit.retrieve_the_control_plane_audit_log()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_control_plane_audit_log(
            limit=limit, request_options=request_options
        )
        return _response.data
