

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.berth import Berth
from .raw_client import AsyncRawBerthsClient, RawBerthsClient


class BerthsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBerthsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBerthsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBerthsClient
        """
        return self._raw_client

    def list_berths(
        self,
        *,
        zone: str,
        codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Berth]:
        """
        Parameters
        ----------
        zone : str

        codes : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Berth]
            The berths in the zone.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            strict_mode="YOUR_STRICT_MODE",
            tenant_code="YOUR_TENANT_CODE",
            shift_number="YOUR_SHIFT_NUMBER",
        )
        client.berths.list_berths(
            zone="zone",
            codes=["codes[]"],
        )
        """
        _response = self._raw_client.list_berths(zone=zone, codes=codes, request_options=request_options)
        return _response.data

    def release_berths(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            strict_mode="YOUR_STRICT_MODE",
            tenant_code="YOUR_TENANT_CODE",
            shift_number="YOUR_SHIFT_NUMBER",
        )
        client.berths.release_berths(
            ids=["B-7"],
        )
        """
        _response = self._raw_client.release_berths(ids=ids, request_options=request_options)
        return _response.data


class AsyncBerthsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBerthsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBerthsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBerthsClient
        """
        return self._raw_client

    async def list_berths(
        self,
        *,
        zone: str,
        codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Berth]:
        """
        Parameters
        ----------
        zone : str

        codes : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Berth]
            The berths in the zone.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            strict_mode="YOUR_STRICT_MODE",
            tenant_code="YOUR_TENANT_CODE",
            shift_number="YOUR_SHIFT_NUMBER",
        )


        async def main() -> None:
            await client.berths.list_berths(
                zone="zone",
                codes=["codes[]"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_berths(zone=zone, codes=codes, request_options=request_options)
        return _response.data

    async def release_berths(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            strict_mode="YOUR_STRICT_MODE",
            tenant_code="YOUR_TENANT_CODE",
            shift_number="YOUR_SHIFT_NUMBER",
        )


        async def main() -> None:
            await client.berths.release_berths(
                ids=["B-7"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release_berths(ids=ids, request_options=request_options)
        return _response.data
