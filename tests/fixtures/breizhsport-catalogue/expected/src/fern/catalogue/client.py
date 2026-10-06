

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCatalogueClient, RawCatalogueClient
from .types.get_api_catalogue_response import GetApiCatalogueResponse
from .types.post_api_catalogue_response import PostApiCatalogueResponse
from .types.put_api_catalogue_quantity_response import PutApiCatalogueQuantityResponse
from .types.update_item_items_item import UpdateItemItemsItem


OMIT = typing.cast(typing.Any, ...)


class CatalogueClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogueClient
        """
        return self._raw_client

    def get_articles(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiCatalogueResponse:
        """
        Retrieves a list of articles with optional pagination.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset for pagination

        limit : typing.Optional[int]
            Maximum number of articles to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiCatalogueResponse
            List of articles

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalogue.get_articles(
            offset=0,
            limit=10,
        )
        """
        _response = self._raw_client.get_articles(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def create_an_article(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        price: typing.Optional[typing.Any] = OMIT,
        quantity: typing.Optional[typing.Any] = OMIT,
        brand: typing.Optional[str] = OMIT,
        rating: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiCatalogueResponse:
        """
        Creates a new article in the catalogue.

        Parameters
        ----------
        title : typing.Optional[str]

        description : typing.Optional[str]

        image : typing.Optional[str]

        price : typing.Optional[typing.Any]

        quantity : typing.Optional[typing.Any]

        brand : typing.Optional[str]

        rating : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiCatalogueResponse
            Article created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalogue.create_an_article()
        """
        _response = self._raw_client.create_an_article(
            title=title,
            description=description,
            image=image,
            price=price,
            quantity=quantity,
            brand=brand,
            rating=rating,
            request_options=request_options,
        )
        return _response.data

    def update_article_quantities(
        self,
        *,
        order_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[UpdateItemItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutApiCatalogueQuantityResponse:
        """
        Updates the quantities of multiple articles.

        Parameters
        ----------
        order_id : typing.Optional[str]

        items : typing.Optional[typing.Sequence[UpdateItemItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutApiCatalogueQuantityResponse
            Articles updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalogue.update_article_quantities()
        """
        _response = self._raw_client.update_article_quantities(
            order_id=order_id, items=items, request_options=request_options
        )
        return _response.data


class AsyncCatalogueClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogueClient
        """
        return self._raw_client

    async def get_articles(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiCatalogueResponse:
        """
        Retrieves a list of articles with optional pagination.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset for pagination

        limit : typing.Optional[int]
            Maximum number of articles to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiCatalogueResponse
            List of articles

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalogue.get_articles(
                offset=0,
                limit=10,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_articles(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    async def create_an_article(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        price: typing.Optional[typing.Any] = OMIT,
        quantity: typing.Optional[typing.Any] = OMIT,
        brand: typing.Optional[str] = OMIT,
        rating: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiCatalogueResponse:
        """
        Creates a new article in the catalogue.

        Parameters
        ----------
        title : typing.Optional[str]

        description : typing.Optional[str]

        image : typing.Optional[str]

        price : typing.Optional[typing.Any]

        quantity : typing.Optional[typing.Any]

        brand : typing.Optional[str]

        rating : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiCatalogueResponse
            Article created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalogue.create_an_article()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_an_article(
            title=title,
            description=description,
            image=image,
            price=price,
            quantity=quantity,
            brand=brand,
            rating=rating,
            request_options=request_options,
        )
        return _response.data

    async def update_article_quantities(
        self,
        *,
        order_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[UpdateItemItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutApiCatalogueQuantityResponse:
        """
        Updates the quantities of multiple articles.

        Parameters
        ----------
        order_id : typing.Optional[str]

        items : typing.Optional[typing.Sequence[UpdateItemItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutApiCatalogueQuantityResponse
            Articles updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalogue.update_article_quantities()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_article_quantities(
            order_id=order_id, items=items, request_options=request_options
        )
        return _response.data
