

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.trait_map import TraitMap
from ..types.variety import Variety
from ..types.variety_record import VarietyRecord
from .raw_client import AsyncRawVarietiesClient, RawVarietiesClient


OMIT = typing.cast(typing.Any, ...)


class VarietiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVarietiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVarietiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVarietiesClient
        """
        return self._raw_client

    def register_variety(
        self, *, request: VarietyRecord, request_options: typing.Optional[RequestOptions] = None
    ) -> Variety:
        """
        Parameters
        ----------
        request : VarietyRecord

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variety
            The registered variety.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.varieties.register_variety(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.register_variety(request=request, request_options=request_options)
        return _response.data

    def replace_traits(
        self, variety_id: str, *, request: TraitMap, request_options: typing.Optional[RequestOptions] = None
    ) -> Variety:
        """
        Parameters
        ----------
        variety_id : str

        request : TraitMap

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variety
            The variety.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.varieties.replace_traits(
            variety_id="varietyId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.replace_traits(variety_id, request=request, request_options=request_options)
        return _response.data

    def patch_notes(
        self,
        variety_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Variety:
        """
        Parameters
        ----------
        variety_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variety
            The variety.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.varieties.patch_notes(
            variety_id="varietyId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.patch_notes(variety_id, request=request, request_options=request_options)
        return _response.data


class AsyncVarietiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVarietiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVarietiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVarietiesClient
        """
        return self._raw_client

    async def register_variety(
        self, *, request: VarietyRecord, request_options: typing.Optional[RequestOptions] = None
    ) -> Variety:
        """
        Parameters
        ----------
        request : VarietyRecord

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variety
            The registered variety.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.varieties.register_variety(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_variety(request=request, request_options=request_options)
        return _response.data

    async def replace_traits(
        self, variety_id: str, *, request: TraitMap, request_options: typing.Optional[RequestOptions] = None
    ) -> Variety:
        """
        Parameters
        ----------
        variety_id : str

        request : TraitMap

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variety
            The variety.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.varieties.replace_traits(
                variety_id="varietyId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_traits(variety_id, request=request, request_options=request_options)
        return _response.data

    async def patch_notes(
        self,
        variety_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Variety:
        """
        Parameters
        ----------
        variety_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variety
            The variety.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.varieties.patch_notes(
                variety_id="varietyId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_notes(variety_id, request=request, request_options=request_options)
        return _response.data
