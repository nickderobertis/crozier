

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.store_line import StoreLine
from .raw_client import AsyncRawGalleysClient, RawGalleysClient


OMIT = typing.cast(typing.Any, ...)


class GalleysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGalleysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGalleysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGalleysClient
        """
        return self._raw_client

    def remove_galley_stores(
        self,
        galley_id: str,
        *,
        request: typing.Sequence[StoreLine],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        An array body of referenced objects with a named example, on an operation answering text.

        Parameters
        ----------
        galley_id : str

        request : typing.Sequence[StoreLine]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Removed

        Examples
        --------
        from fern import FernApi, StoreLine

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.galleys.remove_galley_stores(
            galley_id="galleyId",
            request=[StoreLine(), StoreLine()],
        )
        """
        _response = self._raw_client.remove_galley_stores(galley_id, request=request, request_options=request_options)
        return _response.data

    def append_galley_log(
        self,
        galley_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        A free-form map body with array named examples, on an operation answering text.

        Parameters
        ----------
        galley_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Count

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.galleys.append_galley_log(
            galley_id="galleyId",
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.append_galley_log(galley_id, request=request, request_options=request_options)
        return _response.data

    def amend_galley_log(
        self,
        galley_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        An array body of unknown items with an example, on an operation answering text.

        Parameters
        ----------
        galley_id : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Count

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.galleys.amend_galley_log(
            galley_id="galleyId",
            request=[{"key": "value"}, {"key": "value"}],
        )
        """
        _response = self._raw_client.amend_galley_log(galley_id, request=request, request_options=request_options)
        return _response.data


class AsyncGalleysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGalleysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGalleysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGalleysClient
        """
        return self._raw_client

    async def remove_galley_stores(
        self,
        galley_id: str,
        *,
        request: typing.Sequence[StoreLine],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        An array body of referenced objects with a named example, on an operation answering text.

        Parameters
        ----------
        galley_id : str

        request : typing.Sequence[StoreLine]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Removed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, StoreLine

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.galleys.remove_galley_stores(
                galley_id="galleyId",
                request=[StoreLine(), StoreLine()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_galley_stores(
            galley_id, request=request, request_options=request_options
        )
        return _response.data

    async def append_galley_log(
        self,
        galley_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        A free-form map body with array named examples, on an operation answering text.

        Parameters
        ----------
        galley_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Count

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.galleys.append_galley_log(
                galley_id="galleyId",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.append_galley_log(
            galley_id, request=request, request_options=request_options
        )
        return _response.data

    async def amend_galley_log(
        self,
        galley_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        An array body of unknown items with an example, on an operation answering text.

        Parameters
        ----------
        galley_id : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Count

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.galleys.amend_galley_log(
                galley_id="galleyId",
                request=[{"key": "value"}, {"key": "value"}],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.amend_galley_log(galley_id, request=request, request_options=request_options)
        return _response.data
