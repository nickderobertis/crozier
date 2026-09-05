

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
from ..types.generic_error import GenericError
from ..types.location import Location
from ..types.location_information_response import LocationInformationResponse
from ..types.uuid_response import UuidResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLocationInformationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_v1location_informations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LocationInformationResponse]:
        """
        Get the location information status of the given request ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LocationInformationResponse]
            List of location mapped information and configurations.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/location-informations",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LocationInformationResponse,
                    parse_obj_as(
                        type_=LocationInformationResponse,
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

    def post_v1location_informations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        info_type: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Retrieve location-mapped information or configuration through a POST request and returns the request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        info_type : typing.Optional[str]
            Information type. For example, region information.

        description : typing.Optional[str]
            optional user description

        locations : typing.Optional[typing.Sequence[Location]]
            locations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/location-informations",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
                "info_type": info_type,
            },
            json={
                "description": description,
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
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


class AsyncRawLocationInformationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_v1location_informations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LocationInformationResponse]:
        """
        Get the location information status of the given request ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LocationInformationResponse]
            List of location mapped information and configurations.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/location-informations",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LocationInformationResponse,
                    parse_obj_as(
                        type_=LocationInformationResponse,
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

    async def post_v1location_informations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        info_type: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Retrieve location-mapped information or configuration through a POST request and returns the request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        info_type : typing.Optional[str]
            Information type. For example, region information.

        description : typing.Optional[str]
            optional user description

        locations : typing.Optional[typing.Sequence[Location]]
            locations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/location-informations",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
                "info_type": info_type,
            },
            json={
                "description": description,
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
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
