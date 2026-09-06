

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collection_dto import CollectionDto
from ..types.page_collection_dto import PageCollectionDto
from .raw_client import AsyncRawCollectionsClient, RawCollectionsClient


OMIT = typing.cast(typing.Any, ...)


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionsClient
        """
        return self._raw_client

    def get_collections(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageCollectionDto:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageCollectionDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.get_collections()
        """
        _response = self._raw_client.get_collections(
            search=search, library_id=library_id, unpaged=unpaged, page=page, size=size, request_options=request_options
        )
        return _response.data

    def create_collection(
        self,
        *,
        name: str,
        ordered: bool,
        series_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        name : str

        ordered : bool

        series_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.create_collection(
            name="name",
            ordered=True,
            series_ids=["seriesIds"],
        )
        """
        _response = self._raw_client.create_collection(
            name=name, ordered=ordered, series_ids=series_ids, request_options=request_options
        )
        return _response.data

    def get_collection_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionDto:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.get_collection_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_collection_by_id(id, request_options=request_options)
        return _response.data

    def delete_collection_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.delete_collection_by_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_collection_by_id(id, request_options=request_options)
        return _response.data

    def update_collection_by_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        ordered: typing.Optional[bool] = OMIT,
        series_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        ordered : typing.Optional[bool]

        series_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.update_collection_by_id(
            id="id",
        )
        """
        _response = self._raw_client.update_collection_by_id(
            id, name=name, ordered=ordered, series_ids=series_ids, request_options=request_options
        )
        return _response.data


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionsClient
        """
        return self._raw_client

    async def get_collections(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageCollectionDto:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageCollectionDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.get_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections(
            search=search, library_id=library_id, unpaged=unpaged, page=page, size=size, request_options=request_options
        )
        return _response.data

    async def create_collection(
        self,
        *,
        name: str,
        ordered: bool,
        series_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        name : str

        ordered : bool

        series_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.create_collection(
                name="name",
                ordered=True,
                series_ids=["seriesIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_collection(
            name=name, ordered=ordered, series_ids=series_ids, request_options=request_options
        )
        return _response.data

    async def get_collection_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionDto:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.get_collection_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection_by_id(id, request_options=request_options)
        return _response.data

    async def delete_collection_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.delete_collection_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_collection_by_id(id, request_options=request_options)
        return _response.data

    async def update_collection_by_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        ordered: typing.Optional[bool] = OMIT,
        series_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        ordered : typing.Optional[bool]

        series_ids : typing.Optional[typing.Sequence[str]]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.update_collection_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_collection_by_id(
            id, name=name, ordered=ordered, series_ids=series_ids, request_options=request_options
        )
        return _response.data
