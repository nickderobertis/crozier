

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOtherClient, RawOtherClient
from .types.other_slurp_request_parts_item import OtherSlurpRequestPartsItem
from .types.other_slurp_request_source import OtherSlurpRequestSource
from .types.other_slurp_response import OtherSlurpResponse


class OtherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOtherClient
        """
        return self._raw_client

    def slurp(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parts: typing.Optional[
            typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]
        ] = None,
        appearances: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        source: typing.Optional[OtherSlurpRequestSource] = None,
        count: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtherSlurpResponse:
        """
        Fetch data from Etherscan and other APIs for any address. Corresponds to the <a href="/chifra/other/#chifra-slurp">chifra slurp</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses to slurp from Etherscan

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional range of blocks to slurp

        parts : typing.Optional[typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]]
            which types of transactions to request

        appearances : typing.Optional[bool]
            show only the blocknumber.tx_id appearances of the exported transactions

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        source : typing.Optional[OtherSlurpRequestSource]
            the source of the slurped data

        count : typing.Optional[bool]
            for --appearances mode only, display only the count of records

        page : typing.Optional[int]
            the page to retrieve (page number)

        page_id : typing.Optional[str]
            the page to retrieve (page ID)

        per_page : typing.Optional[int]
            the number of records to request on each page

        sleep : typing.Optional[float]
            seconds to sleep between requests

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
        OtherSlurpResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.slurp(
            addrs=["addrs"],
        )
        """
        _response = self._raw_client.slurp(
            addrs=addrs,
            blocks=blocks,
            parts=parts,
            appearances=appearances,
            articulate=articulate,
            source=source,
            count=count,
            page=page,
            page_id=page_id,
            per_page=per_page,
            sleep=sleep,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data


class AsyncOtherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOtherClient
        """
        return self._raw_client

    async def slurp(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parts: typing.Optional[
            typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]
        ] = None,
        appearances: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        source: typing.Optional[OtherSlurpRequestSource] = None,
        count: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtherSlurpResponse:
        """
        Fetch data from Etherscan and other APIs for any address. Corresponds to the <a href="/chifra/other/#chifra-slurp">chifra slurp</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses to slurp from Etherscan

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional range of blocks to slurp

        parts : typing.Optional[typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]]
            which types of transactions to request

        appearances : typing.Optional[bool]
            show only the blocknumber.tx_id appearances of the exported transactions

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        source : typing.Optional[OtherSlurpRequestSource]
            the source of the slurped data

        count : typing.Optional[bool]
            for --appearances mode only, display only the count of records

        page : typing.Optional[int]
            the page to retrieve (page number)

        page_id : typing.Optional[str]
            the page to retrieve (page ID)

        per_page : typing.Optional[int]
            the number of records to request on each page

        sleep : typing.Optional[float]
            seconds to sleep between requests

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
        OtherSlurpResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.slurp(
                addrs=["addrs"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurp(
            addrs=addrs,
            blocks=blocks,
            parts=parts,
            appearances=appearances,
            articulate=articulate,
            source=source,
            count=count,
            page=page,
            page_id=page_id,
            per_page=per_page,
            sleep=sleep,
            chain=chain,
            no_header=no_header,
            cache=cache,
            decache=decache,
            ether=ether,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data
