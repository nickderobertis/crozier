

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.listed_post_list import ListedPostList
from ..types.metadata import Metadata
from ..types.post import Post
from ..types.post_spec import PostSpec
from ..types.post_status import PostStatus
from ..types.snap_shot_spec import SnapShotSpec
from ..types.snapshot import Snapshot
from .raw_client import AsyncRawPostV1Alpha1UcClient, RawPostV1Alpha1UcClient
from .types.list_my_posts_request_publish_phase import ListMyPostsRequestPublishPhase


OMIT = typing.cast(typing.Any, ...)


class PostV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPostV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPostV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPostV1Alpha1UcClient
        """
        return self._raw_client

    def list_my_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListMyPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedPostList:
        """
        List posts owned by the current user with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListMyPostsRequestPublishPhase]
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
        client.post_v1alpha1uc.list_my_posts()
        """
        _response = self._raw_client.list_my_posts(
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

    def create_my_post(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Create a draft post for the current user. To create it with initial content, put JSON-serialized Content into metadata.annotations['content.halo.run/content-json'].

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import Excerpt, FernApi, Metadata, PostSpec

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1uc.create_my_post(
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
        )
        """
        _response = self._raw_client.create_my_post(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def get_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Get a post owned by the current user by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
        client.post_v1alpha1uc.get_my_post(
            name="name",
        )
        """
        _response = self._raw_client.get_my_post(name, request_options=request_options)
        return _response.data

    def update_my_post(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Update post metadata and editable spec fields for the current user. Content is not updated by this operation.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        from fern import Excerpt, FernApi, Metadata, PostSpec

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1uc.update_my_post(
            name="name",
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
        )
        """
        _response = self._raw_client.update_my_post(
            name,
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def get_my_post_draft(
        self,
        name: str,
        *,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Get the editable draft snapshot of a post owned by the current user.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        patched : typing.Optional[bool]
            Whether to return the head snapshot patched against the base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1uc.get_my_post_draft(
            name="name",
        )
        """
        _response = self._raw_client.get_my_post_draft(name, patched=patched, request_options=request_options)
        return _response.data

    def update_my_post_draft(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: SnapShotSpec,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Update the editable draft snapshot of a post owned by the current user. The snapshot must belong to the post and must be the current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : SnapShotSpec

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            default response

        Examples
        --------
        from fern import FernApi, Metadata, Ref, SnapShotSpec

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_v1alpha1uc.update_my_post_draft(
            name="name",
            api_version="apiVersion",
            kind="kind",
            metadata=Metadata(
                name="name",
            ),
            spec=SnapShotSpec(
                owner="owner",
                raw_type="rawType",
                subject_ref=Ref(
                    group="group",
                    kind="kind",
                    name="name",
                ),
            ),
        )
        """
        _response = self._raw_client.update_my_post_draft(
            name, api_version=api_version, kind=kind, metadata=metadata, spec=spec, request_options=request_options
        )
        return _response.data

    def publish_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Publish a post owned by the current user from its current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
        client.post_v1alpha1uc.publish_my_post(
            name="name",
        )
        """
        _response = self._raw_client.publish_my_post(name, request_options=request_options)
        return _response.data

    def recycle_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Move a post owned by the current user to the recycle bin.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
        client.post_v1alpha1uc.recycle_my_post(
            name="name",
        )
        """
        _response = self._raw_client.recycle_my_post(name, request_options=request_options)
        return _response.data

    def unpublish_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Unpublish a post owned by the current user so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
        client.post_v1alpha1uc.unpublish_my_post(
            name="name",
        )
        """
        _response = self._raw_client.unpublish_my_post(name, request_options=request_options)
        return _response.data


class AsyncPostV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPostV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPostV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPostV1Alpha1UcClient
        """
        return self._raw_client

    async def list_my_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListMyPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListedPostList:
        """
        List posts owned by the current user with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListMyPostsRequestPublishPhase]
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
            await client.post_v1alpha1uc.list_my_posts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_posts(
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

    async def create_my_post(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Create a draft post for the current user. To create it with initial content, put JSON-serialized Content into metadata.annotations['content.halo.run/content-json'].

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Excerpt, Metadata, PostSpec

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.post_v1alpha1uc.create_my_post(
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
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_my_post(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def get_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Get a post owned by the current user by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
            await client.post_v1alpha1uc.get_my_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_post(name, request_options=request_options)
        return _response.data

    async def update_my_post(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Post:
        """
        Update post metadata and editable spec fields for the current user. Content is not updated by this operation.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Post
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Excerpt, Metadata, PostSpec

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.post_v1alpha1uc.update_my_post(
                name="name",
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
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_my_post(
            name,
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def get_my_post_draft(
        self,
        name: str,
        *,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Get the editable draft snapshot of a post owned by the current user.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        patched : typing.Optional[bool]
            Whether to return the head snapshot patched against the base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
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
            await client.post_v1alpha1uc.get_my_post_draft(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_post_draft(name, patched=patched, request_options=request_options)
        return _response.data

    async def update_my_post_draft(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: SnapShotSpec,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Update the editable draft snapshot of a post owned by the current user. The snapshot must belong to the post and must be the current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : SnapShotSpec

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Metadata, Ref, SnapShotSpec

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.post_v1alpha1uc.update_my_post_draft(
                name="name",
                api_version="apiVersion",
                kind="kind",
                metadata=Metadata(
                    name="name",
                ),
                spec=SnapShotSpec(
                    owner="owner",
                    raw_type="rawType",
                    subject_ref=Ref(
                        group="group",
                        kind="kind",
                        name="name",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_my_post_draft(
            name, api_version=api_version, kind=kind, metadata=metadata, spec=spec, request_options=request_options
        )
        return _response.data

    async def publish_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Publish a post owned by the current user from its current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
            await client.post_v1alpha1uc.publish_my_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_my_post(name, request_options=request_options)
        return _response.data

    async def recycle_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Move a post owned by the current user to the recycle bin.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
            await client.post_v1alpha1uc.recycle_my_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recycle_my_post(name, request_options=request_options)
        return _response.data

    async def unpublish_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Post:
        """
        Unpublish a post owned by the current user so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

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
            await client.post_v1alpha1uc.unpublish_my_post(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unpublish_my_post(name, request_options=request_options)
        return _response.data
