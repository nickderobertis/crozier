

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAccountsClient, RawAccountsClient
from .types.accounts_abis_response import AccountsAbisResponse
from .types.accounts_export_request_flow import AccountsExportRequestFlow
from .types.accounts_export_response import AccountsExportResponse
from .types.accounts_list_response import AccountsListResponse
from .types.accounts_monitors_response import AccountsMonitorsResponse
from .types.accounts_names_response import AccountsNamesResponse


class AccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        bounds: typing.Optional[bool] = None,
        unripe: typing.Optional[bool] = None,
        silent: typing.Optional[bool] = None,
        first_record: typing.Optional[int] = None,
        max_records: typing.Optional[int] = None,
        reversed: typing.Optional[bool] = None,
        first_block: typing.Optional[float] = None,
        last_block: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsListResponse:
        """
        List every appearance of an address anywhere on the chain. Corresponds to the <a href="/chifra/accounts/#chifra-list">chifra list</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) to list

        count : typing.Optional[bool]
            display only the count of records for each monitor

        no_zero : typing.Optional[bool]
            for the --count option only, suppress the display of zero appearance accounts

        bounds : typing.Optional[bool]
            report first and last block this address appears

        unripe : typing.Optional[bool]
            list transactions labeled unripe (i.e. less than 28 blocks old)

        silent : typing.Optional[bool]
            freshen the monitor only (no reporting)

        first_record : typing.Optional[int]
            the first record to process

        max_records : typing.Optional[int]
            the maximum number of records to process

        reversed : typing.Optional[bool]
            produce results in reverse chronological order

        first_block : typing.Optional[float]
            first block to export (inclusive, ignored when freshening)

        last_block : typing.Optional[float]
            last block to export (inclusive, ignored when freshening)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsListResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounts.list(
            addrs=["addrs"],
        )
        """
        _response = self._raw_client.list(
            addrs=addrs,
            count=count,
            no_zero=no_zero,
            bounds=bounds,
            unripe=unripe,
            silent=silent,
            first_record=first_record,
            max_records=max_records,
            reversed=reversed,
            first_block=first_block,
            last_block=last_block,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def export(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topics: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fourbytes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        appearances: typing.Optional[bool] = None,
        receipts: typing.Optional[bool] = None,
        logs: typing.Optional[bool] = None,
        approvals: typing.Optional[bool] = None,
        traces: typing.Optional[bool] = None,
        neighbors: typing.Optional[bool] = None,
        statements: typing.Optional[bool] = None,
        transfers: typing.Optional[bool] = None,
        assets: typing.Optional[bool] = None,
        balances: typing.Optional[bool] = None,
        withdrawals: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        cache_traces: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        first_record: typing.Optional[int] = None,
        max_records: typing.Optional[int] = None,
        relevant: typing.Optional[bool] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        nfts: typing.Optional[bool] = None,
        reverted: typing.Optional[bool] = None,
        asset: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        flow: typing.Optional[AccountsExportRequestFlow] = None,
        factory: typing.Optional[bool] = None,
        unripe: typing.Optional[bool] = None,
        reversed: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        first_block: typing.Optional[float] = None,
        last_block: typing.Optional[float] = None,
        accounting: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsExportResponse:
        """
        Export full details of transactions for one or more addresses. Corresponds to the <a href="/chifra/accounts/#chifra-export">chifra export</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) to export

        topics : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter by one or more log topics (only for --logs option)

        fourbytes : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter by one or more fourbytes (only for transactions and trace options)

        appearances : typing.Optional[bool]
            export a list of appearances

        receipts : typing.Optional[bool]
            export receipts instead of transactional data

        logs : typing.Optional[bool]
            export logs instead of transactional data

        approvals : typing.Optional[bool]
            export all token approval transactions for the given address

        traces : typing.Optional[bool]
            export traces instead of transactional data

        neighbors : typing.Optional[bool]
            export the neighbors of the given address

        statements : typing.Optional[bool]
            export only statements

        transfers : typing.Optional[bool]
            export only eth or token transfers

        assets : typing.Optional[bool]
            list all assets (with names) that appear in any transfer

        balances : typing.Optional[bool]
            traverse the transaction history and show each change in ETH balances

        withdrawals : typing.Optional[bool]
            export withdrawals for the given address

        articulate : typing.Optional[bool]
            articulate transactions, traces, logs, and outputs

        cache_traces : typing.Optional[bool]
            force the transaction's traces into the cache

        count : typing.Optional[bool]
            for --appearances mode only, display only the count of records

        first_record : typing.Optional[int]
            the first record to process

        max_records : typing.Optional[int]
            the maximum number of records to process

        relevant : typing.Optional[bool]
            for log and accounting export only, export only logs relevant to one of the given export addresses

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those with this topic(s)

        nfts : typing.Optional[bool]
            for the --logs option only, filter logs to show only nft transfers

        reverted : typing.Optional[bool]
            export only transactions that were reverted

        asset : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            export transfers, balances, or statements only for this asset

        flow : typing.Optional[AccountsExportRequestFlow]
            export transfers, balances, or statements with incoming, outgoing, or zero value

        factory : typing.Optional[bool]
            for --traces only, report addresses created by (or self-destructed by) the given address(es)

        unripe : typing.Optional[bool]
            export transactions labeled unripe (i.e. less than 28 blocks old)

        reversed : typing.Optional[bool]
            produce results in reverse chronological order

        no_zero : typing.Optional[bool]
            for the --count option only, suppress the display of zero appearance accounts

        first_block : typing.Optional[float]
            first block to process (inclusive)

        last_block : typing.Optional[float]
            last block to process (inclusive)

        accounting : typing.Optional[bool]
            deprecated option, you may simply remove it

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
        AccountsExportResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounts.export(
            addrs=["addrs"],
        )
        """
        _response = self._raw_client.export(
            addrs=addrs,
            topics=topics,
            fourbytes=fourbytes,
            appearances=appearances,
            receipts=receipts,
            logs=logs,
            approvals=approvals,
            traces=traces,
            neighbors=neighbors,
            statements=statements,
            transfers=transfers,
            assets=assets,
            balances=balances,
            withdrawals=withdrawals,
            articulate=articulate,
            cache_traces=cache_traces,
            count=count,
            first_record=first_record,
            max_records=max_records,
            relevant=relevant,
            emitter=emitter,
            topic=topic,
            nfts=nfts,
            reverted=reverted,
            asset=asset,
            flow=flow,
            factory=factory,
            unripe=unripe,
            reversed=reversed,
            no_zero=no_zero,
            first_block=first_block,
            last_block=last_block,
            accounting=accounting,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def monitors(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        delete: typing.Optional[bool] = None,
        undelete: typing.Optional[bool] = None,
        remove: typing.Optional[bool] = None,
        clean: typing.Optional[bool] = None,
        list_: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        staged: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsMonitorsResponse:
        """
        Add, remove, clean, and list address monitors. Corresponds to the <a href="/chifra/accounts/#chifra-monitors">chifra monitors</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) to process

        delete : typing.Optional[bool]
            delete a monitor, but do not remove it

        undelete : typing.Optional[bool]
            undelete a previously deleted monitor

        remove : typing.Optional[bool]
            remove a previously deleted monitor

        clean : typing.Optional[bool]
            clean (i.e. remove duplicate appearances) from monitors, optionally clear stage

        list_ : typing.Optional[bool]
            list monitors in the cache (--verbose for more detail)

        count : typing.Optional[bool]
            show the number of active monitors (included deleted but not removed monitors)

        staged : typing.Optional[bool]
            for --clean, --list, and --count options only, include staged monitors

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
        AccountsMonitorsResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounts.monitors()
        """
        _response = self._raw_client.monitors(
            addrs=addrs,
            delete=delete,
            undelete=undelete,
            remove=remove,
            clean=clean,
            list_=list_,
            count=count,
            staged=staged,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def names(
        self,
        *,
        terms: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        expand: typing.Optional[bool] = None,
        match_case: typing.Optional[bool] = None,
        all_: typing.Optional[bool] = None,
        custom: typing.Optional[bool] = None,
        prefund: typing.Optional[bool] = None,
        addr: typing.Optional[bool] = None,
        tags: typing.Optional[bool] = None,
        clean: typing.Optional[bool] = None,
        regular: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        dry_run: typing.Optional[bool] = None,
        autoname: typing.Optional[str] = None,
        create: typing.Optional[str] = None,
        update: typing.Optional[str] = None,
        delete: typing.Optional[str] = None,
        undelete: typing.Optional[str] = None,
        remove: typing.Optional[str] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsNamesResponse:
        """
        Query addresses or names of well-known accounts. Corresponds to the <a href="/chifra/accounts/#chifra-names">chifra names</a> command line.

        Parameters
        ----------
        terms : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space separated list of one or more search terms

        expand : typing.Optional[bool]
            expand search to include all fields (search name, address, and symbol otherwise)

        match_case : typing.Optional[bool]
            do case-sensitive search

        all_ : typing.Optional[bool]
            include all (including custom) names in the search

        custom : typing.Optional[bool]
            include only custom named accounts in the search

        prefund : typing.Optional[bool]
            include prefund accounts in the search

        addr : typing.Optional[bool]
            display only addresses in the results (useful for scripting, assumes --no_header)

        tags : typing.Optional[bool]
            export the list of tags and subtags only

        clean : typing.Optional[bool]
            clean the data (addrs to lower case, sort by addr)

        regular : typing.Optional[bool]
            only available with --clean, cleans regular names database

        count : typing.Optional[bool]
            return the number of names matching the search terms or other options

        dry_run : typing.Optional[bool]
            only available with --clean or --autoname, outputs changes to stdout instead of updating databases

        autoname : typing.Optional[str]
            an address assumed to be a token, added automatically to names database if true

        create : typing.Optional[str]
            create a new item

        update : typing.Optional[str]
            update an existing item

        delete : typing.Optional[str]
            delete the item, but do not remove it

        undelete : typing.Optional[str]
            undelete a previously deleted item

        remove : typing.Optional[str]
            remove a previously deleted item

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsNamesResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounts.names(
            terms=["terms"],
        )
        """
        _response = self._raw_client.names(
            terms=terms,
            expand=expand,
            match_case=match_case,
            all_=all_,
            custom=custom,
            prefund=prefund,
            addr=addr,
            tags=tags,
            clean=clean,
            regular=regular,
            count=count,
            dry_run=dry_run,
            autoname=autoname,
            create=create,
            update=update,
            delete=delete,
            undelete=undelete,
            remove=remove,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def abis(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        known: typing.Optional[bool] = None,
        proxy_for: typing.Optional[str] = None,
        list_: typing.Optional[bool] = None,
        details: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        find: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hint: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        encode: typing.Optional[str] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsAbisResponse:
        """
        Fetches the ABI for a smart contract. Corresponds to the <a href="/chifra/accounts/#chifra-abis">chifra abis</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a list of one or more smart contracts whose ABIs to display

        known : typing.Optional[bool]
            load common 'known' ABIs from cache

        proxy_for : typing.Optional[str]
            redirects the query to this implementation

        list_ : typing.Optional[bool]
            a list of downloaded abi files

        details : typing.Optional[bool]
            show the functions and events instead of summaries for all abi files

        count : typing.Optional[bool]
            show the number of abis downloaded

        find : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            search for function or event declarations given a four- or 32-byte code(s)

        hint : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --find option only, provide hints to speed up the search

        encode : typing.Optional[str]
            generate the 32-byte encoding for a given canonical function or event signature

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
        AccountsAbisResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounts.abis(
            addrs=["addrs"],
        )
        """
        _response = self._raw_client.abis(
            addrs=addrs,
            known=known,
            proxy_for=proxy_for,
            list_=list_,
            details=details,
            count=count,
            find=find,
            hint=hint,
            encode=encode,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data


class AsyncAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        bounds: typing.Optional[bool] = None,
        unripe: typing.Optional[bool] = None,
        silent: typing.Optional[bool] = None,
        first_record: typing.Optional[int] = None,
        max_records: typing.Optional[int] = None,
        reversed: typing.Optional[bool] = None,
        first_block: typing.Optional[float] = None,
        last_block: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsListResponse:
        """
        List every appearance of an address anywhere on the chain. Corresponds to the <a href="/chifra/accounts/#chifra-list">chifra list</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) to list

        count : typing.Optional[bool]
            display only the count of records for each monitor

        no_zero : typing.Optional[bool]
            for the --count option only, suppress the display of zero appearance accounts

        bounds : typing.Optional[bool]
            report first and last block this address appears

        unripe : typing.Optional[bool]
            list transactions labeled unripe (i.e. less than 28 blocks old)

        silent : typing.Optional[bool]
            freshen the monitor only (no reporting)

        first_record : typing.Optional[int]
            the first record to process

        max_records : typing.Optional[int]
            the maximum number of records to process

        reversed : typing.Optional[bool]
            produce results in reverse chronological order

        first_block : typing.Optional[float]
            first block to export (inclusive, ignored when freshening)

        last_block : typing.Optional[float]
            last block to export (inclusive, ignored when freshening)

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsListResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.list(
                addrs=["addrs"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            addrs=addrs,
            count=count,
            no_zero=no_zero,
            bounds=bounds,
            unripe=unripe,
            silent=silent,
            first_record=first_record,
            max_records=max_records,
            reversed=reversed,
            first_block=first_block,
            last_block=last_block,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def export(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topics: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fourbytes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        appearances: typing.Optional[bool] = None,
        receipts: typing.Optional[bool] = None,
        logs: typing.Optional[bool] = None,
        approvals: typing.Optional[bool] = None,
        traces: typing.Optional[bool] = None,
        neighbors: typing.Optional[bool] = None,
        statements: typing.Optional[bool] = None,
        transfers: typing.Optional[bool] = None,
        assets: typing.Optional[bool] = None,
        balances: typing.Optional[bool] = None,
        withdrawals: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        cache_traces: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        first_record: typing.Optional[int] = None,
        max_records: typing.Optional[int] = None,
        relevant: typing.Optional[bool] = None,
        emitter: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        topic: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        nfts: typing.Optional[bool] = None,
        reverted: typing.Optional[bool] = None,
        asset: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        flow: typing.Optional[AccountsExportRequestFlow] = None,
        factory: typing.Optional[bool] = None,
        unripe: typing.Optional[bool] = None,
        reversed: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        first_block: typing.Optional[float] = None,
        last_block: typing.Optional[float] = None,
        accounting: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsExportResponse:
        """
        Export full details of transactions for one or more addresses. Corresponds to the <a href="/chifra/accounts/#chifra-export">chifra export</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) to export

        topics : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter by one or more log topics (only for --logs option)

        fourbytes : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            filter by one or more fourbytes (only for transactions and trace options)

        appearances : typing.Optional[bool]
            export a list of appearances

        receipts : typing.Optional[bool]
            export receipts instead of transactional data

        logs : typing.Optional[bool]
            export logs instead of transactional data

        approvals : typing.Optional[bool]
            export all token approval transactions for the given address

        traces : typing.Optional[bool]
            export traces instead of transactional data

        neighbors : typing.Optional[bool]
            export the neighbors of the given address

        statements : typing.Optional[bool]
            export only statements

        transfers : typing.Optional[bool]
            export only eth or token transfers

        assets : typing.Optional[bool]
            list all assets (with names) that appear in any transfer

        balances : typing.Optional[bool]
            traverse the transaction history and show each change in ETH balances

        withdrawals : typing.Optional[bool]
            export withdrawals for the given address

        articulate : typing.Optional[bool]
            articulate transactions, traces, logs, and outputs

        cache_traces : typing.Optional[bool]
            force the transaction's traces into the cache

        count : typing.Optional[bool]
            for --appearances mode only, display only the count of records

        first_record : typing.Optional[int]
            the first record to process

        max_records : typing.Optional[int]
            the maximum number of records to process

        relevant : typing.Optional[bool]
            for log and accounting export only, export only logs relevant to one of the given export addresses

        emitter : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those logs emitted by the given address(es)

        topic : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --logs option only, filter logs to show only those with this topic(s)

        nfts : typing.Optional[bool]
            for the --logs option only, filter logs to show only nft transfers

        reverted : typing.Optional[bool]
            export only transactions that were reverted

        asset : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            export transfers, balances, or statements only for this asset

        flow : typing.Optional[AccountsExportRequestFlow]
            export transfers, balances, or statements with incoming, outgoing, or zero value

        factory : typing.Optional[bool]
            for --traces only, report addresses created by (or self-destructed by) the given address(es)

        unripe : typing.Optional[bool]
            export transactions labeled unripe (i.e. less than 28 blocks old)

        reversed : typing.Optional[bool]
            produce results in reverse chronological order

        no_zero : typing.Optional[bool]
            for the --count option only, suppress the display of zero appearance accounts

        first_block : typing.Optional[float]
            first block to process (inclusive)

        last_block : typing.Optional[float]
            last block to process (inclusive)

        accounting : typing.Optional[bool]
            deprecated option, you may simply remove it

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
        AccountsExportResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.export(
                addrs=["addrs"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export(
            addrs=addrs,
            topics=topics,
            fourbytes=fourbytes,
            appearances=appearances,
            receipts=receipts,
            logs=logs,
            approvals=approvals,
            traces=traces,
            neighbors=neighbors,
            statements=statements,
            transfers=transfers,
            assets=assets,
            balances=balances,
            withdrawals=withdrawals,
            articulate=articulate,
            cache_traces=cache_traces,
            count=count,
            first_record=first_record,
            max_records=max_records,
            relevant=relevant,
            emitter=emitter,
            topic=topic,
            nfts=nfts,
            reverted=reverted,
            asset=asset,
            flow=flow,
            factory=factory,
            unripe=unripe,
            reversed=reversed,
            no_zero=no_zero,
            first_block=first_block,
            last_block=last_block,
            accounting=accounting,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def monitors(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        delete: typing.Optional[bool] = None,
        undelete: typing.Optional[bool] = None,
        remove: typing.Optional[bool] = None,
        clean: typing.Optional[bool] = None,
        list_: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        staged: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsMonitorsResponse:
        """
        Add, remove, clean, and list address monitors. Corresponds to the <a href="/chifra/accounts/#chifra-monitors">chifra monitors</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) to process

        delete : typing.Optional[bool]
            delete a monitor, but do not remove it

        undelete : typing.Optional[bool]
            undelete a previously deleted monitor

        remove : typing.Optional[bool]
            remove a previously deleted monitor

        clean : typing.Optional[bool]
            clean (i.e. remove duplicate appearances) from monitors, optionally clear stage

        list_ : typing.Optional[bool]
            list monitors in the cache (--verbose for more detail)

        count : typing.Optional[bool]
            show the number of active monitors (included deleted but not removed monitors)

        staged : typing.Optional[bool]
            for --clean, --list, and --count options only, include staged monitors

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
        AccountsMonitorsResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.monitors()


        asyncio.run(main())
        """
        _response = await self._raw_client.monitors(
            addrs=addrs,
            delete=delete,
            undelete=undelete,
            remove=remove,
            clean=clean,
            list_=list_,
            count=count,
            staged=staged,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def names(
        self,
        *,
        terms: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        expand: typing.Optional[bool] = None,
        match_case: typing.Optional[bool] = None,
        all_: typing.Optional[bool] = None,
        custom: typing.Optional[bool] = None,
        prefund: typing.Optional[bool] = None,
        addr: typing.Optional[bool] = None,
        tags: typing.Optional[bool] = None,
        clean: typing.Optional[bool] = None,
        regular: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        dry_run: typing.Optional[bool] = None,
        autoname: typing.Optional[str] = None,
        create: typing.Optional[str] = None,
        update: typing.Optional[str] = None,
        delete: typing.Optional[str] = None,
        undelete: typing.Optional[str] = None,
        remove: typing.Optional[str] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsNamesResponse:
        """
        Query addresses or names of well-known accounts. Corresponds to the <a href="/chifra/accounts/#chifra-names">chifra names</a> command line.

        Parameters
        ----------
        terms : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a space separated list of one or more search terms

        expand : typing.Optional[bool]
            expand search to include all fields (search name, address, and symbol otherwise)

        match_case : typing.Optional[bool]
            do case-sensitive search

        all_ : typing.Optional[bool]
            include all (including custom) names in the search

        custom : typing.Optional[bool]
            include only custom named accounts in the search

        prefund : typing.Optional[bool]
            include prefund accounts in the search

        addr : typing.Optional[bool]
            display only addresses in the results (useful for scripting, assumes --no_header)

        tags : typing.Optional[bool]
            export the list of tags and subtags only

        clean : typing.Optional[bool]
            clean the data (addrs to lower case, sort by addr)

        regular : typing.Optional[bool]
            only available with --clean, cleans regular names database

        count : typing.Optional[bool]
            return the number of names matching the search terms or other options

        dry_run : typing.Optional[bool]
            only available with --clean or --autoname, outputs changes to stdout instead of updating databases

        autoname : typing.Optional[str]
            an address assumed to be a token, added automatically to names database if true

        create : typing.Optional[str]
            create a new item

        update : typing.Optional[str]
            update an existing item

        delete : typing.Optional[str]
            delete the item, but do not remove it

        undelete : typing.Optional[str]
            undelete a previously deleted item

        remove : typing.Optional[str]
            remove a previously deleted item

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsNamesResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.names(
                terms=["terms"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.names(
            terms=terms,
            expand=expand,
            match_case=match_case,
            all_=all_,
            custom=custom,
            prefund=prefund,
            addr=addr,
            tags=tags,
            clean=clean,
            regular=regular,
            count=count,
            dry_run=dry_run,
            autoname=autoname,
            create=create,
            update=update,
            delete=delete,
            undelete=undelete,
            remove=remove,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def abis(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        known: typing.Optional[bool] = None,
        proxy_for: typing.Optional[str] = None,
        list_: typing.Optional[bool] = None,
        details: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        find: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hint: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        encode: typing.Optional[str] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsAbisResponse:
        """
        Fetches the ABI for a smart contract. Corresponds to the <a href="/chifra/accounts/#chifra-abis">chifra abis</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            a list of one or more smart contracts whose ABIs to display

        known : typing.Optional[bool]
            load common 'known' ABIs from cache

        proxy_for : typing.Optional[str]
            redirects the query to this implementation

        list_ : typing.Optional[bool]
            a list of downloaded abi files

        details : typing.Optional[bool]
            show the functions and events instead of summaries for all abi files

        count : typing.Optional[bool]
            show the number of abis downloaded

        find : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            search for function or event declarations given a four- or 32-byte code(s)

        hint : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            for the --find option only, provide hints to speed up the search

        encode : typing.Optional[str]
            generate the 32-byte encoding for a given canonical function or event signature

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
        AccountsAbisResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.abis(
                addrs=["addrs"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abis(
            addrs=addrs,
            known=known,
            proxy_for=proxy_for,
            list_=list_,
            details=details,
            count=count,
            find=find,
            hint=hint,
            encode=encode,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data
