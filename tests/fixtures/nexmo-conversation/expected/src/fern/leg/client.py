

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLegClient, RawLegClient
from .types.list_legs_response import ListLegsResponse


class LegClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLegClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLegClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLegClient
        """
        return self._raw_client

    def list_legs(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListLegsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLegsResponse
            List Legs Successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leg.list_legs()
        """
        _response = self._raw_client.list_legs(request_options=request_options)
        return _response.data

    def delete_leg(
        self, leg_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        leg_id : str
            Leg ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leg.delete_leg(
            leg_id="leg_id",
        )
        """
        _response = self._raw_client.delete_leg(leg_id, request_options=request_options)
        return _response.data


class AsyncLegClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLegClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLegClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLegClient
        """
        return self._raw_client

    async def list_legs(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListLegsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLegsResponse
            List Legs Successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.leg.list_legs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_legs(request_options=request_options)
        return _response.data

    async def delete_leg(
        self, leg_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        leg_id : str
            Leg ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.leg.delete_leg(
                leg_id="leg_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_leg(leg_id, request_options=request_options)
        return _response.data
