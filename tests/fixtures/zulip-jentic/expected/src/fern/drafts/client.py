

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.draft import Draft
from ..types.json_success import JsonSuccess
from .raw_client import AsyncRawDraftsClient, RawDraftsClient
from .types.create_drafts_response import CreateDraftsResponse
from .types.create_saved_snippet_response import CreateSavedSnippetResponse
from .types.edit_draft_request_draft import EditDraftRequestDraft
from .types.get_drafts_response import GetDraftsResponse
from .types.get_saved_snippets_response import GetSavedSnippetsResponse


OMIT = typing.cast(typing.Any, ...)


class DraftsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDraftsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDraftsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDraftsClient
        """
        return self._raw_client

    def get_drafts(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetDraftsResponse:
        """
        Fetch all drafts for the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDraftsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.get_drafts()
        """
        _response = self._raw_client.get_drafts(request_options=request_options)
        return _response.data

    def create_drafts(
        self,
        *,
        drafts: typing.Optional[typing.Sequence[Draft]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDraftsResponse:
        """
        Create one or more drafts on the server. These drafts will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        drafts : typing.Optional[typing.Sequence[Draft]]
            A JSON-encoded list of containing new draft objects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDraftsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.create_drafts()
        """
        _response = self._raw_client.create_drafts(drafts=drafts, request_options=request_options)
        return _response.data

    def delete_draft(self, draft_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        Delete a single draft from the server. The deletion will be automatically
        synchronized to other clients via a `drafts` event.

        Parameters
        ----------
        draft_id : int
            The ID of the draft you want to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.delete_draft(
            draft_id=1,
        )
        """
        _response = self._raw_client.delete_draft(draft_id, request_options=request_options)
        return _response.data

    def edit_draft(
        self, draft_id: int, *, draft: EditDraftRequestDraft, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Edit a draft on the server. The edit will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        draft_id : int
            The ID of the draft to be edited.

        draft : EditDraftRequestDraft
            A JSON-encoded object containing a replacement draft object for this ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern.drafts import EditDraftRequestDraft, EditDraftRequestDraftType

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.edit_draft(
            draft_id=1,
            draft=EditDraftRequestDraft(
                type=EditDraftRequestDraftType.STREAM,
                to=[1],
                topic="questions",
                content="how tough is a Lamy Safari?",
                timestamp=1595479019,
            ),
        )
        """
        _response = self._raw_client.edit_draft(draft_id, draft=draft, request_options=request_options)
        return _response.data

    def get_saved_snippets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSavedSnippetsResponse:
        """
        Fetch all the saved snippets for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSavedSnippetsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.get_saved_snippets()
        """
        _response = self._raw_client.get_saved_snippets(request_options=request_options)
        return _response.data

    def create_saved_snippet(
        self, *, title: str, content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateSavedSnippetResponse:
        """
        Create a new saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        title : str
            The title of the saved snippet.

        content : str
            The content of the saved snippet in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSavedSnippetResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.create_saved_snippet(
            title="Example title",
            content="Welcome to the organization.",
        )
        """
        _response = self._raw_client.create_saved_snippet(title=title, content=content, request_options=request_options)
        return _response.data

    def delete_saved_snippet(
        self, saved_snippet_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete a saved snippet.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.delete_saved_snippet(
            saved_snippet_id=1,
        )
        """
        _response = self._raw_client.delete_saved_snippet(saved_snippet_id, request_options=request_options)
        return _response.data

    def edit_saved_snippet(
        self,
        saved_snippet_id: int,
        *,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Edit a saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 368).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to edit.

        title : typing.Optional[str]
            The title of the saved snippet.

        content : typing.Optional[str]
            The content of the saved snippet in the original [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drafts.edit_saved_snippet(
            saved_snippet_id=1,
        )
        """
        _response = self._raw_client.edit_saved_snippet(
            saved_snippet_id, title=title, content=content, request_options=request_options
        )
        return _response.data


class AsyncDraftsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDraftsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDraftsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDraftsClient
        """
        return self._raw_client

    async def get_drafts(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetDraftsResponse:
        """
        Fetch all drafts for the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDraftsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.get_drafts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_drafts(request_options=request_options)
        return _response.data

    async def create_drafts(
        self,
        *,
        drafts: typing.Optional[typing.Sequence[Draft]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDraftsResponse:
        """
        Create one or more drafts on the server. These drafts will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        drafts : typing.Optional[typing.Sequence[Draft]]
            A JSON-encoded list of containing new draft objects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDraftsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.create_drafts()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_drafts(drafts=drafts, request_options=request_options)
        return _response.data

    async def delete_draft(
        self, draft_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete a single draft from the server. The deletion will be automatically
        synchronized to other clients via a `drafts` event.

        Parameters
        ----------
        draft_id : int
            The ID of the draft you want to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.delete_draft(
                draft_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_draft(draft_id, request_options=request_options)
        return _response.data

    async def edit_draft(
        self, draft_id: int, *, draft: EditDraftRequestDraft, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Edit a draft on the server. The edit will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        draft_id : int
            The ID of the draft to be edited.

        draft : EditDraftRequestDraft
            A JSON-encoded object containing a replacement draft object for this ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern.drafts import EditDraftRequestDraft, EditDraftRequestDraftType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.edit_draft(
                draft_id=1,
                draft=EditDraftRequestDraft(
                    type=EditDraftRequestDraftType.STREAM,
                    to=[1],
                    topic="questions",
                    content="how tough is a Lamy Safari?",
                    timestamp=1595479019,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_draft(draft_id, draft=draft, request_options=request_options)
        return _response.data

    async def get_saved_snippets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSavedSnippetsResponse:
        """
        Fetch all the saved snippets for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSavedSnippetsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.get_saved_snippets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_saved_snippets(request_options=request_options)
        return _response.data

    async def create_saved_snippet(
        self, *, title: str, content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateSavedSnippetResponse:
        """
        Create a new saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        title : str
            The title of the saved snippet.

        content : str
            The content of the saved snippet in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSavedSnippetResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.create_saved_snippet(
                title="Example title",
                content="Welcome to the organization.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_saved_snippet(
            title=title, content=content, request_options=request_options
        )
        return _response.data

    async def delete_saved_snippet(
        self, saved_snippet_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete a saved snippet.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.delete_saved_snippet(
                saved_snippet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_saved_snippet(saved_snippet_id, request_options=request_options)
        return _response.data

    async def edit_saved_snippet(
        self,
        saved_snippet_id: int,
        *,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Edit a saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 368).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to edit.

        title : typing.Optional[str]
            The title of the saved snippet.

        content : typing.Optional[str]
            The content of the saved snippet in the original [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.drafts.edit_saved_snippet(
                saved_snippet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_saved_snippet(
            saved_snippet_id, title=title, content=content, request_options=request_options
        )
        return _response.data
