

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCategoriesClient, RawCategoriesClient
from .types.create_category_request_permissions import CreateCategoryRequestPermissions
from .types.create_category_response import CreateCategoryResponse
from .types.get_category_response import GetCategoryResponse
from .types.list_categories_response import ListCategoriesResponse
from .types.list_category_topics_response import ListCategoryTopicsResponse
from .types.update_category_request_permissions import UpdateCategoryRequestPermissions
from .types.update_category_response import UpdateCategoryResponse


OMIT = typing.cast(typing.Any, ...)


class CategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCategoriesClient
        """
        return self._raw_client

    def get_category(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> GetCategoryResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCategoryResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.categories.get_category(
            id=1,
        )
        """
        _response = self._raw_client.get_category(id, request_options=request_options)
        return _response.data

    def list_category_topics(
        self, slug: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListCategoryTopicsResponse:
        """
        Parameters
        ----------
        slug : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCategoryTopicsResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.categories.list_category_topics(
            slug="slug",
            id=1,
        )
        """
        _response = self._raw_client.list_category_topics(slug, id, request_options=request_options)
        return _response.data

    def list_categories(
        self,
        *,
        include_subcategories: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCategoriesResponse:
        """
        Parameters
        ----------
        include_subcategories : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCategoriesResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.categories.list_categories()
        """
        _response = self._raw_client.list_categories(
            include_subcategories=include_subcategories, request_options=request_options
        )
        return _response.data

    def create_category(
        self,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[CreateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCategoryResponse:
        """
        Parameters
        ----------
        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Any]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[CreateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCategoryResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.categories.create_category(
            name="name",
        )
        """
        _response = self._raw_client.create_category(
            name=name,
            allow_badges=allow_badges,
            color=color,
            form_template_ids=form_template_ids,
            parent_category_id=parent_category_id,
            permissions=permissions,
            search_priority=search_priority,
            slug=slug,
            text_color=text_color,
            topic_featured_links_allowed=topic_featured_links_allowed,
            request_options=request_options,
        )
        return _response.data

    def update_category(
        self,
        id: int,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[UpdateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCategoryResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Any]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[UpdateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCategoryResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.categories.update_category(
            id=1,
            name="name",
        )
        """
        _response = self._raw_client.update_category(
            id,
            name=name,
            allow_badges=allow_badges,
            color=color,
            form_template_ids=form_template_ids,
            parent_category_id=parent_category_id,
            permissions=permissions,
            search_priority=search_priority,
            slug=slug,
            text_color=text_color,
            topic_featured_links_allowed=topic_featured_links_allowed,
            request_options=request_options,
        )
        return _response.data


class AsyncCategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCategoriesClient
        """
        return self._raw_client

    async def get_category(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCategoryResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCategoryResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.categories.get_category(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_category(id, request_options=request_options)
        return _response.data

    async def list_category_topics(
        self, slug: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListCategoryTopicsResponse:
        """
        Parameters
        ----------
        slug : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCategoryTopicsResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.categories.list_category_topics(
                slug="slug",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_category_topics(slug, id, request_options=request_options)
        return _response.data

    async def list_categories(
        self,
        *,
        include_subcategories: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCategoriesResponse:
        """
        Parameters
        ----------
        include_subcategories : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCategoriesResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.categories.list_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_categories(
            include_subcategories=include_subcategories, request_options=request_options
        )
        return _response.data

    async def create_category(
        self,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[CreateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCategoryResponse:
        """
        Parameters
        ----------
        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Any]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[CreateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCategoryResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.categories.create_category(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_category(
            name=name,
            allow_badges=allow_badges,
            color=color,
            form_template_ids=form_template_ids,
            parent_category_id=parent_category_id,
            permissions=permissions,
            search_priority=search_priority,
            slug=slug,
            text_color=text_color,
            topic_featured_links_allowed=topic_featured_links_allowed,
            request_options=request_options,
        )
        return _response.data

    async def update_category(
        self,
        id: int,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[UpdateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCategoryResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Any]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[UpdateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCategoryResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.categories.update_category(
                id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_category(
            id,
            name=name,
            allow_badges=allow_badges,
            color=color,
            form_template_ids=form_template_ids,
            parent_category_id=parent_category_id,
            permissions=permissions,
            search_priority=search_priority,
            slug=slug,
            text_color=text_color,
            topic_featured_links_allowed=topic_featured_links_allowed,
            request_options=request_options,
        )
        return _response.data
