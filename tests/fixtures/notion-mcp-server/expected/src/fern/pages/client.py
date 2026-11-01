

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.move_page_parent_request import MovePageParentRequest
from .raw_client import AsyncRawPagesClient, RawPagesClient
from .types.retrieve_page_markdown_response import RetrievePageMarkdownResponse
from .types.update_page_markdown_request_insert_content import UpdatePageMarkdownRequestInsertContent
from .types.update_page_markdown_request_replace_content import UpdatePageMarkdownRequestReplaceContent
from .types.update_page_markdown_request_replace_content_range import UpdatePageMarkdownRequestReplaceContentRange
from .types.update_page_markdown_request_type import UpdatePageMarkdownRequestType
from .types.update_page_markdown_request_update_content import UpdatePageMarkdownRequestUpdateContent
from .types.update_page_markdown_response import UpdatePageMarkdownResponse


OMIT = typing.cast(typing.Any, ...)


class PagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPagesClient
        """
        return self._raw_client

    def move_page(
        self, page_id: str, *, parent: MovePageParentRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Move a page to a different parent location

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        parent : MovePageParentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import (
            FernApi,
            MovePageParentRequestPageId,
            MovePageParentRequestPageIdType,
        )

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.pages.move_page(
            page_id="page_id",
            parent=MovePageParentRequestPageId(
                type=MovePageParentRequestPageIdType.PAGE_ID,
                page_id="page_id",
            ),
        )
        """
        _response = self._raw_client.move_page(page_id, parent=parent, request_options=request_options)
        return _response.data

    def retrieve_page_markdown(
        self,
        page_id: str,
        *,
        include_transcript: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrievePageMarkdownResponse:
        """
        Retrieve the full content of a Notion page rendered as enhanced Markdown. Designed for agentic and developer tools that work natively with Markdown instead of the block JSON returned by Retrieve block children.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        include_transcript : typing.Optional[bool]
            Whether to include meeting note transcripts. When false (default), a placeholder with the meeting note URL is shown instead of the full transcript.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrievePageMarkdownResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.pages.retrieve_page_markdown(
            page_id="page_id",
        )
        """
        _response = self._raw_client.retrieve_page_markdown(
            page_id, include_transcript=include_transcript, request_options=request_options
        )
        return _response.data

    def update_page_markdown(
        self,
        page_id: str,
        *,
        type: UpdatePageMarkdownRequestType,
        replace_content: typing.Optional[UpdatePageMarkdownRequestReplaceContent] = OMIT,
        update_content: typing.Optional[UpdatePageMarkdownRequestUpdateContent] = OMIT,
        insert_content: typing.Optional[UpdatePageMarkdownRequestInsertContent] = OMIT,
        replace_content_range: typing.Optional[UpdatePageMarkdownRequestReplaceContentRange] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePageMarkdownResponse:
        """
        Update the content of a Notion page using enhanced Markdown. Prefer `replace_content` to overwrite the whole page or `update_content` for targeted find-and-replace edits.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        type : UpdatePageMarkdownRequestType
            The kind of edit to apply. Prefer `replace_content` (overwrite the whole page) or `update_content` (targeted find-and-replace). `insert_content` and `replace_content_range` are deprecated.

        replace_content : typing.Optional[UpdatePageMarkdownRequestReplaceContent]
            Provide when type is `replace_content`. Replaces the entire page content.

        update_content : typing.Optional[UpdatePageMarkdownRequestUpdateContent]
            Provide when type is `update_content`. Applies targeted find-and-replace edits.

        insert_content : typing.Optional[UpdatePageMarkdownRequestInsertContent]
            Deprecated. Provide when type is `insert_content`. Inserts Markdown at a position.

        replace_content_range : typing.Optional[UpdatePageMarkdownRequestReplaceContentRange]
            Deprecated. Provide when type is `replace_content_range`. Replaces a selected range of Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePageMarkdownResponse
            Successful response

        Examples
        --------
        from fern.pages import UpdatePageMarkdownRequestType

        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.pages.update_page_markdown(
            page_id="page_id",
            type=UpdatePageMarkdownRequestType.REPLACE_CONTENT,
        )
        """
        _response = self._raw_client.update_page_markdown(
            page_id,
            type=type,
            replace_content=replace_content,
            update_content=update_content,
            insert_content=insert_content,
            replace_content_range=replace_content_range,
            request_options=request_options,
        )
        return _response.data


class AsyncPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPagesClient
        """
        return self._raw_client

    async def move_page(
        self, page_id: str, *, parent: MovePageParentRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Move a page to a different parent location

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        parent : MovePageParentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            MovePageParentRequestPageId,
            MovePageParentRequestPageIdType,
        )

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.move_page(
                page_id="page_id",
                parent=MovePageParentRequestPageId(
                    type=MovePageParentRequestPageIdType.PAGE_ID,
                    page_id="page_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_page(page_id, parent=parent, request_options=request_options)
        return _response.data

    async def retrieve_page_markdown(
        self,
        page_id: str,
        *,
        include_transcript: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrievePageMarkdownResponse:
        """
        Retrieve the full content of a Notion page rendered as enhanced Markdown. Designed for agentic and developer tools that work natively with Markdown instead of the block JSON returned by Retrieve block children.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        include_transcript : typing.Optional[bool]
            Whether to include meeting note transcripts. When false (default), a placeholder with the meeting note URL is shown instead of the full transcript.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrievePageMarkdownResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.retrieve_page_markdown(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_page_markdown(
            page_id, include_transcript=include_transcript, request_options=request_options
        )
        return _response.data

    async def update_page_markdown(
        self,
        page_id: str,
        *,
        type: UpdatePageMarkdownRequestType,
        replace_content: typing.Optional[UpdatePageMarkdownRequestReplaceContent] = OMIT,
        update_content: typing.Optional[UpdatePageMarkdownRequestUpdateContent] = OMIT,
        insert_content: typing.Optional[UpdatePageMarkdownRequestInsertContent] = OMIT,
        replace_content_range: typing.Optional[UpdatePageMarkdownRequestReplaceContentRange] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePageMarkdownResponse:
        """
        Update the content of a Notion page using enhanced Markdown. Prefer `replace_content` to overwrite the whole page or `update_content` for targeted find-and-replace edits.

        Parameters
        ----------
        page_id : str
            Identifier for a Notion page (or block) to read or update as markdown.

        type : UpdatePageMarkdownRequestType
            The kind of edit to apply. Prefer `replace_content` (overwrite the whole page) or `update_content` (targeted find-and-replace). `insert_content` and `replace_content_range` are deprecated.

        replace_content : typing.Optional[UpdatePageMarkdownRequestReplaceContent]
            Provide when type is `replace_content`. Replaces the entire page content.

        update_content : typing.Optional[UpdatePageMarkdownRequestUpdateContent]
            Provide when type is `update_content`. Applies targeted find-and-replace edits.

        insert_content : typing.Optional[UpdatePageMarkdownRequestInsertContent]
            Deprecated. Provide when type is `insert_content`. Inserts Markdown at a position.

        replace_content_range : typing.Optional[UpdatePageMarkdownRequestReplaceContentRange]
            Deprecated. Provide when type is `replace_content_range`. Replaces a selected range of Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePageMarkdownResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.pages import UpdatePageMarkdownRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.update_page_markdown(
                page_id="page_id",
                type=UpdatePageMarkdownRequestType.REPLACE_CONTENT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_page_markdown(
            page_id,
            type=type,
            replace_content=replace_content,
            update_content=update_content,
            insert_content=insert_content,
            replace_content_range=replace_content_range,
            request_options=request_options,
        )
        return _response.data
