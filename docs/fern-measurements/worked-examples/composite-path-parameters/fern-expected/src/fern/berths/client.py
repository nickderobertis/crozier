

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.berth_key import BerthKey
from ..types.hull_ids import HullIds
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

    def get_berth(self, berth: BerthKey, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        berth : BerthKey

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.get_berth(berth, request_options=request_options)
        return _response.data

    def get_hulls(self, hull_ids: HullIds, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        hull_ids : HullIds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.berths.get_hulls(
            hull_ids="hullIds",
        )
        """
        _response = self._raw_client.get_hulls(hull_ids, request_options=request_options)
        return _response.data

    def get_tides(
        self, marks: typing.Dict[str, str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        marks : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.berths.get_tides(
            marks="marks",
        )
        """
        _response = self._raw_client.get_tides(marks, request_options=request_options)
        return _response.data

    def get_logs(
        self, stamps: typing.Dict[str, dt.datetime], *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        stamps : typing.Dict[str, dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.berths.get_logs(
            stamps="stamps",
        )
        """
        _response = self._raw_client.get_logs(stamps, request_options=request_options)
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

    async def get_berth(self, berth: BerthKey, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        berth : BerthKey

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.get_berth(berth, request_options=request_options)
        return _response.data

    async def get_hulls(self, hull_ids: HullIds, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        hull_ids : HullIds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.berths.get_hulls(
                hull_ids="hullIds",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hulls(hull_ids, request_options=request_options)
        return _response.data

    async def get_tides(
        self, marks: typing.Dict[str, str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        marks : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.berths.get_tides(
                marks="marks",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tides(marks, request_options=request_options)
        return _response.data

    async def get_logs(
        self, stamps: typing.Dict[str, dt.datetime], *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        stamps : typing.Dict[str, dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.berths.get_logs(
                stamps="stamps",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_logs(stamps, request_options=request_options)
        return _response.data
