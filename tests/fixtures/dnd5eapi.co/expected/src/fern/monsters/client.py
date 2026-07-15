

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.monster import Monster
from .raw_client import AsyncRawMonstersClient, RawMonstersClient


class MonstersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonstersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonstersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonstersClient
        """
        return self._raw_client

    def get_list_of_monsters_with_optional_filtering(
        self,
        *,
        challenge_rating: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        challenge_rating : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            The challenge rating or ratings to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.monsters.get_list_of_monsters_with_optional_filtering()
        """
        _response = self._raw_client.get_list_of_monsters_with_optional_filtering(
            challenge_rating=challenge_rating, request_options=request_options
        )
        return _response.data

    def get_monster_by_index(self, index: str, *, request_options: typing.Optional[RequestOptions] = None) -> Monster:
        """
        Parameters
        ----------
        index : str
            The `index` of the `Monster` to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monster
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.monsters.get_monster_by_index(
            index="aboleth",
        )
        """
        _response = self._raw_client.get_monster_by_index(index, request_options=request_options)
        return _response.data


class AsyncMonstersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonstersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonstersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonstersClient
        """
        return self._raw_client

    async def get_list_of_monsters_with_optional_filtering(
        self,
        *,
        challenge_rating: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        challenge_rating : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            The challenge rating or ratings to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.monsters.get_list_of_monsters_with_optional_filtering()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_list_of_monsters_with_optional_filtering(
            challenge_rating=challenge_rating, request_options=request_options
        )
        return _response.data

    async def get_monster_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Monster:
        """
        Parameters
        ----------
        index : str
            The `index` of the `Monster` to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monster
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.monsters.get_monster_by_index(
                index="aboleth",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_monster_by_index(index, request_options=request_options)
        return _response.data
