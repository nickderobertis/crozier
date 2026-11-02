

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.reading import Reading
from .raw_client import AsyncRawBaysClient, RawBaysClient


OMIT = typing.cast(typing.Any, ...)


class BaysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBaysClient
        """
        return self._raw_client

    def set_targets(
        self,
        bay_id: str,
        *,
        celsius: float,
        humidity: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bay_id : str

        celsius : float

        humidity : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bays.set_targets(
            bay_id="bayId",
            celsius=1.1,
        )
        """
        _response = self._raw_client.set_targets(
            bay_id, celsius=celsius, humidity=humidity, request_options=request_options
        )
        return _response.data

    def submit_readings(
        self, *, request: typing.Sequence[Reading], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[Reading]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, Reading

        client = FernApi()
        client.bays.submit_readings(
            request=[
                Reading(
                    sensor="sensor",
                    value=1.1,
                )
            ],
        )
        """
        _response = self._raw_client.submit_readings(request=request, request_options=request_options)
        return _response.data


class AsyncBaysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBaysClient
        """
        return self._raw_client

    async def set_targets(
        self,
        bay_id: str,
        *,
        celsius: float,
        humidity: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bay_id : str

        celsius : float

        humidity : typing.Optional[float]

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
            await client.bays.set_targets(
                bay_id="bayId",
                celsius=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_targets(
            bay_id, celsius=celsius, humidity=humidity, request_options=request_options
        )
        return _response.data

    async def submit_readings(
        self, *, request: typing.Sequence[Reading], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[Reading]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Reading

        client = AsyncFernApi()


        async def main() -> None:
            await client.bays.submit_readings(
                request=[
                    Reading(
                        sensor="sensor",
                        value=1.1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_readings(request=request, request_options=request_options)
        return _response.data
