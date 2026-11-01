

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDepotsClient, RawDepotsClient
from .types.compare_depots_response import CompareDepotsResponse
from .types.create_depot_response import CreateDepotResponse


OMIT = typing.cast(typing.Any, ...)


class DepotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDepotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDepotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDepotsClient
        """
        return self._raw_client

    def create_depot(
        self,
        *,
        postcode: str,
        capacity: int,
        code: str,
        aliases: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDepotResponse:
        """
        Parameters
        ----------
        postcode : str

        capacity : int

        code : str

        aliases : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDepotResponse
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.depots.create_depot(
            postcode="postcode",
            capacity=1000000,
            code="code",
            aliases=["west quay"],
        )
        """
        _response = self._raw_client.create_depot(
            postcode=postcode, capacity=capacity, code=code, aliases=aliases, request_options=request_options
        )
        return _response.data

    def compare_depots(
        self, *, left: str, right: str, level: float, request_options: typing.Optional[RequestOptions] = None
    ) -> CompareDepotsResponse:
        """
        Parameters
        ----------
        left : str

        right : str

        level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareDepotsResponse
            Compared

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.depots.compare_depots(
            left="dpt-1",
            right="dpt-2",
            level=1.1,
        )
        """
        _response = self._raw_client.compare_depots(
            left=left, right=right, level=level, request_options=request_options
        )
        return _response.data


class AsyncDepotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDepotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDepotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDepotsClient
        """
        return self._raw_client

    async def create_depot(
        self,
        *,
        postcode: str,
        capacity: int,
        code: str,
        aliases: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDepotResponse:
        """
        Parameters
        ----------
        postcode : str

        capacity : int

        code : str

        aliases : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDepotResponse
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.depots.create_depot(
                postcode="postcode",
                capacity=1000000,
                code="code",
                aliases=["west quay"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_depot(
            postcode=postcode, capacity=capacity, code=code, aliases=aliases, request_options=request_options
        )
        return _response.data

    async def compare_depots(
        self, *, left: str, right: str, level: float, request_options: typing.Optional[RequestOptions] = None
    ) -> CompareDepotsResponse:
        """
        Parameters
        ----------
        left : str

        right : str

        level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareDepotsResponse
            Compared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.depots.compare_depots(
                left="dpt-1",
                right="dpt-2",
                level=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compare_depots(
            left=left, right=right, level=level, request_options=request_options
        )
        return _response.data
