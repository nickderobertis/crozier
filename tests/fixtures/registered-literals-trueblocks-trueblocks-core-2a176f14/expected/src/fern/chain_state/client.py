

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChainStateClient, RawChainStateClient
from .types.chainstate_state_request_parts_item import ChainstateStateRequestPartsItem
from .types.chainstate_state_response import ChainstateStateResponse
from .types.chainstate_tokens_request_parts_item import ChainstateTokensRequestPartsItem
from .types.chainstate_tokens_response import ChainstateTokensResponse


class ChainStateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChainStateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChainStateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChainStateClient
        """
        return self._raw_client

    def chainstate_state(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parts: typing.Optional[
            typing.Union[ChainstateStateRequestPartsItem, typing.Sequence[ChainstateStateRequestPartsItem]]
        ] = None,
        changes: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        call: typing.Optional[bool] = None,
        calldata: typing.Optional[str] = None,
        articulate: typing.Optional[bool] = None,
        proxy_for: typing.Optional[str] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChainstateStateResponse:
        """
        Retrieve account balance(s) for one or more addresses at given block(s). Corresponds to the <a href="/chifra/chainstate/#chifra-state">chifra state</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) from which to retrieve balances

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional list of one or more blocks at which to report balances, defaults to 'latest'

        parts : typing.Optional[typing.Union[ChainstateStateRequestPartsItem, typing.Sequence[ChainstateStateRequestPartsItem]]]
            control which state to export

        changes : typing.Optional[bool]
            only report a balance when it changes from one block to the next

        no_zero : typing.Optional[bool]
            suppress the display of zero balance accounts

        call : typing.Optional[bool]
            write-only call (a query) to a smart contract

        calldata : typing.Optional[str]
            for commands (--call or --send), provides the call data (in various forms) for the command (may be empty for --send)

        articulate : typing.Optional[bool]
            for commands only, articulate the retrieved data if ABIs can be found

        proxy_for : typing.Optional[str]
            for commands only, redirects calls to this implementation

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
        ChainstateStateResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_state.chainstate_state(
            addrs=["addrs"],
        )
        """
        _response = self._raw_client.chainstate_state(
            addrs=addrs,
            blocks=blocks,
            parts=parts,
            changes=changes,
            no_zero=no_zero,
            call=call,
            calldata=calldata,
            articulate=articulate,
            proxy_for=proxy_for,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def chainstate_tokens(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        approvals: typing.Optional[bool] = None,
        parts: typing.Optional[
            typing.Union[ChainstateTokensRequestPartsItem, typing.Sequence[ChainstateTokensRequestPartsItem]]
        ] = None,
        by_acct: typing.Optional[bool] = None,
        changes: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChainstateTokensResponse:
        """
        Retrieve token balance(s) for one or more addresses at given block(s). Corresponds to the <a href="/chifra/chainstate/#chifra-tokens">chifra tokens</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            two or more addresses (one for --approvals), the first is an ERC20 token, balances for the rest are reported

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional list of one or more blocks at which to report balances, defaults to 'latest'

        approvals : typing.Optional[bool]
            returns all open approvals for the given address(es)

        parts : typing.Optional[typing.Union[ChainstateTokensRequestPartsItem, typing.Sequence[ChainstateTokensRequestPartsItem]]]
            which parts of the token information to retrieve

        by_acct : typing.Optional[bool]
            consider each address an ERC20 token except the last, whose balance is reported for each token

        changes : typing.Optional[bool]
            only report a balance when it changes from one block to the next

        no_zero : typing.Optional[bool]
            suppress the display of zero balance accounts

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
        ChainstateTokensResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chain_state.chainstate_tokens(
            addrs=["addrs"],
        )
        """
        _response = self._raw_client.chainstate_tokens(
            addrs=addrs,
            blocks=blocks,
            approvals=approvals,
            parts=parts,
            by_acct=by_acct,
            changes=changes,
            no_zero=no_zero,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data


class AsyncChainStateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChainStateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChainStateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChainStateClient
        """
        return self._raw_client

    async def chainstate_state(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parts: typing.Optional[
            typing.Union[ChainstateStateRequestPartsItem, typing.Sequence[ChainstateStateRequestPartsItem]]
        ] = None,
        changes: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        call: typing.Optional[bool] = None,
        calldata: typing.Optional[str] = None,
        articulate: typing.Optional[bool] = None,
        proxy_for: typing.Optional[str] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChainstateStateResponse:
        """
        Retrieve account balance(s) for one or more addresses at given block(s). Corresponds to the <a href="/chifra/chainstate/#chifra-state">chifra state</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses (0x...) from which to retrieve balances

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional list of one or more blocks at which to report balances, defaults to 'latest'

        parts : typing.Optional[typing.Union[ChainstateStateRequestPartsItem, typing.Sequence[ChainstateStateRequestPartsItem]]]
            control which state to export

        changes : typing.Optional[bool]
            only report a balance when it changes from one block to the next

        no_zero : typing.Optional[bool]
            suppress the display of zero balance accounts

        call : typing.Optional[bool]
            write-only call (a query) to a smart contract

        calldata : typing.Optional[str]
            for commands (--call or --send), provides the call data (in various forms) for the command (may be empty for --send)

        articulate : typing.Optional[bool]
            for commands only, articulate the retrieved data if ABIs can be found

        proxy_for : typing.Optional[str]
            for commands only, redirects calls to this implementation

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
        ChainstateStateResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_state.chainstate_state(
                addrs=["addrs"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chainstate_state(
            addrs=addrs,
            blocks=blocks,
            parts=parts,
            changes=changes,
            no_zero=no_zero,
            call=call,
            calldata=calldata,
            articulate=articulate,
            proxy_for=proxy_for,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def chainstate_tokens(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        approvals: typing.Optional[bool] = None,
        parts: typing.Optional[
            typing.Union[ChainstateTokensRequestPartsItem, typing.Sequence[ChainstateTokensRequestPartsItem]]
        ] = None,
        by_acct: typing.Optional[bool] = None,
        changes: typing.Optional[bool] = None,
        no_zero: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChainstateTokensResponse:
        """
        Retrieve token balance(s) for one or more addresses at given block(s). Corresponds to the <a href="/chifra/chainstate/#chifra-tokens">chifra tokens</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            two or more addresses (one for --approvals), the first is an ERC20 token, balances for the rest are reported

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional list of one or more blocks at which to report balances, defaults to 'latest'

        approvals : typing.Optional[bool]
            returns all open approvals for the given address(es)

        parts : typing.Optional[typing.Union[ChainstateTokensRequestPartsItem, typing.Sequence[ChainstateTokensRequestPartsItem]]]
            which parts of the token information to retrieve

        by_acct : typing.Optional[bool]
            consider each address an ERC20 token except the last, whose balance is reported for each token

        changes : typing.Optional[bool]
            only report a balance when it changes from one block to the next

        no_zero : typing.Optional[bool]
            suppress the display of zero balance accounts

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
        ChainstateTokensResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chain_state.chainstate_tokens(
                addrs=["addrs"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chainstate_tokens(
            addrs=addrs,
            blocks=blocks,
            approvals=approvals,
            parts=parts,
            by_acct=by_acct,
            changes=changes,
            no_zero=no_zero,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data
