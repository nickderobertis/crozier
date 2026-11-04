

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawYewWalkClient, RawYewWalkClient
from .types.trim_hedge_request_finish import TrimHedgeRequestFinish
from .types.trim_hedge_response import TrimHedgeResponse


OMIT = typing.cast(typing.Any, ...)


class YewWalkClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawYewWalkClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawYewWalkClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawYewWalkClient
        """
        return self._raw_client

    def trim_hedge(
        self,
        *,
        length: float,
        finish: typing.Optional[TrimHedgeRequestFinish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrimHedgeResponse:
        """
        Parameters
        ----------
        length : float

        finish : typing.Optional[TrimHedgeRequestFinish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrimHedgeResponse
            The trimmed hedge.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.yew_walk.trim_hedge(
            length=1.1,
        )
        """
        _response = self._raw_client.trim_hedge(length=length, finish=finish, request_options=request_options)
        return _response.data


class AsyncYewWalkClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawYewWalkClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawYewWalkClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawYewWalkClient
        """
        return self._raw_client

    async def trim_hedge(
        self,
        *,
        length: float,
        finish: typing.Optional[TrimHedgeRequestFinish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrimHedgeResponse:
        """
        Parameters
        ----------
        length : float

        finish : typing.Optional[TrimHedgeRequestFinish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrimHedgeResponse
            The trimmed hedge.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.yew_walk.trim_hedge(
                length=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trim_hedge(length=length, finish=finish, request_options=request_options)
        return _response.data
