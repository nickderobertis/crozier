

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.block import Block
from .types.block_number_or_tag_or_hash import BlockNumberOrTagOrHash
from .types.block_receipts_response import BlockReceiptsResponse
from .types.bytes import Bytes
from .types.chain_id_response import ChainIdResponse
from .types.filter import Filter
from .types.new_filter_request_kind import NewFilterRequestKind
from .types.new_filter_response import NewFilterResponse
from .types.send_raw_tx_response import SendRawTxResponse
from .types.uint import Uint
from .types.uninstall_filter_response import UninstallFilterResponse

if typing.TYPE_CHECKING:
    from .verifiable.client import AsyncVerifiableClient, VerifiableClient

OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._verifiable: typing.Optional[VerifiableClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_chain_id(self, *, request_options: typing.Optional[RequestOptions] = None) -> ChainIdResponse:
        """
        Returns the chain id of the network of the underlying RPC node.
        ### Why is this useful?
        Replaces the `eth_chainId` RPC method.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChainIdResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_chain_id()
        """
        _response = self._raw_client.get_chain_id(request_options=request_options)
        return _response.data

    def get_block_information(
        self,
        block_id: BlockNumberOrTagOrHash,
        *,
        transaction_detail_flag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Returns information about a block.
        ### Why is this useful?
        Replaces the `eth_getBlockByNumber` and `eth_getBlockByHash` RPC methods.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        transaction_detail_flag : typing.Optional[bool]
            A flag indicating whether to include full transaction details or just the hashes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_block_information(
            block_id="earliest",
        )
        """
        _response = self._raw_client.get_block_information(
            block_id, transaction_detail_flag=transaction_detail_flag, request_options=request_options
        )
        return _response.data

    def get_block_receipts(
        self, block_id: BlockNumberOrTagOrHash, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BlockReceiptsResponse:
        """
        Returns all transaction receipts for a given block.
        ### Why is this useful?
        Replaces the `eth_getBlockReceipts` RPC method.
        ### How to verify response?
        - RLP encode each receipt and keccak-256 hash these encoded receipts.
        - Construct a Merkle Patricia Trie (MPT) from these hashes.
        - Verify the root of the constructed MPT against the trusted block's receipt root.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlockReceiptsResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_block_receipts(
            block_id="earliest",
        )
        """
        _response = self._raw_client.get_block_receipts(block_id, request_options=request_options)
        return _response.data

    def send_raw_transaction(
        self, *, bytes: typing.Optional[Bytes] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SendRawTxResponse:
        """
        Creates a new message call transaction or a contract creation for signed transactions.
        ### Why is this useful?
        Replaces the `eth_sendRawTransaction` RPC method.

        Parameters
        ----------
        bytes : typing.Optional[Bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendRawTxResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.send_raw_transaction()
        """
        _response = self._raw_client.send_raw_transaction(bytes=bytes, request_options=request_options)
        return _response.data

    def create_new_filter(
        self,
        *,
        kind: typing.Optional[NewFilterRequestKind] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NewFilterResponse:
        """
        Creates a filter in the node, to notify when the state changes.

        State changes can be of three types: logs, new blocks and pending transactions.

        To check if the state has changed, query `/filterChanges/{filterId}`.
        ### Why is this useful?
        Replaces the `eth_newFilter`, `eth_newBlockFilter` and `eth_newPendingTransactionFilter` RPC methods.

        Parameters
        ----------
        kind : typing.Optional[NewFilterRequestKind]

        filter : typing.Optional[Filter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewFilterResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_new_filter()
        """
        _response = self._raw_client.create_new_filter(kind=kind, filter=filter, request_options=request_options)
        return _response.data

    def uninstall_a_filter(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UninstallFilterResponse:
        """
        Uninstalls a filter with given id.
        ### Why is this useful?
        Replaces the `eth_uninstallFilter` RPC method.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UninstallFilterResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.uninstall_a_filter(
            filter_id="filterId",
        )
        """
        _response = self._raw_client.uninstall_a_filter(filter_id, request_options=request_options)
        return _response.data

    @property
    def verifiable(self):
        if self._verifiable is None:
            from .verifiable.client import VerifiableClient

            self._verifiable = VerifiableClient(client_wrapper=self._client_wrapper)
        return self._verifiable


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._verifiable: typing.Optional[AsyncVerifiableClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_chain_id(self, *, request_options: typing.Optional[RequestOptions] = None) -> ChainIdResponse:
        """
        Returns the chain id of the network of the underlying RPC node.
        ### Why is this useful?
        Replaces the `eth_chainId` RPC method.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChainIdResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_chain_id()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_chain_id(request_options=request_options)
        return _response.data

    async def get_block_information(
        self,
        block_id: BlockNumberOrTagOrHash,
        *,
        transaction_detail_flag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Returns information about a block.
        ### Why is this useful?
        Replaces the `eth_getBlockByNumber` and `eth_getBlockByHash` RPC methods.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        transaction_detail_flag : typing.Optional[bool]
            A flag indicating whether to include full transaction details or just the hashes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_block_information(
                block_id="earliest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_block_information(
            block_id, transaction_detail_flag=transaction_detail_flag, request_options=request_options
        )
        return _response.data

    async def get_block_receipts(
        self, block_id: BlockNumberOrTagOrHash, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BlockReceiptsResponse:
        """
        Returns all transaction receipts for a given block.
        ### Why is this useful?
        Replaces the `eth_getBlockReceipts` RPC method.
        ### How to verify response?
        - RLP encode each receipt and keccak-256 hash these encoded receipts.
        - Construct a Merkle Patricia Trie (MPT) from these hashes.
        - Verify the root of the constructed MPT against the trusted block's receipt root.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlockReceiptsResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_block_receipts(
                block_id="earliest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_block_receipts(block_id, request_options=request_options)
        return _response.data

    async def send_raw_transaction(
        self, *, bytes: typing.Optional[Bytes] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SendRawTxResponse:
        """
        Creates a new message call transaction or a contract creation for signed transactions.
        ### Why is this useful?
        Replaces the `eth_sendRawTransaction` RPC method.

        Parameters
        ----------
        bytes : typing.Optional[Bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendRawTxResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.send_raw_transaction()


        asyncio.run(main())
        """
        _response = await self._raw_client.send_raw_transaction(bytes=bytes, request_options=request_options)
        return _response.data

    async def create_new_filter(
        self,
        *,
        kind: typing.Optional[NewFilterRequestKind] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NewFilterResponse:
        """
        Creates a filter in the node, to notify when the state changes.

        State changes can be of three types: logs, new blocks and pending transactions.

        To check if the state has changed, query `/filterChanges/{filterId}`.
        ### Why is this useful?
        Replaces the `eth_newFilter`, `eth_newBlockFilter` and `eth_newPendingTransactionFilter` RPC methods.

        Parameters
        ----------
        kind : typing.Optional[NewFilterRequestKind]

        filter : typing.Optional[Filter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewFilterResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_new_filter()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_new_filter(kind=kind, filter=filter, request_options=request_options)
        return _response.data

    async def uninstall_a_filter(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UninstallFilterResponse:
        """
        Uninstalls a filter with given id.
        ### Why is this useful?
        Replaces the `eth_uninstallFilter` RPC method.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UninstallFilterResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.uninstall_a_filter(
                filter_id="filterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.uninstall_a_filter(filter_id, request_options=request_options)
        return _response.data

    @property
    def verifiable(self):
        if self._verifiable is None:
            from .verifiable.client import AsyncVerifiableClient

            self._verifiable = AsyncVerifiableClient(client_wrapper=self._client_wrapper)
        return self._verifiable
