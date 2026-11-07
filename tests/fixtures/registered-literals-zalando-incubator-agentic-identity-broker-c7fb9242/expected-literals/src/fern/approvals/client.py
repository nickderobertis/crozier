

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.approval_detail_response import ApprovalDetailResponse
from ..types.approval_sync_response import ApprovalSyncResponse
from ..types.approve_response import ApproveResponse
from ..types.consume_response import ConsumeResponse
from ..types.create_approval_response import CreateApprovalResponse
from ..types.deny_response import DenyResponse
from ..types.scope_preview_response import ScopePreviewResponse
from .raw_client import AsyncRawApprovalsClient, RawApprovalsClient
from .types.approve_request_persistence import ApproveRequestPersistence
from .types.create_approval_request_metadata import CreateApprovalRequestMetadata
from .types.create_approval_request_risk_level import CreateApprovalRequestRiskLevel
from .types.deny_request_persistence import DenyRequestPersistence
from .types.list_pending_approvals_response import ListPendingApprovalsResponse
from .types.list_permanent_approvals_response import ListPermanentApprovalsResponse


OMIT = typing.cast(typing.Any, ...)


class ApprovalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApprovalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApprovalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApprovalsClient
        """
        return self._raw_client

    def sync_approvals(
        self,
        *,
        principal: typing.Optional[str] = None,
        agent_session_id: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        long_poll_timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApprovalSyncResponse:
        """
        Returns all active approvals grouped by (principal, agent) pair.
        Supports long-poll via If-None-Match + X-Long-Poll-Timeout headers.
        Auth: client assertion only (CEL-validated). No subject token is required because this is a gateway control-plane sync channel rather than a user-facing operation.

        Parameters
        ----------
        principal : typing.Optional[str]

        agent_session_id : typing.Optional[str]
            Repeat for each active agent session. Session-scoped approvals are returned only for matching IDs.

        if_none_match : typing.Optional[str]

        long_poll_timeout : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApprovalSyncResponse
            Current approval state with ETag

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.sync_approvals()
        """
        _response = self._raw_client.sync_approvals(
            principal=principal,
            agent_session_id=agent_session_id,
            if_none_match=if_none_match,
            long_poll_timeout=long_poll_timeout,
            request_options=request_options,
        )
        return _response.data

    def create_approval(
        self,
        *,
        metadata: CreateApprovalRequestMetadata,
        tool_name: str,
        arguments: typing.Dict[str, typing.Any],
        traceparent: typing.Optional[str] = None,
        risk_level: typing.Optional[CreateApprovalRequestRiskLevel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApprovalResponse:
        """
        Creates a pending approval record for a tool invocation that requires human-in-the-loop authorization.
        Called by ExtProc when a tool call is intercepted that requires approval.
        Dual-auth required: subject token + client assertion. The subject token binds the request to user/agent context, while the client assertion proves the trusted gateway caller that is allowed to mint approval prompts.
        Idempotent: returns existing record for duplicate pending requests.

        Parameters
        ----------
        metadata : CreateApprovalRequestMetadata

        tool_name : str

        arguments : typing.Dict[str, typing.Any]

        traceparent : typing.Optional[str]
            W3C Trace Context propagation header.

        risk_level : typing.Optional[CreateApprovalRequestRiskLevel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateApprovalResponse
            Existing pending approval returned (idempotent)

        Examples
        --------
        from fern.approvals import CreateApprovalRequestMetadata

        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.create_approval(
            metadata=CreateApprovalRequestMetadata(
                description="description",
            ),
            tool_name="tool_name",
            arguments={"key": "value"},
        )
        """
        _response = self._raw_client.create_approval(
            metadata=metadata,
            tool_name=tool_name,
            arguments=arguments,
            traceparent=traceparent,
            risk_level=risk_level,
            request_options=request_options,
        )
        return _response.data

    def list_pending_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPendingApprovalsResponse:
        """
        Returns all pending approvals for the authenticated user.
        Used by the approval and tool authorization UIs.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPendingApprovalsResponse
            List of pending approvals

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.list_pending_approvals()
        """
        _response = self._raw_client.list_pending_approvals(request_options=request_options)
        return _response.data

    def list_permanent_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPermanentApprovalsResponse:
        """
        Returns all permanent approvals and denials for the authenticated user.
        Used by the consent management UI.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPermanentApprovalsResponse
            List of permanent approvals

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.list_permanent_approvals()
        """
        _response = self._raw_client.list_permanent_approvals(request_options=request_options)
        return _response.data

    def get_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApprovalDetailResponse:
        """
        Retrieves a tool approval record by ID for the Approval UI.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApprovalDetailResponse
            Approval record

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.get_approval(
            id="id",
        )
        """
        _response = self._raw_client.get_approval(id, request_options=request_options)
        return _response.data

    def approve_approval(
        self,
        id: str,
        *,
        persistence: ApproveRequestPersistence,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApproveResponse:
        """
        Transitions a pending approval to approved state with selected persistence scope.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : ApproveRequestPersistence

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field to cover only the reviewed argument values. This field is permitted only for session or permanent persistence. With once persistence, every supplied value, including an empty object, returns 422 invalid_pattern. The resulting pattern must cover the reviewed arguments.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApproveResponse
            Approval accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.approve_approval(
            id="id",
            persistence="once",
        )
        """
        _response = self._raw_client.approve_approval(
            id, persistence=persistence, params_pattern=params_pattern, request_options=request_options
        )
        return _response.data

    def preview_approval_scope(
        self,
        id: str,
        *,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScopePreviewResponse:
        """
        Parameters
        ----------
        id : str

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field entirely to cover only the reviewed argument values; send an empty object to leave every argument unconstrained.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScopePreviewResponse
            Resolved approval scope

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.preview_approval_scope(
            id="id",
        )
        """
        _response = self._raw_client.preview_approval_scope(
            id, params_pattern=params_pattern, request_options=request_options
        )
        return _response.data

    def deny_approval(
        self,
        id: str,
        *,
        persistence: typing.Optional[DenyRequestPersistence] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DenyResponse:
        """
        Transitions a pending approval to denied state.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : typing.Optional[DenyRequestPersistence]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DenyResponse
            Denial recorded

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.deny_approval(
            id="id",
        )
        """
        _response = self._raw_client.deny_approval(id, persistence=persistence, request_options=request_options)
        return _response.data

    def consume_approval(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ConsumeResponse:
        """
        Marks an approved once-persistence approval as consumed.
        Auth: subject token only (Bearer); principal must match.
        Idempotent: consuming already-consumed returns 200.
        No client assertion is required because this is a per-approval, principal-scoped machine mutation.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsumeResponse
            Approval consumed (or already consumed)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.consume_approval(
            id="id",
        )
        """
        _response = self._raw_client.consume_approval(id, request_options=request_options)
        return _response.data

    def revoke_permanent_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DenyResponse:
        """
        Revokes a permanent approval or denial.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DenyResponse
            Permanent approval revoked

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.approvals.revoke_permanent_approval(
            id="id",
        )
        """
        _response = self._raw_client.revoke_permanent_approval(id, request_options=request_options)
        return _response.data


class AsyncApprovalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApprovalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApprovalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApprovalsClient
        """
        return self._raw_client

    async def sync_approvals(
        self,
        *,
        principal: typing.Optional[str] = None,
        agent_session_id: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        long_poll_timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApprovalSyncResponse:
        """
        Returns all active approvals grouped by (principal, agent) pair.
        Supports long-poll via If-None-Match + X-Long-Poll-Timeout headers.
        Auth: client assertion only (CEL-validated). No subject token is required because this is a gateway control-plane sync channel rather than a user-facing operation.

        Parameters
        ----------
        principal : typing.Optional[str]

        agent_session_id : typing.Optional[str]
            Repeat for each active agent session. Session-scoped approvals are returned only for matching IDs.

        if_none_match : typing.Optional[str]

        long_poll_timeout : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApprovalSyncResponse
            Current approval state with ETag

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.sync_approvals()


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_approvals(
            principal=principal,
            agent_session_id=agent_session_id,
            if_none_match=if_none_match,
            long_poll_timeout=long_poll_timeout,
            request_options=request_options,
        )
        return _response.data

    async def create_approval(
        self,
        *,
        metadata: CreateApprovalRequestMetadata,
        tool_name: str,
        arguments: typing.Dict[str, typing.Any],
        traceparent: typing.Optional[str] = None,
        risk_level: typing.Optional[CreateApprovalRequestRiskLevel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApprovalResponse:
        """
        Creates a pending approval record for a tool invocation that requires human-in-the-loop authorization.
        Called by ExtProc when a tool call is intercepted that requires approval.
        Dual-auth required: subject token + client assertion. The subject token binds the request to user/agent context, while the client assertion proves the trusted gateway caller that is allowed to mint approval prompts.
        Idempotent: returns existing record for duplicate pending requests.

        Parameters
        ----------
        metadata : CreateApprovalRequestMetadata

        tool_name : str

        arguments : typing.Dict[str, typing.Any]

        traceparent : typing.Optional[str]
            W3C Trace Context propagation header.

        risk_level : typing.Optional[CreateApprovalRequestRiskLevel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateApprovalResponse
            Existing pending approval returned (idempotent)

        Examples
        --------
        import asyncio

        from fern.approvals import CreateApprovalRequestMetadata

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.create_approval(
                metadata=CreateApprovalRequestMetadata(
                    description="description",
                ),
                tool_name="tool_name",
                arguments={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_approval(
            metadata=metadata,
            tool_name=tool_name,
            arguments=arguments,
            traceparent=traceparent,
            risk_level=risk_level,
            request_options=request_options,
        )
        return _response.data

    async def list_pending_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPendingApprovalsResponse:
        """
        Returns all pending approvals for the authenticated user.
        Used by the approval and tool authorization UIs.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPendingApprovalsResponse
            List of pending approvals

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.list_pending_approvals()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_pending_approvals(request_options=request_options)
        return _response.data

    async def list_permanent_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPermanentApprovalsResponse:
        """
        Returns all permanent approvals and denials for the authenticated user.
        Used by the consent management UI.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPermanentApprovalsResponse
            List of permanent approvals

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.list_permanent_approvals()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_permanent_approvals(request_options=request_options)
        return _response.data

    async def get_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApprovalDetailResponse:
        """
        Retrieves a tool approval record by ID for the Approval UI.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApprovalDetailResponse
            Approval record

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.get_approval(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_approval(id, request_options=request_options)
        return _response.data

    async def approve_approval(
        self,
        id: str,
        *,
        persistence: ApproveRequestPersistence,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApproveResponse:
        """
        Transitions a pending approval to approved state with selected persistence scope.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : ApproveRequestPersistence

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field to cover only the reviewed argument values. This field is permitted only for session or permanent persistence. With once persistence, every supplied value, including an empty object, returns 422 invalid_pattern. The resulting pattern must cover the reviewed arguments.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApproveResponse
            Approval accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.approve_approval(
                id="id",
                persistence="once",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approve_approval(
            id, persistence=persistence, params_pattern=params_pattern, request_options=request_options
        )
        return _response.data

    async def preview_approval_scope(
        self,
        id: str,
        *,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScopePreviewResponse:
        """
        Parameters
        ----------
        id : str

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field entirely to cover only the reviewed argument values; send an empty object to leave every argument unconstrained.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScopePreviewResponse
            Resolved approval scope

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.preview_approval_scope(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_approval_scope(
            id, params_pattern=params_pattern, request_options=request_options
        )
        return _response.data

    async def deny_approval(
        self,
        id: str,
        *,
        persistence: typing.Optional[DenyRequestPersistence] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DenyResponse:
        """
        Transitions a pending approval to denied state.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : typing.Optional[DenyRequestPersistence]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DenyResponse
            Denial recorded

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.deny_approval(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deny_approval(id, persistence=persistence, request_options=request_options)
        return _response.data

    async def consume_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsumeResponse:
        """
        Marks an approved once-persistence approval as consumed.
        Auth: subject token only (Bearer); principal must match.
        Idempotent: consuming already-consumed returns 200.
        No client assertion is required because this is a per-approval, principal-scoped machine mutation.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsumeResponse
            Approval consumed (or already consumed)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.consume_approval(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.consume_approval(id, request_options=request_options)
        return _response.data

    async def revoke_permanent_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DenyResponse:
        """
        Revokes a permanent approval or denial.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DenyResponse
            Permanent approval revoked

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approvals.revoke_permanent_approval(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_permanent_approval(id, request_options=request_options)
        return _response.data
