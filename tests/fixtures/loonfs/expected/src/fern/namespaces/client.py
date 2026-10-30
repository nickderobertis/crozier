

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.change_seq import ChangeSeq
from ..types.delete_namespace_response import DeleteNamespaceResponse
from ..types.namespace_access import NamespaceAccess
from ..types.namespace_id import NamespaceId
from ..types.namespace_metadata import NamespaceMetadata
from ..types.pin_id import PinId
from .raw_client import AsyncRawNamespacesClient, RawNamespacesClient


OMIT = typing.cast(typing.Any, ...)


class NamespacesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNamespacesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNamespacesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNamespacesClient
        """
        return self._raw_client

    def create(
        self,
        *,
        namespace_id: NamespaceId,
        access: typing.Optional[NamespaceAccess] = OMIT,
        retention_window_ms: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NamespaceMetadata:
        """
        Creates a new empty namespace.

        Parameters
        ----------
        namespace_id : NamespaceId
            The durable ID of the new namespace.

        access : typing.Optional[NamespaceAccess]
            The namespace's access mode, which can't be changed after the namespace is created. The
            default is unrestricted.

        retention_window_ms : typing.Optional[int]
            The namespace's retention window, in milliseconds, which must be positive. The reference
            server's maintenance sweep then uses this window for the namespace instead of the server's
            `retention_window_ms` setting. A `retention_window` maintenance run can change or clear the
            window later.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceMetadata
            Namespace created

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
        client.namespaces.create(
            namespace_id="demo",
        )
        """
        _response = self._raw_client.create(
            namespace_id=namespace_id,
            access=access,
            retention_window_ms=retention_window_ms,
            request_options=request_options,
        )
        return _response.data

    def retrieve(
        self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamespaceMetadata:
        """
        Returns the current head and retention state for a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceMetadata
            Namespace

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
        client.namespaces.retrieve(
            namespace_id="namespace_id",
        )
        """
        _response = self._raw_client.retrieve(namespace_id, request_options=request_options)
        return _response.data

    def delete(
        self,
        namespace_id: str,
        *,
        expected_head_seq: typing.Optional[ChangeSeq] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteNamespaceResponse:
        """
        Marks a namespace as deleted. The namespace ID can never be used again to create or fork a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        expected_head_seq : typing.Optional[ChangeSeq]
            The head sequence that the namespace must still have for the delete to succeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteNamespaceResponse
            Namespace deleted

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
        client.namespaces.delete(
            namespace_id="namespace_id",
        )
        """
        _response = self._raw_client.delete(
            namespace_id, expected_head_seq=expected_head_seq, request_options=request_options
        )
        return _response.data

    def fork(
        self,
        namespace_id: str,
        *,
        new_namespace_id: NamespaceId,
        snapshot_id: typing.Optional[PinId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NamespaceMetadata:
        """
        Creates a new namespace from the source namespace's current head or from an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The source namespace ID.

        new_namespace_id : NamespaceId
            The durable ID of the new namespace that the fork creates.

        snapshot_id : typing.Optional[PinId]
            An unexpired snapshot to fork from. Without it, the fork starts from the current head.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceMetadata
            Namespace forked

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
        client.namespaces.fork(
            namespace_id="namespace_id",
            new_namespace_id="demo",
        )
        """
        _response = self._raw_client.fork(
            namespace_id, new_namespace_id=new_namespace_id, snapshot_id=snapshot_id, request_options=request_options
        )
        return _response.data


class AsyncNamespacesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNamespacesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNamespacesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNamespacesClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        namespace_id: NamespaceId,
        access: typing.Optional[NamespaceAccess] = OMIT,
        retention_window_ms: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NamespaceMetadata:
        """
        Creates a new empty namespace.

        Parameters
        ----------
        namespace_id : NamespaceId
            The durable ID of the new namespace.

        access : typing.Optional[NamespaceAccess]
            The namespace's access mode, which can't be changed after the namespace is created. The
            default is unrestricted.

        retention_window_ms : typing.Optional[int]
            The namespace's retention window, in milliseconds, which must be positive. The reference
            server's maintenance sweep then uses this window for the namespace instead of the server's
            `retention_window_ms` setting. A `retention_window` maintenance run can change or clear the
            window later.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceMetadata
            Namespace created

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
            await client.namespaces.create(
                namespace_id="demo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            namespace_id=namespace_id,
            access=access,
            retention_window_ms=retention_window_ms,
            request_options=request_options,
        )
        return _response.data

    async def retrieve(
        self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamespaceMetadata:
        """
        Returns the current head and retention state for a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceMetadata
            Namespace

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
            await client.namespaces.retrieve(
                namespace_id="namespace_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(namespace_id, request_options=request_options)
        return _response.data

    async def delete(
        self,
        namespace_id: str,
        *,
        expected_head_seq: typing.Optional[ChangeSeq] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteNamespaceResponse:
        """
        Marks a namespace as deleted. The namespace ID can never be used again to create or fork a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        expected_head_seq : typing.Optional[ChangeSeq]
            The head sequence that the namespace must still have for the delete to succeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteNamespaceResponse
            Namespace deleted

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
            await client.namespaces.delete(
                namespace_id="namespace_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            namespace_id, expected_head_seq=expected_head_seq, request_options=request_options
        )
        return _response.data

    async def fork(
        self,
        namespace_id: str,
        *,
        new_namespace_id: NamespaceId,
        snapshot_id: typing.Optional[PinId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NamespaceMetadata:
        """
        Creates a new namespace from the source namespace's current head or from an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The source namespace ID.

        new_namespace_id : NamespaceId
            The durable ID of the new namespace that the fork creates.

        snapshot_id : typing.Optional[PinId]
            An unexpired snapshot to fork from. Without it, the fork starts from the current head.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespaceMetadata
            Namespace forked

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
            await client.namespaces.fork(
                namespace_id="namespace_id",
                new_namespace_id="demo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fork(
            namespace_id, new_namespace_id=new_namespace_id, snapshot_id=snapshot_id, request_options=request_options
        )
        return _response.data
