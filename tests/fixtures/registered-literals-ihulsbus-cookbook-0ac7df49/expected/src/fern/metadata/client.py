

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMetadataClient, RawMetadataClient
from .types.metadata_search_response import MetadataSearchResponse


OMIT = typing.cast(typing.Any, ...)


class MetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetadataClient
        """
        return self._raw_client

    def search_metadata(
        self,
        *,
        recipe_id: typing.Optional[str] = OMIT,
        category_id: typing.Optional[str] = OMIT,
        tag_id: typing.Optional[str] = OMIT,
        difficulty_level_id: typing.Optional[str] = OMIT,
        cuisine_type_id: typing.Optional[str] = OMIT,
        min_prep_time: typing.Optional[int] = OMIT,
        max_prep_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataSearchResponse:
        """
        Search through metadata

        Parameters
        ----------
        recipe_id : typing.Optional[str]
            ID of a recipe to base the search on

        category_id : typing.Optional[str]
            ID of a category to base the search on

        tag_id : typing.Optional[str]
            ID of a tag to base the search on

        difficulty_level_id : typing.Optional[str]
            ID of a difficulty level to base the search on

        cuisine_type_id : typing.Optional[str]
            ID of a cuisine type to base the search on

        min_prep_time : typing.Optional[int]
            minimum preparation time in minutes

        max_prep_time : typing.Optional[int]
            maximum preparation time in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metadata.search_metadata(
            category_id="0194b87e-7b64-44ad-98e3-6e292d7fc437",
        )
        """
        _response = self._raw_client.search_metadata(
            recipe_id=recipe_id,
            category_id=category_id,
            tag_id=tag_id,
            difficulty_level_id=difficulty_level_id,
            cuisine_type_id=cuisine_type_id,
            min_prep_time=min_prep_time,
            max_prep_time=max_prep_time,
            request_options=request_options,
        )
        return _response.data


class AsyncMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetadataClient
        """
        return self._raw_client

    async def search_metadata(
        self,
        *,
        recipe_id: typing.Optional[str] = OMIT,
        category_id: typing.Optional[str] = OMIT,
        tag_id: typing.Optional[str] = OMIT,
        difficulty_level_id: typing.Optional[str] = OMIT,
        cuisine_type_id: typing.Optional[str] = OMIT,
        min_prep_time: typing.Optional[int] = OMIT,
        max_prep_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataSearchResponse:
        """
        Search through metadata

        Parameters
        ----------
        recipe_id : typing.Optional[str]
            ID of a recipe to base the search on

        category_id : typing.Optional[str]
            ID of a category to base the search on

        tag_id : typing.Optional[str]
            ID of a tag to base the search on

        difficulty_level_id : typing.Optional[str]
            ID of a difficulty level to base the search on

        cuisine_type_id : typing.Optional[str]
            ID of a cuisine type to base the search on

        min_prep_time : typing.Optional[int]
            minimum preparation time in minutes

        max_prep_time : typing.Optional[int]
            maximum preparation time in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metadata.search_metadata(
                category_id="0194b87e-7b64-44ad-98e3-6e292d7fc437",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_metadata(
            recipe_id=recipe_id,
            category_id=category_id,
            tag_id=tag_id,
            difficulty_level_id=difficulty_level_id,
            cuisine_type_id=cuisine_type_id,
            min_prep_time=min_prep_time,
            max_prep_time=max_prep_time,
            request_options=request_options,
        )
        return _response.data
