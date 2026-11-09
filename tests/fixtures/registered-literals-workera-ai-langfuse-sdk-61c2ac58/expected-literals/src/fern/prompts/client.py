

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_prompt_request import CreatePromptRequest
from ..types.prompt import Prompt
from ..types.prompt_meta_list_response import PromptMetaListResponse
from .raw_client import AsyncRawPromptsClient, RawPromptsClient


OMIT = typing.cast(typing.Any, ...)


class PromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPromptsClient
        """
        return self._raw_client

    def get(
        self,
        prompt_name: str,
        *,
        version: typing.Optional[int] = None,
        label: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Get a prompt

        Parameters
        ----------
        prompt_name : str
            The name of the prompt

        version : typing.Optional[int]
            Version of the prompt to be retrieved.

        label : typing.Optional[str]
            Label of the prompt to be retrieved. Defaults to "production" if no label or version is set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prompts.get(
            prompt_name="promptName",
        )
        """
        _response = self._raw_client.get(prompt_name, version=version, label=label, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        from_updated_at: typing.Optional[dt.datetime] = None,
        to_updated_at: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptMetaListResponse:
        """
        Get a list of prompt names with versions and labels

        Parameters
        ----------
        name : typing.Optional[str]

        label : typing.Optional[str]

        tag : typing.Optional[str]

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        from_updated_at : typing.Optional[dt.datetime]
            Optional filter to only include prompt versions created/updated on or after a certain datetime (ISO 8601)

        to_updated_at : typing.Optional[dt.datetime]
            Optional filter to only include prompt versions created/updated before a certain datetime (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptMetaListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prompts.list()
        """
        _response = self._raw_client.list(
            name=name,
            label=label,
            tag=tag,
            page=page,
            limit=limit,
            from_updated_at=from_updated_at,
            to_updated_at=to_updated_at,
            request_options=request_options,
        )
        return _response.data

    def create(
        self, *, request: CreatePromptRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> Prompt:
        """
        Create a new version for the prompt with the given `name`

        Parameters
        ----------
        request : CreatePromptRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt


        Examples
        --------
        from fern import ChatMessage, CreatePromptRequestZero, FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prompts.create(
            request=CreatePromptRequestZero(
                name="name",
                prompt=[
                    ChatMessage(
                        role="role",
                        content="content",
                    )
                ],
                type="chat",
            ),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data


class AsyncPromptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPromptsClient
        """
        return self._raw_client

    async def get(
        self,
        prompt_name: str,
        *,
        version: typing.Optional[int] = None,
        label: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Get a prompt

        Parameters
        ----------
        prompt_name : str
            The name of the prompt

        version : typing.Optional[int]
            Version of the prompt to be retrieved.

        label : typing.Optional[str]
            Label of the prompt to be retrieved. Defaults to "production" if no label or version is set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prompts.get(
                prompt_name="promptName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            prompt_name, version=version, label=label, request_options=request_options
        )
        return _response.data

    async def list(
        self,
        *,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        from_updated_at: typing.Optional[dt.datetime] = None,
        to_updated_at: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptMetaListResponse:
        """
        Get a list of prompt names with versions and labels

        Parameters
        ----------
        name : typing.Optional[str]

        label : typing.Optional[str]

        tag : typing.Optional[str]

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        from_updated_at : typing.Optional[dt.datetime]
            Optional filter to only include prompt versions created/updated on or after a certain datetime (ISO 8601)

        to_updated_at : typing.Optional[dt.datetime]
            Optional filter to only include prompt versions created/updated before a certain datetime (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptMetaListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prompts.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            name=name,
            label=label,
            tag=tag,
            page=page,
            limit=limit,
            from_updated_at=from_updated_at,
            to_updated_at=to_updated_at,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self, *, request: CreatePromptRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> Prompt:
        """
        Create a new version for the prompt with the given `name`

        Parameters
        ----------
        request : CreatePromptRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChatMessage, CreatePromptRequestZero

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prompts.create(
                request=CreatePromptRequestZero(
                    name="name",
                    prompt=[
                        ChatMessage(
                            role="role",
                            content="content",
                        )
                    ],
                    type="chat",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data
