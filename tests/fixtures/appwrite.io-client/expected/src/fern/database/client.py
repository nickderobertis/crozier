

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.document import Document
from ..types.document_list import DocumentList
from .raw_client import AsyncRawDatabaseClient, RawDatabaseClient


OMIT = typing.cast(typing.Any, ...)


class DatabaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatabaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatabaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatabaseClient
        """
        return self._raw_client

    def list_documents(
        self,
        collection_id: str,
        *,
        filters: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_field: typing.Optional[str] = None,
        order_type: typing.Optional[str] = None,
        order_cast: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentList:
        """
        Get a list of all the user documents. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's documents. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        filters : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of filter strings. Each filter is constructed from a key name, comparison operator (=, !=, >, <, <=, >=) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: 'name=John Doe' or 'category.$id>=5bed2d152c362'.

        limit : typing.Optional[int]
            Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Offset value. The default value is 0. Use this param to manage pagination.

        order_field : typing.Optional[str]
            Document field that results will be sorted by.

        order_type : typing.Optional[str]
            Order direction. Possible values are DESC for descending order, or ASC for ascending order.

        order_cast : typing.Optional[str]
            Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string.

        search : typing.Optional[str]
            Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentList
            Documents List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.database.list_documents(
            collection_id="collectionId",
        )
        """
        _response = self._raw_client.list_documents(
            collection_id,
            filters=filters,
            limit=limit,
            offset=offset,
            order_field=order_field,
            order_type=order_type,
            order_cast=order_cast,
            search=search,
            request_options=request_options,
        )
        return _response.data

    def create_document(
        self,
        collection_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        parent_document: typing.Optional[str] = OMIT,
        parent_property: typing.Optional[str] = OMIT,
        parent_property_type: typing.Optional[str] = OMIT,
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        data : typing.Dict[str, typing.Any]
            Document data as JSON object.

        parent_document : typing.Optional[str]
            Parent document unique ID. Use when you want your new document to be a child of a parent document.

        parent_property : typing.Optional[str]
            Parent document property name. Use when you want your new document to be a child of a parent document.

        parent_property_type : typing.Optional[str]
            Parent document property connection type. You can set this value to **assign**, **append** or **prepend**, default value is assign. Use when you want your new document to be a child of a parent document.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            Document

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.database.create_document(
            collection_id="collectionId",
            data={"key": "value"},
        )
        """
        _response = self._raw_client.create_document(
            collection_id,
            data=data,
            parent_document=parent_document,
            parent_property=parent_property,
            parent_property_type=parent_property_type,
            read=read,
            write=write,
            request_options=request_options,
        )
        return _response.data

    def get_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Document:
        """
        Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            Document

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.database.get_document(
            collection_id="collectionId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.get_document(collection_id, document_id, request_options=request_options)
        return _response.data

    def delete_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a document by its unique ID. This endpoint deletes only the parent documents, its attributes and relations to other documents. Child documents **will not** be deleted.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.database.delete_document(
            collection_id="collectionId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.delete_document(collection_id, document_id, request_options=request_options)
        return _response.data

    def update_document(
        self,
        collection_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

        data : typing.Dict[str, typing.Any]
            Document data as JSON object.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            Document

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.database.update_document(
            collection_id="collectionId",
            document_id="documentId",
            data={"key": "value"},
        )
        """
        _response = self._raw_client.update_document(
            collection_id, document_id, data=data, read=read, write=write, request_options=request_options
        )
        return _response.data


class AsyncDatabaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatabaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatabaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatabaseClient
        """
        return self._raw_client

    async def list_documents(
        self,
        collection_id: str,
        *,
        filters: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_field: typing.Optional[str] = None,
        order_type: typing.Optional[str] = None,
        order_cast: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentList:
        """
        Get a list of all the user documents. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's documents. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        filters : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of filter strings. Each filter is constructed from a key name, comparison operator (=, !=, >, <, <=, >=) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: 'name=John Doe' or 'category.$id>=5bed2d152c362'.

        limit : typing.Optional[int]
            Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Offset value. The default value is 0. Use this param to manage pagination.

        order_field : typing.Optional[str]
            Document field that results will be sorted by.

        order_type : typing.Optional[str]
            Order direction. Possible values are DESC for descending order, or ASC for ascending order.

        order_cast : typing.Optional[str]
            Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string.

        search : typing.Optional[str]
            Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentList
            Documents List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.database.list_documents(
                collection_id="collectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_documents(
            collection_id,
            filters=filters,
            limit=limit,
            offset=offset,
            order_field=order_field,
            order_type=order_type,
            order_cast=order_cast,
            search=search,
            request_options=request_options,
        )
        return _response.data

    async def create_document(
        self,
        collection_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        parent_document: typing.Optional[str] = OMIT,
        parent_property: typing.Optional[str] = OMIT,
        parent_property_type: typing.Optional[str] = OMIT,
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        data : typing.Dict[str, typing.Any]
            Document data as JSON object.

        parent_document : typing.Optional[str]
            Parent document unique ID. Use when you want your new document to be a child of a parent document.

        parent_property : typing.Optional[str]
            Parent document property name. Use when you want your new document to be a child of a parent document.

        parent_property_type : typing.Optional[str]
            Parent document property connection type. You can set this value to **assign**, **append** or **prepend**, default value is assign. Use when you want your new document to be a child of a parent document.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            Document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.database.create_document(
                collection_id="collectionId",
                data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_document(
            collection_id,
            data=data,
            parent_document=parent_document,
            parent_property=parent_property,
            parent_property_type=parent_property_type,
            read=read,
            write=write,
            request_options=request_options,
        )
        return _response.data

    async def get_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Document:
        """
        Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            Document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.database.get_document(
                collection_id="collectionId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_document(collection_id, document_id, request_options=request_options)
        return _response.data

    async def delete_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a document by its unique ID. This endpoint deletes only the parent documents, its attributes and relations to other documents. Child documents **will not** be deleted.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.database.delete_document(
                collection_id="collectionId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_document(collection_id, document_id, request_options=request_options)
        return _response.data

    async def update_document(
        self,
        collection_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

        data : typing.Dict[str, typing.Any]
            Document data as JSON object.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            Document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.database.update_document(
                collection_id="collectionId",
                document_id="documentId",
                data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_document(
            collection_id, document_id, data=data, read=read, write=write, request_options=request_options
        )
        return _response.data
