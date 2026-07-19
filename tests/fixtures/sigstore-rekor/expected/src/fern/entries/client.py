

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.error import Error
from ..types.proposed_entry import ProposedEntry
from .raw_client import AsyncRawEntriesClient, RawEntriesClient


OMIT = typing.cast(typing.Any, ...)


class EntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntriesClient
        """
        return self._raw_client

    def get_log_entry_by_index(
        self, *, log_index: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Error:
        """
        Parameters
        ----------
        log_index : typing.Optional[int]
            specifies the index of the entry in the transparency log to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.entries.get_log_entry_by_index()
        """
        _response = self._raw_client.get_log_entry_by_index(log_index=log_index, request_options=request_options)
        return _response.data

    def create_log_entry(self, *, kind: str, request_options: typing.Optional[RequestOptions] = None) -> Error:
        """
        Creates an entry in the transparency log for a detached signature, public key, and content. Items can be included in the request or fetched by the server when URLs are specified.

        Parameters
        ----------
        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.entries.create_log_entry(
            kind="kind",
        )
        """
        _response = self._raw_client.create_log_entry(kind=kind, request_options=request_options)
        return _response.data

    def search_log_query(
        self,
        *,
        entries: typing.Optional[typing.Sequence[ProposedEntry]] = OMIT,
        entry_uui_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        log_indexes: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Error:
        """
        Parameters
        ----------
        entries : typing.Optional[typing.Sequence[ProposedEntry]]

        entry_uui_ds : typing.Optional[typing.Sequence[str]]

        log_indexes : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.entries.search_log_query()
        """
        _response = self._raw_client.search_log_query(
            entries=entries, entry_uui_ds=entry_uui_ds, log_indexes=log_indexes, request_options=request_options
        )
        return _response.data

    def get_log_entry_by_uuid(
        self, entry_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Error:
        """
        Returns the entry, root hash, tree size, and a list of hashes that can be used to calculate proof of an entry being included in the transparency log

        Parameters
        ----------
        entry_uuid : str
            the UUID of the entry for which the inclusion proof information should be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.entries.get_log_entry_by_uuid(
            entry_uuid="entryUUID",
        )
        """
        _response = self._raw_client.get_log_entry_by_uuid(entry_uuid, request_options=request_options)
        return _response.data


class AsyncEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntriesClient
        """
        return self._raw_client

    async def get_log_entry_by_index(
        self, *, log_index: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Error:
        """
        Parameters
        ----------
        log_index : typing.Optional[int]
            specifies the index of the entry in the transparency log to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.entries.get_log_entry_by_index()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_entry_by_index(log_index=log_index, request_options=request_options)
        return _response.data

    async def create_log_entry(self, *, kind: str, request_options: typing.Optional[RequestOptions] = None) -> Error:
        """
        Creates an entry in the transparency log for a detached signature, public key, and content. Items can be included in the request or fetched by the server when URLs are specified.

        Parameters
        ----------
        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.entries.create_log_entry(
                kind="kind",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_log_entry(kind=kind, request_options=request_options)
        return _response.data

    async def search_log_query(
        self,
        *,
        entries: typing.Optional[typing.Sequence[ProposedEntry]] = OMIT,
        entry_uui_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        log_indexes: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Error:
        """
        Parameters
        ----------
        entries : typing.Optional[typing.Sequence[ProposedEntry]]

        entry_uui_ds : typing.Optional[typing.Sequence[str]]

        log_indexes : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.entries.search_log_query()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_log_query(
            entries=entries, entry_uui_ds=entry_uui_ds, log_indexes=log_indexes, request_options=request_options
        )
        return _response.data

    async def get_log_entry_by_uuid(
        self, entry_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Error:
        """
        Returns the entry, root hash, tree size, and a list of hashes that can be used to calculate proof of an entry being included in the transparency log

        Parameters
        ----------
        entry_uuid : str
            the UUID of the entry for which the inclusion proof information should be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.entries.get_log_entry_by_uuid(
                entry_uuid="entryUUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_entry_by_uuid(entry_uuid, request_options=request_options)
        return _response.data
