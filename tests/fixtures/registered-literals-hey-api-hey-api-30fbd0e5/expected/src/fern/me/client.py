

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMeClient, RawMeClient
from .types.me_get_response import MeGetResponse
from .types.me_vals2response import MeVals2Response


class MeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMeClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeGetResponse:
        """
        Get profile information for the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeGetResponse
            Your user information, with tier and email included

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.me.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def me_vals2(
        self, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> MeVals2Response:
        """
        [BETA] List all of a user's vals for authenticated users

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeVals2Response
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.me.me_vals2(
            offset=1,
            limit=1,
        )
        """
        _response = self._raw_client.me_vals2(offset=offset, limit=limit, request_options=request_options)
        return _response.data


class AsyncMeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMeClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeGetResponse:
        """
        Get profile information for the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeGetResponse
            Your user information, with tier and email included

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.me.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def me_vals2(
        self, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> MeVals2Response:
        """
        [BETA] List all of a user's vals for authenticated users

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeVals2Response
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.me.me_vals2(
                offset=1,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.me_vals2(offset=offset, limit=limit, request_options=request_options)
        return _response.data
