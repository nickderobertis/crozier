

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAccountingClient, RawAccountingClient


OMIT = typing.cast(typing.Any, ...)


class AccountingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountingClient
        """
        return self._raw_client

    def createjournalexport(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounting.createjournalexport(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.createjournalexport(request=request, request_options=request_options)
        return _response.data

    def downloadjournal(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounting.downloadjournal(
            key="key",
        )
        """
        _response = self._raw_client.downloadjournal(key, request_options=request_options)
        return _response.data

    def listjournaltemplates(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounting.listjournaltemplates()
        """
        _response = self._raw_client.listjournaltemplates(request_options=request_options)
        return _response.data


class AsyncAccountingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountingClient
        """
        return self._raw_client

    async def createjournalexport(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounting.createjournalexport(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createjournalexport(request=request, request_options=request_options)
        return _response.data

    async def downloadjournal(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        key : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounting.downloadjournal(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.downloadjournal(key, request_options=request_options)
        return _response.data

    async def listjournaltemplates(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounting.listjournaltemplates()


        asyncio.run(main())
        """
        _response = await self._raw_client.listjournaltemplates(request_options=request_options)
        return _response.data
