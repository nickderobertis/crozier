

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..instruction.types.instruction_search import InstructionSearch
from .raw_client import AsyncRawSearchClient, RawSearchClient
from .types.global_search_response import GlobalSearchResponse


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

    def instruction(
        self, *, recipe_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstructionSearch:
        """
        Search instructions. Currently, this endpoint does not support pagination. This will be added in the future

        Parameters
        ----------
        recipe_id : str
            ID of an recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstructionSearch
            Successful request and returned data

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.instruction(
            recipe_id="RecipeID",
        )
        """
        _response = self._raw_client.instruction(recipe_id=recipe_id, request_options=request_options)
        return _response.data

    def global_search(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalSearchResponse:
        """
        Search through all records globally in the API. This request is still being developed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.global_search()
        """
        _response = self._raw_client.global_search(request_options=request_options)
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

    async def instruction(
        self, *, recipe_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstructionSearch:
        """
        Search instructions. Currently, this endpoint does not support pagination. This will be added in the future

        Parameters
        ----------
        recipe_id : str
            ID of an recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstructionSearch
            Successful request and returned data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.instruction(
                recipe_id="RecipeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.instruction(recipe_id=recipe_id, request_options=request_options)
        return _response.data

    async def global_search(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalSearchResponse:
        """
        Search through all records globally in the API. This request is still being developed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.global_search()


        asyncio.run(main())
        """
        _response = await self._raw_client.global_search(request_options=request_options)
        return _response.data
