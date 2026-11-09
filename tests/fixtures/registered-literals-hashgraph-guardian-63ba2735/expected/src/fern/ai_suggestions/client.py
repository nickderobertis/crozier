

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAiSuggestionsClient, RawAiSuggestionsClient


class AiSuggestionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAiSuggestionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAiSuggestionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAiSuggestionsClient
        """
        return self._raw_client

    def ai_suggestions_api_get_ai_answer(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns AI response to the current question

        Parameters
        ----------
        q : str
            The question of choosing a methodology

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai_suggestions.ai_suggestions_api_get_ai_answer(
            q="Find me large scale projects",
        )
        """
        _response = self._raw_client.ai_suggestions_api_get_ai_answer(q=q, request_options=request_options)
        return _response.data

    def ai_suggestions_api_rebuild_vector(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Rebuilds vector based on policy data in the DB

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
        client.ai_suggestions.ai_suggestions_api_rebuild_vector()
        """
        _response = self._raw_client.ai_suggestions_api_rebuild_vector(request_options=request_options)
        return _response.data


class AsyncAiSuggestionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAiSuggestionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAiSuggestionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAiSuggestionsClient
        """
        return self._raw_client

    async def ai_suggestions_api_get_ai_answer(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns AI response to the current question

        Parameters
        ----------
        q : str
            The question of choosing a methodology

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai_suggestions.ai_suggestions_api_get_ai_answer(
                q="Find me large scale projects",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_suggestions_api_get_ai_answer(q=q, request_options=request_options)
        return _response.data

    async def ai_suggestions_api_rebuild_vector(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Rebuilds vector based on policy data in the DB

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
            await client.ai_suggestions.ai_suggestions_api_rebuild_vector()


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_suggestions_api_rebuild_vector(request_options=request_options)
        return _response.data
