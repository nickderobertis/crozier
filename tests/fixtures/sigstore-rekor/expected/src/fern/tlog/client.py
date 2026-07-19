

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.error import Error
from .raw_client import AsyncRawTlogClient, RawTlogClient


class TlogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTlogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTlogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTlogClient
        """
        return self._raw_client

    def get_log_info(
        self, *, stable: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Error:
        """
        Returns the current root hash and size of the merkle tree used to store the log entries.

        Parameters
        ----------
        stable : typing.Optional[bool]
            Whether to return a stable checkpoint for the active shard

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
        client.tlog.get_log_info()
        """
        _response = self._raw_client.get_log_info(stable=stable, request_options=request_options)
        return _response.data

    def get_log_proof(
        self,
        *,
        first_size: typing.Optional[int] = None,
        last_size: typing.Optional[int] = None,
        tree_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Error:
        """
        Returns a list of hashes for specified tree sizes that can be used to confirm the consistency of the transparency log

        Parameters
        ----------
        first_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency from (1 means the beginning of the log) Defaults to 1 if not specified

        last_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency to

        tree_id : typing.Optional[str]
            The tree ID of the tree that you wish to prove consistency for

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
        client.tlog.get_log_proof()
        """
        _response = self._raw_client.get_log_proof(
            first_size=first_size, last_size=last_size, tree_id=tree_id, request_options=request_options
        )
        return _response.data


class AsyncTlogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTlogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTlogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTlogClient
        """
        return self._raw_client

    async def get_log_info(
        self, *, stable: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Error:
        """
        Returns the current root hash and size of the merkle tree used to store the log entries.

        Parameters
        ----------
        stable : typing.Optional[bool]
            Whether to return a stable checkpoint for the active shard

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
            await client.tlog.get_log_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_info(stable=stable, request_options=request_options)
        return _response.data

    async def get_log_proof(
        self,
        *,
        first_size: typing.Optional[int] = None,
        last_size: typing.Optional[int] = None,
        tree_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Error:
        """
        Returns a list of hashes for specified tree sizes that can be used to confirm the consistency of the transparency log

        Parameters
        ----------
        first_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency from (1 means the beginning of the log) Defaults to 1 if not specified

        last_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency to

        tree_id : typing.Optional[str]
            The tree ID of the tree that you wish to prove consistency for

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
            await client.tlog.get_log_proof()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_proof(
            first_size=first_size, last_size=last_size, tree_id=tree_id, request_options=request_options
        )
        return _response.data
