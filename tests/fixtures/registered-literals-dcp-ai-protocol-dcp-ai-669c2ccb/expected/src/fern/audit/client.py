

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuditClient, RawAuditClient
from .types.append_audit_response import AppendAuditResponse
from .types.compact_audit_request_compaction import CompactAuditRequestCompaction
from .types.compact_audit_response import CompactAuditResponse


OMIT = typing.cast(typing.Any, ...)


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

    def append_audit(
        self,
        *,
        audit_event: typing.Dict[str, typing.Any],
        signature: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppendAuditResponse:
        """
        Appends a signed audit event to the agent's audit chain, verifying prev_hash continuity.

        Parameters
        ----------
        audit_event : typing.Dict[str, typing.Any]

        signature : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppendAuditResponse
            Audit event appended

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.audit.append_audit(
            audit_event={"key": "value"},
        )
        """
        _response = self._raw_client.append_audit(
            audit_event=audit_event, signature=signature, request_options=request_options
        )
        return _response.data

    def compact_audit(
        self, *, compaction: CompactAuditRequestCompaction, request_options: typing.Optional[RequestOptions] = None
    ) -> CompactAuditResponse:
        """
        Submits an audit compaction with a Merkle root covering a range of events.

        Parameters
        ----------
        compaction : CompactAuditRequestCompaction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompactAuditResponse
            Compaction accepted

        Examples
        --------
        from fern.audit import (
            CompactAuditRequestCompaction,
            CompactAuditRequestCompactionType,
        )

        from fern import CompositeSignature, FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.audit.compact_audit(
            compaction=CompactAuditRequestCompaction(
                type=CompactAuditRequestCompactionType.AUDIT_COMPACTION,
                session_nonce="session_nonce",
                range={"key": "value"},
                merkle_root="merkle_root",
                composite_sig=CompositeSignature(),
            ),
        )
        """
        _response = self._raw_client.compact_audit(compaction=compaction, request_options=request_options)
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

    async def append_audit(
        self,
        *,
        audit_event: typing.Dict[str, typing.Any],
        signature: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppendAuditResponse:
        """
        Appends a signed audit event to the agent's audit chain, verifying prev_hash continuity.

        Parameters
        ----------
        audit_event : typing.Dict[str, typing.Any]

        signature : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppendAuditResponse
            Audit event appended

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audit.append_audit(
                audit_event={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.append_audit(
            audit_event=audit_event, signature=signature, request_options=request_options
        )
        return _response.data

    async def compact_audit(
        self, *, compaction: CompactAuditRequestCompaction, request_options: typing.Optional[RequestOptions] = None
    ) -> CompactAuditResponse:
        """
        Submits an audit compaction with a Merkle root covering a range of events.

        Parameters
        ----------
        compaction : CompactAuditRequestCompaction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompactAuditResponse
            Compaction accepted

        Examples
        --------
        import asyncio

        from fern.audit import (
            CompactAuditRequestCompaction,
            CompactAuditRequestCompactionType,
        )

        from fern import AsyncFernApi, CompositeSignature

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audit.compact_audit(
                compaction=CompactAuditRequestCompaction(
                    type=CompactAuditRequestCompactionType.AUDIT_COMPACTION,
                    session_nonce="session_nonce",
                    range={"key": "value"},
                    merkle_root="merkle_root",
                    composite_sig=CompositeSignature(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compact_audit(compaction=compaction, request_options=request_options)
        return _response.data
