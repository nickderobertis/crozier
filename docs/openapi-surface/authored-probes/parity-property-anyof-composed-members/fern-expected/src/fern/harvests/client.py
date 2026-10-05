

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.harvest import Harvest
from ..types.harvest_container import HarvestContainer
from ..types.harvest_grade import HarvestGrade
from ..types.harvest_holder import HarvestHolder
from ..types.harvest_yield_note import HarvestYieldNote
from .raw_client import AsyncRawHarvestsClient, RawHarvestsClient


OMIT = typing.cast(typing.Any, ...)


class HarvestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHarvestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHarvestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHarvestsClient
        """
        return self._raw_client

    def record_harvest(
        self,
        *,
        orchard: str,
        yield_note: typing.Optional[HarvestYieldNote] = OMIT,
        grade: typing.Optional[HarvestGrade] = OMIT,
        container: typing.Optional[HarvestContainer] = OMIT,
        holder: typing.Optional[HarvestHolder] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Harvest:
        """
        Parameters
        ----------
        orchard : str

        yield_note : typing.Optional[HarvestYieldNote]

        grade : typing.Optional[HarvestGrade]

        container : typing.Optional[HarvestContainer]

        holder : typing.Optional[HarvestHolder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Harvest
            The recorded harvest.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harvests.record_harvest(
            orchard="orchard",
        )
        """
        _response = self._raw_client.record_harvest(
            orchard=orchard,
            yield_note=yield_note,
            grade=grade,
            container=container,
            holder=holder,
            request_options=request_options,
        )
        return _response.data


class AsyncHarvestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHarvestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHarvestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHarvestsClient
        """
        return self._raw_client

    async def record_harvest(
        self,
        *,
        orchard: str,
        yield_note: typing.Optional[HarvestYieldNote] = OMIT,
        grade: typing.Optional[HarvestGrade] = OMIT,
        container: typing.Optional[HarvestContainer] = OMIT,
        holder: typing.Optional[HarvestHolder] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Harvest:
        """
        Parameters
        ----------
        orchard : str

        yield_note : typing.Optional[HarvestYieldNote]

        grade : typing.Optional[HarvestGrade]

        container : typing.Optional[HarvestContainer]

        holder : typing.Optional[HarvestHolder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Harvest
            The recorded harvest.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harvests.record_harvest(
                orchard="orchard",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_harvest(
            orchard=orchard,
            yield_note=yield_note,
            grade=grade,
            container=container,
            holder=holder,
            request_options=request_options,
        )
        return _response.data
