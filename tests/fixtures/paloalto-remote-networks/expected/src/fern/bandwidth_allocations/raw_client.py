

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.bandwidth_allocation import BandwidthAllocation
from ..types.bandwidth_allocation_set import BandwidthAllocationSet
from ..types.bandwidth_allocation_set_v2 import BandwidthAllocationSetV2
from ..types.bandwidth_allocation_v2 import BandwidthAllocationV2
from ..types.generic_error import GenericError
from ..types.uuid_response import UuidResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBandwidthAllocationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_v1bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BandwidthAllocationSet]:
        """
        Get the status of aggregated bandwidth regions and allocations, which includes a list of regions and allocations.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BandwidthAllocationSet]
            Aggregated bandwidth regions or allocations set.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BandwidthAllocationSet,
                    parse_obj_as(
                        type_=BandwidthAllocationSet,
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

    def post_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Allocate aggregated bandwidth for the regions based on location data.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocation], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def put_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Modify an aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocation], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def delete_v1bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Allows you to delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "region": region,
                "SpnName": spn_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def get_v1bandwidth_allocations_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BandwidthAllocationSet]:
        """
        Retrieve the bandwidth allocation configurations for a specified set of regions.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BandwidthAllocationSet]
            List of bandwidth allocation configurations.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BandwidthAllocationSet,
                    parse_obj_as(
                        type_=BandwidthAllocationSet,
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

    def post_v1bandwidth_allocations_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocation_region_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Create a request to read bandwidth allocation configuration.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocation_region_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocation_region_names": bandwidth_allocation_region_names,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def get_v2bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BandwidthAllocationSetV2]:
        """
        Get an aggregated bandwidth regions based on the location data.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BandwidthAllocationSetV2]
            Status for the given IS
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BandwidthAllocationSetV2,
                    parse_obj_as(
                        type_=BandwidthAllocationSetV2,
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

    def post_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Status for the given request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocationV2], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def put_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Modify aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocationV2], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def delete_v2bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "region": region,
                "SpnName": spn_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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


class AsyncRawBandwidthAllocationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_v1bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BandwidthAllocationSet]:
        """
        Get the status of aggregated bandwidth regions and allocations, which includes a list of regions and allocations.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BandwidthAllocationSet]
            Aggregated bandwidth regions or allocations set.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BandwidthAllocationSet,
                    parse_obj_as(
                        type_=BandwidthAllocationSet,
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

    async def post_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Allocate aggregated bandwidth for the regions based on location data.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocation], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def put_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Modify an aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocation], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def delete_v1bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Allows you to delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "region": region,
                "SpnName": spn_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def get_v1bandwidth_allocations_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BandwidthAllocationSet]:
        """
        Retrieve the bandwidth allocation configurations for a specified set of regions.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BandwidthAllocationSet]
            List of bandwidth allocation configurations.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BandwidthAllocationSet,
                    parse_obj_as(
                        type_=BandwidthAllocationSet,
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

    async def post_v1bandwidth_allocations_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocation_region_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Create a request to read bandwidth allocation configuration.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocation_region_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/bandwidth-allocations-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocation_region_names": bandwidth_allocation_region_names,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def get_v2bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BandwidthAllocationSetV2]:
        """
        Get an aggregated bandwidth regions based on the location data.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BandwidthAllocationSetV2]
            Status for the given IS
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BandwidthAllocationSetV2,
                    parse_obj_as(
                        type_=BandwidthAllocationSetV2,
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

    async def post_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Status for the given request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocationV2], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def put_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Modify aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "bandwidth_allocations": convert_and_respect_annotation_metadata(
                    object_=bandwidth_allocations, annotation=typing.Sequence[BandwidthAllocationV2], direction="write"
                ),
                "uuid": convert_and_respect_annotation_metadata(
                    object_=uuid_, annotation=UuidResponse, direction="write"
                ),
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def delete_v2bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bandwidth-allocations",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "region": region,
                "SpnName": spn_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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
