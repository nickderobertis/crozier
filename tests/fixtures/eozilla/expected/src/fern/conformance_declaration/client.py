

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conformance_declaration import ConformanceDeclaration
from .raw_client import AsyncRawConformanceDeclarationClient, RawConformanceDeclarationClient


class ConformanceDeclarationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConformanceDeclarationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConformanceDeclarationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConformanceDeclarationClient
        """
        return self._raw_client

    def get_conformance(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConformanceDeclaration:
        """
        A list of all conformance classes, specified in a standard, that the server conforms to.

        | Conformance class | URI |
        |-----------|-------|
        |Core|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core|
        |OGC Process Description|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description|
        |JSON|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json|
        |HTML|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/html|
        |OpenAPI Specification 3.0|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30|
        |Job list|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/job-list|
        |Callback|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/callback|
        |Dismiss|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/dismiss|

        For more information, see [OGC API — Processes — Part 1 Section 7.4](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_conformance_classes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConformanceDeclaration
            The URIs of all conformance classes supported
            by the server. To support "generic" clients that want
            to access multiple OGC API - Processes implementations - and
            not "just" a specific API / server, the server declares
            the conformance classes it implements and conforms to.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conformance_declaration.get_conformance()
        """
        _response = self._raw_client.get_conformance(request_options=request_options)
        return _response.data


class AsyncConformanceDeclarationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConformanceDeclarationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConformanceDeclarationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConformanceDeclarationClient
        """
        return self._raw_client

    async def get_conformance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConformanceDeclaration:
        """
        A list of all conformance classes, specified in a standard, that the server conforms to.

        | Conformance class | URI |
        |-----------|-------|
        |Core|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core|
        |OGC Process Description|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description|
        |JSON|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json|
        |HTML|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/html|
        |OpenAPI Specification 3.0|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30|
        |Job list|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/job-list|
        |Callback|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/callback|
        |Dismiss|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/dismiss|

        For more information, see [OGC API — Processes — Part 1 Section 7.4](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_conformance_classes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConformanceDeclaration
            The URIs of all conformance classes supported
            by the server. To support "generic" clients that want
            to access multiple OGC API - Processes implementations - and
            not "just" a specific API / server, the server declares
            the conformance classes it implements and conforms to.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conformance_declaration.get_conformance()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conformance(request_options=request_options)
        return _response.data
