

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_image_list import PaginatedImageList
from ..types.paginated_vulnerability_list import PaginatedVulnerabilityList
from ..types.paginated_vulnerable_image_list import PaginatedVulnerableImageList
from .raw_client import AsyncRawQueryClient, RawQueryClient
from .types.query_images_by_vulnerability_request_severity import QueryImagesByVulnerabilityRequestSeverity


class QueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryClient
        """
        return self._raw_client

    def images_by_package(
        self,
        *,
        name: str,
        package_type: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedImageList:
        """
        Filterable query interface to search for images containing specified package

        Parameters
        ----------
        name : str
            Name of package to search for (e.g. sed)

        package_type : typing.Optional[str]
            Type of package to filter on (e.g. dpkg)

        version : typing.Optional[str]
            Version of named package to filter on (e.g. 4.4-1)

        page : typing.Optional[str]
            The page of results to fetch. Pages start at 1

        limit : typing.Optional[int]
            Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageList
            Image listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.query.images_by_package(
            name="name",
        )
        """
        _response = self._raw_client.images_by_package(
            name=name,
            package_type=package_type,
            version=version,
            page=page,
            limit=limit,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    def images_by_vulnerability(
        self,
        *,
        vulnerability_id: str,
        namespace: typing.Optional[str] = None,
        affected_package: typing.Optional[str] = None,
        severity: typing.Optional[QueryImagesByVulnerabilityRequestSeverity] = None,
        vendor_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedVulnerableImageList:
        """
        Returns a listing of images and their respective packages vulnerable to the given vulnerability ID

        Parameters
        ----------
        vulnerability_id : str
            The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001)

        namespace : typing.Optional[str]
            Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04)

        affected_package : typing.Optional[str]
            Filter results to images with vulnable packages with the given package name (e.g. libssl)

        severity : typing.Optional[QueryImagesByVulnerabilityRequestSeverity]
            Filter results to vulnerable package/vulnerability with the given severity

        vendor_only : typing.Optional[bool]
            Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data

        page : typing.Optional[int]
            The page of results to fetch. Pages start at 1

        limit : typing.Optional[int]
            Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedVulnerableImageList
            Image lookup success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.query.images_by_vulnerability(
            vulnerability_id="vulnerability_id",
        )
        """
        _response = self._raw_client.images_by_vulnerability(
            vulnerability_id=vulnerability_id,
            namespace=namespace,
            affected_package=affected_package,
            severity=severity,
            vendor_only=vendor_only,
            page=page,
            limit=limit,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    def vulnerabilities(
        self,
        *,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        affected_package: typing.Optional[str] = None,
        affected_package_version: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        namespace: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedVulnerabilityList:
        """
        List (w/filters) vulnerability records known by the system, with affected packages information if present

        Parameters
        ----------
        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The ID of the vulnerability (e.g. CVE-1999-0001)

        affected_package : typing.Optional[str]
            Filter results by specified package name (e.g. sed)

        affected_package_version : typing.Optional[str]
            Filter results by specified package version (e.g. 4.4-1)

        page : typing.Optional[str]
            The page of results to fetch. Pages start at 1

        limit : typing.Optional[int]
            Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page

        namespace : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Namespace(s) to filter vulnerability records by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedVulnerabilityList
            Vulnerability listing paginated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.query.vulnerabilities(
            id=["id"],
        )
        """
        _response = self._raw_client.vulnerabilities(
            id=id,
            affected_package=affected_package,
            affected_package_version=affected_package_version,
            page=page,
            limit=limit,
            namespace=namespace,
            request_options=request_options,
        )
        return _response.data


class AsyncQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryClient
        """
        return self._raw_client

    async def images_by_package(
        self,
        *,
        name: str,
        package_type: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedImageList:
        """
        Filterable query interface to search for images containing specified package

        Parameters
        ----------
        name : str
            Name of package to search for (e.g. sed)

        package_type : typing.Optional[str]
            Type of package to filter on (e.g. dpkg)

        version : typing.Optional[str]
            Version of named package to filter on (e.g. 4.4-1)

        page : typing.Optional[str]
            The page of results to fetch. Pages start at 1

        limit : typing.Optional[int]
            Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageList
            Image listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query.images_by_package(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.images_by_package(
            name=name,
            package_type=package_type,
            version=version,
            page=page,
            limit=limit,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    async def images_by_vulnerability(
        self,
        *,
        vulnerability_id: str,
        namespace: typing.Optional[str] = None,
        affected_package: typing.Optional[str] = None,
        severity: typing.Optional[QueryImagesByVulnerabilityRequestSeverity] = None,
        vendor_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedVulnerableImageList:
        """
        Returns a listing of images and their respective packages vulnerable to the given vulnerability ID

        Parameters
        ----------
        vulnerability_id : str
            The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001)

        namespace : typing.Optional[str]
            Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04)

        affected_package : typing.Optional[str]
            Filter results to images with vulnable packages with the given package name (e.g. libssl)

        severity : typing.Optional[QueryImagesByVulnerabilityRequestSeverity]
            Filter results to vulnerable package/vulnerability with the given severity

        vendor_only : typing.Optional[bool]
            Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data

        page : typing.Optional[int]
            The page of results to fetch. Pages start at 1

        limit : typing.Optional[int]
            Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedVulnerableImageList
            Image lookup success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query.images_by_vulnerability(
                vulnerability_id="vulnerability_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.images_by_vulnerability(
            vulnerability_id=vulnerability_id,
            namespace=namespace,
            affected_package=affected_package,
            severity=severity,
            vendor_only=vendor_only,
            page=page,
            limit=limit,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    async def vulnerabilities(
        self,
        *,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        affected_package: typing.Optional[str] = None,
        affected_package_version: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        namespace: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedVulnerabilityList:
        """
        List (w/filters) vulnerability records known by the system, with affected packages information if present

        Parameters
        ----------
        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The ID of the vulnerability (e.g. CVE-1999-0001)

        affected_package : typing.Optional[str]
            Filter results by specified package name (e.g. sed)

        affected_package_version : typing.Optional[str]
            Filter results by specified package version (e.g. 4.4-1)

        page : typing.Optional[str]
            The page of results to fetch. Pages start at 1

        limit : typing.Optional[int]
            Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page

        namespace : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Namespace(s) to filter vulnerability records by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedVulnerabilityList
            Vulnerability listing paginated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query.vulnerabilities(
                id=["id"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vulnerabilities(
            id=id,
            affected_package=affected_package,
            affected_package_version=affected_package_version,
            page=page,
            limit=limit,
            namespace=namespace,
            request_options=request_options,
        )
        return _response.data
