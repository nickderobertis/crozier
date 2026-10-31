

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_formats import ArtifactFormats
from ..types.change_log_item import ChangeLogItem
from ..types.event_type import EventType
from .raw_client import AsyncRawInfoClient, RawInfoClient


class InfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInfoClient
        """
        return self._raw_client

    def artifact_formats(self, *, request_options: typing.Optional[RequestOptions] = None) -> ArtifactFormats:
        """
        List the available artifact formats

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactFormats
            A list of artifact formats

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.info.artifact_formats()
        """
        _response = self._raw_client.artifact_formats(request_options=request_options)
        return _response.data

    def recent_changes(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ChangeLogItem]:
        """
        The Contribly change log.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ChangeLogItem]
            A list of change log items

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.info.recent_changes()
        """
        _response = self._raw_client.recent_changes(request_options=request_options)
        return _response.data

    def event_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[EventType]:
        """
        List available notification event types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventType]
            A list of event types

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.info.event_types()
        """
        _response = self._raw_client.event_types(request_options=request_options)
        return _response.data


class AsyncInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInfoClient
        """
        return self._raw_client

    async def artifact_formats(self, *, request_options: typing.Optional[RequestOptions] = None) -> ArtifactFormats:
        """
        List the available artifact formats

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactFormats
            A list of artifact formats

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.info.artifact_formats()


        asyncio.run(main())
        """
        _response = await self._raw_client.artifact_formats(request_options=request_options)
        return _response.data

    async def recent_changes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ChangeLogItem]:
        """
        The Contribly change log.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ChangeLogItem]
            A list of change log items

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.info.recent_changes()


        asyncio.run(main())
        """
        _response = await self._raw_client.recent_changes(request_options=request_options)
        return _response.data

    async def event_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[EventType]:
        """
        List available notification event types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventType]
            A list of event types

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.info.event_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.event_types(request_options=request_options)
        return _response.data
