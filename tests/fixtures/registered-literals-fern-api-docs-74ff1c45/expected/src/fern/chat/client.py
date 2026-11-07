

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_message import ChatMessage
from ..types.language_model import LanguageModel
from ..types.post_chat_completion_response import PostChatCompletionResponse
from .raw_client import AsyncRawChatClient, RawChatClient


OMIT = typing.cast(typing.Any, ...)


class ChatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChatClient
        """
        return self._raw_client

    def post_chat_completion(
        self,
        domain: str,
        *,
        messages: typing.Sequence[ChatMessage],
        model: typing.Optional[LanguageModel] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        system_prompt: typing.Optional[str] = OMIT,
        rewrite_query: typing.Optional[bool] = OMIT,
        user_is_authed: typing.Optional[bool] = OMIT,
        allowed_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        source: typing.Optional[str] = OMIT,
        basepaths: typing.Optional[typing.Sequence[str]] = OMIT,
        skip_save_query: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostChatCompletionResponse:
        """
        Parameters
        ----------
        domain : str

        messages : typing.Sequence[ChatMessage]
            The messages to use for the chat completion

        model : typing.Optional[LanguageModel]
            The model to use for the chat completion

        max_tokens : typing.Optional[int]
            The maximum number of tokens to generate. Note: setting a token count lower than 2000 may result in incomplete responses. You can add a custom system prompt to control the verbosity of the response.

        system_prompt : typing.Optional[str]
            The system prompt to use for the chat completion

        rewrite_query : typing.Optional[bool]
            Whether to rewrite the query using query decomposition

        user_is_authed : typing.Optional[bool]
            Whether the requesting user is authenticated. When true, authed chunks are included in results.

        allowed_roles : typing.Optional[typing.Sequence[str]]
            Roles the authenticated user has. Used to filter chunks by role-based access control.

        source : typing.Optional[str]
            The origin of the request (e.g. 'web', 'slack', 'api').

        basepaths : typing.Optional[typing.Sequence[str]]
            Restrict retrieval to pages under these URL path prefixes (e.g. ['/my-product']). Matches the scoping the Ask AI widget applies when embedded under a product path. Omit to search the whole site.

        skip_save_query : typing.Optional[bool]
            Set to true for test or eval traffic. The request is answered (and billed) normally but is excluded from usage analytics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostChatCompletionResponse
            Successful Response

        Examples
        --------
        from fern import ChatMessage, ChatMessageRole, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat.post_chat_completion(
            domain="domain",
            messages=[
                ChatMessage(
                    role=ChatMessageRole.USER,
                    content="content",
                )
            ],
        )
        """
        _response = self._raw_client.post_chat_completion(
            domain,
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            system_prompt=system_prompt,
            rewrite_query=rewrite_query,
            user_is_authed=user_is_authed,
            allowed_roles=allowed_roles,
            source=source,
            basepaths=basepaths,
            skip_save_query=skip_save_query,
            request_options=request_options,
        )
        return _response.data


class AsyncChatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChatClient
        """
        return self._raw_client

    async def post_chat_completion(
        self,
        domain: str,
        *,
        messages: typing.Sequence[ChatMessage],
        model: typing.Optional[LanguageModel] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        system_prompt: typing.Optional[str] = OMIT,
        rewrite_query: typing.Optional[bool] = OMIT,
        user_is_authed: typing.Optional[bool] = OMIT,
        allowed_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        source: typing.Optional[str] = OMIT,
        basepaths: typing.Optional[typing.Sequence[str]] = OMIT,
        skip_save_query: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostChatCompletionResponse:
        """
        Parameters
        ----------
        domain : str

        messages : typing.Sequence[ChatMessage]
            The messages to use for the chat completion

        model : typing.Optional[LanguageModel]
            The model to use for the chat completion

        max_tokens : typing.Optional[int]
            The maximum number of tokens to generate. Note: setting a token count lower than 2000 may result in incomplete responses. You can add a custom system prompt to control the verbosity of the response.

        system_prompt : typing.Optional[str]
            The system prompt to use for the chat completion

        rewrite_query : typing.Optional[bool]
            Whether to rewrite the query using query decomposition

        user_is_authed : typing.Optional[bool]
            Whether the requesting user is authenticated. When true, authed chunks are included in results.

        allowed_roles : typing.Optional[typing.Sequence[str]]
            Roles the authenticated user has. Used to filter chunks by role-based access control.

        source : typing.Optional[str]
            The origin of the request (e.g. 'web', 'slack', 'api').

        basepaths : typing.Optional[typing.Sequence[str]]
            Restrict retrieval to pages under these URL path prefixes (e.g. ['/my-product']). Matches the scoping the Ask AI widget applies when embedded under a product path. Omit to search the whole site.

        skip_save_query : typing.Optional[bool]
            Set to true for test or eval traffic. The request is answered (and billed) normally but is excluded from usage analytics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostChatCompletionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChatMessage, ChatMessageRole

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat.post_chat_completion(
                domain="domain",
                messages=[
                    ChatMessage(
                        role=ChatMessageRole.USER,
                        content="content",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_chat_completion(
            domain,
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            system_prompt=system_prompt,
            rewrite_query=rewrite_query,
            user_is_authed=user_is_authed,
            allowed_roles=allowed_roles,
            source=source,
            basepaths=basepaths,
            skip_save_query=skip_save_query,
            request_options=request_options,
        )
        return _response.data
