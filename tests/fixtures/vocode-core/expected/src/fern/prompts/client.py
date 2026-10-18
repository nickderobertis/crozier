

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collect_field import CollectField
from ..types.prompt import Prompt
from ..types.prompt_page import PromptPage
from ..types.prompt_params_prompt_template import PromptParamsPromptTemplate
from ..types.prompt_update_params_collect_fields import PromptUpdateParamsCollectFields
from ..types.prompt_update_params_content import PromptUpdateParamsContent
from ..types.prompt_update_params_context_endpoint import PromptUpdateParamsContextEndpoint
from ..types.prompt_update_params_prompt_template import PromptUpdateParamsPromptTemplate
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

    def get_prompt(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Prompt:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.get_prompt(
            id="id",
        )
        """
        _response = self._raw_client.get_prompt(id=id, request_options=request_options)
        return _response.data

    def list_prompts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.list_prompts()
        """
        _response = self._raw_client.list_prompts(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def create_prompt(
        self,
        *,
        content: typing.Optional[str] = OMIT,
        collect_fields: typing.Optional[typing.Sequence[CollectField]] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[PromptParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Parameters
        ----------
        content : typing.Optional[str]

        collect_fields : typing.Optional[typing.Sequence[CollectField]]

        context_endpoint : typing.Optional[str]

        prompt_template : typing.Optional[PromptParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.create_prompt()
        """
        _response = self._raw_client.create_prompt(
            content=content,
            collect_fields=collect_fields,
            context_endpoint=context_endpoint,
            prompt_template=prompt_template,
            request_options=request_options,
        )
        return _response.data

    def update_prompt(
        self,
        *,
        id: str,
        content: typing.Optional[PromptUpdateParamsContent] = OMIT,
        collect_fields: typing.Optional[PromptUpdateParamsCollectFields] = OMIT,
        context_endpoint: typing.Optional[PromptUpdateParamsContextEndpoint] = OMIT,
        prompt_template: typing.Optional[PromptUpdateParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Parameters
        ----------
        id : str

        content : typing.Optional[PromptUpdateParamsContent]

        collect_fields : typing.Optional[PromptUpdateParamsCollectFields]

        context_endpoint : typing.Optional[PromptUpdateParamsContextEndpoint]

        prompt_template : typing.Optional[PromptUpdateParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.update_prompt(
            id="id",
        )
        """
        _response = self._raw_client.update_prompt(
            id=id,
            content=content,
            collect_fields=collect_fields,
            context_endpoint=context_endpoint,
            prompt_template=prompt_template,
            request_options=request_options,
        )
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

    async def get_prompt(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Prompt:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.get_prompt(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prompt(id=id, request_options=request_options)
        return _response.data

    async def list_prompts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptPage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.list_prompts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_prompts(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def create_prompt(
        self,
        *,
        content: typing.Optional[str] = OMIT,
        collect_fields: typing.Optional[typing.Sequence[CollectField]] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[PromptParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Parameters
        ----------
        content : typing.Optional[str]

        collect_fields : typing.Optional[typing.Sequence[CollectField]]

        context_endpoint : typing.Optional[str]

        prompt_template : typing.Optional[PromptParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.create_prompt()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_prompt(
            content=content,
            collect_fields=collect_fields,
            context_endpoint=context_endpoint,
            prompt_template=prompt_template,
            request_options=request_options,
        )
        return _response.data

    async def update_prompt(
        self,
        *,
        id: str,
        content: typing.Optional[PromptUpdateParamsContent] = OMIT,
        collect_fields: typing.Optional[PromptUpdateParamsCollectFields] = OMIT,
        context_endpoint: typing.Optional[PromptUpdateParamsContextEndpoint] = OMIT,
        prompt_template: typing.Optional[PromptUpdateParamsPromptTemplate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Parameters
        ----------
        id : str

        content : typing.Optional[PromptUpdateParamsContent]

        collect_fields : typing.Optional[PromptUpdateParamsCollectFields]

        context_endpoint : typing.Optional[PromptUpdateParamsContextEndpoint]

        prompt_template : typing.Optional[PromptUpdateParamsPromptTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.update_prompt(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_prompt(
            id=id,
            content=content,
            collect_fields=collect_fields,
            context_endpoint=context_endpoint,
            prompt_template=prompt_template,
            request_options=request_options,
        )
        return _response.data
