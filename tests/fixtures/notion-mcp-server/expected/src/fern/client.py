

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.block_object_request import BlockObjectRequest
from .types.create_a_comment_request_parent import CreateACommentRequestParent
from .types.create_a_comment_request_rich_text_item import CreateACommentRequestRichTextItem
from .types.get_self_response import GetSelfResponse
from .types.parent_request import ParentRequest
from .types.patch_page_request_cover import PatchPageRequestCover
from .types.patch_page_request_icon import PatchPageRequestIcon
from .types.post_search_request_filter import PostSearchRequestFilter
from .types.post_search_request_sort import PostSearchRequestSort
from .types.update_a_block_request_type import UpdateABlockRequestType

if typing.TYPE_CHECKING:
    from .data_sources.client import AsyncDataSourcesClient, DataSourcesClient
    from .databases.client import AsyncDatabasesClient, DatabasesClient
    from .pages.client import AsyncPagesClient, PagesClient

OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    notion_version : typing.Optional[typing.Literal["2025-09-03"]]
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        notion_version="YOUR_NOTION_VERSION",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        notion_version: typing.Optional[typing.Literal["2025-09-03"]] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            notion_version=notion_version,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._data_sources: typing.Optional[DataSourcesClient] = None
        self._databases: typing.Optional[DatabasesClient] = None
        self._pages: typing.Optional[PagesClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """


        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.get_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    def get_users(
        self,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        start_cursor : typing.Optional[str]
            If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

        page_size : typing.Optional[int]
            The number of items from the full list desired in the response. Maximum: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.get_users()
        """
        _response = self._raw_client.get_users(
            start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_self(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSelfResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSelfResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.get_self()
        """
        _response = self._raw_client.get_self(request_options=request_options)
        return _response.data

    def post_search(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        sort: typing.Optional[PostSearchRequestSort] = OMIT,
        filter: typing.Optional[PostSearchRequestFilter] = OMIT,
        start_cursor: typing.Optional[str] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        query : typing.Optional[str]
            The text that the API compares page and database titles against.

        sort : typing.Optional[PostSearchRequestSort]
            A set of criteria, `direction` and `timestamp` keys, that orders the results. The **only** supported timestamp value is `"last_edited_time"`. Supported `direction` values are `"ascending"` and `"descending"`. If `sort` is not provided, then the most recently edited results are returned first.

        filter : typing.Optional[PostSearchRequestFilter]
            A set of criteria, `value` and `property` keys, that limits the results to either only pages or only data sources. Possible `value` values are `"page"` or `"data_source"`. The only supported `property` value is `"object"`.

        start_cursor : typing.Optional[str]
            A `cursor` value returned in a previous response that If supplied, limits the response to results starting after the `cursor`. If not supplied, then the first page of results is returned. Refer to [pagination](https://developers.notion.com/reference/intro#pagination) for more details.

        page_size : typing.Optional[int]
            The number of items from the full list to include in the response. Maximum: `100`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.post_search()
        """
        _response = self._raw_client.post_search(
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def get_block_children(
        self,
        block_id: str,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a [block](ref:block)

        start_cursor : typing.Optional[str]
            If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

        page_size : typing.Optional[int]
            The number of items from the full list desired in the response. Maximum: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.get_block_children(
            block_id="block_id",
        )
        """
        _response = self._raw_client.get_block_children(
            block_id, start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    def patch_block_children(
        self,
        block_id: str,
        *,
        children: typing.Sequence[BlockObjectRequest],
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a [block](ref:block). Also accepts a [page](ref:page) ID.

        children : typing.Sequence[BlockObjectRequest]
            Child content to append to a container block as an array of [block objects](ref:block)

        after : typing.Optional[str]
            The ID of the existing block that the new block should be appended after.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import BlockObjectRequest_Paragraph, FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.patch_block_children(
            block_id="block_id",
            children=[BlockObjectRequest_Paragraph()],
        )
        """
        _response = self._raw_client.patch_block_children(
            block_id, children=children, after=after, request_options=request_options
        )
        return _response.data

    def retrieve_a_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a Notion block

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.retrieve_a_block(
            block_id="block_id",
        )
        """
        _response = self._raw_client.retrieve_a_block(block_id, request_options=request_options)
        return _response.data

    def delete_a_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a Notion block

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.delete_a_block(
            block_id="block_id",
        )
        """
        _response = self._raw_client.delete_a_block(block_id, request_options=request_options)
        return _response.data

    def update_a_block(
        self,
        block_id: str,
        *,
        type: typing.Optional[UpdateABlockRequestType] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a Notion block

        type : typing.Optional[UpdateABlockRequestType]
            The [block object `type`](ref:block#block-object-keys) value with the properties to be updated. Currently only `text` (for supported block types) and `checked` (for `to_do` blocks) fields can be updated.

        archived : typing.Optional[bool]
            Set to true to archive (delete) a block. Set to false to un-archive (restore) a block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.update_a_block(
            block_id="block_id",
        )
        """
        _response = self._raw_client.update_a_block(
            block_id, type=type, archived=archived, request_options=request_options
        )
        return _response.data

    def retrieve_a_page(
        self,
        page_id: str,
        *,
        filter_properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        filter_properties : typing.Optional[str]
            A list of page property value IDs associated with the page. Use this param to limit the response to a specific page property value or values. To retrieve multiple properties, specify each page property ID. For example: `?filter_properties=iAk8&filter_properties=b7dh`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.retrieve_a_page(
            page_id="page_id",
        )
        """
        _response = self._raw_client.retrieve_a_page(
            page_id, filter_properties=filter_properties, request_options=request_options
        )
        return _response.data

    def patch_page(
        self,
        page_id: str,
        *,
        properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        in_trash: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        icon: typing.Optional[PatchPageRequestIcon] = OMIT,
        cover: typing.Optional[PatchPageRequestCover] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        page_id : str
            The identifier for the Notion page to be updated.

        properties : typing.Optional[typing.Dict[str, typing.Any]]
            The property values to update for the page. The keys are the names or IDs of the property and the values are property values. If a page property ID is not included, then it is not changed.

        in_trash : typing.Optional[bool]
            Set to true to delete a block. Set to false to restore a block.

        archived : typing.Optional[bool]

        icon : typing.Optional[PatchPageRequestIcon]
            A page icon for the page. Supported types are [external file object](https://developers.notion.com/reference/file-object) or [emoji object](https://developers.notion.com/reference/emoji-object).

        cover : typing.Optional[PatchPageRequestCover]
            A cover image for the page. Only [external file objects](https://developers.notion.com/reference/file-object) are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.patch_page(
            page_id="page_id",
        )
        """
        _response = self._raw_client.patch_page(
            page_id,
            properties=properties,
            in_trash=in_trash,
            archived=archived,
            icon=icon,
            cover=cover,
            request_options=request_options,
        )
        return _response.data

    def post_page(
        self,
        *,
        parent: ParentRequest,
        properties: typing.Dict[str, typing.Any],
        children: typing.Optional[typing.Sequence[str]] = OMIT,
        icon: typing.Optional[str] = OMIT,
        cover: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        parent : ParentRequest

        properties : typing.Dict[str, typing.Any]
            The property values for the new page. The keys are the names or IDs of the property and the values are property values.

        children : typing.Optional[typing.Sequence[str]]
            The content to be rendered on the new page, represented as an array of [block objects](https://developers.notion.com/reference/block).

        icon : typing.Optional[str]
            The icon of the new page. Either an [emoji object](https://developers.notion.com/reference/emoji-object) or an [external file object](https://developers.notion.com/reference/file-object)..

        cover : typing.Optional[str]
            The cover image of the new page, represented as a [file object](https://developers.notion.com/reference/file-object).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi, PageIdParentRequest

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.post_page(
            parent=PageIdParentRequest(
                page_id="page_id",
            ),
            properties={"key": "value"},
        )
        """
        _response = self._raw_client.post_page(
            parent=parent,
            properties=properties,
            children=children,
            icon=icon,
            cover=cover,
            request_options=request_options,
        )
        return _response.data

    def retrieve_a_page_property(
        self,
        page_id: str,
        property_id: str,
        *,
        page_size: typing.Optional[int] = None,
        start_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """


        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        property_id : str
            Identifier for a page [property](https://developers.notion.com/reference/page#all-property-values)

        page_size : typing.Optional[int]
            For paginated properties. The max number of property item objects on a page. The default size is 100

        start_cursor : typing.Optional[str]
            For paginated properties.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.retrieve_a_page_property(
            page_id="page_id",
            property_id="property_id",
        )
        """
        _response = self._raw_client.retrieve_a_page_property(
            page_id, property_id, page_size=page_size, start_cursor=start_cursor, request_options=request_options
        )
        return _response.data

    def retrieve_a_comment(
        self,
        *,
        block_id: str,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Retrieves a list of un-resolved [Comment objects](ref:comment-object) from a page or block.

        Parameters
        ----------
        block_id : str
            Identifier for a Notion block or page

        start_cursor : typing.Optional[str]
            If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

        page_size : typing.Optional[int]
            The number of items from the full list desired in the response. Maximum: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.retrieve_a_comment(
            block_id="block_id",
        )
        """
        _response = self._raw_client.retrieve_a_comment(
            block_id=block_id, start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_a_comment(
        self,
        *,
        parent: CreateACommentRequestParent,
        rich_text: typing.Sequence[CreateACommentRequestRichTextItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Creates a comment in a page or existing discussion thread.

        Parameters
        ----------
        parent : CreateACommentRequestParent
            The page that contains the comment

        rich_text : typing.Sequence[CreateACommentRequestRichTextItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        from fern import (
            CreateACommentRequestParent,
            CreateACommentRequestRichTextItem,
            CreateACommentRequestRichTextItemText,
            FernApi,
        )

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.create_a_comment(
            parent=CreateACommentRequestParent(
                page_id="page_id",
            ),
            rich_text=[
                CreateACommentRequestRichTextItem(
                    text=CreateACommentRequestRichTextItemText(
                        content="content",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.create_a_comment(
            parent=parent, rich_text=rich_text, request_options=request_options
        )
        return _response.data

    @property
    def data_sources(self):
        if self._data_sources is None:
            from .data_sources.client import DataSourcesClient

            self._data_sources = DataSourcesClient(client_wrapper=self._client_wrapper)
        return self._data_sources

    @property
    def databases(self):
        if self._databases is None:
            from .databases.client import DatabasesClient

            self._databases = DatabasesClient(client_wrapper=self._client_wrapper)
        return self._databases

    @property
    def pages(self):
        if self._pages is None:
            from .pages.client import PagesClient

            self._pages = PagesClient(client_wrapper=self._client_wrapper)
        return self._pages


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    notion_version : typing.Optional[typing.Literal["2025-09-03"]]
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        notion_version="YOUR_NOTION_VERSION",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        notion_version: typing.Optional[typing.Literal["2025-09-03"]] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            notion_version=notion_version,
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._data_sources: typing.Optional[AsyncDataSourcesClient] = None
        self._databases: typing.Optional[AsyncDatabasesClient] = None
        self._pages: typing.Optional[AsyncPagesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """


        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    async def get_users(
        self,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        start_cursor : typing.Optional[str]
            If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

        page_size : typing.Optional[int]
            The number of items from the full list desired in the response. Maximum: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_self(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSelfResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSelfResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_self()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_self(request_options=request_options)
        return _response.data

    async def post_search(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        sort: typing.Optional[PostSearchRequestSort] = OMIT,
        filter: typing.Optional[PostSearchRequestFilter] = OMIT,
        start_cursor: typing.Optional[str] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        query : typing.Optional[str]
            The text that the API compares page and database titles against.

        sort : typing.Optional[PostSearchRequestSort]
            A set of criteria, `direction` and `timestamp` keys, that orders the results. The **only** supported timestamp value is `"last_edited_time"`. Supported `direction` values are `"ascending"` and `"descending"`. If `sort` is not provided, then the most recently edited results are returned first.

        filter : typing.Optional[PostSearchRequestFilter]
            A set of criteria, `value` and `property` keys, that limits the results to either only pages or only data sources. Possible `value` values are `"page"` or `"data_source"`. The only supported `property` value is `"object"`.

        start_cursor : typing.Optional[str]
            A `cursor` value returned in a previous response that If supplied, limits the response to results starting after the `cursor`. If not supplied, then the first page of results is returned. Refer to [pagination](https://developers.notion.com/reference/intro#pagination) for more details.

        page_size : typing.Optional[int]
            The number of items from the full list to include in the response. Maximum: `100`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.post_search()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_search(
            query=query,
            sort=sort,
            filter=filter,
            start_cursor=start_cursor,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def get_block_children(
        self,
        block_id: str,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a [block](ref:block)

        start_cursor : typing.Optional[str]
            If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

        page_size : typing.Optional[int]
            The number of items from the full list desired in the response. Maximum: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.get_block_children(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_block_children(
            block_id, start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def patch_block_children(
        self,
        block_id: str,
        *,
        children: typing.Sequence[BlockObjectRequest],
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a [block](ref:block). Also accepts a [page](ref:page) ID.

        children : typing.Sequence[BlockObjectRequest]
            Child content to append to a container block as an array of [block objects](ref:block)

        after : typing.Optional[str]
            The ID of the existing block that the new block should be appended after.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BlockObjectRequest_Paragraph

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_block_children(
                block_id="block_id",
                children=[BlockObjectRequest_Paragraph()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_block_children(
            block_id, children=children, after=after, request_options=request_options
        )
        return _response.data

    async def retrieve_a_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a Notion block

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.retrieve_a_block(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_block(block_id, request_options=request_options)
        return _response.data

    async def delete_a_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a Notion block

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.delete_a_block(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_block(block_id, request_options=request_options)
        return _response.data

    async def update_a_block(
        self,
        block_id: str,
        *,
        type: typing.Optional[UpdateABlockRequestType] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        block_id : str
            Identifier for a Notion block

        type : typing.Optional[UpdateABlockRequestType]
            The [block object `type`](ref:block#block-object-keys) value with the properties to be updated. Currently only `text` (for supported block types) and `checked` (for `to_do` blocks) fields can be updated.

        archived : typing.Optional[bool]
            Set to true to archive (delete) a block. Set to false to un-archive (restore) a block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.update_a_block(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_block(
            block_id, type=type, archived=archived, request_options=request_options
        )
        return _response.data

    async def retrieve_a_page(
        self,
        page_id: str,
        *,
        filter_properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        filter_properties : typing.Optional[str]
            A list of page property value IDs associated with the page. Use this param to limit the response to a specific page property value or values. To retrieve multiple properties, specify each page property ID. For example: `?filter_properties=iAk8&filter_properties=b7dh`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.retrieve_a_page(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_page(
            page_id, filter_properties=filter_properties, request_options=request_options
        )
        return _response.data

    async def patch_page(
        self,
        page_id: str,
        *,
        properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        in_trash: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        icon: typing.Optional[PatchPageRequestIcon] = OMIT,
        cover: typing.Optional[PatchPageRequestCover] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        page_id : str
            The identifier for the Notion page to be updated.

        properties : typing.Optional[typing.Dict[str, typing.Any]]
            The property values to update for the page. The keys are the names or IDs of the property and the values are property values. If a page property ID is not included, then it is not changed.

        in_trash : typing.Optional[bool]
            Set to true to delete a block. Set to false to restore a block.

        archived : typing.Optional[bool]

        icon : typing.Optional[PatchPageRequestIcon]
            A page icon for the page. Supported types are [external file object](https://developers.notion.com/reference/file-object) or [emoji object](https://developers.notion.com/reference/emoji-object).

        cover : typing.Optional[PatchPageRequestCover]
            A cover image for the page. Only [external file objects](https://developers.notion.com/reference/file-object) are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.patch_page(
                page_id="page_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_page(
            page_id,
            properties=properties,
            in_trash=in_trash,
            archived=archived,
            icon=icon,
            cover=cover,
            request_options=request_options,
        )
        return _response.data

    async def post_page(
        self,
        *,
        parent: ParentRequest,
        properties: typing.Dict[str, typing.Any],
        children: typing.Optional[typing.Sequence[str]] = OMIT,
        icon: typing.Optional[str] = OMIT,
        cover: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """


        Parameters
        ----------
        parent : ParentRequest

        properties : typing.Dict[str, typing.Any]
            The property values for the new page. The keys are the names or IDs of the property and the values are property values.

        children : typing.Optional[typing.Sequence[str]]
            The content to be rendered on the new page, represented as an array of [block objects](https://developers.notion.com/reference/block).

        icon : typing.Optional[str]
            The icon of the new page. Either an [emoji object](https://developers.notion.com/reference/emoji-object) or an [external file object](https://developers.notion.com/reference/file-object)..

        cover : typing.Optional[str]
            The cover image of the new page, represented as a [file object](https://developers.notion.com/reference/file-object).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PageIdParentRequest

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_page(
                parent=PageIdParentRequest(
                    page_id="page_id",
                ),
                properties={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_page(
            parent=parent,
            properties=properties,
            children=children,
            icon=icon,
            cover=cover,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_a_page_property(
        self,
        page_id: str,
        property_id: str,
        *,
        page_size: typing.Optional[int] = None,
        start_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """


        Parameters
        ----------
        page_id : str
            Identifier for a Notion page

        property_id : str
            Identifier for a page [property](https://developers.notion.com/reference/page#all-property-values)

        page_size : typing.Optional[int]
            For paginated properties. The max number of property item objects on a page. The default size is 100

        start_cursor : typing.Optional[str]
            For paginated properties.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.retrieve_a_page_property(
                page_id="page_id",
                property_id="property_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_page_property(
            page_id, property_id, page_size=page_size, start_cursor=start_cursor, request_options=request_options
        )
        return _response.data

    async def retrieve_a_comment(
        self,
        *,
        block_id: str,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Retrieves a list of un-resolved [Comment objects](ref:comment-object) from a page or block.

        Parameters
        ----------
        block_id : str
            Identifier for a Notion block or page

        start_cursor : typing.Optional[str]
            If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

        page_size : typing.Optional[int]
            The number of items from the full list desired in the response. Maximum: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.retrieve_a_comment(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_comment(
            block_id=block_id, start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_a_comment(
        self,
        *,
        parent: CreateACommentRequestParent,
        rich_text: typing.Sequence[CreateACommentRequestRichTextItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Creates a comment in a page or existing discussion thread.

        Parameters
        ----------
        parent : CreateACommentRequestParent
            The page that contains the comment

        rich_text : typing.Sequence[CreateACommentRequestRichTextItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            200

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CreateACommentRequestParent,
            CreateACommentRequestRichTextItem,
            CreateACommentRequestRichTextItemText,
        )

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_a_comment(
                parent=CreateACommentRequestParent(
                    page_id="page_id",
                ),
                rich_text=[
                    CreateACommentRequestRichTextItem(
                        text=CreateACommentRequestRichTextItemText(
                            content="content",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_comment(
            parent=parent, rich_text=rich_text, request_options=request_options
        )
        return _response.data

    @property
    def data_sources(self):
        if self._data_sources is None:
            from .data_sources.client import AsyncDataSourcesClient

            self._data_sources = AsyncDataSourcesClient(client_wrapper=self._client_wrapper)
        return self._data_sources

    @property
    def databases(self):
        if self._databases is None:
            from .databases.client import AsyncDatabasesClient

            self._databases = AsyncDatabasesClient(client_wrapper=self._client_wrapper)
        return self._databases

    @property
    def pages(self):
        if self._pages is None:
            from .pages.client import AsyncPagesClient

            self._pages = AsyncPagesClient(client_wrapper=self._client_wrapper)
        return self._pages


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
