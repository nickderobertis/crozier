

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.suggestions_config_dto import SuggestionsConfigDto
from ..types.suggestions_config_item_dto import SuggestionsConfigItemDto
from ..types.suggestions_output_dto import SuggestionsOutputDto
from .raw_client import AsyncRawSuggestionsClient, RawSuggestionsClient


OMIT = typing.cast(typing.Any, ...)


class SuggestionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSuggestionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSuggestionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSuggestionsClient
        """
        return self._raw_client

    def suggestions_api_policy_suggestions(
        self,
        *,
        block_type: str,
        children: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuggestionsOutputDto:
        """
        Get next and nested suggested block types. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        block_type : str

        children : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestionsOutputDto
            Successful operation. Suggested next and nested block types respectively.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suggestions.suggestions_api_policy_suggestions(
            block_type="blockType",
        )
        """
        _response = self._raw_client.suggestions_api_policy_suggestions(
            block_type=block_type, children=children, request_options=request_options
        )
        return _response.data

    def suggestions_api_get_policy_suggestions_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuggestionsConfigDto:
        """
        Get suggestions config. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestionsConfigDto
            Successful operation. Response suggestions config.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suggestions.suggestions_api_get_policy_suggestions_config()
        """
        _response = self._raw_client.suggestions_api_get_policy_suggestions_config(request_options=request_options)
        return _response.data

    def suggestions_api_set_policy_suggestions_config(
        self, *, items: SuggestionsConfigItemDto, request_options: typing.Optional[RequestOptions] = None
    ) -> SuggestionsConfigDto:
        """
        Set suggestions config. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        items : SuggestionsConfigItemDto

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestionsConfigDto
            Successful operation. Response setted suggestions config.

        Examples
        --------
        from fern import FernApi, SuggestionsConfigItemDto

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suggestions.suggestions_api_set_policy_suggestions_config(
            items=SuggestionsConfigItemDto(
                id="id",
                type="Policy",
                index=1.1,
            ),
        )
        """
        _response = self._raw_client.suggestions_api_set_policy_suggestions_config(
            items=items, request_options=request_options
        )
        return _response.data


class AsyncSuggestionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSuggestionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSuggestionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSuggestionsClient
        """
        return self._raw_client

    async def suggestions_api_policy_suggestions(
        self,
        *,
        block_type: str,
        children: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuggestionsOutputDto:
        """
        Get next and nested suggested block types. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        block_type : str

        children : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestionsOutputDto
            Successful operation. Suggested next and nested block types respectively.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suggestions.suggestions_api_policy_suggestions(
                block_type="blockType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suggestions_api_policy_suggestions(
            block_type=block_type, children=children, request_options=request_options
        )
        return _response.data

    async def suggestions_api_get_policy_suggestions_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuggestionsConfigDto:
        """
        Get suggestions config. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestionsConfigDto
            Successful operation. Response suggestions config.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suggestions.suggestions_api_get_policy_suggestions_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.suggestions_api_get_policy_suggestions_config(
            request_options=request_options
        )
        return _response.data

    async def suggestions_api_set_policy_suggestions_config(
        self, *, items: SuggestionsConfigItemDto, request_options: typing.Optional[RequestOptions] = None
    ) -> SuggestionsConfigDto:
        """
        Set suggestions config. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        items : SuggestionsConfigItemDto

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestionsConfigDto
            Successful operation. Response setted suggestions config.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SuggestionsConfigItemDto

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suggestions.suggestions_api_set_policy_suggestions_config(
                items=SuggestionsConfigItemDto(
                    id="id",
                    type="Policy",
                    index=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suggestions_api_set_policy_suggestions_config(
            items=items, request_options=request_options
        )
        return _response.data
