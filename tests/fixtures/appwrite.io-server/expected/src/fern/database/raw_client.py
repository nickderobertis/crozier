

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.collection import Collection
from ..types.collection_list import CollectionList
from ..types.document import Document
from ..types.document_list import DocumentList


OMIT = typing.cast(typing.Any, ...)


class RawDatabaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_collections(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CollectionList]:
        """
        Get a list of all the user collections. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's collections. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CollectionList]
            Collections List
        """
        _response = self._client_wrapper.httpx_client.request(
            "database/collections",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CollectionList,
                    parse_obj_as(
                        type_=CollectionList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_collection(
        self,
        *,
        name: str,
        read: typing.Sequence[str],
        rules: typing.Sequence[str],
        write: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Collection]:
        """
        Create a new Collection.

        Parameters
        ----------
        name : str
            Collection name. Max length: 128 chars.

        read : typing.Sequence[str]
            An array of strings with read permissions. By default no user is granted with any read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        rules : typing.Sequence[str]
            Array of [rule objects](/docs/rules). Each rule define a collection field name, data type and validation.

        write : typing.Sequence[str]
            An array of strings with write permissions. By default no user is granted with any write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Collection
        """
        _response = self._client_wrapper.httpx_client.request(
            "database/collections",
            method="POST",
            json={
                "name": name,
                "read": read,
                "rules": rules,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Collection]:
        """
        Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

        Parameters
        ----------
        collection_id : str
            Collection unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Collection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_collection(
        self,
        collection_id: str,
        *,
        name: str,
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Collection]:
        """
        Update a collection by its unique ID.

        Parameters
        ----------
        collection_id : str
            Collection unique ID.

        name : str
            Collection name. Max length: 128 chars.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        rules : typing.Optional[typing.Sequence[str]]
            Array of [rule objects](/docs/rules). Each rule define a collection field name, data type and validation.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Collection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}",
            method="PUT",
            json={
                "name": name,
                "read": read,
                "rules": rules,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        collection_id : str
            Collection unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[DocumentList]:
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
        HttpResponse[DocumentList]
            Documents List
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents",
            method="GET",
            params={
                "filters": filters,
                "limit": limit,
                "offset": offset,
                "orderField": order_field,
                "orderType": order_type,
                "orderCast": order_cast,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentList,
                    parse_obj_as(
                        type_=DocumentList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_document(
        self,
        collection_id: str,
        *,
        data: typing.Dict[str, typing.Optional[typing.Any]],
        parent_document: typing.Optional[str] = OMIT,
        parent_property: typing.Optional[str] = OMIT,
        parent_property_type: typing.Optional[str] = OMIT,
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Document]:
        """
        Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        data : typing.Dict[str, typing.Optional[typing.Any]]
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
        HttpResponse[Document]
            Document
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents",
            method="POST",
            json={
                "data": data,
                "parentDocument": parent_document,
                "parentProperty": parent_property,
                "parentPropertyType": parent_property_type,
                "read": read,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Document,
                    parse_obj_as(
                        type_=Document,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Document]:
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
        HttpResponse[Document]
            Document
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Document,
                    parse_obj_as(
                        type_=Document,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_document(
        self,
        collection_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Optional[typing.Any]],
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Document]:
        """
        Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

        data : typing.Dict[str, typing.Optional[typing.Any]]
            Document data as JSON object.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Document]
            Document
        """
        _response = self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="PATCH",
            json={
                "data": data,
                "read": read,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Document,
                    parse_obj_as(
                        type_=Document,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDatabaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_collections(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CollectionList]:
        """
        Get a list of all the user collections. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's collections. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CollectionList]
            Collections List
        """
        _response = await self._client_wrapper.httpx_client.request(
            "database/collections",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CollectionList,
                    parse_obj_as(
                        type_=CollectionList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_collection(
        self,
        *,
        name: str,
        read: typing.Sequence[str],
        rules: typing.Sequence[str],
        write: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Collection]:
        """
        Create a new Collection.

        Parameters
        ----------
        name : str
            Collection name. Max length: 128 chars.

        read : typing.Sequence[str]
            An array of strings with read permissions. By default no user is granted with any read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        rules : typing.Sequence[str]
            Array of [rule objects](/docs/rules). Each rule define a collection field name, data type and validation.

        write : typing.Sequence[str]
            An array of strings with write permissions. By default no user is granted with any write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            "database/collections",
            method="POST",
            json={
                "name": name,
                "read": read,
                "rules": rules,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Collection]:
        """
        Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

        Parameters
        ----------
        collection_id : str
            Collection unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_collection(
        self,
        collection_id: str,
        *,
        name: str,
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Collection]:
        """
        Update a collection by its unique ID.

        Parameters
        ----------
        collection_id : str
            Collection unique ID.

        name : str
            Collection name. Max length: 128 chars.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        rules : typing.Optional[typing.Sequence[str]]
            Array of [rule objects](/docs/rules). Each rule define a collection field name, data type and validation.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}",
            method="PUT",
            json={
                "name": name,
                "read": read,
                "rules": rules,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        collection_id : str
            Collection unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[DocumentList]:
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
        AsyncHttpResponse[DocumentList]
            Documents List
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents",
            method="GET",
            params={
                "filters": filters,
                "limit": limit,
                "offset": offset,
                "orderField": order_field,
                "orderType": order_type,
                "orderCast": order_cast,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentList,
                    parse_obj_as(
                        type_=DocumentList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_document(
        self,
        collection_id: str,
        *,
        data: typing.Dict[str, typing.Optional[typing.Any]],
        parent_document: typing.Optional[str] = OMIT,
        parent_property: typing.Optional[str] = OMIT,
        parent_property_type: typing.Optional[str] = OMIT,
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Document]:
        """
        Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        data : typing.Dict[str, typing.Optional[typing.Any]]
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
        AsyncHttpResponse[Document]
            Document
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents",
            method="POST",
            json={
                "data": data,
                "parentDocument": parent_document,
                "parentProperty": parent_property,
                "parentPropertyType": parent_property_type,
                "read": read,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Document,
                    parse_obj_as(
                        type_=Document,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Document]:
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
        AsyncHttpResponse[Document]
            Document
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Document,
                    parse_obj_as(
                        type_=Document,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_document(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_document(
        self,
        collection_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Optional[typing.Any]],
        read: typing.Optional[typing.Sequence[str]] = OMIT,
        write: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Document]:
        """
        Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

        Parameters
        ----------
        collection_id : str
            Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).

        document_id : str
            Document unique ID.

        data : typing.Dict[str, typing.Optional[typing.Any]]
            Document data as JSON object.

        read : typing.Optional[typing.Sequence[str]]
            An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.Sequence[str]]
            An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Document]
            Document
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"database/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="PATCH",
            json={
                "data": data,
                "read": read,
                "write": write,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Document,
                    parse_obj_as(
                        type_=Document,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
