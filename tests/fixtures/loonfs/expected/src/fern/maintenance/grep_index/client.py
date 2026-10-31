

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.grep_index import GrepIndex
from .raw_client import AsyncRawGrepIndexClient, RawGrepIndexClient


class GrepIndexClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGrepIndexClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGrepIndexClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGrepIndexClient
        """
        return self._raw_client

    def retrieve(self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GrepIndex:
        """
        Reports whether the namespace's grep index is `disabled`, `backfilling`, or `active`, with build progress when it's available. A namespace that has never enabled the index is `disabled`. A deployment that doesn't maintain grep indexes returns `not_supported`, and this operation doesn't change the index.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrepIndex
            Grep index status and build progress

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
        client.maintenance.grep_index.retrieve(
            namespace_id="namespace_id",
        )
        """
        _response = self._raw_client.retrieve(namespace_id, request_options=request_options)
        return _response.data

    def disable(self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GrepIndex:
        """
        Disables the namespace's grep index by publishing a manifest with the next number and no segment references. Index maintenance stops when a step reads the disabled manifest, and an explicit grep garbage collection run reclaims the segments later. Repeating the request has the same result. A deployment that doesn't maintain the grep index returns `not_supported`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrepIndex
            Grep index disabled or already disabled

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
        client.maintenance.grep_index.disable(
            namespace_id="namespace_id",
        )
        """
        _response = self._raw_client.disable(namespace_id, request_options=request_options)
        return _response.data

    def enable(self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GrepIndex:
        """
        Enables the namespace's grep index. A deployment that runs maintenance starts the backfill on its next session tick and continues until the index is active. The response reports the index state read after the change. A new enable reports `backfilling`, with the sequence that its checkpoint captured, and an index that was already enabled reports its current status. Repeating the request has the same result. A deployment that doesn't maintain the grep index returns `not_supported`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrepIndex
            Grep index enabled or already enabled

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
        client.maintenance.grep_index.enable(
            namespace_id="namespace_id",
        )
        """
        _response = self._raw_client.enable(namespace_id, request_options=request_options)
        return _response.data


class AsyncGrepIndexClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGrepIndexClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGrepIndexClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGrepIndexClient
        """
        return self._raw_client

    async def retrieve(
        self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GrepIndex:
        """
        Reports whether the namespace's grep index is `disabled`, `backfilling`, or `active`, with build progress when it's available. A namespace that has never enabled the index is `disabled`. A deployment that doesn't maintain grep indexes returns `not_supported`, and this operation doesn't change the index.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrepIndex
            Grep index status and build progress

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
            await client.maintenance.grep_index.retrieve(
                namespace_id="namespace_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(namespace_id, request_options=request_options)
        return _response.data

    async def disable(self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GrepIndex:
        """
        Disables the namespace's grep index by publishing a manifest with the next number and no segment references. Index maintenance stops when a step reads the disabled manifest, and an explicit grep garbage collection run reclaims the segments later. Repeating the request has the same result. A deployment that doesn't maintain the grep index returns `not_supported`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrepIndex
            Grep index disabled or already disabled

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
            await client.maintenance.grep_index.disable(
                namespace_id="namespace_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable(namespace_id, request_options=request_options)
        return _response.data

    async def enable(self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GrepIndex:
        """
        Enables the namespace's grep index. A deployment that runs maintenance starts the backfill on its next session tick and continues until the index is active. The response reports the index state read after the change. A new enable reports `backfilling`, with the sequence that its checkpoint captured, and an index that was already enabled reports its current status. Repeating the request has the same result. A deployment that doesn't maintain the grep index returns `not_supported`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrepIndex
            Grep index enabled or already enabled

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
            await client.maintenance.grep_index.enable(
                namespace_id="namespace_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable(namespace_id, request_options=request_options)
        return _response.data
