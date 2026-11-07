

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.content_update_param import ContentUpdateParam
from ..types.content_wrapper import ContentWrapper
from ..types.listed_post_list import ListedPostList
from ..types.listed_snapshot_dto import ListedSnapshotDto
from ..types.post import Post
from .raw_client import AsyncRawPostV1Alpha1ConsoleClient, RawPostV1Alpha1ConsoleClient
from .types.list_posts_request_publish_phase import ListPostsRequestPublishPhase


OMIT = typing.cast(typing.Any, ...)


class PostV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPostV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPostV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPostV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedPostList:
        """
        List posts with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListPostsRequestPublishPhase]
            Filter posts by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        keyword : typing.Optional[str]
            Keyword used to match post title, slug, or excerpt.

        category_with_children : typing.Optional[str]
            Category metadata name used to include posts in that category and its child categories.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedPostList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.list_posts()
        """
        _response = self._raw_client.list_posts(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            publish_phase=publish_phase,
            keyword=keyword,
            category_with_children=category_with_children,
            request_options=request_options,
        )
        return _response.data

    def draft_post(
        self, *, content: ContentUpdateParam, post: Post, request_options: typing.Optional[RequestOptions] = None
    ) -> Post:
        """
        Create a draft post together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import ContentUpdateParam, Excerpt, FernApi, Metadata, Post, PostSpec

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.draft_post(
            content=ContentUpdateParam(
                content="content",
                raw="raw",
                raw_type="rawType",
            ),
            post=Post(
                api_version="apiVersion",
                kind="kind",
                metadata=Metadata(
                    name="name",
                ),
                spec=PostSpec(
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
                    visible="PUBLIC",
                ),
            ),
        )
        """
        _response = self._raw_client.draft_post(content=content, post=post, request_options=request_options)
        return _response.data

    def update_draft_post(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        post: Post,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Update post metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the post to update.

        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import ContentUpdateParam, Excerpt, FernApi, Metadata, Post, PostSpec

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.update_draft_post(
            name="name",
            content=ContentUpdateParam(
                content="content",
                raw="raw",
                raw_type="rawType",
            ),
            post=Post(
                api_version="apiVersion",
                kind="kind",
                metadata=Metadata(
                    name="name",
                ),
                spec=PostSpec(
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
                    visible="PUBLIC",
                ),
            ),
        )
        """
        _response = self._raw_client.update_draft_post(
            name, content=content, post=post, request_options=request_options
        )
        return _response.data

    def fetch_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch a post content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
        client.post_v1alpha1console.fetch_post_content(
            name="name",
            snapshot_name="snapshotName",
        )
        """
        _response = self._raw_client.fetch_post_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    def update_post_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Update only the content of an existing post.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be updated.

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
        Post
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.update_post_content(
            name="name",
            content="content",
            raw="raw",
            raw_type="rawType",
        )
        """
        _response = self._raw_client.update_post_content(
            name, content=content, raw=raw, raw_type=raw_type, request_options=request_options
        )
        return _response.data

    def delete_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Delete a content snapshot from a post and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
        client.post_v1alpha1console.delete_post_content(
            name="name",
            snapshot_name="snapshotName",
        )
        """
        _response = self._raw_client.delete_post_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    def fetch_post_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the editable head content of a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
        client.post_v1alpha1console.fetch_post_head_content(
            name="name",
        )
        """
        _response = self._raw_client.fetch_post_head_content(name, request_options=request_options)
        return _response.data

    def publish_post(
        self,
        name: str,
        *,
        head_snapshot: typing.Optional[str] = None,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Publish a post. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the post to publish.

        head_snapshot : typing.Optional[str]
            Snapshot metadata.name to publish. Defaults to the current base snapshot when no head snapshot exists.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the post for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.publish_post(
            name="name",
        )
        """
        _response = self._raw_client.publish_post(
            name, head_snapshot=head_snapshot, async_=async_, request_options=request_options
        )
        return _response.data

    def recycle_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Move a post to the recycle bin by marking it as deleted.

        Parameters
        ----------
        name : str
            metadata.name of the post to recycle.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.recycle_post(
            name="name",
        )
        """
        _response = self._raw_client.recycle_post(name, request_options=request_options)
        return _response.data

    def fetch_post_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the released content currently served for a published post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
        client.post_v1alpha1console.fetch_post_release_content(
            name="name",
        )
        """
        _response = self._raw_client.fetch_post_release_content(name, request_options=request_options)
        return _response.data

    def revert_to_specified_snapshot_for_post(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Post:
        """
        Restore the post content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the post's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.revert_to_specified_snapshot_for_post(
            name="name",
            snapshot_name="snapshotName",
        )
        """
        _response = self._raw_client.revert_to_specified_snapshot_for_post(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    def list_post_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListedSnapshotDto]:
        """
        List content snapshots for a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
        client.post_v1alpha1console.list_post_snapshots(
            name="name",
        )
        """
        _response = self._raw_client.list_post_snapshots(name, request_options=request_options)
        return _response.data

    def unpublish_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Unpublish a post so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of the post to unpublish.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1console.unpublish_post(
            name="name",
        )
        """
        _response = self._raw_client.unpublish_post(name, request_options=request_options)
        return _response.data


class AsyncPostV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPostV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPostV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPostV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedPostList:
        """
        List posts with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListPostsRequestPublishPhase]
            Filter posts by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        keyword : typing.Optional[str]
            Keyword used to match post title, slug, or excerpt.

        category_with_children : typing.Optional[str]
            Category metadata name used to include posts in that category and its child categories.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListedPostList
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
            await client.post_v1alpha1console.list_posts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_posts(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            publish_phase=publish_phase,
            keyword=keyword,
            category_with_children=category_with_children,
            request_options=request_options,
        )
        return _response.data

    async def draft_post(
        self, *, content: ContentUpdateParam, post: Post, request_options: typing.Optional[RequestOptions] = None
    ) -> Post:
        """
        Create a draft post together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ContentUpdateParam,
            Excerpt,
            Metadata,
            Post,
            PostSpec,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.post_v1alpha1console.draft_post(
                content=ContentUpdateParam(
                    content="content",
                    raw="raw",
                    raw_type="rawType",
                ),
                post=Post(
                    api_version="apiVersion",
                    kind="kind",
                    metadata=Metadata(
                        name="name",
                    ),
                    spec=PostSpec(
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
                        visible="PUBLIC",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_post(content=content, post=post, request_options=request_options)
        return _response.data

    async def update_draft_post(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        post: Post,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Update post metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the post to update.

        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ContentUpdateParam,
            Excerpt,
            Metadata,
            Post,
            PostSpec,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.post_v1alpha1console.update_draft_post(
                name="name",
                content=ContentUpdateParam(
                    content="content",
                    raw="raw",
                    raw_type="rawType",
                ),
                post=Post(
                    api_version="apiVersion",
                    kind="kind",
                    metadata=Metadata(
                        name="name",
                    ),
                    spec=PostSpec(
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
                        visible="PUBLIC",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_draft_post(
            name, content=content, post=post, request_options=request_options
        )
        return _response.data

    async def fetch_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch a post content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            await client.post_v1alpha1console.fetch_post_content(
                name="name",
                snapshot_name="snapshotName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_post_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    async def update_post_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Update only the content of an existing post.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be updated.

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
        Post
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
            await client.post_v1alpha1console.update_post_content(
                name="name",
                content="content",
                raw="raw",
                raw_type="rawType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_post_content(
            name, content=content, raw=raw, raw_type=raw_type, request_options=request_options
        )
        return _response.data

    async def delete_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Delete a content snapshot from a post and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            await client.post_v1alpha1console.delete_post_content(
                name="name",
                snapshot_name="snapshotName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_post_content(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    async def fetch_post_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the editable head content of a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            await client.post_v1alpha1console.fetch_post_head_content(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_post_head_content(name, request_options=request_options)
        return _response.data

    async def publish_post(
        self,
        name: str,
        *,
        head_snapshot: typing.Optional[str] = None,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Publish a post. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the post to publish.

        head_snapshot : typing.Optional[str]
            Snapshot metadata.name to publish. Defaults to the current base snapshot when no head snapshot exists.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the post for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
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
            await client.post_v1alpha1console.publish_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_post(
            name, head_snapshot=head_snapshot, async_=async_, request_options=request_options
        )
        return _response.data

    async def recycle_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Move a post to the recycle bin by marking it as deleted.

        Parameters
        ----------
        name : str
            metadata.name of the post to recycle.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
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
            await client.post_v1alpha1console.recycle_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recycle_post(name, request_options=request_options)
        return _response.data

    async def fetch_post_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentWrapper:
        """
        Fetch the released content currently served for a published post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            await client.post_v1alpha1console.fetch_post_release_content(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_post_release_content(name, request_options=request_options)
        return _response.data

    async def revert_to_specified_snapshot_for_post(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Post:
        """
        Restore the post content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the post's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
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
            await client.post_v1alpha1console.revert_to_specified_snapshot_for_post(
                name="name",
                snapshot_name="snapshotName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revert_to_specified_snapshot_for_post(
            name, snapshot_name=snapshot_name, request_options=request_options
        )
        return _response.data

    async def list_post_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListedSnapshotDto]:
        """
        List content snapshots for a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            await client.post_v1alpha1console.list_post_snapshots(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_post_snapshots(name, request_options=request_options)
        return _response.data

    async def unpublish_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Unpublish a post so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of the post to unpublish.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
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
            await client.post_v1alpha1console.unpublish_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unpublish_post(name, request_options=request_options)
        return _response.data
