

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.accessibility_request_restriction import AccessibilityRequestRestriction
from ..types.accessibility_response_geo_json import AccessibilityResponseGeoJson
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.area_request import AreaRequest
from ..types.exclusions import Exclusions
from ..types.location import Location
from ..types.vehicle_characteristics import VehicleCharacteristics
from ..types.visiting_window import VisitingWindow
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAccessibilityV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_accessibility_as_geo_json(
        self,
        *,
        area: AreaRequest,
        vehicle: VehicleCharacteristics,
        accept_encoding: typing.Optional[str] = None,
        include_accessible_road_sections: typing.Optional[bool] = OMIT,
        include_inaccessible_road_sections: typing.Optional[bool] = OMIT,
        effectively_accessible: typing.Optional[bool] = OMIT,
        from_: typing.Optional[Location] = OMIT,
        destination: typing.Optional[Location] = OMIT,
        visiting_window: typing.Optional[VisitingWindow] = OMIT,
        exclusions: typing.Optional[Exclusions] = OMIT,
        restrictions: typing.Optional[typing.Sequence[AccessibilityRequestRestriction]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccessibilityResponseGeoJson]:
        """
        Parameters
        ----------
        area : AreaRequest

        vehicle : VehicleCharacteristics

        accept_encoding : typing.Optional[str]
            The HTTP Accept-Encoding request and response header indicates the content encoding (usually a compression algorithm) that the sender can understand.

        include_accessible_road_sections : typing.Optional[bool]
            Directive to include accessible road sections in the response.

        include_inaccessible_road_sections : typing.Optional[bool]
            Directive to include inaccessible road sections in the response.

        effectively_accessible : typing.Optional[bool]
            Effective accessibility means that you can reach the road section segment from at least one direction

        from_ : typing.Optional[Location]

        destination : typing.Optional[Location]

        visiting_window : typing.Optional[VisitingWindow]

        exclusions : typing.Optional[Exclusions]

        restrictions : typing.Optional[typing.Sequence[AccessibilityRequestRestriction]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessibilityResponseGeoJson]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "accessibility.geojson",
            method="POST",
            json={
                "includeAccessibleRoadSections": include_accessible_road_sections,
                "includeInaccessibleRoadSections": include_inaccessible_road_sections,
                "effectivelyAccessible": effectively_accessible,
                "area": convert_and_respect_annotation_metadata(
                    object_=area, annotation=AreaRequest, direction="write"
                ),
                "from": convert_and_respect_annotation_metadata(object_=from_, annotation=Location, direction="write"),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=Location, direction="write"
                ),
                "vehicle": convert_and_respect_annotation_metadata(
                    object_=vehicle, annotation=VehicleCharacteristics, direction="write"
                ),
                "visitingWindow": convert_and_respect_annotation_metadata(
                    object_=visiting_window, annotation=VisitingWindow, direction="write"
                ),
                "exclusions": convert_and_respect_annotation_metadata(
                    object_=exclusions, annotation=Exclusions, direction="write"
                ),
                "restrictions": convert_and_respect_annotation_metadata(
                    object_=restrictions, annotation=typing.Sequence[AccessibilityRequestRestriction], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Accept-Encoding": str(accept_encoding) if accept_encoding is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccessibilityResponseGeoJson,
                    parse_obj_as(
                        type_=AccessibilityResponseGeoJson,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )


class AsyncRawAccessibilityV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_accessibility_as_geo_json(
        self,
        *,
        area: AreaRequest,
        vehicle: VehicleCharacteristics,
        accept_encoding: typing.Optional[str] = None,
        include_accessible_road_sections: typing.Optional[bool] = OMIT,
        include_inaccessible_road_sections: typing.Optional[bool] = OMIT,
        effectively_accessible: typing.Optional[bool] = OMIT,
        from_: typing.Optional[Location] = OMIT,
        destination: typing.Optional[Location] = OMIT,
        visiting_window: typing.Optional[VisitingWindow] = OMIT,
        exclusions: typing.Optional[Exclusions] = OMIT,
        restrictions: typing.Optional[typing.Sequence[AccessibilityRequestRestriction]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccessibilityResponseGeoJson]:
        """
        Parameters
        ----------
        area : AreaRequest

        vehicle : VehicleCharacteristics

        accept_encoding : typing.Optional[str]
            The HTTP Accept-Encoding request and response header indicates the content encoding (usually a compression algorithm) that the sender can understand.

        include_accessible_road_sections : typing.Optional[bool]
            Directive to include accessible road sections in the response.

        include_inaccessible_road_sections : typing.Optional[bool]
            Directive to include inaccessible road sections in the response.

        effectively_accessible : typing.Optional[bool]
            Effective accessibility means that you can reach the road section segment from at least one direction

        from_ : typing.Optional[Location]

        destination : typing.Optional[Location]

        visiting_window : typing.Optional[VisitingWindow]

        exclusions : typing.Optional[Exclusions]

        restrictions : typing.Optional[typing.Sequence[AccessibilityRequestRestriction]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessibilityResponseGeoJson]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accessibility.geojson",
            method="POST",
            json={
                "includeAccessibleRoadSections": include_accessible_road_sections,
                "includeInaccessibleRoadSections": include_inaccessible_road_sections,
                "effectivelyAccessible": effectively_accessible,
                "area": convert_and_respect_annotation_metadata(
                    object_=area, annotation=AreaRequest, direction="write"
                ),
                "from": convert_and_respect_annotation_metadata(object_=from_, annotation=Location, direction="write"),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=Location, direction="write"
                ),
                "vehicle": convert_and_respect_annotation_metadata(
                    object_=vehicle, annotation=VehicleCharacteristics, direction="write"
                ),
                "visitingWindow": convert_and_respect_annotation_metadata(
                    object_=visiting_window, annotation=VisitingWindow, direction="write"
                ),
                "exclusions": convert_and_respect_annotation_metadata(
                    object_=exclusions, annotation=Exclusions, direction="write"
                ),
                "restrictions": convert_and_respect_annotation_metadata(
                    object_=restrictions, annotation=typing.Sequence[AccessibilityRequestRestriction], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Accept-Encoding": str(accept_encoding) if accept_encoding is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccessibilityResponseGeoJson,
                    parse_obj_as(
                        type_=AccessibilityResponseGeoJson,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )
