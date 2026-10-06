

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_cooling_firings_request_atmosphere import ListCoolingFiringsRequestAtmosphere
from .raw_client import AsyncRawFiringsClient, RawFiringsClient
from .types.list_cooling_firings_request_pyrometer import ListCoolingFiringsRequestPyrometer
from .types.list_firings_request_glaze import ListFiringsRequestGlaze
from .types.list_firings_request_shelf import ListFiringsRequestShelf


class FiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFiringsClient
        """
        return self._raw_client

    def list_firings(
        self,
        *,
        shelf: ListFiringsRequestShelf,
        glaze: ListFiringsRequestGlaze,
        cone: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        shelf : ListFiringsRequestShelf

        glaze : ListFiringsRequestGlaze

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Scheduled firings.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.firings.list_firings(
            shelf=1,
            glaze="glaze",
        )
        """
        _response = self._raw_client.list_firings(shelf=shelf, glaze=glaze, cone=cone, request_options=request_options)
        return _response.data

    def list_cooling_firings(
        self,
        *,
        kiln: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        batch: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        atmosphere: typing.Optional[ListCoolingFiringsRequestAtmosphere] = None,
        pyrometer: typing.Optional[ListCoolingFiringsRequestPyrometer] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kiln : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        batch : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        atmosphere : typing.Optional[ListCoolingFiringsRequestAtmosphere]

        pyrometer : typing.Optional[ListCoolingFiringsRequestPyrometer]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Firings that are cooling.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.firings.list_cooling_firings(
            batch=1,
        )
        """
        _response = self._raw_client.list_cooling_firings(
            kiln=kiln, batch=batch, atmosphere=atmosphere, pyrometer=pyrometer, request_options=request_options
        )
        return _response.data


class AsyncFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFiringsClient
        """
        return self._raw_client

    async def list_firings(
        self,
        *,
        shelf: ListFiringsRequestShelf,
        glaze: ListFiringsRequestGlaze,
        cone: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        shelf : ListFiringsRequestShelf

        glaze : ListFiringsRequestGlaze

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Scheduled firings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.firings.list_firings(
                shelf=1,
                glaze="glaze",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_firings(
            shelf=shelf, glaze=glaze, cone=cone, request_options=request_options
        )
        return _response.data

    async def list_cooling_firings(
        self,
        *,
        kiln: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        batch: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        atmosphere: typing.Optional[ListCoolingFiringsRequestAtmosphere] = None,
        pyrometer: typing.Optional[ListCoolingFiringsRequestPyrometer] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kiln : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        batch : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        atmosphere : typing.Optional[ListCoolingFiringsRequestAtmosphere]

        pyrometer : typing.Optional[ListCoolingFiringsRequestPyrometer]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Firings that are cooling.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.firings.list_cooling_firings(
                batch=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_cooling_firings(
            kiln=kiln, batch=batch, atmosphere=atmosphere, pyrometer=pyrometer, request_options=request_options
        )
        return _response.data
