

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_get_autocompletes import EndpointGetAutocompletes
from .raw_client import AsyncRawAutocompletesClient, RawAutocompletesClient


class AutocompletesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAutocompletesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAutocompletesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAutocompletesClient
        """
        return self._raw_client

    def get_autocompletes(
        self, *, query: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetAutocompletes:
        """
        Retrieve an array of names and locations, filtered by category, that begin with the query string passed in. Ideally used for search autocomplete dropdowns, as the search functionality filters against name and location. The four potential categories are: `conversations` for names of users you are in existing conversations with; `matches` for names of users you have previously skipped over; `people` for names of all other users; `locations` for locations of users. Only users and their locations who exist with the current access token's bubble are considered.

        Parameters
        ----------
        query : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAutocompletes
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.autocompletes.get_autocompletes()
        """
        _response = self._raw_client.get_autocompletes(query=query, request_options=request_options)
        return _response.data


class AsyncAutocompletesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAutocompletesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAutocompletesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAutocompletesClient
        """
        return self._raw_client

    async def get_autocompletes(
        self, *, query: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetAutocompletes:
        """
        Retrieve an array of names and locations, filtered by category, that begin with the query string passed in. Ideally used for search autocomplete dropdowns, as the search functionality filters against name and location. The four potential categories are: `conversations` for names of users you are in existing conversations with; `matches` for names of users you have previously skipped over; `people` for names of all other users; `locations` for locations of users. Only users and their locations who exist with the current access token's bubble are considered.

        Parameters
        ----------
        query : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAutocompletes
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.autocompletes.get_autocompletes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_autocompletes(query=query, request_options=request_options)
        return _response.data
