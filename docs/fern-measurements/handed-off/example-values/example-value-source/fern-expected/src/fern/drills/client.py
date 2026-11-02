

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDrillsClient, RawDrillsClient
from .types.start_drill_request_settings_value import StartDrillRequestSettingsValue
from .types.start_drill_response import StartDrillResponse


OMIT = typing.cast(typing.Any, ...)


class DrillsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDrillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDrillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDrillsClient
        """
        return self._raw_client

    def start_drill(
        self,
        *,
        crew: str,
        settings: typing.Dict[str, StartDrillRequestSettingsValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartDrillResponse:
        """
        A map property's schema-level example.

        Parameters
        ----------
        crew : str

        settings : typing.Dict[str, StartDrillRequestSettingsValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartDrillResponse
            Started

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.drills.start_drill(
            crew="crew",
            settings={"night": True, "station": "Penlee"},
        )
        """
        _response = self._raw_client.start_drill(crew=crew, settings=settings, request_options=request_options)
        return _response.data


class AsyncDrillsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDrillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDrillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDrillsClient
        """
        return self._raw_client

    async def start_drill(
        self,
        *,
        crew: str,
        settings: typing.Dict[str, StartDrillRequestSettingsValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartDrillResponse:
        """
        A map property's schema-level example.

        Parameters
        ----------
        crew : str

        settings : typing.Dict[str, StartDrillRequestSettingsValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartDrillResponse
            Started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.drills.start_drill(
                crew="crew",
                settings={"night": True, "station": "Penlee"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_drill(crew=crew, settings=settings, request_options=request_options)
        return _response.data
