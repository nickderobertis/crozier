

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.favourites_response import FavouritesResponse
from ..types.favourites_section import FavouritesSection
from .raw_client import AsyncRawFavouritesClient, RawFavouritesClient
from .types.get_favourites_request_representation import GetFavouritesRequestRepresentation
from .types.get_favourites_request_sort_field import GetFavouritesRequestSortField
from .types.get_favourites_request_sort_order import GetFavouritesRequestSortOrder


class FavouritesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFavouritesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFavouritesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFavouritesClient
        """
        return self._raw_client

    def get_favourites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetFavouritesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_section_name: typing.Optional[str] = None,
        sort_field: typing.Optional[GetFavouritesRequestSortField] = None,
        representation: typing.Optional[GetFavouritesRequestRepresentation] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FavouritesResponse:
        """
        Get all favourite sections, in flat or tree view

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetFavouritesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_section_name : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
            - representation: flat
              - `section.name`

        sort_field : typing.Optional[GetFavouritesRequestSortField]

        representation : typing.Optional[GetFavouritesRequestRepresentation]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
              - `lineItem.itemName`,
            - representation: flat
              - `section.name`
              - `section.description`,
              - `lineItem.itemName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FavouritesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.favourites.get_favourites()
        """
        _response = self._raw_client.get_favourites(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_section_name=filter_section_name,
            sort_field=sort_field,
            representation=representation,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    def get_favourites_section_id(
        self, section_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FavouritesSection:
        """
        Get a specific favourite section

        Parameters
        ----------
        section_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FavouritesSection
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.favourites.get_favourites_section_id(
            section_id="sectionId",
        )
        """
        _response = self._raw_client.get_favourites_section_id(section_id, request_options=request_options)
        return _response.data


class AsyncFavouritesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFavouritesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFavouritesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFavouritesClient
        """
        return self._raw_client

    async def get_favourites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetFavouritesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_section_name: typing.Optional[str] = None,
        sort_field: typing.Optional[GetFavouritesRequestSortField] = None,
        representation: typing.Optional[GetFavouritesRequestRepresentation] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FavouritesResponse:
        """
        Get all favourite sections, in flat or tree view

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetFavouritesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_section_name : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
            - representation: flat
              - `section.name`

        sort_field : typing.Optional[GetFavouritesRequestSortField]

        representation : typing.Optional[GetFavouritesRequestRepresentation]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
              - `lineItem.itemName`,
            - representation: flat
              - `section.name`
              - `section.description`,
              - `lineItem.itemName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FavouritesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.favourites.get_favourites()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_favourites(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_section_name=filter_section_name,
            sort_field=sort_field,
            representation=representation,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    async def get_favourites_section_id(
        self, section_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FavouritesSection:
        """
        Get a specific favourite section

        Parameters
        ----------
        section_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FavouritesSection
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.favourites.get_favourites_section_id(
                section_id="sectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_favourites_section_id(section_id, request_options=request_options)
        return _response.data
