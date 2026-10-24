

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.decode_swapstring_response import DecodeSwapstringResponse
from ..types.empty_response import EmptyResponse
from ..types.get_swap_response import GetSwapResponse
from ..types.list_swaps_response import ListSwapsResponse
from ..types.maker_init_response import MakerInitResponse
from .raw_client import AsyncRawSwapsClient, RawSwapsClient


OMIT = typing.cast(typing.Any, ...)


class SwapsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSwapsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSwapsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSwapsClient
        """
        return self._raw_client

    def decode_a_swapstring(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DecodeSwapstringResponse:
        """
        Decode the provided swapstring

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecodeSwapstringResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.swaps.decode_a_swapstring(
            swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
        )
        """
        _response = self._raw_client.decode_a_swapstring(swapstring=swapstring, request_options=request_options)
        return _response.data

    def get_a_swap(
        self, *, payment_hash: str, taker: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSwapResponse:
        """
        Get a swap by its payment hash

        Parameters
        ----------
        payment_hash : str

        taker : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSwapResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.swaps.get_a_swap(
            payment_hash="5ca5d81b482b4015e7b14df7a27fe0a38c226273604ffd3b008b752571811938",
            taker=False,
        )
        """
        _response = self._raw_client.get_a_swap(payment_hash=payment_hash, taker=taker, request_options=request_options)
        return _response.data

    def list_swaps(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSwapsResponse:
        """
        List the node's swaps

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSwapsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.swaps.list_swaps()
        """
        _response = self._raw_client.list_swaps(request_options=request_options)
        return _response.data

    def execute_a_maker_swap(
        self,
        *,
        swapstring: str,
        payment_secret: str,
        taker_pubkey: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Execute a swap on the maker side

        Parameters
        ----------
        swapstring : str

        payment_secret : str

        taker_pubkey : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.swaps.execute_a_maker_swap(
            swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
            payment_secret="777a7756c620868199ed5fdc35bee4095b5709d543e5c2bf0494396bf27d2ea2",
            taker_pubkey="02270dadcd6e7ba0ef707dac72acccae1a3607453a8dd2aef36ff3be4e0d31f043",
        )
        """
        _response = self._raw_client.execute_a_maker_swap(
            swapstring=swapstring,
            payment_secret=payment_secret,
            taker_pubkey=taker_pubkey,
            request_options=request_options,
        )
        return _response.data

    def init_a_maker_swap(
        self,
        *,
        qty_from: int,
        qty_to: int,
        timeout_sec: int,
        from_asset: typing.Optional[str] = OMIT,
        to_asset: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MakerInitResponse:
        """
        Init a swap on the maker side

        Parameters
        ----------
        qty_from : int

        qty_to : int

        timeout_sec : int

        from_asset : typing.Optional[str]

        to_asset : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MakerInitResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.swaps.init_a_maker_swap(
            qty_from=30,
            qty_to=10,
            timeout_sec=100,
        )
        """
        _response = self._raw_client.init_a_maker_swap(
            qty_from=qty_from,
            qty_to=qty_to,
            timeout_sec=timeout_sec,
            from_asset=from_asset,
            to_asset=to_asset,
            request_options=request_options,
        )
        return _response.data

    def accept_a_swap(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Accept a swap on the taker side

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.swaps.accept_a_swap(
            swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
        )
        """
        _response = self._raw_client.accept_a_swap(swapstring=swapstring, request_options=request_options)
        return _response.data


class AsyncSwapsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSwapsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSwapsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSwapsClient
        """
        return self._raw_client

    async def decode_a_swapstring(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DecodeSwapstringResponse:
        """
        Decode the provided swapstring

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecodeSwapstringResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.swaps.decode_a_swapstring(
                swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.decode_a_swapstring(swapstring=swapstring, request_options=request_options)
        return _response.data

    async def get_a_swap(
        self, *, payment_hash: str, taker: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSwapResponse:
        """
        Get a swap by its payment hash

        Parameters
        ----------
        payment_hash : str

        taker : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSwapResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.swaps.get_a_swap(
                payment_hash="5ca5d81b482b4015e7b14df7a27fe0a38c226273604ffd3b008b752571811938",
                taker=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_swap(
            payment_hash=payment_hash, taker=taker, request_options=request_options
        )
        return _response.data

    async def list_swaps(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSwapsResponse:
        """
        List the node's swaps

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSwapsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.swaps.list_swaps()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_swaps(request_options=request_options)
        return _response.data

    async def execute_a_maker_swap(
        self,
        *,
        swapstring: str,
        payment_secret: str,
        taker_pubkey: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Execute a swap on the maker side

        Parameters
        ----------
        swapstring : str

        payment_secret : str

        taker_pubkey : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.swaps.execute_a_maker_swap(
                swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
                payment_secret="777a7756c620868199ed5fdc35bee4095b5709d543e5c2bf0494396bf27d2ea2",
                taker_pubkey="02270dadcd6e7ba0ef707dac72acccae1a3607453a8dd2aef36ff3be4e0d31f043",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_a_maker_swap(
            swapstring=swapstring,
            payment_secret=payment_secret,
            taker_pubkey=taker_pubkey,
            request_options=request_options,
        )
        return _response.data

    async def init_a_maker_swap(
        self,
        *,
        qty_from: int,
        qty_to: int,
        timeout_sec: int,
        from_asset: typing.Optional[str] = OMIT,
        to_asset: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MakerInitResponse:
        """
        Init a swap on the maker side

        Parameters
        ----------
        qty_from : int

        qty_to : int

        timeout_sec : int

        from_asset : typing.Optional[str]

        to_asset : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MakerInitResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.swaps.init_a_maker_swap(
                qty_from=30,
                qty_to=10,
                timeout_sec=100,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.init_a_maker_swap(
            qty_from=qty_from,
            qty_to=qty_to,
            timeout_sec=timeout_sec,
            from_asset=from_asset,
            to_asset=to_asset,
            request_options=request_options,
        )
        return _response.data

    async def accept_a_swap(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Accept a swap on the taker side

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.swaps.accept_a_swap(
                swapstring="30/rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8/10/rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/1715896416/9d342c6ba006e24abee84a2e034a22d5e30c1f2599fb9c3574d46d3cde3d65a2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_a_swap(swapstring=swapstring, request_options=request_options)
        return _response.data
