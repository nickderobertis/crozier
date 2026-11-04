

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..cuisinetype.types.cuisine_type import CuisineType
from ..types.paginated_category_response import PaginatedCategoryResponse
from .raw_client import AsyncRawCategoryClient, RawCategoryClient
from .types.category import Category


OMIT = typing.cast(typing.Any, ...)


class CategoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCategoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCategoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCategoryClient
        """
        return self._raw_client

    def get_all_category(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCategoryResponse:
        """
        Retrieves categories known to the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCategoryResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.category.get_all_category()
        """
        _response = self._raw_client.get_all_category(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_category(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Category:
        """
        Create a category

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a category

        name : typing.Optional[str]
            Name of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Category
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.category.create_category(
            name="category",
        )
        """
        _response = self._raw_client.create_category(id=id, name=name, request_options=request_options)
        return _response.data

    def get_category(self, category_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Category:
        """
        Get a single category

        Parameters
        ----------
        category_id : str
            UUID of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Category
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.category.get_category(
            category_id="CategoryID",
        )
        """
        _response = self._raw_client.get_category(category_id, request_options=request_options)
        return _response.data

    def update_category(
        self,
        category_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Category:
        """
        Updates a category

        Parameters
        ----------
        category_id : str
            UUID of a category

        id : typing.Optional[str]
            ID of a category

        name : typing.Optional[str]
            Name of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Category
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.category.update_category(
            category_id="CategoryID",
            name="category",
        )
        """
        _response = self._raw_client.update_category(category_id, id=id, name=name, request_options=request_options)
        return _response.data

    def delete_category(self, category_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a category

        Parameters
        ----------
        category_id : str
            UUID of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.category.delete_category(
            category_id="CategoryID",
        )
        """
        _response = self._raw_client.delete_category(category_id, request_options=request_options)
        return _response.data

    def create_cuisinetype(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CuisineType:
        """
        Create a cuisinetype

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a cuisine type

        name : typing.Optional[str]
            name of a cuisine type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuisineType
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.category.create_cuisinetype(
            name="Italian",
        )
        """
        _response = self._raw_client.create_cuisinetype(id=id, name=name, request_options=request_options)
        return _response.data


class AsyncCategoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCategoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCategoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCategoryClient
        """
        return self._raw_client

    async def get_all_category(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCategoryResponse:
        """
        Retrieves categories known to the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCategoryResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.category.get_all_category()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_category(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create_category(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Category:
        """
        Create a category

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a category

        name : typing.Optional[str]
            Name of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Category
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.category.create_category(
                name="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_category(id=id, name=name, request_options=request_options)
        return _response.data

    async def get_category(
        self, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Category:
        """
        Get a single category

        Parameters
        ----------
        category_id : str
            UUID of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Category
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.category.get_category(
                category_id="CategoryID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_category(category_id, request_options=request_options)
        return _response.data

    async def update_category(
        self,
        category_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Category:
        """
        Updates a category

        Parameters
        ----------
        category_id : str
            UUID of a category

        id : typing.Optional[str]
            ID of a category

        name : typing.Optional[str]
            Name of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Category
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.category.update_category(
                category_id="CategoryID",
                name="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_category(
            category_id, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_category(
        self, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a category

        Parameters
        ----------
        category_id : str
            UUID of a category

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.category.delete_category(
                category_id="CategoryID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_category(category_id, request_options=request_options)
        return _response.data

    async def create_cuisinetype(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CuisineType:
        """
        Create a cuisinetype

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a cuisine type

        name : typing.Optional[str]
            name of a cuisine type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuisineType
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.category.create_cuisinetype(
                name="Italian",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cuisinetype(id=id, name=name, request_options=request_options)
        return _response.data
