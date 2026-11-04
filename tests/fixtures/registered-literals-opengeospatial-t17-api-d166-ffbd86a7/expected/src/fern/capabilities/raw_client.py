

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.collection import Collection
from ..types.collections import Collections
from ..types.conf_classes import ConfClasses
from ..types.exception import Exception
from ..types.landing_page import LandingPage
from pydantic import ValidationError


class RawCapabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_landing_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[LandingPage]:
        """
        The landing page provides links to the API definition, the conformance
        statements and to the feature collections in this dataset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LandingPage]
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `conformance`), and the Feature
            Collections (path `/collections`, link relation
            `data`).
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LandingPage,
                    parse_obj_as(
                        type_=LandingPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    def get_conformance_declaration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfClasses]:
        """
        A list of all conformance classes specified in a standard that the
        server conforms to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfClasses]
            The URIs of all conformance classes supported by the server.

            To support "generic" clients that want to access multiple
            OGC API Features implementations - and not "just" a specific
            API / server, the server declares the conformance
            classes it implements and conforms to.
        """
        _response = self._client_wrapper.httpx_client.request(
            "conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfClasses,
                    parse_obj_as(
                        type_=ConfClasses,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    def get_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Collections]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collections]
            The feature collections shared by this API.

            The dataset is organized as one or more feature collections. This resource
            provides information about and access to the collections.

            The response contains the list of collections. For each collection, a link
            to the items in the collection (path `/collections/{collectionId}/items`,
            link relation `items`) as well as key information about the collection.
            This information includes:

            * A local identifier for the collection that is unique for the dataset;
            * A list of coordinate reference systems (CRS) in which geometries may be returned by the server. The first CRS is the default coordinate reference system (the default is always WGS 84 with axis order longitude/latitude);
            * An optional title and description for the collection;
            * An optional extent that can be used to provide an indication of the spatial and temporal extent of the collection - typically derived from the data;
            * An optional indicator about the type of the items in the collection (the default value, if the indicator is not provided, is 'feature').
        """
        _response = self._client_wrapper.httpx_client.request(
            "collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collections,
                    parse_obj_as(
                        type_=Collections,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    def describe_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Collection]:
        """
        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Information about the feature collection with id `collectionId`.

            The response contains a link to the items in the collection
            (path `/collections/{collectionId}/items`, link relation `items`)
            as well as key information about the collection. This information
            includes:

            * A local identifier for the collection that is unique for the dataset;
            * A list of coordinate reference systems (CRS) in which geometries may be returned by the server. The first CRS is the default coordinate reference system (the default is always WGS 84 with axis order longitude/latitude);
            * An optional title and description for the collection;
            * An optional extent that can be used to provide an indication of the spatial and temporal extent of the collection - typically derived from the data;
            * An optional indicator about the type of the items in the collection (the default value, if the indicator is not provided, is 'feature').
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}",
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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


class AsyncRawCapabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_landing_page(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LandingPage]:
        """
        The landing page provides links to the API definition, the conformance
        statements and to the feature collections in this dataset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LandingPage]
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `conformance`), and the Feature
            Collections (path `/collections`, link relation
            `data`).
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LandingPage,
                    parse_obj_as(
                        type_=LandingPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    async def get_conformance_declaration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfClasses]:
        """
        A list of all conformance classes specified in a standard that the
        server conforms to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfClasses]
            The URIs of all conformance classes supported by the server.

            To support "generic" clients that want to access multiple
            OGC API Features implementations - and not "just" a specific
            API / server, the server declares the conformance
            classes it implements and conforms to.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfClasses,
                    parse_obj_as(
                        type_=ConfClasses,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    async def get_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Collections]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collections]
            The feature collections shared by this API.

            The dataset is organized as one or more feature collections. This resource
            provides information about and access to the collections.

            The response contains the list of collections. For each collection, a link
            to the items in the collection (path `/collections/{collectionId}/items`,
            link relation `items`) as well as key information about the collection.
            This information includes:

            * A local identifier for the collection that is unique for the dataset;
            * A list of coordinate reference systems (CRS) in which geometries may be returned by the server. The first CRS is the default coordinate reference system (the default is always WGS 84 with axis order longitude/latitude);
            * An optional title and description for the collection;
            * An optional extent that can be used to provide an indication of the spatial and temporal extent of the collection - typically derived from the data;
            * An optional indicator about the type of the items in the collection (the default value, if the indicator is not provided, is 'feature').
        """
        _response = await self._client_wrapper.httpx_client.request(
            "collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collections,
                    parse_obj_as(
                        type_=Collections,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    async def describe_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Collection]:
        """
        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Information about the feature collection with id `collectionId`.

            The response contains a link to the items in the collection
            (path `/collections/{collectionId}/items`, link relation `items`)
            as well as key information about the collection. This information
            includes:

            * A local identifier for the collection that is unique for the dataset;
            * A list of coordinate reference systems (CRS) in which geometries may be returned by the server. The first CRS is the default coordinate reference system (the default is always WGS 84 with axis order longitude/latitude);
            * An optional title and description for the collection;
            * An optional extent that can be used to provide an indication of the spatial and temporal extent of the collection - typically derived from the data;
            * An optional indicator about the type of the items in the collection (the default value, if the indicator is not provided, is 'feature').
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}",
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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
