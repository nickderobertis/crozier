

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuditlogClient, RawAuditlogClient
from .types.audit_log_fetch_by_cursor_response import AuditLogFetchByCursorResponse


class AuditlogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuditlogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuditlogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuditlogClient
        """
        return self._raw_client

    def fetchbycursor(
        self,
        *,
        workspace_id: str,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuditLogFetchByCursorResponse:
        """
        Fetch workspace audit log

        Parameters
        ----------
        workspace_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuditLogFetchByCursorResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auditlog.fetchbycursor(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.fetchbycursor(
            workspace_id=workspace_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def clear(self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        clear all workspace audit log

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auditlog.clear(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.clear(workspace_id=workspace_id, request_options=request_options)
        return _response.data


class AsyncAuditlogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuditlogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuditlogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuditlogClient
        """
        return self._raw_client

    async def fetchbycursor(
        self,
        *,
        workspace_id: str,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuditLogFetchByCursorResponse:
        """
        Fetch workspace audit log

        Parameters
        ----------
        workspace_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuditLogFetchByCursorResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auditlog.fetchbycursor(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetchbycursor(
            workspace_id=workspace_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def clear(self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        clear all workspace audit log

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auditlog.clear(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clear(workspace_id=workspace_id, request_options=request_options)
        return _response.data
