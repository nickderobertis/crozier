

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1profile_response_output import V1ProfileResponseOutput
from .raw_client import AsyncRawProfileClient, RawProfileClient


class ProfileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProfileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProfileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProfileClient
        """
        return self._raw_client

    def v1get_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> V1ProfileResponseOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProfileResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profile.v1get_profile()
        """
        _response = self._raw_client.v1get_profile(request_options=request_options)
        return _response.data


class AsyncProfileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProfileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProfileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProfileClient
        """
        return self._raw_client

    async def v1get_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProfileResponseOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProfileResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profile.v1get_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_profile(request_options=request_options)
        return _response.data
