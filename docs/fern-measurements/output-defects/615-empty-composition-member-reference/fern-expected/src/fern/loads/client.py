

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.kiln import Kiln
from ..types.load import Load
from ..types.load_noted_kiln import LoadNotedKiln
from ..types.load_reserved_kiln import LoadReservedKiln
from .raw_client import AsyncRawLoadsClient, RawLoadsClient
from .types.transfer_load_request_fallback import TransferLoadRequestFallback


OMIT = typing.cast(typing.Any, ...)


class LoadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLoadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoadsClient
        """
        return self._raw_client

    def schedule_load(
        self,
        *,
        label: str,
        kiln: Kiln,
        overflow_kiln: typing.Optional[Kiln] = OMIT,
        usual_kiln: typing.Optional[Kiln] = OMIT,
        solo_kiln: typing.Optional[Kiln] = OMIT,
        noted_kiln: typing.Optional[LoadNotedKiln] = OMIT,
        reserved_kiln: typing.Optional[LoadReservedKiln] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Load:
        """
        Parameters
        ----------
        label : str

        kiln : Kiln

        overflow_kiln : typing.Optional[Kiln]

        usual_kiln : typing.Optional[Kiln]

        solo_kiln : typing.Optional[Kiln]

        noted_kiln : typing.Optional[LoadNotedKiln]
            Kiln named in the firing log.

        reserved_kiln : typing.Optional[LoadReservedKiln]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Load
            The scheduled load.

        Examples
        --------
        from fern import FernApi, Kiln

        client = FernApi()
        client.loads.schedule_load(
            label="label",
            kiln=Kiln(
                name="name",
            ),
        )
        """
        _response = self._raw_client.schedule_load(
            label=label,
            kiln=kiln,
            overflow_kiln=overflow_kiln,
            usual_kiln=usual_kiln,
            solo_kiln=solo_kiln,
            noted_kiln=noted_kiln,
            reserved_kiln=reserved_kiln,
            request_options=request_options,
        )
        return _response.data

    def transfer_load(
        self,
        load_id: str,
        *,
        destination: Kiln,
        fallback: typing.Optional[TransferLoadRequestFallback] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Load:
        """
        Parameters
        ----------
        load_id : str

        destination : Kiln

        fallback : typing.Optional[TransferLoadRequestFallback]
            Kiln to use when the destination is full.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Load
            The moved load.

        Examples
        --------
        from fern import FernApi, Kiln

        client = FernApi()
        client.loads.transfer_load(
            load_id="loadId",
            destination=Kiln(
                name="name",
            ),
        )
        """
        _response = self._raw_client.transfer_load(
            load_id, destination=destination, fallback=fallback, request_options=request_options
        )
        return _response.data


class AsyncLoadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLoadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoadsClient
        """
        return self._raw_client

    async def schedule_load(
        self,
        *,
        label: str,
        kiln: Kiln,
        overflow_kiln: typing.Optional[Kiln] = OMIT,
        usual_kiln: typing.Optional[Kiln] = OMIT,
        solo_kiln: typing.Optional[Kiln] = OMIT,
        noted_kiln: typing.Optional[LoadNotedKiln] = OMIT,
        reserved_kiln: typing.Optional[LoadReservedKiln] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Load:
        """
        Parameters
        ----------
        label : str

        kiln : Kiln

        overflow_kiln : typing.Optional[Kiln]

        usual_kiln : typing.Optional[Kiln]

        solo_kiln : typing.Optional[Kiln]

        noted_kiln : typing.Optional[LoadNotedKiln]
            Kiln named in the firing log.

        reserved_kiln : typing.Optional[LoadReservedKiln]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Load
            The scheduled load.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Kiln

        client = AsyncFernApi()


        async def main() -> None:
            await client.loads.schedule_load(
                label="label",
                kiln=Kiln(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schedule_load(
            label=label,
            kiln=kiln,
            overflow_kiln=overflow_kiln,
            usual_kiln=usual_kiln,
            solo_kiln=solo_kiln,
            noted_kiln=noted_kiln,
            reserved_kiln=reserved_kiln,
            request_options=request_options,
        )
        return _response.data

    async def transfer_load(
        self,
        load_id: str,
        *,
        destination: Kiln,
        fallback: typing.Optional[TransferLoadRequestFallback] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Load:
        """
        Parameters
        ----------
        load_id : str

        destination : Kiln

        fallback : typing.Optional[TransferLoadRequestFallback]
            Kiln to use when the destination is full.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Load
            The moved load.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Kiln

        client = AsyncFernApi()


        async def main() -> None:
            await client.loads.transfer_load(
                load_id="loadId",
                destination=Kiln(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_load(
            load_id, destination=destination, fallback=fallback, request_options=request_options
        )
        return _response.data
