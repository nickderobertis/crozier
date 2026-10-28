

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.item_collection import ItemCollection
from ..types.post_fields_extension import PostFieldsExtension
from ..types.search_post_request_filter_lang import SearchPostRequestFilterLang
from ..types.search_post_request_intersects import SearchPostRequestIntersects
from ..types.sort_extension import SortExtension
from .raw_client import AsyncRawCadipStationsClient, RawCadipStationsClient
from .types.get_cadip_collection_cadip_collections_collection_id_get_response import (
    GetCadipCollectionCadipCollectionsCollectionIdGetResponse,
)
from .types.get_cadip_collection_items_cadip_collections_collection_id_items_get_request_filter_lang import (
    GetCadipCollectionItemsCadipCollectionsCollectionIdItemsGetRequestFilterLang,
)


OMIT = typing.cast(typing.Any, ...)


class CadipStationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCadipStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCadipStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCadipStationsClient
        """
        return self._raw_client

    def search(
        self,
        *,
        collections: typing.Optional[typing.Sequence[str]] = OMIT,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        intersects: typing.Optional[SearchPostRequestIntersects] = OMIT,
        datetime: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        sortby: typing.Optional[typing.Sequence[SortExtension]] = OMIT,
        fields: typing.Optional[PostFieldsExtension] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filter_crs: typing.Optional[str] = OMIT,
        filter_lang: typing.Optional[SearchPostRequestFilterLang] = OMIT,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemCollection:
        """
        Endpoint.

        Parameters
        ----------
        collections : typing.Optional[typing.Sequence[str]]

        ids : typing.Optional[typing.Sequence[str]]

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        intersects : typing.Optional[SearchPostRequestIntersects]

        datetime : typing.Optional[str]

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        conf : typing.Optional[typing.Dict[str, typing.Any]]

        query : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        sortby : typing.Optional[typing.Sequence[SortExtension]]
            An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'

        fields : typing.Optional[PostFieldsExtension]
            Include or exclude fields from items body.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            A CQL filter expression for filtering items.

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[SearchPostRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemCollection
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cadip_stations.search()
        """
        _response = self._raw_client.search(
            collections=collections,
            ids=ids,
            bbox=bbox,
            intersects=intersects,
            datetime=datetime,
            limit=limit,
            conf=conf,
            query=query,
            sortby=sortby,
            fields=fields,
            filter=filter,
            filter_crs=filter_crs,
            filter_lang=filter_lang,
            token=token,
            request_options=request_options,
        )
        return _response.data

    def get_root_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieve the RSPY CADIP Search catalog landing page.

        This endpoint generates a STAC (SpatioTemporal Asset Catalog) Catalog object that serves as the landing
        page for the RSPY CADIP service. The catalog includes basic metadata about the service and links to
        available collections.

        The resulting catalog contains:
        - `id`: A unique identifier for the catalog, generated as a UUID.
        - `description`: A brief description of the catalog.
        - `title`: The title of the catalog.
        - `stac_version`: The version of the STAC specification to which the catalog conforms.
        - `conformsTo`: A list of STAC and OGC API specifications that the catalog conforms to.
        - `links`: A link to the `/cadip/collections` endpoint where users can find available collections.

        The `stac_version` is set to "1.1.0", and the `conformsTo` field lists the relevant STAC and OGC API
        specifications that the catalog adheres to. A link to the collections endpoint is added to the catalog's
        `links` field, allowing users to discover available collections in the CADIP service.

        Parameters:
        - request: The HTTP request object which includes details about the incoming request.

        Returns:
        - dict: A dictionary representation of the STAC catalog, including metadata and links.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cadip_stations.get_root_catalog()
        """
        _response = self._raw_client.get_root_catalog(request_options=request_options)
        return _response.data

    def get_conformance(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cadip_stations.get_conformance()
        """
        _response = self._raw_client.get_conformance(request_options=request_options)
        return _response.data

    def get_allowed_cadip_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Endpoint to retrieve an object containing collections and links that a user is authorized to
            access based on their API key.

        This endpoint reads the API key from the request to determine the roles associated with the user.
        Using these roles, it identifies the stations the user can access and filters the available collections
        accordingly. The endpoint then constructs a JSON, which includes links to the collections that match the allowed
        stations.

        - It begins by extracting roles from the `request.state.auth_roles` and derives the station names
          the user has access to.
        - Then, it filters the collections from the configuration to include only those belonging to the
          allowed stations.
        - For each filtered collection, a corresponding STAC collection is created with links to detailed
          session searches.

        The final response is a dictionary representation of the STAC catalog, which includes details about
        the collections the user is allowed to access.

        Returns:
            dict: Object containing an array of Collection objects in the Catalog, and Link relations.

        Raises:
            HTTPException: If there are issues with reading configurations or processing session searches.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cadip_stations.get_allowed_cadip_collections()
        """
        _response = self._raw_client.get_allowed_cadip_collections(request_options=request_options)
        return _response.data

    def get_cadip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCadipCollectionCadipCollectionsCollectionIdGetResponse:
        """
        Retrieve a STAC-Compliant Collection for a Specific CADIP Station.

        This endpoint fetches and returns session data from an external CADIP server, structured as a STAC-compliant
        Collection. By specifying a `collection_id`, the client can retrieve a collection of session metadata related to
        that CADIP station.

        ### Path Parameters:
        - `collection_id` (string): The unique identifier of the CADIP collection to retrieve.

        ### Response:
        The response is a STAC Collection object formatted as a dictionary, which contains links to session details.
        Each session is represented as a link inside the `links` array, following the STAC specification. These links point
         to the detailed metadata for each session.

        ### Key Operations:
        1. **Configuration Lookup**: Reads the relevant configuration from `RSPY_CADIP_SEARCH_CONFIG`.
        2. **CADIP Server Request**: Sends a request to the CADIP server to retrieve session data.
        3. **STAC Formatting**: Transforms the session data into a STAC Collection format.
        4. **Link Creation**: Adds links to session details in the response.

        ### Responses:
        - **200 OK**: Returns the STAC Collection containing links to session metadata. If multiple collections are
        available, returns a list of collections.
        - **422 Unprocessable Entity**: Returns an error if the STAC Collection cannot be created due to missing or invalid
        configuration details.

        ### Raises:
        - **HTTPException**:
          - **422 Unprocessable Entity**: If any configuration data is missing, invalid, or causes an error when creating
          the STAC Collection.

        This endpoint is secured by an API key validator, ensuring that only authorized users can retrieve data from the
        CADIP station.

        Parameters
        ----------
        collection_id : str
            E.G. ins_s1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCadipCollectionCadipCollectionsCollectionIdGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cadip_stations.get_cadip_collection(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_cadip_collection(collection_id, request_options=request_options)
        return _response.data

    def get_cadip_collection_items(
        self,
        collection_id: str,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[
            GetCadipCollectionItemsCadipCollectionsCollectionIdItemsGetRequestFilterLang
        ] = None,
        sortby: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Retrieve a List of items for a specific collection.

        This endpoint provides access to a list of sessions for a given collection from the CADIP station.
        By specifying the `collection_id` in the path, clients can retrieve session metadata in the form of a STAC
        (SpatioTemporal Asset Catalog) ItemCollection.

        ### Path Parameters:
        - `collection_id` (string): The unique identifier of the collection from which session data is being requested.

        ### Response:
        Returns a STAC ItemCollection containing metadata for each session in the specified collection.
        Each session is represented as a STAC Item, containing key information such as:
        - **Session metadata**: Information about the session's time, satellite, and session ID.

        ### Responses:
        - **200 OK**: If sessions are found, returns the ItemCollection in JSON format.
        - **404 Not Found**: If no matching sessions or collection is found.

        ### Errors:
        - **500 Internal Server Error**: If an error occurs in reading configurations, creating query parameters, or
        processing the session search.

        This endpoint is protected by an API key validator, ensuring appropriate access to the CADIP station.

        Parameters
        ----------
        collection_id : str
            Collection ID

        bbox : typing.Optional[str]
            Bounding box (geospatial footprint or extent, four or six comma-separated numbers).

        datetime : typing.Optional[str]
            Time interval e.g "2024-01-01T00:00:00Z/2024-01-02T23:59:59Z"

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.html

        filter_lang : typing.Optional[GetCadipCollectionItemsCadipCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL2 filter encoding that the 'filter' value uses.

        sortby : typing.Optional[str]
            Sort by +/-fieldName (ascending/descending)

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (between 1000 and 10_000)

        page : typing.Optional[str]
            Page number to be displayed, defaults to first one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cadip_stations.get_cadip_collection_items(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_cadip_collection_items(
            collection_id,
            bbox=bbox,
            datetime=datetime,
            filter=filter,
            filter_lang=filter_lang,
            sortby=sortby,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def get_cadip_collection_item_details(
        self, collection_id: str, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve Detailed Information for a specific session in a collection.

        This endpoint fetches metadata and asset details for a specific session within a collection from the CADIP station.
        Clients can request session details by providing the `collection_id` and `session_id` as path parameters.
        The session data is retrieved and converted from the original OData format into the STAC format,
        which provides standardized metadata for spatiotemporal datasets.

        ### Path Parameters:
        - `collection_id` (string): The unique identifier of the collection from which the session is being retrieved.
        - `session_id` (string): The identifier of the specific session within the collection for which details are
        requested.

        ### Response:
        Returns a STAC Item containing metadata and asset details about the requested session, including:
        - **Session metadata**: Contains important temporal information (e.g., `datetime`, `start_datetime`, and
        `end_datetime`),
          the platform (`platform`), and session-specific details such as `externalIds`, `cadip:num_channels`,
          `cadip:station_id`, `cadip:station_unit_id`, `cadip:antenna_id`, and more.
        - **Satellite information**: Includes satellite attributes such as `sat:absolute_orbit`, `cadip:acquisition_id`, and
        status fields like `cadip:antenna_status_ok`, `cadip:front_end_status_ok`, and `cadip:downlink_status_ok`.
        - **Assets**: A collection of asset objects associated with the session. Each asset contains:
          - A unique asset `href` (link) pointing to the asset resource.
          - Metadata such as `externalIds`, `cadip:retransfer`, `cadip:block_number`, `cadip:channel`,
            `created`, `eviction_datetime`, and `file:size`.
          - Asset `roles`, indicating the type of resource (e.g., "cadu").
          - Asset title and name.

        ### Responses:
        - **200 OK**: If the session details are found, returns the STAC Item in JSON format.
        - **404 Not Found**: If the `session_id` is not found within the specified collection.

        The endpoint is protected by an API key validator, which requires appropriate access permissions.

        Parameters
        ----------
        collection_id : str
            E.G. ins_s1

        session_id : str
            E.G. S1A_20231120061537234567

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cadip_stations.get_cadip_collection_item_details(
            collection_id="collection_id",
            session_id="session_id",
        )
        """
        _response = self._raw_client.get_cadip_collection_item_details(
            collection_id, session_id, request_options=request_options
        )
        return _response.data


class AsyncCadipStationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCadipStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCadipStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCadipStationsClient
        """
        return self._raw_client

    async def search(
        self,
        *,
        collections: typing.Optional[typing.Sequence[str]] = OMIT,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        intersects: typing.Optional[SearchPostRequestIntersects] = OMIT,
        datetime: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        sortby: typing.Optional[typing.Sequence[SortExtension]] = OMIT,
        fields: typing.Optional[PostFieldsExtension] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filter_crs: typing.Optional[str] = OMIT,
        filter_lang: typing.Optional[SearchPostRequestFilterLang] = OMIT,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemCollection:
        """
        Endpoint.

        Parameters
        ----------
        collections : typing.Optional[typing.Sequence[str]]

        ids : typing.Optional[typing.Sequence[str]]

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        intersects : typing.Optional[SearchPostRequestIntersects]

        datetime : typing.Optional[str]

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        conf : typing.Optional[typing.Dict[str, typing.Any]]

        query : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        sortby : typing.Optional[typing.Sequence[SortExtension]]
            An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'

        fields : typing.Optional[PostFieldsExtension]
            Include or exclude fields from items body.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            A CQL filter expression for filtering items.

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[SearchPostRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemCollection
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cadip_stations.search()


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            collections=collections,
            ids=ids,
            bbox=bbox,
            intersects=intersects,
            datetime=datetime,
            limit=limit,
            conf=conf,
            query=query,
            sortby=sortby,
            fields=fields,
            filter=filter,
            filter_crs=filter_crs,
            filter_lang=filter_lang,
            token=token,
            request_options=request_options,
        )
        return _response.data

    async def get_root_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieve the RSPY CADIP Search catalog landing page.

        This endpoint generates a STAC (SpatioTemporal Asset Catalog) Catalog object that serves as the landing
        page for the RSPY CADIP service. The catalog includes basic metadata about the service and links to
        available collections.

        The resulting catalog contains:
        - `id`: A unique identifier for the catalog, generated as a UUID.
        - `description`: A brief description of the catalog.
        - `title`: The title of the catalog.
        - `stac_version`: The version of the STAC specification to which the catalog conforms.
        - `conformsTo`: A list of STAC and OGC API specifications that the catalog conforms to.
        - `links`: A link to the `/cadip/collections` endpoint where users can find available collections.

        The `stac_version` is set to "1.1.0", and the `conformsTo` field lists the relevant STAC and OGC API
        specifications that the catalog adheres to. A link to the collections endpoint is added to the catalog's
        `links` field, allowing users to discover available collections in the CADIP service.

        Parameters:
        - request: The HTTP request object which includes details about the incoming request.

        Returns:
        - dict: A dictionary representation of the STAC catalog, including metadata and links.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cadip_stations.get_root_catalog()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_root_catalog(request_options=request_options)
        return _response.data

    async def get_conformance(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cadip_stations.get_conformance()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conformance(request_options=request_options)
        return _response.data

    async def get_allowed_cadip_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Endpoint to retrieve an object containing collections and links that a user is authorized to
            access based on their API key.

        This endpoint reads the API key from the request to determine the roles associated with the user.
        Using these roles, it identifies the stations the user can access and filters the available collections
        accordingly. The endpoint then constructs a JSON, which includes links to the collections that match the allowed
        stations.

        - It begins by extracting roles from the `request.state.auth_roles` and derives the station names
          the user has access to.
        - Then, it filters the collections from the configuration to include only those belonging to the
          allowed stations.
        - For each filtered collection, a corresponding STAC collection is created with links to detailed
          session searches.

        The final response is a dictionary representation of the STAC catalog, which includes details about
        the collections the user is allowed to access.

        Returns:
            dict: Object containing an array of Collection objects in the Catalog, and Link relations.

        Raises:
            HTTPException: If there are issues with reading configurations or processing session searches.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cadip_stations.get_allowed_cadip_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_allowed_cadip_collections(request_options=request_options)
        return _response.data

    async def get_cadip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCadipCollectionCadipCollectionsCollectionIdGetResponse:
        """
        Retrieve a STAC-Compliant Collection for a Specific CADIP Station.

        This endpoint fetches and returns session data from an external CADIP server, structured as a STAC-compliant
        Collection. By specifying a `collection_id`, the client can retrieve a collection of session metadata related to
        that CADIP station.

        ### Path Parameters:
        - `collection_id` (string): The unique identifier of the CADIP collection to retrieve.

        ### Response:
        The response is a STAC Collection object formatted as a dictionary, which contains links to session details.
        Each session is represented as a link inside the `links` array, following the STAC specification. These links point
         to the detailed metadata for each session.

        ### Key Operations:
        1. **Configuration Lookup**: Reads the relevant configuration from `RSPY_CADIP_SEARCH_CONFIG`.
        2. **CADIP Server Request**: Sends a request to the CADIP server to retrieve session data.
        3. **STAC Formatting**: Transforms the session data into a STAC Collection format.
        4. **Link Creation**: Adds links to session details in the response.

        ### Responses:
        - **200 OK**: Returns the STAC Collection containing links to session metadata. If multiple collections are
        available, returns a list of collections.
        - **422 Unprocessable Entity**: Returns an error if the STAC Collection cannot be created due to missing or invalid
        configuration details.

        ### Raises:
        - **HTTPException**:
          - **422 Unprocessable Entity**: If any configuration data is missing, invalid, or causes an error when creating
          the STAC Collection.

        This endpoint is secured by an API key validator, ensuring that only authorized users can retrieve data from the
        CADIP station.

        Parameters
        ----------
        collection_id : str
            E.G. ins_s1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCadipCollectionCadipCollectionsCollectionIdGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cadip_stations.get_cadip_collection(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cadip_collection(collection_id, request_options=request_options)
        return _response.data

    async def get_cadip_collection_items(
        self,
        collection_id: str,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[
            GetCadipCollectionItemsCadipCollectionsCollectionIdItemsGetRequestFilterLang
        ] = None,
        sortby: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Retrieve a List of items for a specific collection.

        This endpoint provides access to a list of sessions for a given collection from the CADIP station.
        By specifying the `collection_id` in the path, clients can retrieve session metadata in the form of a STAC
        (SpatioTemporal Asset Catalog) ItemCollection.

        ### Path Parameters:
        - `collection_id` (string): The unique identifier of the collection from which session data is being requested.

        ### Response:
        Returns a STAC ItemCollection containing metadata for each session in the specified collection.
        Each session is represented as a STAC Item, containing key information such as:
        - **Session metadata**: Information about the session's time, satellite, and session ID.

        ### Responses:
        - **200 OK**: If sessions are found, returns the ItemCollection in JSON format.
        - **404 Not Found**: If no matching sessions or collection is found.

        ### Errors:
        - **500 Internal Server Error**: If an error occurs in reading configurations, creating query parameters, or
        processing the session search.

        This endpoint is protected by an API key validator, ensuring appropriate access to the CADIP station.

        Parameters
        ----------
        collection_id : str
            Collection ID

        bbox : typing.Optional[str]
            Bounding box (geospatial footprint or extent, four or six comma-separated numbers).

        datetime : typing.Optional[str]
            Time interval e.g "2024-01-01T00:00:00Z/2024-01-02T23:59:59Z"

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.html

        filter_lang : typing.Optional[GetCadipCollectionItemsCadipCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL2 filter encoding that the 'filter' value uses.

        sortby : typing.Optional[str]
            Sort by +/-fieldName (ascending/descending)

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (between 1000 and 10_000)

        page : typing.Optional[str]
            Page number to be displayed, defaults to first one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cadip_stations.get_cadip_collection_items(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cadip_collection_items(
            collection_id,
            bbox=bbox,
            datetime=datetime,
            filter=filter,
            filter_lang=filter_lang,
            sortby=sortby,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def get_cadip_collection_item_details(
        self, collection_id: str, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve Detailed Information for a specific session in a collection.

        This endpoint fetches metadata and asset details for a specific session within a collection from the CADIP station.
        Clients can request session details by providing the `collection_id` and `session_id` as path parameters.
        The session data is retrieved and converted from the original OData format into the STAC format,
        which provides standardized metadata for spatiotemporal datasets.

        ### Path Parameters:
        - `collection_id` (string): The unique identifier of the collection from which the session is being retrieved.
        - `session_id` (string): The identifier of the specific session within the collection for which details are
        requested.

        ### Response:
        Returns a STAC Item containing metadata and asset details about the requested session, including:
        - **Session metadata**: Contains important temporal information (e.g., `datetime`, `start_datetime`, and
        `end_datetime`),
          the platform (`platform`), and session-specific details such as `externalIds`, `cadip:num_channels`,
          `cadip:station_id`, `cadip:station_unit_id`, `cadip:antenna_id`, and more.
        - **Satellite information**: Includes satellite attributes such as `sat:absolute_orbit`, `cadip:acquisition_id`, and
        status fields like `cadip:antenna_status_ok`, `cadip:front_end_status_ok`, and `cadip:downlink_status_ok`.
        - **Assets**: A collection of asset objects associated with the session. Each asset contains:
          - A unique asset `href` (link) pointing to the asset resource.
          - Metadata such as `externalIds`, `cadip:retransfer`, `cadip:block_number`, `cadip:channel`,
            `created`, `eviction_datetime`, and `file:size`.
          - Asset `roles`, indicating the type of resource (e.g., "cadu").
          - Asset title and name.

        ### Responses:
        - **200 OK**: If the session details are found, returns the STAC Item in JSON format.
        - **404 Not Found**: If the `session_id` is not found within the specified collection.

        The endpoint is protected by an API key validator, which requires appropriate access permissions.

        Parameters
        ----------
        collection_id : str
            E.G. ins_s1

        session_id : str
            E.G. S1A_20231120061537234567

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cadip_stations.get_cadip_collection_item_details(
                collection_id="collection_id",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cadip_collection_item_details(
            collection_id, session_id, request_options=request_options
        )
        return _response.data
