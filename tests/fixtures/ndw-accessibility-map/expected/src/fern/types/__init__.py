



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accessibility_request_restriction import (
        AccessibilityRequestRestriction,
        AccessibilityRequestRestriction_RoadSection,
    )
    from .accessibility_request_road_section_restriction import AccessibilityRequestRoadSectionRestriction
    from .accessibility_response_geo_json import AccessibilityResponseGeoJson
    from .accessible import Accessible
    from .accessible_reason import AccessibleReason
    from .api_error import ApiError
    from .area_request import AreaRequest, AreaRequest_BoundingBox, AreaRequest_Municipality
    from .bounding_box import BoundingBox
    from .bounding_box_area_request import BoundingBoxAreaRequest
    from .delay_in_milli_seconds_because_of_restrictions import DelayInMilliSecondsBecauseOfRestrictions
    from .destination_feature_properties import DestinationFeatureProperties
    from .direction import Direction
    from .emission_class import EmissionClass
    from .emission_zone_type import EmissionZoneType
    from .exclusions import Exclusions
    from .feature import Feature
    from .feature_collection import FeatureCollection
    from .feature_collection_type import FeatureCollectionType
    from .feature_properties import (
        FeatureProperties,
        FeatureProperties_Destination,
        FeatureProperties_RoadSectionSegment,
        FeatureProperties_Unknown,
    )
    from .feature_type import FeatureType
    from .fraction import Fraction
    from .fuel_type import FuelType
    from .fuel_type_reason import FuelTypeReason
    from .functional_road_class import FunctionalRoadClass
    from .latitude import Latitude
    from .location import Location
    from .longitude import Longitude
    from .municipality_area_request import MunicipalityAreaRequest
    from .municipality_feature import MunicipalityFeature
    from .municipality_feature_collection import MunicipalityFeatureCollection
    from .municipality_properties import MunicipalityProperties
    from .reason import (
        Reason,
        Reason_AccessibleReason,
        Reason_FuelTypeReason,
        Reason_Unknown,
        Reason_VehicleAxleWeightReason,
        Reason_VehicleHeightReason,
        Reason_VehicleLengthReason,
        Reason_VehicleTypeReason,
        Reason_VehicleWeightReason,
        Reason_VehicleWidthReason,
    )
    from .reason_condition import ReasonCondition
    from .reason_unit_symbol import ReasonUnitSymbol
    from .restriction import Restriction, Restriction_RoadSection, Restriction_TrafficSign
    from .road_operator import RoadOperator
    from .road_operator_road_operator_type import RoadOperatorRoadOperatorType
    from .road_operators import RoadOperators
    from .road_section_id import RoadSectionId
    from .road_section_restriction import RoadSectionRestriction
    from .road_section_segment_feature_properties import RoadSectionSegmentFeatureProperties
    from .traffic_sign_id import TrafficSignId
    from .traffic_sign_restriction import TrafficSignRestriction
    from .traffic_sign_type import TrafficSignType
    from .vehicle_axle_weight_reason import VehicleAxleWeightReason
    from .vehicle_characteristics import VehicleCharacteristics
    from .vehicle_height_reason import VehicleHeightReason
    from .vehicle_length_reason import VehicleLengthReason
    from .vehicle_type import VehicleType
    from .vehicle_type_reason import VehicleTypeReason
    from .vehicle_weight_reason import VehicleWeightReason
    from .vehicle_width_reason import VehicleWidthReason
    from .visiting_window import VisitingWindow
_dynamic_imports: typing.Dict[str, str] = {
    "AccessibilityRequestRestriction": ".accessibility_request_restriction",
    "AccessibilityRequestRestriction_RoadSection": ".accessibility_request_restriction",
    "AccessibilityRequestRoadSectionRestriction": ".accessibility_request_road_section_restriction",
    "AccessibilityResponseGeoJson": ".accessibility_response_geo_json",
    "Accessible": ".accessible",
    "AccessibleReason": ".accessible_reason",
    "ApiError": ".api_error",
    "AreaRequest": ".area_request",
    "AreaRequest_BoundingBox": ".area_request",
    "AreaRequest_Municipality": ".area_request",
    "BoundingBox": ".bounding_box",
    "BoundingBoxAreaRequest": ".bounding_box_area_request",
    "DelayInMilliSecondsBecauseOfRestrictions": ".delay_in_milli_seconds_because_of_restrictions",
    "DestinationFeatureProperties": ".destination_feature_properties",
    "Direction": ".direction",
    "EmissionClass": ".emission_class",
    "EmissionZoneType": ".emission_zone_type",
    "Exclusions": ".exclusions",
    "Feature": ".feature",
    "FeatureCollection": ".feature_collection",
    "FeatureCollectionType": ".feature_collection_type",
    "FeatureProperties": ".feature_properties",
    "FeatureProperties_Destination": ".feature_properties",
    "FeatureProperties_RoadSectionSegment": ".feature_properties",
    "FeatureProperties_Unknown": ".feature_properties",
    "FeatureType": ".feature_type",
    "Fraction": ".fraction",
    "FuelType": ".fuel_type",
    "FuelTypeReason": ".fuel_type_reason",
    "FunctionalRoadClass": ".functional_road_class",
    "Latitude": ".latitude",
    "Location": ".location",
    "Longitude": ".longitude",
    "MunicipalityAreaRequest": ".municipality_area_request",
    "MunicipalityFeature": ".municipality_feature",
    "MunicipalityFeatureCollection": ".municipality_feature_collection",
    "MunicipalityProperties": ".municipality_properties",
    "Reason": ".reason",
    "ReasonCondition": ".reason_condition",
    "ReasonUnitSymbol": ".reason_unit_symbol",
    "Reason_AccessibleReason": ".reason",
    "Reason_FuelTypeReason": ".reason",
    "Reason_Unknown": ".reason",
    "Reason_VehicleAxleWeightReason": ".reason",
    "Reason_VehicleHeightReason": ".reason",
    "Reason_VehicleLengthReason": ".reason",
    "Reason_VehicleTypeReason": ".reason",
    "Reason_VehicleWeightReason": ".reason",
    "Reason_VehicleWidthReason": ".reason",
    "Restriction": ".restriction",
    "Restriction_RoadSection": ".restriction",
    "Restriction_TrafficSign": ".restriction",
    "RoadOperator": ".road_operator",
    "RoadOperatorRoadOperatorType": ".road_operator_road_operator_type",
    "RoadOperators": ".road_operators",
    "RoadSectionId": ".road_section_id",
    "RoadSectionRestriction": ".road_section_restriction",
    "RoadSectionSegmentFeatureProperties": ".road_section_segment_feature_properties",
    "TrafficSignId": ".traffic_sign_id",
    "TrafficSignRestriction": ".traffic_sign_restriction",
    "TrafficSignType": ".traffic_sign_type",
    "VehicleAxleWeightReason": ".vehicle_axle_weight_reason",
    "VehicleCharacteristics": ".vehicle_characteristics",
    "VehicleHeightReason": ".vehicle_height_reason",
    "VehicleLengthReason": ".vehicle_length_reason",
    "VehicleType": ".vehicle_type",
    "VehicleTypeReason": ".vehicle_type_reason",
    "VehicleWeightReason": ".vehicle_weight_reason",
    "VehicleWidthReason": ".vehicle_width_reason",
    "VisitingWindow": ".visiting_window",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AccessibilityRequestRestriction",
    "AccessibilityRequestRestriction_RoadSection",
    "AccessibilityRequestRoadSectionRestriction",
    "AccessibilityResponseGeoJson",
    "Accessible",
    "AccessibleReason",
    "ApiError",
    "AreaRequest",
    "AreaRequest_BoundingBox",
    "AreaRequest_Municipality",
    "BoundingBox",
    "BoundingBoxAreaRequest",
    "DelayInMilliSecondsBecauseOfRestrictions",
    "DestinationFeatureProperties",
    "Direction",
    "EmissionClass",
    "EmissionZoneType",
    "Exclusions",
    "Feature",
    "FeatureCollection",
    "FeatureCollectionType",
    "FeatureProperties",
    "FeatureProperties_Destination",
    "FeatureProperties_RoadSectionSegment",
    "FeatureProperties_Unknown",
    "FeatureType",
    "Fraction",
    "FuelType",
    "FuelTypeReason",
    "FunctionalRoadClass",
    "Latitude",
    "Location",
    "Longitude",
    "MunicipalityAreaRequest",
    "MunicipalityFeature",
    "MunicipalityFeatureCollection",
    "MunicipalityProperties",
    "Reason",
    "ReasonCondition",
    "ReasonUnitSymbol",
    "Reason_AccessibleReason",
    "Reason_FuelTypeReason",
    "Reason_Unknown",
    "Reason_VehicleAxleWeightReason",
    "Reason_VehicleHeightReason",
    "Reason_VehicleLengthReason",
    "Reason_VehicleTypeReason",
    "Reason_VehicleWeightReason",
    "Reason_VehicleWidthReason",
    "Restriction",
    "Restriction_RoadSection",
    "Restriction_TrafficSign",
    "RoadOperator",
    "RoadOperatorRoadOperatorType",
    "RoadOperators",
    "RoadSectionId",
    "RoadSectionRestriction",
    "RoadSectionSegmentFeatureProperties",
    "TrafficSignId",
    "TrafficSignRestriction",
    "TrafficSignType",
    "VehicleAxleWeightReason",
    "VehicleCharacteristics",
    "VehicleHeightReason",
    "VehicleLengthReason",
    "VehicleType",
    "VehicleTypeReason",
    "VehicleWeightReason",
    "VehicleWidthReason",
    "VisitingWindow",
]
