

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawValClient, RawValClient
from .types.get_v3val_viewer_response import GetV3ValViewerResponse


class ValClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawValClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValClient
        """
        return self._raw_client

    def get_v3val_viewer(
        self, *, val_town_user: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV3ValViewerResponse:
        """
        Look up the identity of the viewer of an app-authenticated (intranet) val, given the X-Val-Town-User header value that Fastify forwarded to the val. Authenticated with the val's own API token (bearer auth). The projectId inside the signed header must match the caller's own project.

        Parameters
        ----------
        val_town_user : str
            The signed X-Val-Town-User header value Fastify forwarded to the val.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV3ValViewerResponse
            Public identity of the viewer derived from a verified X-Val-Town-User header. Only safe, public profile fields are returned — no email or tier.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.val.get_v3val_viewer(
            val_town_user="x-val-town-user",
        )
        """
        _response = self._raw_client.get_v3val_viewer(val_town_user=val_town_user, request_options=request_options)
        return _response.data


class AsyncValClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawValClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValClient
        """
        return self._raw_client

    async def get_v3val_viewer(
        self, *, val_town_user: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV3ValViewerResponse:
        """
        Look up the identity of the viewer of an app-authenticated (intranet) val, given the X-Val-Town-User header value that Fastify forwarded to the val. Authenticated with the val's own API token (bearer auth). The projectId inside the signed header must match the caller's own project.

        Parameters
        ----------
        val_town_user : str
            The signed X-Val-Town-User header value Fastify forwarded to the val.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV3ValViewerResponse
            Public identity of the viewer derived from a verified X-Val-Town-User header. Only safe, public profile fields are returned — no email or tier.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.val.get_v3val_viewer(
                val_town_user="x-val-town-user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v3val_viewer(
            val_town_user=val_town_user, request_options=request_options
        )
        return _response.data
