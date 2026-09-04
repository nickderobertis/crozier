

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.participant_list import ParticipantList
from .raw_client import AsyncRawRegistryClient, RawRegistryClient


class RegistryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRegistryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRegistryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRegistryClient
        """
        return self._raw_client

    def list_participants(self, *, request_options: typing.Optional[RequestOptions] = None) -> ParticipantList:
        """
        Listet alle aktiven Teilnehmer im föderierten System auf

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantList
            Teilnehmer erfolgreich abgerufen

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.registry.list_participants()
        """
        _response = self._raw_client.list_participants(request_options=request_options)
        return _response.data


class AsyncRegistryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRegistryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRegistryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRegistryClient
        """
        return self._raw_client

    async def list_participants(self, *, request_options: typing.Optional[RequestOptions] = None) -> ParticipantList:
        """
        Listet alle aktiven Teilnehmer im föderierten System auf

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantList
            Teilnehmer erfolgreich abgerufen

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.registry.list_participants()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_participants(request_options=request_options)
        return _response.data
