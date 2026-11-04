

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collection import Collection
from ..types.collections import Collections
from ..types.conf_classes import ConfClasses
from ..types.landing_page import LandingPage
from .raw_client import AsyncRawCapabilitiesClient, RawCapabilitiesClient


class CapabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCapabilitiesClient
        """
        return self._raw_client

    def get_landing_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> LandingPage:
        """
        The landing page provides links to the API definition, the conformance
        statements and to the feature collections in this dataset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `conformance`), and the Feature
            Collections (path `/collections`, link relation
            `data`).

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.capabilities.get_landing_page()
        """
        _response = self._raw_client.get_landing_page(request_options=request_options)
        return _response.data

    def get_conformance_declaration(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConfClasses:
        """
        A list of all conformance classes specified in a standard that the
        server conforms to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfClasses
            The URIs of all conformance classes supported by the server.

            To support "generic" clients that want to access multiple
            OGC API Features implementations - and not "just" a specific
            API / server, the server declares the conformance
            classes it implements and conforms to.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.capabilities.get_conformance_declaration()
        """
        _response = self._raw_client.get_conformance_declaration(request_options=request_options)
        return _response.data

    def get_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> Collections:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collections
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

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.capabilities.get_collections()
        """
        _response = self._raw_client.get_collections(request_options=request_options)
        return _response.data

    def describe_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
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

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.capabilities.describe_collection(
            collection_id="collectionId",
        )
        """
        _response = self._raw_client.describe_collection(collection_id, request_options=request_options)
        return _response.data


class AsyncCapabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCapabilitiesClient
        """
        return self._raw_client

    async def get_landing_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> LandingPage:
        """
        The landing page provides links to the API definition, the conformance
        statements and to the feature collections in this dataset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `conformance`), and the Feature
            Collections (path `/collections`, link relation
            `data`).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.capabilities.get_landing_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_landing_page(request_options=request_options)
        return _response.data

    async def get_conformance_declaration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfClasses:
        """
        A list of all conformance classes specified in a standard that the
        server conforms to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfClasses
            The URIs of all conformance classes supported by the server.

            To support "generic" clients that want to access multiple
            OGC API Features implementations - and not "just" a specific
            API / server, the server declares the conformance
            classes it implements and conforms to.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.capabilities.get_conformance_declaration()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conformance_declaration(request_options=request_options)
        return _response.data

    async def get_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> Collections:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collections
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

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.capabilities.get_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections(request_options=request_options)
        return _response.data

    async def describe_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
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

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.capabilities.describe_collection(
                collection_id="collectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_collection(collection_id, request_options=request_options)
        return _response.data
