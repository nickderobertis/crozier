

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient


OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhooksClient
        """
        return self._raw_client

    def listwebhooks(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.webhooks.listwebhooks()
        """
        _response = self._raw_client.listwebhooks(request_options=request_options)
        return _response.data

    def createwebhook(
        self, *, url: str, events: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        url : str

        events : typing.Sequence[str]

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
        client.webhooks.createwebhook(
            url="url",
            events=["events"],
        )
        """
        _response = self._raw_client.createwebhook(url=url, events=events, request_options=request_options)
        return _response.data

    def getwebhook(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.webhooks.getwebhook(
            id="id",
        )
        """
        _response = self._raw_client.getwebhook(id, request_options=request_options)
        return _response.data

    def updatewebhook(
        self,
        id: str,
        *,
        url: str,
        events: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        url : str

        events : typing.Sequence[str]

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
        client.webhooks.updatewebhook(
            id="id",
            url="url",
            events=["events"],
        )
        """
        _response = self._raw_client.updatewebhook(id, url=url, events=events, request_options=request_options)
        return _response.data

    def deletewebhook(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.webhooks.deletewebhook(
            id="id",
        )
        """
        _response = self._raw_client.deletewebhook(id, request_options=request_options)
        return _response.data


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhooksClient
        """
        return self._raw_client

    async def listwebhooks(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.webhooks.listwebhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.listwebhooks(request_options=request_options)
        return _response.data

    async def createwebhook(
        self, *, url: str, events: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        url : str

        events : typing.Sequence[str]

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
            await client.webhooks.createwebhook(
                url="url",
                events=["events"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createwebhook(url=url, events=events, request_options=request_options)
        return _response.data

    async def getwebhook(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.webhooks.getwebhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getwebhook(id, request_options=request_options)
        return _response.data

    async def updatewebhook(
        self,
        id: str,
        *,
        url: str,
        events: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        url : str

        events : typing.Sequence[str]

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
            await client.webhooks.updatewebhook(
                id="id",
                url="url",
                events=["events"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatewebhook(id, url=url, events=events, request_options=request_options)
        return _response.data

    async def deletewebhook(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.webhooks.deletewebhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletewebhook(id, request_options=request_options)
        return _response.data
