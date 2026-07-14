

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.paginated_image_list import PaginatedImageList
from ..types.paginated_vulnerability_list import PaginatedVulnerabilityList
from ..types.paginated_vulnerable_image_list import PaginatedVulnerableImageList
from .types.query_images_by_vulnerability_request_severity import QueryImagesByVulnerabilityRequestSeverity


class RawQueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[PaginatedImageList]:
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
        HttpResponse[PaginatedImageList]
            Image listing
        """
        _response = self._client_wrapper.httpx_client.request(
            "query/images/by_package",
            method="GET",
            params={
                "name": name,
                "package_type": package_type,
                "version": version,
                "page": page,
                "limit": limit,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedImageList,
                    parse_obj_as(
                        type_=PaginatedImageList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PaginatedVulnerableImageList]:
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
        HttpResponse[PaginatedVulnerableImageList]
            Image lookup success
        """
        _response = self._client_wrapper.httpx_client.request(
            "query/images/by_vulnerability",
            method="GET",
            params={
                "vulnerability_id": vulnerability_id,
                "namespace": namespace,
                "affected_package": affected_package,
                "severity": severity,
                "vendor_only": vendor_only,
                "page": page,
                "limit": limit,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedVulnerableImageList,
                    parse_obj_as(
                        type_=PaginatedVulnerableImageList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PaginatedVulnerabilityList]:
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
        HttpResponse[PaginatedVulnerabilityList]
            Vulnerability listing paginated
        """
        _response = self._client_wrapper.httpx_client.request(
            "query/vulnerabilities",
            method="GET",
            params={
                "id": id,
                "affected_package": affected_package,
                "affected_package_version": affected_package_version,
                "page": page,
                "limit": limit,
                "namespace": namespace,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedVulnerabilityList,
                    parse_obj_as(
                        type_=PaginatedVulnerabilityList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[PaginatedImageList]:
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
        AsyncHttpResponse[PaginatedImageList]
            Image listing
        """
        _response = await self._client_wrapper.httpx_client.request(
            "query/images/by_package",
            method="GET",
            params={
                "name": name,
                "package_type": package_type,
                "version": version,
                "page": page,
                "limit": limit,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedImageList,
                    parse_obj_as(
                        type_=PaginatedImageList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PaginatedVulnerableImageList]:
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
        AsyncHttpResponse[PaginatedVulnerableImageList]
            Image lookup success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "query/images/by_vulnerability",
            method="GET",
            params={
                "vulnerability_id": vulnerability_id,
                "namespace": namespace,
                "affected_package": affected_package,
                "severity": severity,
                "vendor_only": vendor_only,
                "page": page,
                "limit": limit,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedVulnerableImageList,
                    parse_obj_as(
                        type_=PaginatedVulnerableImageList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PaginatedVulnerabilityList]:
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
        AsyncHttpResponse[PaginatedVulnerabilityList]
            Vulnerability listing paginated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "query/vulnerabilities",
            method="GET",
            params={
                "id": id,
                "affected_package": affected_package,
                "affected_package_version": affected_package_version,
                "page": page,
                "limit": limit,
                "namespace": namespace,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedVulnerabilityList,
                    parse_obj_as(
                        type_=PaginatedVulnerabilityList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
