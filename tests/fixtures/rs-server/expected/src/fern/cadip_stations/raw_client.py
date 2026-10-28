

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.item_collection import ItemCollection
from ..types.post_fields_extension import PostFieldsExtension
from ..types.search_post_request_filter_lang import SearchPostRequestFilterLang
from ..types.search_post_request_intersects import SearchPostRequestIntersects
from ..types.sort_extension import SortExtension
from .types.get_cadip_collection_cadip_collections_collection_id_get_response import (
    GetCadipCollectionCadipCollectionsCollectionIdGetResponse,
)
from .types.get_cadip_collection_items_cadip_collections_collection_id_items_get_request_filter_lang import (
    GetCadipCollectionItemsCadipCollectionsCollectionIdItemsGetRequestFilterLang,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCadipStationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ItemCollection]:
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
        HttpResponse[ItemCollection]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "cadip/search",
            method="POST",
            json={
                "collections": collections,
                "ids": ids,
                "bbox": bbox,
                "intersects": convert_and_respect_annotation_metadata(
                    object_=intersects, annotation=typing.Optional[SearchPostRequestIntersects], direction="write"
                ),
                "datetime": datetime,
                "limit": limit,
                "conf": conf,
                "query": query,
                "sortby": convert_and_respect_annotation_metadata(
                    object_=sortby, annotation=typing.Optional[typing.Sequence[SortExtension]], direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[PostFieldsExtension], direction="write"
                ),
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
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
                    ItemCollection,
                    parse_obj_as(
                        type_=ItemCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_root_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "cadip",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_conformance(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "cadip/conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_allowed_cadip_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
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
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "cadip/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_cadip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCadipCollectionCadipCollectionsCollectionIdGetResponse]:
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
        HttpResponse[GetCadipCollectionCadipCollectionsCollectionIdGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cadip/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCadipCollectionCadipCollectionsCollectionIdGetResponse,
                    parse_obj_as(
                        type_=GetCadipCollectionCadipCollectionsCollectionIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cadip/collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "bbox": bbox,
                "datetime": datetime,
                "filter": filter,
                "filter-lang": filter_lang,
                "sortby": sortby,
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_cadip_collection_item_details(
        self, collection_id: str, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cadip/collections/{encode_path_param(collection_id)}/items/{encode_path_param(session_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCadipStationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ItemCollection]:
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
        AsyncHttpResponse[ItemCollection]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "cadip/search",
            method="POST",
            json={
                "collections": collections,
                "ids": ids,
                "bbox": bbox,
                "intersects": convert_and_respect_annotation_metadata(
                    object_=intersects, annotation=typing.Optional[SearchPostRequestIntersects], direction="write"
                ),
                "datetime": datetime,
                "limit": limit,
                "conf": conf,
                "query": query,
                "sortby": convert_and_respect_annotation_metadata(
                    object_=sortby, annotation=typing.Optional[typing.Sequence[SortExtension]], direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[PostFieldsExtension], direction="write"
                ),
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
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
                    ItemCollection,
                    parse_obj_as(
                        type_=ItemCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_root_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "cadip",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_conformance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "cadip/conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_allowed_cadip_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
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
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "cadip/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_cadip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCadipCollectionCadipCollectionsCollectionIdGetResponse]:
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
        AsyncHttpResponse[GetCadipCollectionCadipCollectionsCollectionIdGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cadip/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCadipCollectionCadipCollectionsCollectionIdGetResponse,
                    parse_obj_as(
                        type_=GetCadipCollectionCadipCollectionsCollectionIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cadip/collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "bbox": bbox,
                "datetime": datetime,
                "filter": filter,
                "filter-lang": filter_lang,
                "sortby": sortby,
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_cadip_collection_item_details(
        self, collection_id: str, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cadip/collections/{encode_path_param(collection_id)}/items/{encode_path_param(session_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
