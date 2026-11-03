

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLettersClient, RawLettersClient
from .types.list_letters_request_carrier import ListLettersRequestCarrier
from .types.list_letters_request_priority import ListLettersRequestPriority


class LettersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLettersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLettersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLettersClient
        """
        return self._raw_client

    def list_letters(
        self,
        *,
        priority: typing.Optional[ListLettersRequestPriority] = None,
        carrier: typing.Optional[ListLettersRequestCarrier] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        priority : typing.Optional[ListLettersRequestPriority]
            Sorting priority.

        carrier : typing.Optional[ListLettersRequestCarrier]
            Carrier to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The letters

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.letters.list_letters()
        """
        _response = self._raw_client.list_letters(priority=priority, carrier=carrier, request_options=request_options)
        return _response.data


class AsyncLettersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLettersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLettersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLettersClient
        """
        return self._raw_client

    async def list_letters(
        self,
        *,
        priority: typing.Optional[ListLettersRequestPriority] = None,
        carrier: typing.Optional[ListLettersRequestCarrier] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        priority : typing.Optional[ListLettersRequestPriority]
            Sorting priority.

        carrier : typing.Optional[ListLettersRequestCarrier]
            Carrier to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The letters

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.letters.list_letters()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_letters(
            priority=priority, carrier=carrier, request_options=request_options
        )
        return _response.data
