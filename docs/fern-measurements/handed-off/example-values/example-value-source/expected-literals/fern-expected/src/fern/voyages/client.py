

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.customs_stamp import CustomsStamp
from ..types.watch_rota import WatchRota
from .raw_client import AsyncRawVoyagesClient, RawVoyagesClient
from .types.plan_voyage_rota_response import PlanVoyageRotaResponse
from .types.set_voyage_watch_response import SetVoyageWatchResponse


OMIT = typing.cast(typing.Any, ...)


class VoyagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoyagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoyagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoyagesClient
        """
        return self._raw_client

    def set_voyage_watch(
        self, voyage_id: str, *, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> SetVoyageWatchResponse:
        """
        A nested field the request example gives an empty array.

        Parameters
        ----------
        voyage_id : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetVoyageWatchResponse
            Set

        Examples
        --------
        from fern import FernApi, WatchRota

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.voyages.set_voyage_watch(
            voyage_id="voyageId",
            rota=WatchRota(
                days=[1, 3, 5],
                cadence="daily",
            ),
        )
        """
        _response = self._raw_client.set_voyage_watch(voyage_id, rota=rota, request_options=request_options)
        return _response.data

    def plan_voyage_rota(
        self, voyage_id: str, *, crew: str, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> PlanVoyageRotaResponse:
        """
        The same field left out of a referenced body's referenced named example.

        Parameters
        ----------
        voyage_id : str

        crew : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlanVoyageRotaResponse
            Planned

        Examples
        --------
        from fern import FernApi, WatchRota

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.voyages.plan_voyage_rota(
            voyage_id="voyageId",
            crew="starboard",
            rota=WatchRota(
                days=[1, 3, 5],
                cadence="daily",
            ),
        )
        """
        _response = self._raw_client.plan_voyage_rota(voyage_id, crew=crew, rota=rota, request_options=request_options)
        return _response.data

    def file_customs_stamps(
        self,
        voyage_id: str,
        *,
        request: typing.Sequence[CustomsStamp],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        An array body of a referenced schema whose schema-level example writes unquoted YAML timestamps, on an int64 field and on a date-time field.

        Parameters
        ----------
        voyage_id : str

        request : typing.Sequence[CustomsStamp]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import CustomsStamp, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.voyages.file_customs_stamps(
            voyage_id="voyageId",
            request=[
                CustomsStamp(
                    port="Falmouth",
                    punched_millis=1000000,
                    inked_at=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.file_customs_stamps(voyage_id, request=request, request_options=request_options)
        return _response.data


class AsyncVoyagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoyagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoyagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoyagesClient
        """
        return self._raw_client

    async def set_voyage_watch(
        self, voyage_id: str, *, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> SetVoyageWatchResponse:
        """
        A nested field the request example gives an empty array.

        Parameters
        ----------
        voyage_id : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetVoyageWatchResponse
            Set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WatchRota

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.voyages.set_voyage_watch(
                voyage_id="voyageId",
                rota=WatchRota(
                    days=[1, 3, 5],
                    cadence="daily",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_voyage_watch(voyage_id, rota=rota, request_options=request_options)
        return _response.data

    async def plan_voyage_rota(
        self, voyage_id: str, *, crew: str, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> PlanVoyageRotaResponse:
        """
        The same field left out of a referenced body's referenced named example.

        Parameters
        ----------
        voyage_id : str

        crew : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlanVoyageRotaResponse
            Planned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WatchRota

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.voyages.plan_voyage_rota(
                voyage_id="voyageId",
                crew="starboard",
                rota=WatchRota(
                    days=[1, 3, 5],
                    cadence="daily",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.plan_voyage_rota(
            voyage_id, crew=crew, rota=rota, request_options=request_options
        )
        return _response.data

    async def file_customs_stamps(
        self,
        voyage_id: str,
        *,
        request: typing.Sequence[CustomsStamp],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        An array body of a referenced schema whose schema-level example writes unquoted YAML timestamps, on an int64 field and on a date-time field.

        Parameters
        ----------
        voyage_id : str

        request : typing.Sequence[CustomsStamp]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, CustomsStamp

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.voyages.file_customs_stamps(
                voyage_id="voyageId",
                request=[
                    CustomsStamp(
                        port="Falmouth",
                        punched_millis=1000000,
                        inked_at=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_customs_stamps(
            voyage_id, request=request, request_options=request_options
        )
        return _response.data
