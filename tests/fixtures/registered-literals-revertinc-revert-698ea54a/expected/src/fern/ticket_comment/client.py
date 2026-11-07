

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ticket_create_or_update_comment_response import TicketCreateOrUpdateCommentResponse
from ..types.ticket_get_comment_response import TicketGetCommentResponse
from ..types.ticket_get_comments_response import TicketGetCommentsResponse
from .raw_client import AsyncRawTicketCommentClient, RawTicketCommentClient


OMIT = typing.cast(typing.Any, ...)


class TicketCommentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTicketCommentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTicketCommentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTicketCommentClient
        """
        return self._raw_client

    def ticket_comment_get_comment(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TicketGetCommentResponse:
        """
        Get details of a comment

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetCommentResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_comment.ticket_comment_get_comment(
            id="id",
        )
        """
        _response = self._raw_client.ticket_comment_get_comment(id, fields=fields, request_options=request_options)
        return _response.data

    def ticket_comment_update_comment(
        self,
        id: str,
        *,
        body: str,
        task_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateCommentResponse:
        """
        Update comment

        Parameters
        ----------
        id : str

        body : str
            The contents of the comment in plain text or HTML format.

        task_id : str
            Task or Issue to which comment must belong

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateCommentResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_comment.ticket_comment_update_comment(
            id="id",
            body="body",
            task_id="taskId",
        )
        """
        _response = self._raw_client.ticket_comment_update_comment(
            id, body=body, task_id=task_id, fields=fields, request_options=request_options
        )
        return _response.data

    def ticket_comment_get_comments(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetCommentsResponse:
        """
        Get all the comments

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetCommentsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_comment.ticket_comment_get_comments()
        """
        _response = self._raw_client.ticket_comment_get_comments(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def ticket_comment_create_comment(
        self,
        *,
        body: str,
        task_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateCommentResponse:
        """
        Post comment

        Parameters
        ----------
        body : str
            The contents of the comment in plain text or HTML format.

        task_id : str
            Task or Issue to which comment must belong

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateCommentResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_comment.ticket_comment_create_comment(
            body="body",
            task_id="taskId",
        )
        """
        _response = self._raw_client.ticket_comment_create_comment(
            body=body, task_id=task_id, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncTicketCommentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTicketCommentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTicketCommentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTicketCommentClient
        """
        return self._raw_client

    async def ticket_comment_get_comment(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TicketGetCommentResponse:
        """
        Get details of a comment

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetCommentResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_comment.ticket_comment_get_comment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_comment_get_comment(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def ticket_comment_update_comment(
        self,
        id: str,
        *,
        body: str,
        task_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateCommentResponse:
        """
        Update comment

        Parameters
        ----------
        id : str

        body : str
            The contents of the comment in plain text or HTML format.

        task_id : str
            Task or Issue to which comment must belong

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateCommentResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_comment.ticket_comment_update_comment(
                id="id",
                body="body",
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_comment_update_comment(
            id, body=body, task_id=task_id, fields=fields, request_options=request_options
        )
        return _response.data

    async def ticket_comment_get_comments(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetCommentsResponse:
        """
        Get all the comments

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetCommentsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_comment.ticket_comment_get_comments()


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_comment_get_comments(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def ticket_comment_create_comment(
        self,
        *,
        body: str,
        task_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateCommentResponse:
        """
        Post comment

        Parameters
        ----------
        body : str
            The contents of the comment in plain text or HTML format.

        task_id : str
            Task or Issue to which comment must belong

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateCommentResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_comment.ticket_comment_create_comment(
                body="body",
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_comment_create_comment(
            body=body, task_id=task_id, fields=fields, request_options=request_options
        )
        return _response.data
