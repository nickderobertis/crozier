

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.listed_reply_list import ListedReplyList
from ..types.reply import Reply
from .raw_client import AsyncRawReplyV1Alpha1ConsoleClient, RawReplyV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class ReplyV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReplyV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReplyV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReplyV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_replies(
        self,
        *,
        comment_name: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedReplyList:
        """
        List replies for a comment with pagination, sorting, labels, and field selectors.

        Parameters
        ----------
        comment_name : str
            Metadata name of the comment whose replies should be listed.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedReplyList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reply_v1alpha1console.list_replies(
            comment_name="commentName",
        )
        """
        _response = self._raw_client.list_replies(
            comment_name=comment_name,
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    def update_reply_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reply:
        """
        Update only the body of an existing reply. Requires its current version.

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
        Reply
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reply_v1alpha1console.update_reply_content(
            name="name",
            content="content",
            raw="raw",
            version=1000000,
        )
        """
        _response = self._raw_client.update_reply_content(
            name, content=content, raw=raw, version=version, request_options=request_options
        )
        return _response.data


class AsyncReplyV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReplyV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReplyV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReplyV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_replies(
        self,
        *,
        comment_name: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedReplyList:
        """
        List replies for a comment with pagination, sorting, labels, and field selectors.

        Parameters
        ----------
        comment_name : str
            Metadata name of the comment whose replies should be listed.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedReplyList
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
            await client.reply_v1alpha1console.list_replies(
                comment_name="commentName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_replies(
            comment_name=comment_name,
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    async def update_reply_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reply:
        """
        Update only the body of an existing reply. Requires its current version.

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
            await client.reply_v1alpha1console.update_reply_content(
                name="name",
                content="content",
                raw="raw",
                version=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_reply_content(
            name, content=content, raw=raw, version=version, request_options=request_options
        )
        return _response.data
