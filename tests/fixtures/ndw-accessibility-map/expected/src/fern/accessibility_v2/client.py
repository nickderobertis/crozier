

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accessibility_request_restriction import AccessibilityRequestRestriction
from ..types.accessibility_response_geo_json import AccessibilityResponseGeoJson
from ..types.area_request import AreaRequest
from ..types.exclusions import Exclusions
from ..types.location import Location
from ..types.vehicle_characteristics import VehicleCharacteristics
from ..types.visiting_window import VisitingWindow
from .raw_client import AsyncRawAccessibilityV2Client, RawAccessibilityV2Client


OMIT = typing.cast(typing.Any, ...)


class AccessibilityV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccessibilityV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccessibilityV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccessibilityV2Client
        """
        return self._raw_client

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
    ) -> AccessibilityResponseGeoJson:
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
        AccessibilityResponseGeoJson
            OK

        Examples
        --------
        from fern import (
            AreaRequest_Municipality,
            EmissionClass,
            EmissionZoneType,
            Exclusions,
            FernApi,
            FuelType,
            Location,
            VehicleCharacteristics,
            VehicleType,
        )

        client = FernApi()
        client.accessibility_v2.get_accessibility_as_geo_json(
            accept_encoding="gzip",
            area=AreaRequest_Municipality(
                id="GM0344",
            ),
            destination=Location(
                latitude=52.093784,
                longitude=5.15289,
            ),
            vehicle=VehicleCharacteristics(
                type=VehicleType.TRUCK,
                width=2.0,
                height=2.5,
                weight=20.0,
                length=5.2,
                axle_load=4.0,
                has_trailer=False,
                emission_class=EmissionClass.EURO6,
                fuel_types=[FuelType.PETROL],
            ),
            exclusions=Exclusions(
                emission_zone_types=[EmissionZoneType.LOW_EMISSION_ZONE],
                emission_zone_ids=["NDW11_63a0104e-0b70-4b01-ad72-1ec692b41c47"],
            ),
        )
        """
        _response = self._raw_client.get_accessibility_as_geo_json(
            area=area,
            vehicle=vehicle,
            accept_encoding=accept_encoding,
            include_accessible_road_sections=include_accessible_road_sections,
            include_inaccessible_road_sections=include_inaccessible_road_sections,
            effectively_accessible=effectively_accessible,
            from_=from_,
            destination=destination,
            visiting_window=visiting_window,
            exclusions=exclusions,
            restrictions=restrictions,
            request_options=request_options,
        )
        return _response.data


class AsyncAccessibilityV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccessibilityV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccessibilityV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccessibilityV2Client
        """
        return self._raw_client

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
    ) -> AccessibilityResponseGeoJson:
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
        AccessibilityResponseGeoJson
            OK

        Examples
        --------
        import asyncio

        from fern import (
            AreaRequest_Municipality,
            AsyncFernApi,
            EmissionClass,
            EmissionZoneType,
            Exclusions,
            FuelType,
            Location,
            VehicleCharacteristics,
            VehicleType,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.accessibility_v2.get_accessibility_as_geo_json(
                accept_encoding="gzip",
                area=AreaRequest_Municipality(
                    id="GM0344",
                ),
                destination=Location(
                    latitude=52.093784,
                    longitude=5.15289,
                ),
                vehicle=VehicleCharacteristics(
                    type=VehicleType.TRUCK,
                    width=2.0,
                    height=2.5,
                    weight=20.0,
                    length=5.2,
                    axle_load=4.0,
                    has_trailer=False,
                    emission_class=EmissionClass.EURO6,
                    fuel_types=[FuelType.PETROL],
                ),
                exclusions=Exclusions(
                    emission_zone_types=[EmissionZoneType.LOW_EMISSION_ZONE],
                    emission_zone_ids=["NDW11_63a0104e-0b70-4b01-ad72-1ec692b41c47"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accessibility_as_geo_json(
            area=area,
            vehicle=vehicle,
            accept_encoding=accept_encoding,
            include_accessible_road_sections=include_accessible_road_sections,
            include_inaccessible_road_sections=include_inaccessible_road_sections,
            effectively_accessible=effectively_accessible,
            from_=from_,
            destination=destination,
            visiting_window=visiting_window,
            exclusions=exclusions,
            restrictions=restrictions,
            request_options=request_options,
        )
        return _response.data
