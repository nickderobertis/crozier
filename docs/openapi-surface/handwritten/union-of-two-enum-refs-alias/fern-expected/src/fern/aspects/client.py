

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.indication import Indication
from .raw_client import AsyncRawAspectsClient, RawAspectsClient


class AspectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAspectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAspectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAspectsClient
        """
        return self._raw_client

    def list_aspects(
        self, *, indication: typing.Optional[Indication] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        indication : typing.Optional[Indication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.aspects.list_aspects()
        """
        _response = self._raw_client.list_aspects(indication=indication, request_options=request_options)
        return _response.data


class AsyncAspectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAspectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAspectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAspectsClient
        """
        return self._raw_client

    async def list_aspects(
        self, *, indication: typing.Optional[Indication] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        indication : typing.Optional[Indication]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.aspects.list_aspects()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_aspects(indication=indication, request_options=request_options)
        return _response.data
