

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_beds_request_shade import ListBedsRequestShade
from .raw_client import AsyncRawBedsClient, RawBedsClient


class BedsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBedsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBedsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBedsClient
        """
        return self._raw_client

    def list_beds(
        self,
        *,
        soil: typing.Optional[str] = None,
        depth: typing.Optional[int] = None,
        crops: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rows: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        trays: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        shade: typing.Optional[ListBedsRequestShade] = None,
        pots: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        soil : typing.Optional[str]

        depth : typing.Optional[int]

        crops : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        rows : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        trays : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        shade : typing.Optional[ListBedsRequestShade]

        pots : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Beds.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.beds.list_beds(
            soil="soil",
            rows=[],
            trays=[],
            shade="shade",
            pots=[1],
        )
        """
        _response = self._raw_client.list_beds(
            soil=soil,
            depth=depth,
            crops=crops,
            rows=rows,
            trays=trays,
            shade=shade,
            pots=pots,
            request_options=request_options,
        )
        return _response.data

    def get_bed(self, bed_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        bed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One bed.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.beds.get_bed(
            bed_id="bed_id",
        )
        """
        _response = self._raw_client.get_bed(bed_id, request_options=request_options)
        return _response.data


class AsyncBedsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBedsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBedsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBedsClient
        """
        return self._raw_client

    async def list_beds(
        self,
        *,
        soil: typing.Optional[str] = None,
        depth: typing.Optional[int] = None,
        crops: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rows: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        trays: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        shade: typing.Optional[ListBedsRequestShade] = None,
        pots: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        soil : typing.Optional[str]

        depth : typing.Optional[int]

        crops : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        rows : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        trays : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        shade : typing.Optional[ListBedsRequestShade]

        pots : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Beds.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.beds.list_beds(
                soil="soil",
                rows=[],
                trays=[],
                shade="shade",
                pots=[1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_beds(
            soil=soil,
            depth=depth,
            crops=crops,
            rows=rows,
            trays=trays,
            shade=shade,
            pots=pots,
            request_options=request_options,
        )
        return _response.data

    async def get_bed(self, bed_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        bed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One bed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.beds.get_bed(
                bed_id="bed_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bed(bed_id, request_options=request_options)
        return _response.data
