

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dispatch import Dispatch
from .raw_client import AsyncRawDispatchesClient, RawDispatchesClient


OMIT = typing.cast(typing.Any, ...)


class DispatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDispatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDispatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDispatchesClient
        """
        return self._raw_client

    def create_dispatch(
        self,
        *,
        request_options: str,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> Dispatch:
        """
        Parameters
        ----------
        request_options : str

        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dispatch
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dispatches.create_dispatch(
            request_options="express",
        )
        """
        _response = self._raw_client.create_dispatch(
            request_options=request_options, kwargs_=kwargs_, self_=self_, _request_options=_request_options
        )
        return _response.data

    def update_dispatch(
        self,
        dispatch_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dispatch:
        """
        Parameters
        ----------
        dispatch_id : str

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dispatch
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dispatches.update_dispatch(
            dispatch_id="dispatch_id",
        )
        """
        _response = self._raw_client.update_dispatch(dispatch_id, note=note, request_options=request_options)
        return _response.data

    def add_note(
        self, dispatch_id: str, *, request_options: str, _request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : str

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dispatches.add_note(
            dispatch_id="dispatch_id",
            request_options="request_options",
        )
        """
        _response = self._raw_client.add_note(
            dispatch_id, request_options=request_options, _request_options=_request_options
        )
        return _response.data

    def download_manifest(
        self,
        dispatch_id: str,
        *,
        request_options: typing.Optional[str] = None,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            the manifest
        """
        with self._raw_client.download_manifest(
            dispatch_id, request_options=request_options, _request_options=_request_options
        ) as r:
            yield from r.data


class AsyncDispatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDispatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDispatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDispatchesClient
        """
        return self._raw_client

    async def create_dispatch(
        self,
        *,
        request_options: str,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> Dispatch:
        """
        Parameters
        ----------
        request_options : str

        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dispatch
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dispatches.create_dispatch(
                request_options="express",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dispatch(
            request_options=request_options, kwargs_=kwargs_, self_=self_, _request_options=_request_options
        )
        return _response.data

    async def update_dispatch(
        self,
        dispatch_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dispatch:
        """
        Parameters
        ----------
        dispatch_id : str

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dispatch
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dispatches.update_dispatch(
                dispatch_id="dispatch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_dispatch(dispatch_id, note=note, request_options=request_options)
        return _response.data

    async def add_note(
        self, dispatch_id: str, *, request_options: str, _request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : str

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dispatches.add_note(
                dispatch_id="dispatch_id",
                request_options="request_options",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_note(
            dispatch_id, request_options=request_options, _request_options=_request_options
        )
        return _response.data

    async def download_manifest(
        self,
        dispatch_id: str,
        *,
        request_options: typing.Optional[str] = None,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            the manifest
        """
        async with self._raw_client.download_manifest(
            dispatch_id, request_options=request_options, _request_options=_request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
