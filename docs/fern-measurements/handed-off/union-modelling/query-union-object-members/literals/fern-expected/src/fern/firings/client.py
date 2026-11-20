

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_firings_request_glaze import ListFiringsRequestGlaze
from .raw_client import AsyncRawFiringsClient, RawFiringsClient
from .types.list_firings_request_cone import ListFiringsRequestCone
from .types.list_firings_request_kiln_id import ListFiringsRequestKilnId


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
        cone: ListFiringsRequestCone,
        glaze: typing.Optional[ListFiringsRequestGlaze] = None,
        kiln_id: typing.Optional[ListFiringsRequestKilnId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        cone : ListFiringsRequestCone
            A cone number, or a range of cones.

        glaze : typing.Optional[ListFiringsRequestGlaze]
            A glaze name, or the glaze document to match.

        kiln_id : typing.Optional[ListFiringsRequestKilnId]
            Kiln identifiers, or `?[any]=true` for any kiln.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The firings.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.firings.list_firings(
            cone=1,
        )
        """
        _response = self._raw_client.list_firings(
            cone=cone, glaze=glaze, kiln_id=kiln_id, request_options=request_options
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
        cone: ListFiringsRequestCone,
        glaze: typing.Optional[ListFiringsRequestGlaze] = None,
        kiln_id: typing.Optional[ListFiringsRequestKilnId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        cone : ListFiringsRequestCone
            A cone number, or a range of cones.

        glaze : typing.Optional[ListFiringsRequestGlaze]
            A glaze name, or the glaze document to match.

        kiln_id : typing.Optional[ListFiringsRequestKilnId]
            Kiln identifiers, or `?[any]=true` for any kiln.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The firings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.firings.list_firings(
                cone=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_firings(
            cone=cone, glaze=glaze, kiln_id=kiln_id, request_options=request_options
        )
        return _response.data
