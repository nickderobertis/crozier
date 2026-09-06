

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_series_dto import PageSeriesDto
from .raw_client import AsyncRawCollectionSeriesClient, RawCollectionSeriesClient
from .types.get_series_by_collection_id_request_read_status_item import GetSeriesByCollectionIdRequestReadStatusItem
from .types.get_series_by_collection_id_request_status_item import GetSeriesByCollectionIdRequestStatusItem


class CollectionSeriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionSeriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionSeriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionSeriesClient
        """
        return self._raw_client

    def get_series_by_collection_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestReadStatusItem,
                typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem],
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageSeriesDto:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestReadStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageSeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collection_series.get_series_by_collection_id(
            id="id",
        )
        """
        _response = self._raw_client.get_series_by_collection_id(
            id,
            library_id=library_id,
            status=status,
            read_status=read_status,
            publisher=publisher,
            language=language,
            genre=genre,
            tag=tag,
            age_rating=age_rating,
            release_year=release_year,
            deleted=deleted,
            complete=complete,
            unpaged=unpaged,
            page=page,
            size=size,
            author=author,
            request_options=request_options,
        )
        return _response.data


class AsyncCollectionSeriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionSeriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionSeriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionSeriesClient
        """
        return self._raw_client

    async def get_series_by_collection_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesByCollectionIdRequestReadStatusItem,
                typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem],
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageSeriesDto:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesByCollectionIdRequestReadStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageSeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collection_series.get_series_by_collection_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_by_collection_id(
            id,
            library_id=library_id,
            status=status,
            read_status=read_status,
            publisher=publisher,
            language=language,
            genre=genre,
            tag=tag,
            age_rating=age_rating,
            release_year=release_year,
            deleted=deleted,
            complete=complete,
            unpaged=unpaged,
            page=page,
            size=size,
            author=author,
            request_options=request_options,
        )
        return _response.data
