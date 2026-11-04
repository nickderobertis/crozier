

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.comment import Comment
from ..types.comment_email_owner import CommentEmailOwner
from ..types.listed_comment_list import ListedCommentList
from ..types.ref import Ref
from ..types.reply import Reply
from .raw_client import AsyncRawCommentV1Alpha1ConsoleClient, RawCommentV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class CommentV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCommentV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCommentV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCommentV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_comments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        approved: typing.Optional[str] = None,
        owner_kind: typing.Optional[str] = None,
        owner_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedCommentList:
        """
        List comments with pagination, sorting, keyword, and commenter filters.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword used to match the raw comment text.

        approved : typing.Optional[str]
            Approval state filter. When false, comments with pending replies are also included.

        owner_kind : typing.Optional[str]
            Kind of the commenter identity. Defaults to User when ownerName is provided.

        owner_name : typing.Optional[str]
            Name of the commenter identity to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedCommentList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.comment_v1alpha1console.list_comments()
        """
        _response = self._raw_client.list_comments(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            keyword=keyword,
            approved=approved,
            owner_kind=owner_kind,
            owner_name=owner_name,
            request_options=request_options,
        )
        return _response.data

    def create_comment(
        self,
        *,
        content: str,
        raw: str,
        subject_ref: Ref,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Comment:
        """
        Create a comment for a subject. Console-created comments are created through the comment service with request IP and user agent captured.

        Parameters
        ----------
        content : str
            Rendered HTML content for the comment. Unsafe HTML is rejected.

        raw : str
            Original comment text submitted by the editor.

        subject_ref : Ref

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the comment should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Comment
            default response

        Examples
        --------
        from fern import FernApi, Ref

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.comment_v1alpha1console.create_comment(
            content="content",
            raw="raw",
            subject_ref=Ref(
                group="group",
                kind="kind",
                name="name",
            ),
        )
        """
        _response = self._raw_client.create_comment(
            content=content,
            raw=raw,
            subject_ref=subject_ref,
            allow_notification=allow_notification,
            hidden=hidden,
            owner=owner,
            request_options=request_options,
        )
        return _response.data

    def update_comment_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Comment:
        """
        Update only the body of an existing comment. Requires its current version.

        Parameters
        ----------
        name : str

        content : str

        raw : str

        version : int
            Resource version when the editor was opened.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Comment
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.comment_v1alpha1console.update_comment_content(
            name="name",
            content="content",
            raw="raw",
            version=1000000,
        )
        """
        _response = self._raw_client.update_comment_content(
            name, content=content, raw=raw, version=version, request_options=request_options
        )
        return _response.data

    def create_reply(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        quote_reply: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reply:
        """
        Create an approved reply under an existing comment.

        Parameters
        ----------
        name : str
            metadata.name of the comment to reply to.

        content : str
            Rendered HTML content for the reply. Unsafe HTML is rejected.

        raw : str
            Original reply text submitted by the editor.

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the reply should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        quote_reply : typing.Optional[str]
            Metadata name of the reply being quoted, if this reply quotes another reply.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reply
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.comment_v1alpha1console.create_reply(
            name="name",
            content="content",
            raw="raw",
        )
        """
        _response = self._raw_client.create_reply(
            name,
            content=content,
            raw=raw,
            allow_notification=allow_notification,
            hidden=hidden,
            owner=owner,
            quote_reply=quote_reply,
            request_options=request_options,
        )
        return _response.data


class AsyncCommentV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCommentV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCommentV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCommentV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_comments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        approved: typing.Optional[str] = None,
        owner_kind: typing.Optional[str] = None,
        owner_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedCommentList:
        """
        List comments with pagination, sorting, keyword, and commenter filters.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword used to match the raw comment text.

        approved : typing.Optional[str]
            Approval state filter. When false, comments with pending replies are also included.

        owner_kind : typing.Optional[str]
            Kind of the commenter identity. Defaults to User when ownerName is provided.

        owner_name : typing.Optional[str]
            Name of the commenter identity to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedCommentList
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.comment_v1alpha1console.list_comments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_comments(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            keyword=keyword,
            approved=approved,
            owner_kind=owner_kind,
            owner_name=owner_name,
            request_options=request_options,
        )
        return _response.data

    async def create_comment(
        self,
        *,
        content: str,
        raw: str,
        subject_ref: Ref,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Comment:
        """
        Create a comment for a subject. Console-created comments are created through the comment service with request IP and user agent captured.

        Parameters
        ----------
        content : str
            Rendered HTML content for the comment. Unsafe HTML is rejected.

        raw : str
            Original comment text submitted by the editor.

        subject_ref : Ref

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the comment should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Comment
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Ref

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.comment_v1alpha1console.create_comment(
                content="content",
                raw="raw",
                subject_ref=Ref(
                    group="group",
                    kind="kind",
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_comment(
            content=content,
            raw=raw,
            subject_ref=subject_ref,
            allow_notification=allow_notification,
            hidden=hidden,
            owner=owner,
            request_options=request_options,
        )
        return _response.data

    async def update_comment_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Comment:
        """
        Update only the body of an existing comment. Requires its current version.

        Parameters
        ----------
        name : str

        content : str

        raw : str

        version : int
            Resource version when the editor was opened.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Comment
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.comment_v1alpha1console.update_comment_content(
                name="name",
                content="content",
                raw="raw",
                version=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_comment_content(
            name, content=content, raw=raw, version=version, request_options=request_options
        )
        return _response.data

    async def create_reply(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        allow_notification: typing.Optional[bool] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        owner: typing.Optional[CommentEmailOwner] = OMIT,
        quote_reply: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reply:
        """
        Create an approved reply under an existing comment.

        Parameters
        ----------
        name : str
            metadata.name of the comment to reply to.

        content : str
            Rendered HTML content for the reply. Unsafe HTML is rejected.

        raw : str
            Original reply text submitted by the editor.

        allow_notification : typing.Optional[bool]
            Whether to notify the owner of future replies. Only an explicit false disables notifications.

        hidden : typing.Optional[bool]
            Whether the reply should be hidden from normal display.

        owner : typing.Optional[CommentEmailOwner]

        quote_reply : typing.Optional[str]
            Metadata name of the reply being quoted, if this reply quotes another reply.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reply
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.comment_v1alpha1console.create_reply(
                name="name",
                content="content",
                raw="raw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_reply(
            name,
            content=content,
            raw=raw,
            allow_notification=allow_notification,
            hidden=hidden,
            owner=owner,
            quote_reply=quote_reply,
            request_options=request_options,
        )
        return _response.data
