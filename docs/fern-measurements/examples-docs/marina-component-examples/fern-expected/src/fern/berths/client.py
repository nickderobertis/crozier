

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBerthsClient, RawBerthsClient
from .types.hull_request_hull import HullRequestHull


OMIT = typing.cast(typing.Any, ...)


class BerthsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBerthsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBerthsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBerthsClient
        """
        return self._raw_client

    def set_hull(
        self, berth_id: str, *, hull: HullRequestHull, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        berth_id : str

        hull : HullRequestHull

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.berths import HullRequestHull_Steel

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.berths.set_hull(
            berth_id="berth_id",
            hull=HullRequestHull_Steel(
                length_m=24,
                beam_m=6,
                draft_cm=180,
            ),
        )
        """
        _response = self._raw_client.set_hull(berth_id, hull=hull, request_options=request_options)
        return _response.data


class AsyncBerthsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBerthsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBerthsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBerthsClient
        """
        return self._raw_client

    async def set_hull(
        self, berth_id: str, *, hull: HullRequestHull, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        berth_id : str

        hull : HullRequestHull

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.berths import HullRequestHull_Steel

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.berths.set_hull(
                berth_id="berth_id",
                hull=HullRequestHull_Steel(
                    length_m=24,
                    beam_m=6,
                    draft_cm=180,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_hull(berth_id, hull=hull, request_options=request_options)
        return _response.data
