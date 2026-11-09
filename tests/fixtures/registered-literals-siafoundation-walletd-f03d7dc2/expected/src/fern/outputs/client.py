

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.element_spent_response import ElementSpentResponse
from ..types.hash256 import Hash256
from ..types.siacoin_element import SiacoinElement
from ..types.siafund_element import SiafundElement
from .raw_client import AsyncRawOutputsClient, RawOutputsClient


class OutputsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOutputsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOutputsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOutputsClient
        """
        return self._raw_client

    def get_siacoin_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiacoinElement:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiacoinElement
            Siacoin element details.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.outputs.get_siacoin_output(
            id="id",
        )
        """
        _response = self._raw_client.get_siacoin_output(id, request_options=request_options)
        return _response.data

    def get_siacoin_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ElementSpentResponse:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElementSpentResponse
            Spent status and optional spend event.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.outputs.get_siacoin_output_spent(
            id="id",
        )
        """
        _response = self._raw_client.get_siacoin_output_spent(id, request_options=request_options)
        return _response.data

    def get_siafund_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiafundElement:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiafundElement
            Siafund element details.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.outputs.get_siafund_output(
            id="id",
        )
        """
        _response = self._raw_client.get_siafund_output(id, request_options=request_options)
        return _response.data

    def get_siafund_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ElementSpentResponse:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElementSpentResponse
            Spent status and optional spend event.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.outputs.get_siafund_output_spent(
            id="id",
        )
        """
        _response = self._raw_client.get_siafund_output_spent(id, request_options=request_options)
        return _response.data


class AsyncOutputsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOutputsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOutputsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOutputsClient
        """
        return self._raw_client

    async def get_siacoin_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiacoinElement:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiacoinElement
            Siacoin element details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.outputs.get_siacoin_output(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_siacoin_output(id, request_options=request_options)
        return _response.data

    async def get_siacoin_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ElementSpentResponse:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElementSpentResponse
            Spent status and optional spend event.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.outputs.get_siacoin_output_spent(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_siacoin_output_spent(id, request_options=request_options)
        return _response.data

    async def get_siafund_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiafundElement:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiafundElement
            Siafund element details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.outputs.get_siafund_output(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_siafund_output(id, request_options=request_options)
        return _response.data

    async def get_siafund_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ElementSpentResponse:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElementSpentResponse
            Spent status and optional spend event.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.outputs.get_siafund_output_spent(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_siafund_output_spent(id, request_options=request_options)
        return _response.data
