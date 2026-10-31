

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.commit import Commit
from ..types.commit_id import CommitId
from ..types.commit_precondition import CommitPrecondition
from ..types.content_token import ContentToken
from ..types.filesystem_operation import FilesystemOperation
from .raw_client import AsyncRawCommitsClient, RawCommitsClient


OMIT = typing.cast(typing.Any, ...)


class CommitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCommitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCommitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCommitsClient
        """
        return self._raw_client

    def create(
        self,
        namespace_id: str,
        *,
        commit_id: CommitId,
        operations: typing.Sequence[FilesystemOperation],
        content_tokens: typing.Optional[typing.Sequence[ContentToken]] = OMIT,
        message: typing.Optional[str] = OMIT,
        preconditions: typing.Optional[typing.Sequence[CommitPrecondition]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Commit:
        """
        Applies one commit, which is an ordered, non-empty list of path operations that are committed together. The commit ID makes retries idempotent. The server checks the request's preconditions against the state before the commit, after it resolves any commit receipt and before it runs the operations. A failed precondition's position is reported in `details.precondition_index`. A request can contain a single operation. If an operation fails, the whole request fails, and for a request with more than one operation, `details.operation_index` reports the failed operation's position.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        commit_id : CommitId
            The caller's idempotency key for the whole request.

        operations : typing.Sequence[FilesystemOperation]
            The operations to commit atomically, in order. The list can't be empty.

        content_tokens : typing.Optional[typing.Sequence[ContentToken]]
            One content token for each uploaded `content_ref` that the request uses.

        message : typing.Optional[str]
            An annotation from the caller. The message is part of the commit's identity.

        preconditions : typing.Optional[typing.Sequence[CommitPrecondition]]
            The conditions that the server checks, in order, before it runs any operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Commit
            Commit applied

        Examples
        --------
        from fern import FernApi, FilesystemOperation_AppendFile

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.commits.create(
            namespace_id="namespace_id",
            commit_id="c_7kn71d9dq885x91hejz3gvf9p0",
            operations=[
                FilesystemOperation_AppendFile(
                    inline_content="inline_content",
                    path="/docs/report.txt",
                )
            ],
        )
        """
        _response = self._raw_client.create(
            namespace_id,
            commit_id=commit_id,
            operations=operations,
            content_tokens=content_tokens,
            message=message,
            preconditions=preconditions,
            request_options=request_options,
        )
        return _response.data


class AsyncCommitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCommitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCommitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCommitsClient
        """
        return self._raw_client

    async def create(
        self,
        namespace_id: str,
        *,
        commit_id: CommitId,
        operations: typing.Sequence[FilesystemOperation],
        content_tokens: typing.Optional[typing.Sequence[ContentToken]] = OMIT,
        message: typing.Optional[str] = OMIT,
        preconditions: typing.Optional[typing.Sequence[CommitPrecondition]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Commit:
        """
        Applies one commit, which is an ordered, non-empty list of path operations that are committed together. The commit ID makes retries idempotent. The server checks the request's preconditions against the state before the commit, after it resolves any commit receipt and before it runs the operations. A failed precondition's position is reported in `details.precondition_index`. A request can contain a single operation. If an operation fails, the whole request fails, and for a request with more than one operation, `details.operation_index` reports the failed operation's position.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        commit_id : CommitId
            The caller's idempotency key for the whole request.

        operations : typing.Sequence[FilesystemOperation]
            The operations to commit atomically, in order. The list can't be empty.

        content_tokens : typing.Optional[typing.Sequence[ContentToken]]
            One content token for each uploaded `content_ref` that the request uses.

        message : typing.Optional[str]
            An annotation from the caller. The message is part of the commit's identity.

        preconditions : typing.Optional[typing.Sequence[CommitPrecondition]]
            The conditions that the server checks, in order, before it runs any operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Commit
            Commit applied

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FilesystemOperation_AppendFile

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.commits.create(
                namespace_id="namespace_id",
                commit_id="c_7kn71d9dq885x91hejz3gvf9p0",
                operations=[
                    FilesystemOperation_AppendFile(
                        inline_content="inline_content",
                        path="/docs/report.txt",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            namespace_id,
            commit_id=commit_id,
            operations=operations,
            content_tokens=content_tokens,
            message=message,
            preconditions=preconditions,
            request_options=request_options,
        )
        return _response.data
