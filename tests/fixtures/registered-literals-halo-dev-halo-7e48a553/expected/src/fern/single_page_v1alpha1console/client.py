

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.content_update_param import ContentUpdateParam
from ..types.content_wrapper import ContentWrapper
from ..types.listed_single_page_list import ListedSinglePageList
from ..types.listed_snapshot_dto import ListedSnapshotDto
from ..types.single_page import SinglePage
from .raw_client import AsyncRawSinglePageV1Alpha1ConsoleClient, RawSinglePageV1Alpha1ConsoleClient
from .types.list_single_pages_request_publish_phase import ListSinglePagesRequestPublishPhase
from .types.list_single_pages_request_visible import ListSinglePagesRequestVisible


OMIT = typing.cast(typing.Any, ...)


class SinglePageV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSinglePageV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSinglePageV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSinglePageV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_single_pages(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contributor: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListSinglePagesRequestPublishPhase] = None,
        visible: typing.Optional[ListSinglePagesRequestVisible] = None,
        keyword: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedSinglePageList:
        """
        List single pages with pagination, sorting, keyword, publish phase, visibility, and contributor filters.

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

        contributor : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Contributor user names used to filter single pages. A page matches when any listed contributor appears in status.contributors.

        publish_phase : typing.Optional[ListSinglePagesRequestPublishPhase]
            Filter single pages by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        visible : typing.Optional[ListSinglePagesRequestVisible]
            Filter single pages by visibility, such as PUBLIC, INTERNAL, or PRIVATE.

        keyword : typing.Optional[str]
            Keyword used to match single page title, slug, or excerpt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedSinglePageList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.list_single_pages()
        """
        _response = self._raw_client.list_single_pages(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            contributor=contributor,
            publish_phase=publish_phase,
            visible=visible,
            keyword=keyword,
            request_options=request_options,
        )
        return _response.data

    def draft_single_page(
        self, *, content: ContentUpdateParam, page: SinglePage, request_options: typing.Optional[RequestOptions] = None
    ) -> SinglePage:
        """
        Create a draft single page together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
            default response

        Examples
        --------
        from fern import (
            ContentUpdateParam,
            Excerpt,
            FernApi,
            Metadata,
            SinglePage,
            SinglePageSpec,
            SinglePageSpecVisible,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.draft_single_page(
            content=ContentUpdateParam(
                content="content",
                raw="raw",
                raw_type="rawType",
            ),
            page=SinglePage(
                api_version="apiVersion",
                kind="kind",
                metadata=Metadata(
                    name="name",
                ),
                spec=SinglePageSpec(
                    allow_comment=True,
                    deleted=True,
                    excerpt=Excerpt(
                        auto_generate=True,
                    ),
                    pinned=True,
                    priority=1,
                    publish=True,
                    slug="slug",
                    title="title",
                    visible=SinglePageSpecVisible.PUBLIC,
                ),
            ),
        )
        """
        _response = self._raw_client.draft_single_page(content=content, page=page, request_options=request_options)
        return _response.data

    def update_draft_single_page(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        page: SinglePage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SinglePage:
        """
        Update single page metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the single page to update.

        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
            default response

        Examples
        --------
        from fern import (
            ContentUpdateParam,
            Excerpt,
            FernApi,
            Metadata,
            SinglePage,
            SinglePageSpec,
            SinglePageSpecVisible,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.update_draft_single_page(
            name="name",
            content=ContentUpdateParam(
                content="content",
                raw="raw",
                raw_type="rawType",
            ),
            page=SinglePage(
                api_version="apiVersion",
                kind="kind",
                metadata=Metadata(
                    name="name",
                ),
                spec=SinglePageSpec(
                    allow_comment=True,
                    deleted=True,
                    excerpt=Excerpt(
                        auto_generate=True,
                    ),
                    pinned=True,
                    priority=1,
                    publish=True,
                    slug="slug",
                    title="title",
                    visible=SinglePageSpecVisible.PUBLIC,
                ),
            ),
        )
        """
        _response = self._raw_client.update_draft_single_page(
            name, content=content, page=page, request_options=request_options
        )
        return _response.data

    def fetch_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch a single page content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.fetch_single_page_content(
            name="name",
            snapshot_name="snapshotName",
        )
        """
        _response = self._raw_client.fetch_single_page_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    def update_single_page_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SinglePage:
        """
        Update only the content of an existing single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be updated.

        content : str
            Rendered HTML or normalized content derived from raw.

        raw : str
            Source text stored by the editor.

        raw_type : str
            Editor/source format of the raw content, for example HTML or Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.update_single_page_content(
            name="name",
            content="content",
            raw="raw",
            raw_type="rawType",
        )
        """
        _response = self._raw_client.update_single_page_content(
            name, content=content, raw=raw, raw_type=raw_type, request_options=request_options
        )
        return _response.data

    def delete_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Delete a content snapshot from a single page and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.delete_single_page_content(
            name="name",
            snapshot_name="snapshotName",
        )
        """
        _response = self._raw_client.delete_single_page_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    def fetch_single_page_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the editable head content of a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.fetch_single_page_head_content(
            name="name",
        )
        """
        _response = self._raw_client.fetch_single_page_head_content(name, request_options=request_options)
        return _response.data

    def publish_single_page(
        self,
        name: str,
        *,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SinglePage:
        """
        Publish a single page. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the single page to publish.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the single page for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.publish_single_page(
            name="name",
        )
        """
        _response = self._raw_client.publish_single_page(name, async_=async_, request_options=request_options)
        return _response.data

    def fetch_single_page_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the released content currently served for a published single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.fetch_single_page_release_content(
            name="name",
        )
        """
        _response = self._raw_client.fetch_single_page_release_content(name, request_options=request_options)
        return _response.data

    def revert_to_specified_snapshot_for_single_page(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SinglePage:
        """
        Restore the single page content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the single page's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.revert_to_specified_snapshot_for_single_page(
            name="name",
            snapshot_name="snapshotName",
        )
        """
        _response = self._raw_client.revert_to_specified_snapshot_for_single_page(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    def list_single_page_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListedSnapshotDto]:
        """
        List content snapshots for a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListedSnapshotDto]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.single_page_v1alpha1console.list_single_page_snapshots(
            name="name",
        )
        """
        _response = self._raw_client.list_single_page_snapshots(name, request_options=request_options)
        return _response.data


class AsyncSinglePageV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSinglePageV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSinglePageV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSinglePageV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_single_pages(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contributor: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListSinglePagesRequestPublishPhase] = None,
        visible: typing.Optional[ListSinglePagesRequestVisible] = None,
        keyword: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedSinglePageList:
        """
        List single pages with pagination, sorting, keyword, publish phase, visibility, and contributor filters.

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

        contributor : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Contributor user names used to filter single pages. A page matches when any listed contributor appears in status.contributors.

        publish_phase : typing.Optional[ListSinglePagesRequestPublishPhase]
            Filter single pages by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        visible : typing.Optional[ListSinglePagesRequestVisible]
            Filter single pages by visibility, such as PUBLIC, INTERNAL, or PRIVATE.

        keyword : typing.Optional[str]
            Keyword used to match single page title, slug, or excerpt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedSinglePageList
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
            await client.single_page_v1alpha1console.list_single_pages()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_single_pages(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            contributor=contributor,
            publish_phase=publish_phase,
            visible=visible,
            keyword=keyword,
            request_options=request_options,
        )
        return _response.data

    async def draft_single_page(
        self, *, content: ContentUpdateParam, page: SinglePage, request_options: typing.Optional[RequestOptions] = None
    ) -> SinglePage:
        """
        Create a draft single page together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
            default response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ContentUpdateParam,
            Excerpt,
            Metadata,
            SinglePage,
            SinglePageSpec,
            SinglePageSpecVisible,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.single_page_v1alpha1console.draft_single_page(
                content=ContentUpdateParam(
                    content="content",
                    raw="raw",
                    raw_type="rawType",
                ),
                page=SinglePage(
                    api_version="apiVersion",
                    kind="kind",
                    metadata=Metadata(
                        name="name",
                    ),
                    spec=SinglePageSpec(
                        allow_comment=True,
                        deleted=True,
                        excerpt=Excerpt(
                            auto_generate=True,
                        ),
                        pinned=True,
                        priority=1,
                        publish=True,
                        slug="slug",
                        title="title",
                        visible=SinglePageSpecVisible.PUBLIC,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_single_page(
            content=content, page=page, request_options=request_options
        )
        return _response.data

    async def update_draft_single_page(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        page: SinglePage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SinglePage:
        """
        Update single page metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the single page to update.

        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
            default response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ContentUpdateParam,
            Excerpt,
            Metadata,
            SinglePage,
            SinglePageSpec,
            SinglePageSpecVisible,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.single_page_v1alpha1console.update_draft_single_page(
                name="name",
                content=ContentUpdateParam(
                    content="content",
                    raw="raw",
                    raw_type="rawType",
                ),
                page=SinglePage(
                    api_version="apiVersion",
                    kind="kind",
                    metadata=Metadata(
                        name="name",
                    ),
                    spec=SinglePageSpec(
                        allow_comment=True,
                        deleted=True,
                        excerpt=Excerpt(
                            auto_generate=True,
                        ),
                        pinned=True,
                        priority=1,
                        publish=True,
                        slug="slug",
                        title="title",
                        visible=SinglePageSpecVisible.PUBLIC,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_draft_single_page(
            name, content=content, page=page, request_options=request_options
        )
        return _response.data

    async def fetch_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch a single page content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
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
            await client.single_page_v1alpha1console.fetch_single_page_content(
                name="name",
                snapshot_name="snapshotName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_single_page_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    async def update_single_page_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SinglePage:
        """
        Update only the content of an existing single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be updated.

        content : str
            Rendered HTML or normalized content derived from raw.

        raw : str
            Source text stored by the editor.

        raw_type : str
            Editor/source format of the raw content, for example HTML or Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
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
            await client.single_page_v1alpha1console.update_single_page_content(
                name="name",
                content="content",
                raw="raw",
                raw_type="rawType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_single_page_content(
            name, content=content, raw=raw, raw_type=raw_type, request_options=request_options
        )
        return _response.data

    async def delete_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Delete a content snapshot from a single page and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
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
            await client.single_page_v1alpha1console.delete_single_page_content(
                name="name",
                snapshot_name="snapshotName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_single_page_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    async def fetch_single_page_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the editable head content of a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
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
            await client.single_page_v1alpha1console.fetch_single_page_head_content(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_single_page_head_content(name, request_options=request_options)
        return _response.data

    async def publish_single_page(
        self,
        name: str,
        *,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SinglePage:
        """
        Publish a single page. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the single page to publish.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the single page for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
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
            await client.single_page_v1alpha1console.publish_single_page(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_single_page(name, async_=async_, request_options=request_options)
        return _response.data

    async def fetch_single_page_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the released content currently served for a published single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentWrapper
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
            await client.single_page_v1alpha1console.fetch_single_page_release_content(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_single_page_release_content(name, request_options=request_options)
        return _response.data

    async def revert_to_specified_snapshot_for_single_page(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SinglePage:
        """
        Restore the single page content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the single page's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SinglePage
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
            await client.single_page_v1alpha1console.revert_to_specified_snapshot_for_single_page(
                name="name",
                snapshot_name="snapshotName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revert_to_specified_snapshot_for_single_page(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    async def list_single_page_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListedSnapshotDto]:
        """
        List content snapshots for a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListedSnapshotDto]
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
            await client.single_page_v1alpha1console.list_single_page_snapshots(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_single_page_snapshots(name, request_options=request_options)
        return _response.data
