

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_firings_request_atmosphere import ListFiringsRequestAtmosphere
from ..types.list_firings_request_cone import ListFiringsRequestCone
from ..types.list_firings_request_glaze import ListFiringsRequestGlaze
from .raw_client import AsyncRawFiringsClient, RawFiringsClient
from .types.list_firings_request_kiln import ListFiringsRequestKiln


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
        kiln: typing.Optional[ListFiringsRequestKiln] = None,
        glaze: typing.Optional[ListFiringsRequestGlaze] = None,
        cone: typing.Optional[ListFiringsRequestCone] = None,
        atmosphere: typing.Optional[ListFiringsRequestAtmosphere] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kiln : typing.Optional[ListFiringsRequestKiln]
            A kiln name, any or all kilns, or a list of names.

        glaze : typing.Optional[ListFiringsRequestGlaze]
            A glaze filter as text, or an empty object.

        cone : typing.Optional[ListFiringsRequestCone]
            A cone filter as text, or a cone and a shelf.

        atmosphere : typing.Optional[ListFiringsRequestAtmosphere]
            One atmosphere, or several.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The matching firings.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.firings.list_firings()
        """
        _response = self._raw_client.list_firings(
            kiln=kiln, glaze=glaze, cone=cone, atmosphere=atmosphere, request_options=request_options
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
        kiln: typing.Optional[ListFiringsRequestKiln] = None,
        glaze: typing.Optional[ListFiringsRequestGlaze] = None,
        cone: typing.Optional[ListFiringsRequestCone] = None,
        atmosphere: typing.Optional[ListFiringsRequestAtmosphere] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kiln : typing.Optional[ListFiringsRequestKiln]
            A kiln name, any or all kilns, or a list of names.

        glaze : typing.Optional[ListFiringsRequestGlaze]
            A glaze filter as text, or an empty object.

        cone : typing.Optional[ListFiringsRequestCone]
            A cone filter as text, or a cone and a shelf.

        atmosphere : typing.Optional[ListFiringsRequestAtmosphere]
            One atmosphere, or several.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The matching firings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.firings.list_firings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_firings(
            kiln=kiln, glaze=glaze, cone=cone, atmosphere=atmosphere, request_options=request_options
        )
        return _response.data
