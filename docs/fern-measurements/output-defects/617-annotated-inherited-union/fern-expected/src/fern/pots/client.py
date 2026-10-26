

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.coat import Coat
from ..types.pot import Pot
from ..types.pot_outer_coat import PotOuterCoat
from .raw_client import AsyncRawPotsClient, RawPotsClient
from .types.recoat_pot_request_coat import RecoatPotRequestCoat


OMIT = typing.cast(typing.Any, ...)


class PotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPotsClient
        """
        return self._raw_client

    def record_pot(
        self,
        *,
        potter: str,
        outer_coat: PotOuterCoat,
        inner_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pot:
        """
        Parameters
        ----------
        potter : str

        outer_coat : PotOuterCoat
            The coat on the pot's outer wall.

        inner_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pot
            The recorded pot.

        Examples
        --------
        from fern import FernApi, PotOuterCoat_Matte

        client = FernApi()
        client.pots.record_pot(
            potter="potter",
            outer_coat=PotOuterCoat_Matte(
                tooth=1,
            ),
        )
        """
        _response = self._raw_client.record_pot(
            potter=potter, outer_coat=outer_coat, inner_coat=inner_coat, request_options=request_options
        )
        return _response.data

    def recoat_pot(
        self,
        pot_id: str,
        *,
        coat: RecoatPotRequestCoat,
        previous_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pot:
        """
        Parameters
        ----------
        pot_id : str

        coat : RecoatPotRequestCoat
            The fresh coat to apply.

        previous_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pot
            The recoated pot.

        Examples
        --------
        from fern.pots import RecoatPotRequestCoat_Matte

        from fern import FernApi

        client = FernApi()
        client.pots.recoat_pot(
            pot_id="potId",
            coat=RecoatPotRequestCoat_Matte(
                tooth=1,
            ),
        )
        """
        _response = self._raw_client.recoat_pot(
            pot_id, coat=coat, previous_coat=previous_coat, request_options=request_options
        )
        return _response.data


class AsyncPotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPotsClient
        """
        return self._raw_client

    async def record_pot(
        self,
        *,
        potter: str,
        outer_coat: PotOuterCoat,
        inner_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pot:
        """
        Parameters
        ----------
        potter : str

        outer_coat : PotOuterCoat
            The coat on the pot's outer wall.

        inner_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pot
            The recorded pot.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PotOuterCoat_Matte

        client = AsyncFernApi()


        async def main() -> None:
            await client.pots.record_pot(
                potter="potter",
                outer_coat=PotOuterCoat_Matte(
                    tooth=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_pot(
            potter=potter, outer_coat=outer_coat, inner_coat=inner_coat, request_options=request_options
        )
        return _response.data

    async def recoat_pot(
        self,
        pot_id: str,
        *,
        coat: RecoatPotRequestCoat,
        previous_coat: typing.Optional[Coat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pot:
        """
        Parameters
        ----------
        pot_id : str

        coat : RecoatPotRequestCoat
            The fresh coat to apply.

        previous_coat : typing.Optional[Coat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pot
            The recoated pot.

        Examples
        --------
        import asyncio

        from fern.pots import RecoatPotRequestCoat_Matte

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pots.recoat_pot(
                pot_id="potId",
                coat=RecoatPotRequestCoat_Matte(
                    tooth=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recoat_pot(
            pot_id, coat=coat, previous_coat=previous_coat, request_options=request_options
        )
        return _response.data
