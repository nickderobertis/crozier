

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.clone_result import CloneResult
from .raw_client import AsyncRawFiringsClient, RawFiringsClient


OMIT = typing.cast(typing.Any, ...)


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

    def clone_firing(
        self,
        firing_id: str,
        *,
        region: str,
        share_with: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloneResult:
        """
        Parameters
        ----------
        firing_id : str

        region : str
            The region the clone is placed in.

        share_with : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloneResult
            Cloned.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.clone_firing(
            firing_id="firingId",
            region="region",
        )
        """
        _response = self._raw_client.clone_firing(
            firing_id, region=region, share_with=share_with, request_options=request_options
        )
        return _response.data

    def copy_firing(
        self,
        firing_id: str,
        *,
        shelf: str,
        position: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloneResult:
        """
        Parameters
        ----------
        firing_id : str

        shelf : str

        position : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloneResult
            Copied.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.copy_firing(
            firing_id="firingId",
            shelf="shelf",
        )
        """
        _response = self._raw_client.copy_firing(
            firing_id, shelf=shelf, position=position, request_options=request_options
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

    async def clone_firing(
        self,
        firing_id: str,
        *,
        region: str,
        share_with: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloneResult:
        """
        Parameters
        ----------
        firing_id : str

        region : str
            The region the clone is placed in.

        share_with : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloneResult
            Cloned.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.clone_firing(
                firing_id="firingId",
                region="region",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clone_firing(
            firing_id, region=region, share_with=share_with, request_options=request_options
        )
        return _response.data

    async def copy_firing(
        self,
        firing_id: str,
        *,
        shelf: str,
        position: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloneResult:
        """
        Parameters
        ----------
        firing_id : str

        shelf : str

        position : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloneResult
            Copied.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.copy_firing(
                firing_id="firingId",
                shelf="shelf",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy_firing(
            firing_id, shelf=shelf, position=position, request_options=request_options
        )
        return _response.data
