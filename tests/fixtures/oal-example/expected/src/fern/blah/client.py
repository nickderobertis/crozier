

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.obj1 import Obj1
from .raw_client import AsyncRawBlahClient, RawBlahClient


class BlahClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBlahClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBlahClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBlahClient
        """
        return self._raw_client

    def get_some_path_id_template(
        self, id: float, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Obj1:
        """
        Parameters
        ----------
        id : float
            some parameter

        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Obj1
            some content

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.blah.get_some_path_id_template(
            id=1.1,
        )
        """
        _response = self._raw_client.get_some_path_id_template(id, q=q, request_options=request_options)
        return _response.data


class AsyncBlahClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBlahClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBlahClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBlahClient
        """
        return self._raw_client

    async def get_some_path_id_template(
        self, id: float, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Obj1:
        """
        Parameters
        ----------
        id : float
            some parameter

        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Obj1
            some content

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blah.get_some_path_id_template(
                id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_some_path_id_template(id, q=q, request_options=request_options)
        return _response.data
