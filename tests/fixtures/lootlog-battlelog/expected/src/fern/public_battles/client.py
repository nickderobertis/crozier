

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.battle_raw_response_dto_output import BattleRawResponseDtoOutput
from ..types.battle_response_dto_output import BattleResponseDtoOutput
from ..types.battle_timeline_response_dto_output import BattleTimelineResponseDtoOutput
from .raw_client import AsyncRawPublicBattlesClient, RawPublicBattlesClient


class PublicBattlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPublicBattlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPublicBattlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPublicBattlesClient
        """
        return self._raw_client

    def public_battles_controller_get_public_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.public_battles.public_battles_controller_get_public_battle(
            battle_id="battleId",
        )
        """
        _response = self._raw_client.public_battles_controller_get_public_battle(
            battle_id, request_options=request_options
        )
        return _response.data

    def public_battles_controller_get_public_battle_raw(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleRawResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleRawResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.public_battles.public_battles_controller_get_public_battle_raw(
            battle_id="battleId",
        )
        """
        _response = self._raw_client.public_battles_controller_get_public_battle_raw(
            battle_id, request_options=request_options
        )
        return _response.data

    def public_battles_controller_get_public_battle_timeline(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleTimelineResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleTimelineResponseDtoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.public_battles.public_battles_controller_get_public_battle_timeline(
            battle_id="battleId",
        )
        """
        _response = self._raw_client.public_battles_controller_get_public_battle_timeline(
            battle_id, request_options=request_options
        )
        return _response.data


class AsyncPublicBattlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPublicBattlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPublicBattlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPublicBattlesClient
        """
        return self._raw_client

    async def public_battles_controller_get_public_battle(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.public_battles.public_battles_controller_get_public_battle(
                battle_id="battleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.public_battles_controller_get_public_battle(
            battle_id, request_options=request_options
        )
        return _response.data

    async def public_battles_controller_get_public_battle_raw(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleRawResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleRawResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.public_battles.public_battles_controller_get_public_battle_raw(
                battle_id="battleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.public_battles_controller_get_public_battle_raw(
            battle_id, request_options=request_options
        )
        return _response.data

    async def public_battles_controller_get_public_battle_timeline(
        self, battle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BattleTimelineResponseDtoOutput:
        """
        Parameters
        ----------
        battle_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BattleTimelineResponseDtoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.public_battles.public_battles_controller_get_public_battle_timeline(
                battle_id="battleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.public_battles_controller_get_public_battle_timeline(
            battle_id, request_options=request_options
        )
        return _response.data
