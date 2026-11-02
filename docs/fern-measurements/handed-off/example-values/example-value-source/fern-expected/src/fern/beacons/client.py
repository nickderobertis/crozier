

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBeaconsClient, RawBeaconsClient


class BeaconsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBeaconsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBeaconsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBeaconsClient
        """
        return self._raw_client

    def set_beacon_script(self, beacon_code: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        An inline path parameter's own example beside a text body.

        Parameters
        ----------
        beacon_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacons.set_beacon_script(
            beacon_code="bcn:west-4",
        )
        """
        _response = self._raw_client.set_beacon_script(beacon_code, request_options=request_options)
        return _response.data

    def set_lantern_script(self, lantern_code: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        A referenced path parameter's own example beside a text body.

        Parameters
        ----------
        lantern_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacons.set_lantern_script(
            lantern_code="ltn:east-2",
        )
        """
        _response = self._raw_client.set_lantern_script(lantern_code, request_options=request_options)
        return _response.data

    def get_lantern_manual(self, lantern_code: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        A referenced path parameter's own example beside an XML answer.

        Parameters
        ----------
        lantern_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacons.get_lantern_manual(
            lantern_code="ltn:east-2",
        )
        """
        _response = self._raw_client.get_lantern_manual(lantern_code, request_options=request_options)
        return _response.data


class AsyncBeaconsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBeaconsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBeaconsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBeaconsClient
        """
        return self._raw_client

    async def set_beacon_script(
        self, beacon_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        An inline path parameter's own example beside a text body.

        Parameters
        ----------
        beacon_code : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacons.set_beacon_script(
                beacon_code="bcn:west-4",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_beacon_script(beacon_code, request_options=request_options)
        return _response.data

    async def set_lantern_script(
        self, lantern_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        A referenced path parameter's own example beside a text body.

        Parameters
        ----------
        lantern_code : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacons.set_lantern_script(
                lantern_code="ltn:east-2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_lantern_script(lantern_code, request_options=request_options)
        return _response.data

    async def get_lantern_manual(
        self, lantern_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        A referenced path parameter's own example beside an XML answer.

        Parameters
        ----------
        lantern_code : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacons.get_lantern_manual(
                lantern_code="ltn:east-2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lantern_manual(lantern_code, request_options=request_options)
        return _response.data
