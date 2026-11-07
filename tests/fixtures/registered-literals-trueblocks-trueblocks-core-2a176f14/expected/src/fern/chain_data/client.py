

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChainDataClient, RawChainDataClient
from .types.chaindata_blocks_request_flow import ChaindataBlocksRequestFlow
from .types.chaindata_blocks_response import ChaindataBlocksResponse
from .types.chaindata_logs_response import ChaindataLogsResponse
from .types.chaindata_receipts_response import ChaindataReceiptsResponse
from .types.chaindata_traces_response import ChaindataTracesResponse
from .types.chaindata_transactions_request_flow import ChaindataTransactionsRequestFlow
from .types.chaindata_transactions_response import ChaindataTransactionsResponse
from .types.chaindata_when_response import ChaindataWhenResponse


class ChainDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChainDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChainDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChainDataClient
        """
        return self._raw_client

    def chaindata_blocks(
        self,
        *,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hashes: typing.Optional[bool] = None,
        uncles: typing.Optional[bool] = None,
        traces: typing.Optional[bool] = None,
        uniq: typing.Optional[bool] = None,
        flow: typing.Optional[ChaindataBlocksRequestFlow] = None,
        logs: typing.Optional[bool] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        withdrawals: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        cache_txs: typing.Optional[bool] = None,
        cache_traces: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataBlocksResponse:
        """
        Retrieve one or more blocks from the chain or local cache. Corresponds to the <a href="/chifra/chaindata/#chifra-blocks">chifra blocks</a> command line.

        Parameters
        ----------
        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more block identifiers

        hashes : typing.Optional[bool]
            display only transaction hashes, default is to display full transaction detail

        uncles : typing.Optional[bool]
            display uncle blocks (if any) instead of the requested block

        traces : typing.Optional[bool]
            export the traces from the block as opposed to the block data

        uniq : typing.Optional[bool]
            display a list of uniq address appearances per transaction

        flow : typing.Optional[ChaindataBlocksRequestFlow]
            for the --uniq option only, export only from or to (including trace from or to)

        logs : typing.Optional[bool]
            display only the logs found in the block(s)

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those with this topic(s)

        withdrawals : typing.Optional[bool]
            export the withdrawals from the block as opposed to the block data

        articulate : typing.Optional[bool]
            for the --logs option only, articulate the retrieved data if ABIs can be found

        count : typing.Optional[bool]
            display only the count of appearances for --addrs or --uniq

        cache_txs : typing.Optional[bool]
            force a write of the block's transactions to the cache (slow)

        cache_traces : typing.Optional[bool]
            force a write of the block's traces to the cache (slower)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataBlocksResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_data.chaindata_blocks(
            blocks=["blocks"],
        )
        """
        _response = self._raw_client.chaindata_blocks(
            blocks=blocks,
            hashes=hashes,
            uncles=uncles,
            traces=traces,
            uniq=uniq,
            flow=flow,
            logs=logs,
            emitter=emitter,
            topic=topic,
            withdrawals=withdrawals,
            articulate=articulate,
            count=count,
            cache_txs=cache_txs,
            cache_traces=cache_traces,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def chaindata_transactions(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        traces: typing.Optional[bool] = None,
        uniq: typing.Optional[bool] = None,
        flow: typing.Optional[ChaindataTransactionsRequestFlow] = None,
        logs: typing.Optional[bool] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        cache_traces: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataTransactionsResponse:
        """
        Retrieve one or more transactions from the chain or local cache. Corresponds to the <a href="/chifra/chaindata/#chifra-transactions">chifra transactions</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        traces : typing.Optional[bool]
            include the transaction's traces in the results

        uniq : typing.Optional[bool]
            display a list of uniq addresses found in the transaction

        flow : typing.Optional[ChaindataTransactionsRequestFlow]
            for the uniq option only, export only from or to (including trace from or to)

        logs : typing.Optional[bool]
            display only the logs found in the transaction(s)

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those with this topic(s)

        cache_traces : typing.Optional[bool]
            force the transaction's traces into the cache

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataTransactionsResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_data.chaindata_transactions(
            transactions=["transactions"],
        )
        """
        _response = self._raw_client.chaindata_transactions(
            transactions=transactions,
            articulate=articulate,
            traces=traces,
            uniq=uniq,
            flow=flow,
            logs=logs,
            emitter=emitter,
            topic=topic,
            cache_traces=cache_traces,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def chaindata_receipts(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataReceiptsResponse:
        """
        Retrieve receipts for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-receipts">chifra receipts</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataReceiptsResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_data.chaindata_receipts(
            transactions=["transactions"],
        )
        """
        _response = self._raw_client.chaindata_receipts(
            transactions=transactions,
            articulate=articulate,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def chaindata_logs(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataLogsResponse:
        """
        Retrieve logs for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-logs">chifra logs</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter logs to show only those with this topic(s)

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataLogsResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_data.chaindata_logs(
            transactions=["transactions"],
        )
        """
        _response = self._raw_client.chaindata_logs(
            transactions=transactions,
            emitter=emitter,
            topic=topic,
            articulate=articulate,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def chaindata_traces(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataTracesResponse:
        """
        Retrieve traces for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-traces">chifra traces</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        filter : typing.Optional[str]
            call the node's trace_filter routine with bang-separated filter

        count : typing.Optional[bool]
            display only the number of traces for the transaction (fast)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataTracesResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_data.chaindata_traces(
            transactions=["transactions"],
        )
        """
        _response = self._raw_client.chaindata_traces(
            transactions=transactions,
            articulate=articulate,
            filter=filter,
            count=count,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def chaindata_when(
        self,
        *,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        list_: typing.Optional[bool] = None,
        timestamps: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        repair: typing.Optional[bool] = None,
        check: typing.Optional[bool] = None,
        update: typing.Optional[bool] = None,
        deep: typing.Optional[int] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataWhenResponse:
        """
        Find block(s) based on date, blockNum, timestamp, or 'special'. Corresponds to the <a href="/chifra/chaindata/#chifra-when">chifra when</a> command line.

        Parameters
        ----------
        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more dates, block numbers, hashes, or special named blocks (see notes)

        list_ : typing.Optional[bool]
            export a list of the 'special' blocks

        timestamps : typing.Optional[bool]
            display or process timestamps

        count : typing.Optional[bool]
            with --timestamps only, returns the number of timestamps in the cache

        repair : typing.Optional[bool]
            with --timestamps only, repairs block(s) in the block range by re-querying from the chain

        check : typing.Optional[bool]
            with --timestamps only, checks the validity of the timestamp data

        update : typing.Optional[bool]
            with --timestamps only, bring the timestamp database forward to the latest block

        deep : typing.Optional[int]
            with --timestamps --check only, verifies every N timestamp directly from the chain (slow)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataWhenResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_data.chaindata_when()
        """
        _response = self._raw_client.chaindata_when(
            blocks=blocks,
            list_=list_,
            timestamps=timestamps,
            count=count,
            repair=repair,
            check=check,
            update=update,
            deep=deep,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data


class AsyncChainDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChainDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChainDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChainDataClient
        """
        return self._raw_client

    async def chaindata_blocks(
        self,
        *,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hashes: typing.Optional[bool] = None,
        uncles: typing.Optional[bool] = None,
        traces: typing.Optional[bool] = None,
        uniq: typing.Optional[bool] = None,
        flow: typing.Optional[ChaindataBlocksRequestFlow] = None,
        logs: typing.Optional[bool] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        withdrawals: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        cache_txs: typing.Optional[bool] = None,
        cache_traces: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataBlocksResponse:
        """
        Retrieve one or more blocks from the chain or local cache. Corresponds to the <a href="/chifra/chaindata/#chifra-blocks">chifra blocks</a> command line.

        Parameters
        ----------
        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more block identifiers

        hashes : typing.Optional[bool]
            display only transaction hashes, default is to display full transaction detail

        uncles : typing.Optional[bool]
            display uncle blocks (if any) instead of the requested block

        traces : typing.Optional[bool]
            export the traces from the block as opposed to the block data

        uniq : typing.Optional[bool]
            display a list of uniq address appearances per transaction

        flow : typing.Optional[ChaindataBlocksRequestFlow]
            for the --uniq option only, export only from or to (including trace from or to)

        logs : typing.Optional[bool]
            display only the logs found in the block(s)

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those with this topic(s)

        withdrawals : typing.Optional[bool]
            export the withdrawals from the block as opposed to the block data

        articulate : typing.Optional[bool]
            for the --logs option only, articulate the retrieved data if ABIs can be found

        count : typing.Optional[bool]
            display only the count of appearances for --addrs or --uniq

        cache_txs : typing.Optional[bool]
            force a write of the block's transactions to the cache (slow)

        cache_traces : typing.Optional[bool]
            force a write of the block's traces to the cache (slower)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataBlocksResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_data.chaindata_blocks(
                blocks=["blocks"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chaindata_blocks(
            blocks=blocks,
            hashes=hashes,
            uncles=uncles,
            traces=traces,
            uniq=uniq,
            flow=flow,
            logs=logs,
            emitter=emitter,
            topic=topic,
            withdrawals=withdrawals,
            articulate=articulate,
            count=count,
            cache_txs=cache_txs,
            cache_traces=cache_traces,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def chaindata_transactions(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        traces: typing.Optional[bool] = None,
        uniq: typing.Optional[bool] = None,
        flow: typing.Optional[ChaindataTransactionsRequestFlow] = None,
        logs: typing.Optional[bool] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        cache_traces: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataTransactionsResponse:
        """
        Retrieve one or more transactions from the chain or local cache. Corresponds to the <a href="/chifra/chaindata/#chifra-transactions">chifra transactions</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        traces : typing.Optional[bool]
            include the transaction's traces in the results

        uniq : typing.Optional[bool]
            display a list of uniq addresses found in the transaction

        flow : typing.Optional[ChaindataTransactionsRequestFlow]
            for the uniq option only, export only from or to (including trace from or to)

        logs : typing.Optional[bool]
            display only the logs found in the transaction(s)

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those with this topic(s)

        cache_traces : typing.Optional[bool]
            force the transaction's traces into the cache

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataTransactionsResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_data.chaindata_transactions(
                transactions=["transactions"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chaindata_transactions(
            transactions=transactions,
            articulate=articulate,
            traces=traces,
            uniq=uniq,
            flow=flow,
            logs=logs,
            emitter=emitter,
            topic=topic,
            cache_traces=cache_traces,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def chaindata_receipts(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataReceiptsResponse:
        """
        Retrieve receipts for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-receipts">chifra receipts</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataReceiptsResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_data.chaindata_receipts(
                transactions=["transactions"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chaindata_receipts(
            transactions=transactions,
            articulate=articulate,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def chaindata_logs(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataLogsResponse:
        """
        Retrieve logs for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-logs">chifra logs</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter logs to show only those with this topic(s)

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataLogsResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_data.chaindata_logs(
                transactions=["transactions"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chaindata_logs(
            transactions=transactions,
            emitter=emitter,
            topic=topic,
            articulate=articulate,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def chaindata_traces(
        self,
        *,
        transactions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        articulate: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataTracesResponse:
        """
        Retrieve traces for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-traces">chifra traces</a> command line.

        Parameters
        ----------
        transactions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space-separated list of one or more transaction identifiers

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        filter : typing.Optional[str]
            call the node's trace_filter routine with bang-separated filter

        count : typing.Optional[bool]
            display only the number of traces for the transaction (fast)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataTracesResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_data.chaindata_traces(
                transactions=["transactions"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chaindata_traces(
            transactions=transactions,
            articulate=articulate,
            filter=filter,
            count=count,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def chaindata_when(
        self,
        *,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        list_: typing.Optional[bool] = None,
        timestamps: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        repair: typing.Optional[bool] = None,
        check: typing.Optional[bool] = None,
        update: typing.Optional[bool] = None,
        deep: typing.Optional[int] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChaindataWhenResponse:
        """
        Find block(s) based on date, blockNum, timestamp, or 'special'. Corresponds to the <a href="/chifra/chaindata/#chifra-when">chifra when</a> command line.

        Parameters
        ----------
        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more dates, block numbers, hashes, or special named blocks (see notes)

        list_ : typing.Optional[bool]
            export a list of the 'special' blocks

        timestamps : typing.Optional[bool]
            display or process timestamps

        count : typing.Optional[bool]
            with --timestamps only, returns the number of timestamps in the cache

        repair : typing.Optional[bool]
            with --timestamps only, repairs block(s) in the block range by re-querying from the chain

        check : typing.Optional[bool]
            with --timestamps only, checks the validity of the timestamp data

        update : typing.Optional[bool]
            with --timestamps only, bring the timestamp database forward to the latest block

        deep : typing.Optional[int]
            with --timestamps --check only, verifies every N timestamp directly from the chain (slow)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaindataWhenResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_data.chaindata_when()


        asyncio.run(main())
        """
        _response = await self._raw_client.chaindata_when(
            blocks=blocks,
            list_=list_,
            timestamps=timestamps,
            count=count,
            repair=repair,
            check=check,
            update=update,
            deep=deep,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data
