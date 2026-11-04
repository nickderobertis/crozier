

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.board import Board
from ..types.panel import Panel
from .raw_client import AsyncRawBoardsClient, RawBoardsClient


OMIT = typing.cast(typing.Any, ...)


class BoardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBoardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBoardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBoardsClient
        """
        return self._raw_client

    def create_board(
        self, *, title: str, panel: Panel, request_options: typing.Optional[RequestOptions] = None
    ) -> Board:
        """
        Parameters
        ----------
        title : str

        panel : Panel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Board
            The board.

        Examples
        --------
        from fern import (
            AlertOperator,
            AutumnSeasonPhase,
            FernApi,
            Panel,
            PanelReading_Sensors,
            SensorReadingAlertsItem_Bench,
            SensorReadingAlertsItem_Vent,
            SensorReadingBench,
            SensorReadingChannelsItem,
            SensorReadingChecksItem_Threshold,
            SensorReadingSeason_Autumn,
            Window,
        )

        client = FernApi()
        client.boards.create_board(
            title="title",
            panel=Panel(
                title="title",
                reading=PanelReading_Sensors(
                    channels=[
                        SensorReadingChannelsItem.AIR_TEMPERATURE,
                        SensorReadingChannelsItem.HUMIDITY,
                    ],
                    window=Window.DAILY,
                    bench=SensorReadingBench(
                        row=4,
                        side="west",
                    ),
                    alerts=[
                        SensorReadingAlertsItem_Vent(
                            operator=AlertOperator.ABOVE,
                            levels=["high"],
                        ),
                        SensorReadingAlertsItem_Bench(
                            operator=AlertOperator.BELOW,
                        ),
                    ],
                    season=SensorReadingSeason_Autumn(
                        phase=AutumnSeasonPhase.EARLY,
                    ),
                    checks=[
                        SensorReadingChecksItem_Threshold(
                            limit=80.0,
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._raw_client.create_board(title=title, panel=panel, request_options=request_options)
        return _response.data

    def preview_board(
        self, *, title: str, panel: Panel, request_options: typing.Optional[RequestOptions] = None
    ) -> Board:
        """
        Parameters
        ----------
        title : str

        panel : Panel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Board
            The previewed board.

        Examples
        --------
        from fern import (
            AlertOperator,
            AutumnSeasonPhase,
            FernApi,
            Panel,
            PanelReading_Sensors,
            SensorReadingAlertsItem_Bench,
            SensorReadingAlertsItem_Vent,
            SensorReadingBench,
            SensorReadingChannelsItem,
            SensorReadingChecksItem_Threshold,
            SensorReadingSeason_Autumn,
            Window,
        )

        client = FernApi()
        client.boards.preview_board(
            title="Propagation house",
            panel=Panel(
                title="Bench humidity",
                reading=PanelReading_Sensors(
                    channels=[
                        SensorReadingChannelsItem.AIR_TEMPERATURE,
                        SensorReadingChannelsItem.HUMIDITY,
                    ],
                    window=Window.DAILY,
                    bench=SensorReadingBench(
                        row=4,
                        side="west",
                    ),
                    alerts=[
                        SensorReadingAlertsItem_Vent(
                            operator=AlertOperator.ABOVE,
                            levels=["high"],
                        ),
                        SensorReadingAlertsItem_Bench(
                            operator=AlertOperator.BELOW,
                        ),
                    ],
                    season=SensorReadingSeason_Autumn(
                        phase=AutumnSeasonPhase.EARLY,
                    ),
                    checks=[
                        SensorReadingChecksItem_Threshold(
                            limit=80.0,
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._raw_client.preview_board(title=title, panel=panel, request_options=request_options)
        return _response.data


class AsyncBoardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBoardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBoardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBoardsClient
        """
        return self._raw_client

    async def create_board(
        self, *, title: str, panel: Panel, request_options: typing.Optional[RequestOptions] = None
    ) -> Board:
        """
        Parameters
        ----------
        title : str

        panel : Panel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Board
            The board.

        Examples
        --------
        import asyncio

        from fern import (
            AlertOperator,
            AsyncFernApi,
            AutumnSeasonPhase,
            Panel,
            PanelReading_Sensors,
            SensorReadingAlertsItem_Bench,
            SensorReadingAlertsItem_Vent,
            SensorReadingBench,
            SensorReadingChannelsItem,
            SensorReadingChecksItem_Threshold,
            SensorReadingSeason_Autumn,
            Window,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.boards.create_board(
                title="title",
                panel=Panel(
                    title="title",
                    reading=PanelReading_Sensors(
                        channels=[
                            SensorReadingChannelsItem.AIR_TEMPERATURE,
                            SensorReadingChannelsItem.HUMIDITY,
                        ],
                        window=Window.DAILY,
                        bench=SensorReadingBench(
                            row=4,
                            side="west",
                        ),
                        alerts=[
                            SensorReadingAlertsItem_Vent(
                                operator=AlertOperator.ABOVE,
                                levels=["high"],
                            ),
                            SensorReadingAlertsItem_Bench(
                                operator=AlertOperator.BELOW,
                            ),
                        ],
                        season=SensorReadingSeason_Autumn(
                            phase=AutumnSeasonPhase.EARLY,
                        ),
                        checks=[
                            SensorReadingChecksItem_Threshold(
                                limit=80.0,
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_board(title=title, panel=panel, request_options=request_options)
        return _response.data

    async def preview_board(
        self, *, title: str, panel: Panel, request_options: typing.Optional[RequestOptions] = None
    ) -> Board:
        """
        Parameters
        ----------
        title : str

        panel : Panel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Board
            The previewed board.

        Examples
        --------
        import asyncio

        from fern import (
            AlertOperator,
            AsyncFernApi,
            AutumnSeasonPhase,
            Panel,
            PanelReading_Sensors,
            SensorReadingAlertsItem_Bench,
            SensorReadingAlertsItem_Vent,
            SensorReadingBench,
            SensorReadingChannelsItem,
            SensorReadingChecksItem_Threshold,
            SensorReadingSeason_Autumn,
            Window,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.boards.preview_board(
                title="Propagation house",
                panel=Panel(
                    title="Bench humidity",
                    reading=PanelReading_Sensors(
                        channels=[
                            SensorReadingChannelsItem.AIR_TEMPERATURE,
                            SensorReadingChannelsItem.HUMIDITY,
                        ],
                        window=Window.DAILY,
                        bench=SensorReadingBench(
                            row=4,
                            side="west",
                        ),
                        alerts=[
                            SensorReadingAlertsItem_Vent(
                                operator=AlertOperator.ABOVE,
                                levels=["high"],
                            ),
                            SensorReadingAlertsItem_Bench(
                                operator=AlertOperator.BELOW,
                            ),
                        ],
                        season=SensorReadingSeason_Autumn(
                            phase=AutumnSeasonPhase.EARLY,
                        ),
                        checks=[
                            SensorReadingChecksItem_Threshold(
                                limit=80.0,
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_board(title=title, panel=panel, request_options=request_options)
        return _response.data
