

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.finish import Finish
from .raw_client import AsyncRawGlazesClient, RawGlazesClient
from .types.list_glazes_request_firing_item import ListGlazesRequestFiringItem


class GlazesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlazesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlazesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlazesClient
        """
        return self._raw_client

    def list_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        firing: typing.Optional[
            typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]
        ] = None,
        palette: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        firing : typing.Optional[typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]]

        palette : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The glazes.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.glazes.list_glazes(
            palette=["celadon"],
        )
        """
        _response = self._raw_client.list_glazes(
            finish=finish, firing=firing, palette=palette, request_options=request_options
        )
        return _response.data

    def list_required_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The glazes.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.glazes.list_required_glazes(
            finish=["matte"],
        )
        """
        _response = self._raw_client.list_required_glazes(finish=finish, request_options=request_options)
        return _response.data


class AsyncGlazesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlazesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlazesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlazesClient
        """
        return self._raw_client

    async def list_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        firing: typing.Optional[
            typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]
        ] = None,
        palette: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        firing : typing.Optional[typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]]

        palette : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The glazes.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.glazes.list_glazes(
                palette=["celadon"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_glazes(
            finish=finish, firing=firing, palette=palette, request_options=request_options
        )
        return _response.data

    async def list_required_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The glazes.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.glazes.list_required_glazes(
                finish=["matte"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_required_glazes(finish=finish, request_options=request_options)
        return _response.data
