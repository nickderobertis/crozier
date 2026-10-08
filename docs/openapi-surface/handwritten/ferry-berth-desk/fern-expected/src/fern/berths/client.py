

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.berth_status import BerthStatus
from .raw_client import AsyncRawBerthsClient, RawBerthsClient


OMIT = typing.cast(typing.Any, ...)


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

    def checkstatus(self, berth_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> BerthStatus:
        """
        Parameters
        ----------
        berth_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BerthStatus
            The berth's status.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.berths.checkstatus(
            berth_id=1,
        )
        """
        _response = self._raw_client.checkstatus(berth_id, request_options=request_options)
        return _response.data

    def assignvessel(
        self, berth_id: int, *, vessel: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        berth_id : int

        vessel : str
            The vessel's call sign.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.berths.assignvessel(
            berth_id=1,
            vessel="vessel",
        )
        """
        _response = self._raw_client.assignvessel(berth_id, vessel=vessel, request_options=request_options)
        return _response.data

    def release_hold(self, berth_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        berth_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.berths.release_hold(
            berth_id=1,
        )
        """
        _response = self._raw_client.release_hold(berth_id, request_options=request_options)
        return _response.data

    def all_(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[BerthStatus]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BerthStatus]
            Every berth.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.berths.all_()
        """
        _response = self._raw_client.all_(request_options=request_options)
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

    async def checkstatus(
        self, berth_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BerthStatus:
        """
        Parameters
        ----------
        berth_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BerthStatus
            The berth's status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.berths.checkstatus(
                berth_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.checkstatus(berth_id, request_options=request_options)
        return _response.data

    async def assignvessel(
        self, berth_id: int, *, vessel: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        berth_id : int

        vessel : str
            The vessel's call sign.

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
            await client.berths.assignvessel(
                berth_id=1,
                vessel="vessel",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.assignvessel(berth_id, vessel=vessel, request_options=request_options)
        return _response.data

    async def release_hold(self, berth_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        berth_id : int

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
            await client.berths.release_hold(
                berth_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release_hold(berth_id, request_options=request_options)
        return _response.data

    async def all_(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[BerthStatus]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BerthStatus]
            Every berth.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.berths.all_()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(request_options=request_options)
        return _response.data
