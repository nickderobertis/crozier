

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHivesClient, RawHivesClient


OMIT = typing.cast(typing.Any, ...)


class HivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHivesClient
        """
        return self._raw_client

    def register_hive(
        self, *, apiary: str, queen_marked: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        apiary : str
            The apiary the hive stands in.

        queen_marked : bool
            Whether the queen carries a paint mark.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.hives.register_hive(
            apiary="apiary",
            queen_marked=True,
        )
        """
        _response = self._raw_client.register_hive(
            apiary=apiary, queen_marked=queen_marked, request_options=request_options
        )
        return _response.data

    def upload_frame(
        self, hive_id: str, *, photo: core.File, position: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        hive_id : str

        photo : core.File
            See core.File for more documentation

        position : int
            The frame's slot, counted from the entrance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.hives.upload_frame(
            hive_id="hiveId",
            position=1,
        )
        """
        _response = self._raw_client.upload_frame(
            hive_id, photo=photo, position=position, request_options=request_options
        )
        return _response.data


class AsyncHivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHivesClient
        """
        return self._raw_client

    async def register_hive(
        self, *, apiary: str, queen_marked: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        apiary : str
            The apiary the hive stands in.

        queen_marked : bool
            Whether the queen carries a paint mark.

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
            await client.hives.register_hive(
                apiary="apiary",
                queen_marked=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_hive(
            apiary=apiary, queen_marked=queen_marked, request_options=request_options
        )
        return _response.data

    async def upload_frame(
        self, hive_id: str, *, photo: core.File, position: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        hive_id : str

        photo : core.File
            See core.File for more documentation

        position : int
            The frame's slot, counted from the entrance.

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
            await client.hives.upload_frame(
                hive_id="hiveId",
                position=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_frame(
            hive_id, photo=photo, position=position, request_options=request_options
        )
        return _response.data
