

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCuratedSetsClient, RawCuratedSetsClient


class CuratedSetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCuratedSetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCuratedSetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCuratedSetsClient
        """
        return self._raw_client

    def get_curated_sets_slug(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.curated_sets.get_curated_sets_slug(
            slug="slug",
        )
        """
        _response = self._raw_client.get_curated_sets_slug(slug, request_options=request_options)
        return _response.data


class AsyncCuratedSetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCuratedSetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCuratedSetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCuratedSetsClient
        """
        return self._raw_client

    async def get_curated_sets_slug(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.curated_sets.get_curated_sets_slug(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_curated_sets_slug(slug, request_options=request_options)
        return _response.data
