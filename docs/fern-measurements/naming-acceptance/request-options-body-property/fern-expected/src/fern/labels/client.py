

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dispatch import Dispatch
from .raw_client import AsyncRawLabelsClient, RawLabelsClient


class LabelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLabelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLabelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLabelsClient
        """
        return self._raw_client

    def get_label(self, request_options_: str, *, request_options: typing.Optional[RequestOptions] = None) -> Dispatch:
        """
        Parameters
        ----------
        request_options_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dispatch
            the label

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.labels.get_label(
            request_options_="request_options",
        )
        """
        _response = self._raw_client.get_label(request_options_, request_options=request_options)
        return _response.data

    def list_labels(
        self, *, request_options: typing.Optional[str] = None, _request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Dispatch]:
        """
        Parameters
        ----------
        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Dispatch]
            every label

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.labels.list_labels()
        """
        _response = self._raw_client.list_labels(request_options=request_options, _request_options=_request_options)
        return _response.data


class AsyncLabelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLabelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLabelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLabelsClient
        """
        return self._raw_client

    async def get_label(
        self, request_options_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dispatch:
        """
        Parameters
        ----------
        request_options_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dispatch
            the label

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.labels.get_label(
                request_options_="request_options",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_label(request_options_, request_options=request_options)
        return _response.data

    async def list_labels(
        self, *, request_options: typing.Optional[str] = None, _request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Dispatch]:
        """
        Parameters
        ----------
        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Dispatch]
            every label

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.labels.list_labels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_labels(
            request_options=request_options, _request_options=_request_options
        )
        return _response.data
