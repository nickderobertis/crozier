

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_id_parent_request import PageIdParentRequest
from ..types.rich_text_request import RichTextRequest
from ..types.sort_object import SortObject
from .raw_client import AsyncRawDataSourcesClient, RawDataSourcesClient


OMIT = typing.cast(typing.Any, ...)


class DataSourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataSourcesClient
        """
        return self._raw_client

    def query_data_source(
        self,
        data_source_id: str,
        *,
        filter_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.Sequence[SortObject]] = OMIT,
        start_cursor: typing.Optional[str] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        in_trash: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Query a data source (database) using filters and sorts

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source (database)

        filter_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A list of page property value IDs to limit the response

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter conditions for querying the data source

        sorts : typing.Optional[typing.Sequence[SortObject]]

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        archived : typing.Optional[bool]

        in_trash : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.data_sources.query_data_source(
            data_source_id="data_source_id",
        )
        """
        _response = self._raw_client.query_data_source(
            data_source_id,
            filter_properties=filter_properties,
            filter=filter,
            sorts=sorts,
            start_cursor=start_cursor,
            page_size=page_size,
            archived=archived,
            in_trash=in_trash,
            request_options=request_options,
        )
        return _response.data

    def retrieve_a_data_source(
        self, data_source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve metadata and schema for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.data_sources.retrieve_a_data_source(
            data_source_id="data_source_id",
        )
        """
        _response = self._raw_client.retrieve_a_data_source(data_source_id, request_options=request_options)
        return _response.data

    def update_a_data_source(
        self,
        data_source_id: str,
        *,
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        description: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update properties of a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        description : typing.Optional[typing.Sequence[RichTextRequest]]

        properties : typing.Optional[typing.Dict[str, typing.Any]]
            Property schema updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.data_sources.update_a_data_source(
            data_source_id="data_source_id",
        )
        """
        _response = self._raw_client.update_a_data_source(
            data_source_id, title=title, description=description, properties=properties, request_options=request_options
        )
        return _response.data

    def create_a_data_source(
        self,
        *,
        parent: PageIdParentRequest,
        properties: typing.Dict[str, typing.Any],
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create a new data source (database)

        Parameters
        ----------
        parent : PageIdParentRequest

        properties : typing.Dict[str, typing.Any]
            Property schema of data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi, PageIdParentRequest

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.data_sources.create_a_data_source(
            parent=PageIdParentRequest(
                page_id="page_id",
            ),
            properties={"key": "value"},
        )
        """
        _response = self._raw_client.create_a_data_source(
            parent=parent, properties=properties, title=title, request_options=request_options
        )
        return _response.data

    def list_data_source_templates(
        self,
        data_source_id: str,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        List available templates for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.data_sources.list_data_source_templates(
            data_source_id="data_source_id",
        )
        """
        _response = self._raw_client.list_data_source_templates(
            data_source_id, start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data


class AsyncDataSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataSourcesClient
        """
        return self._raw_client

    async def query_data_source(
        self,
        data_source_id: str,
        *,
        filter_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.Sequence[SortObject]] = OMIT,
        start_cursor: typing.Optional[str] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        in_trash: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Query a data source (database) using filters and sorts

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source (database)

        filter_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A list of page property value IDs to limit the response

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter conditions for querying the data source

        sorts : typing.Optional[typing.Sequence[SortObject]]

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        archived : typing.Optional[bool]

        in_trash : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_sources.query_data_source(
                data_source_id="data_source_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_data_source(
            data_source_id,
            filter_properties=filter_properties,
            filter=filter,
            sorts=sorts,
            start_cursor=start_cursor,
            page_size=page_size,
            archived=archived,
            in_trash=in_trash,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_a_data_source(
        self, data_source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve metadata and schema for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_sources.retrieve_a_data_source(
                data_source_id="data_source_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_data_source(data_source_id, request_options=request_options)
        return _response.data

    async def update_a_data_source(
        self,
        data_source_id: str,
        *,
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        description: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update properties of a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        description : typing.Optional[typing.Sequence[RichTextRequest]]

        properties : typing.Optional[typing.Dict[str, typing.Any]]
            Property schema updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_sources.update_a_data_source(
                data_source_id="data_source_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_data_source(
            data_source_id, title=title, description=description, properties=properties, request_options=request_options
        )
        return _response.data

    async def create_a_data_source(
        self,
        *,
        parent: PageIdParentRequest,
        properties: typing.Dict[str, typing.Any],
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create a new data source (database)

        Parameters
        ----------
        parent : PageIdParentRequest

        properties : typing.Dict[str, typing.Any]
            Property schema of data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PageIdParentRequest

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_sources.create_a_data_source(
                parent=PageIdParentRequest(
                    page_id="page_id",
                ),
                properties={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_data_source(
            parent=parent, properties=properties, title=title, request_options=request_options
        )
        return _response.data

    async def list_data_source_templates(
        self,
        data_source_id: str,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        List available templates for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_sources.list_data_source_templates(
                data_source_id="data_source_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_data_source_templates(
            data_source_id, start_cursor=start_cursor, page_size=page_size, request_options=request_options
        )
        return _response.data
