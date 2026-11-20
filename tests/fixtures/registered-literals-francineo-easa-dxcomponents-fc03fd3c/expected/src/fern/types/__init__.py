



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .authority import Authority
    from .authority_contact_name_item import AuthorityContactNameItem
    from .authority_name_item import AuthorityNameItem
    from .authority_purpose import AuthorityPurpose
    from .authority_service_item import AuthorityServiceItem
    from .bounding_box import BoundingBox
    from .dataset_metadata import DatasetMetadata
    from .dataset_metadata_description import DatasetMetadataDescription
    from .dataset_metadata_provider import DatasetMetadataProvider
    from .dataset_metadata_technical_limitation import DatasetMetadataTechnicalLimitation
    from .feature import Feature
    from .feature_collection import FeatureCollection
    from .feature_collection_type import FeatureCollectionType
    from .feature_type import FeatureType
    from .geo_json_coordinates import GeoJsonCoordinates
    from .oauth_scope import OauthScope
    from .simple_data_models import SimpleDataModels
    from .simple_data_models_code_authority_role import SimpleDataModelsCodeAuthorityRole
    from .simple_data_models_code_daylight_event_type import SimpleDataModelsCodeDaylightEventType
    from .simple_data_models_code_geometry_sub_type import SimpleDataModelsCodeGeometrySubType
    from .simple_data_models_code_vertical_reference_type import SimpleDataModelsCodeVerticalReferenceType
    from .simple_data_models_code_week_day_type import SimpleDataModelsCodeWeekDayType
    from .simple_data_models_code_yes_no_type import SimpleDataModelsCodeYesNoType
    from .simple_data_models_code_zone_reason_type_item import SimpleDataModelsCodeZoneReasonTypeItem
    from .simple_data_models_code_zone_type import SimpleDataModelsCodeZoneType
    from .simple_data_models_code_zone_variant_type import SimpleDataModelsCodeZoneVariantType
    from .simple_data_models_geo_json_geometry_type import SimpleDataModelsGeoJsonGeometryType
    from .simple_data_models_geo_json_geometry_type_five import SimpleDataModelsGeoJsonGeometryTypeFive
    from .simple_data_models_geo_json_geometry_type_five_type import SimpleDataModelsGeoJsonGeometryTypeFiveType
    from .simple_data_models_geo_json_geometry_type_four import SimpleDataModelsGeoJsonGeometryTypeFour
    from .simple_data_models_geo_json_geometry_type_four_type import SimpleDataModelsGeoJsonGeometryTypeFourType
    from .simple_data_models_geo_json_geometry_type_one import SimpleDataModelsGeoJsonGeometryTypeOne
    from .simple_data_models_geo_json_geometry_type_one_type import SimpleDataModelsGeoJsonGeometryTypeOneType
    from .simple_data_models_geo_json_geometry_type_three import SimpleDataModelsGeoJsonGeometryTypeThree
    from .simple_data_models_geo_json_geometry_type_three_type import SimpleDataModelsGeoJsonGeometryTypeThreeType
    from .simple_data_models_geo_json_geometry_type_two import SimpleDataModelsGeoJsonGeometryTypeTwo
    from .simple_data_models_geo_json_geometry_type_two_type import SimpleDataModelsGeoJsonGeometryTypeTwoType
    from .simple_data_models_geo_json_geometry_type_zero import SimpleDataModelsGeoJsonGeometryTypeZero
    from .simple_data_models_geo_json_geometry_type_zero_type import SimpleDataModelsGeoJsonGeometryTypeZeroType
    from .simple_data_models_geometry_collection import SimpleDataModelsGeometryCollection
    from .simple_data_models_geometry_collection_geometries_item import SimpleDataModelsGeometryCollectionGeometriesItem
    from .simple_data_models_geometry_collection_geometries_item_type import (
        SimpleDataModelsGeometryCollectionGeometriesItemType,
    )
    from .simple_data_models_geometry_collection_type import SimpleDataModelsGeometryCollectionType
    from .simple_data_models_line_string import SimpleDataModelsLineString
    from .simple_data_models_line_string_type import SimpleDataModelsLineStringType
    from .simple_data_models_multi_line_string import SimpleDataModelsMultiLineString
    from .simple_data_models_multi_line_string_type import SimpleDataModelsMultiLineStringType
    from .simple_data_models_multi_point import SimpleDataModelsMultiPoint
    from .simple_data_models_multi_point_type import SimpleDataModelsMultiPointType
    from .simple_data_models_multi_polygon import SimpleDataModelsMultiPolygon
    from .simple_data_models_multi_polygon_type import SimpleDataModelsMultiPolygonType
    from .simple_data_models_normal_geometry import SimpleDataModelsNormalGeometry
    from .simple_data_models_normal_geometry_type import SimpleDataModelsNormalGeometryType
    from .simple_data_models_point_with_extent import SimpleDataModelsPointWithExtent
    from .simple_data_models_point_with_extent_type import SimpleDataModelsPointWithExtentType
    from .simple_data_models_polygon import SimpleDataModelsPolygon
    from .simple_data_models_polygon_type import SimpleDataModelsPolygonType
    from .simple_data_models_text_long_type import SimpleDataModelsTextLongType
    from .simple_data_models_text_short_type import SimpleDataModelsTextShortType
    from .simple_data_models_uom_distance import SimpleDataModelsUomDistance
    from .time_period import TimePeriod
    from .uas_zone_version import UasZoneVersion
    from .uas_zone_version_message_item import UasZoneVersionMessageItem
    from .uas_zone_version_name_item import UasZoneVersionNameItem
    from .uas_zone_version_other_reason_info_item import UasZoneVersionOtherReasonInfoItem
    from .uas_zone_version_reason_item import UasZoneVersionReasonItem
    from .uas_zone_version_regulation_exemption import UasZoneVersionRegulationExemption
    from .uas_zone_version_type import UasZoneVersionType
    from .uas_zone_version_variant import UasZoneVersionVariant
_dynamic_imports: typing.Dict[str, str] = {
    "Authority": ".authority",
    "AuthorityContactNameItem": ".authority_contact_name_item",
    "AuthorityNameItem": ".authority_name_item",
    "AuthorityPurpose": ".authority_purpose",
    "AuthorityServiceItem": ".authority_service_item",
    "BoundingBox": ".bounding_box",
    "DatasetMetadata": ".dataset_metadata",
    "DatasetMetadataDescription": ".dataset_metadata_description",
    "DatasetMetadataProvider": ".dataset_metadata_provider",
    "DatasetMetadataTechnicalLimitation": ".dataset_metadata_technical_limitation",
    "Feature": ".feature",
    "FeatureCollection": ".feature_collection",
    "FeatureCollectionType": ".feature_collection_type",
    "FeatureType": ".feature_type",
    "GeoJsonCoordinates": ".geo_json_coordinates",
    "OauthScope": ".oauth_scope",
    "SimpleDataModels": ".simple_data_models",
    "SimpleDataModelsCodeAuthorityRole": ".simple_data_models_code_authority_role",
    "SimpleDataModelsCodeDaylightEventType": ".simple_data_models_code_daylight_event_type",
    "SimpleDataModelsCodeGeometrySubType": ".simple_data_models_code_geometry_sub_type",
    "SimpleDataModelsCodeVerticalReferenceType": ".simple_data_models_code_vertical_reference_type",
    "SimpleDataModelsCodeWeekDayType": ".simple_data_models_code_week_day_type",
    "SimpleDataModelsCodeYesNoType": ".simple_data_models_code_yes_no_type",
    "SimpleDataModelsCodeZoneReasonTypeItem": ".simple_data_models_code_zone_reason_type_item",
    "SimpleDataModelsCodeZoneType": ".simple_data_models_code_zone_type",
    "SimpleDataModelsCodeZoneVariantType": ".simple_data_models_code_zone_variant_type",
    "SimpleDataModelsGeoJsonGeometryType": ".simple_data_models_geo_json_geometry_type",
    "SimpleDataModelsGeoJsonGeometryTypeFive": ".simple_data_models_geo_json_geometry_type_five",
    "SimpleDataModelsGeoJsonGeometryTypeFiveType": ".simple_data_models_geo_json_geometry_type_five_type",
    "SimpleDataModelsGeoJsonGeometryTypeFour": ".simple_data_models_geo_json_geometry_type_four",
    "SimpleDataModelsGeoJsonGeometryTypeFourType": ".simple_data_models_geo_json_geometry_type_four_type",
    "SimpleDataModelsGeoJsonGeometryTypeOne": ".simple_data_models_geo_json_geometry_type_one",
    "SimpleDataModelsGeoJsonGeometryTypeOneType": ".simple_data_models_geo_json_geometry_type_one_type",
    "SimpleDataModelsGeoJsonGeometryTypeThree": ".simple_data_models_geo_json_geometry_type_three",
    "SimpleDataModelsGeoJsonGeometryTypeThreeType": ".simple_data_models_geo_json_geometry_type_three_type",
    "SimpleDataModelsGeoJsonGeometryTypeTwo": ".simple_data_models_geo_json_geometry_type_two",
    "SimpleDataModelsGeoJsonGeometryTypeTwoType": ".simple_data_models_geo_json_geometry_type_two_type",
    "SimpleDataModelsGeoJsonGeometryTypeZero": ".simple_data_models_geo_json_geometry_type_zero",
    "SimpleDataModelsGeoJsonGeometryTypeZeroType": ".simple_data_models_geo_json_geometry_type_zero_type",
    "SimpleDataModelsGeometryCollection": ".simple_data_models_geometry_collection",
    "SimpleDataModelsGeometryCollectionGeometriesItem": ".simple_data_models_geometry_collection_geometries_item",
    "SimpleDataModelsGeometryCollectionGeometriesItemType": ".simple_data_models_geometry_collection_geometries_item_type",
    "SimpleDataModelsGeometryCollectionType": ".simple_data_models_geometry_collection_type",
    "SimpleDataModelsLineString": ".simple_data_models_line_string",
    "SimpleDataModelsLineStringType": ".simple_data_models_line_string_type",
    "SimpleDataModelsMultiLineString": ".simple_data_models_multi_line_string",
    "SimpleDataModelsMultiLineStringType": ".simple_data_models_multi_line_string_type",
    "SimpleDataModelsMultiPoint": ".simple_data_models_multi_point",
    "SimpleDataModelsMultiPointType": ".simple_data_models_multi_point_type",
    "SimpleDataModelsMultiPolygon": ".simple_data_models_multi_polygon",
    "SimpleDataModelsMultiPolygonType": ".simple_data_models_multi_polygon_type",
    "SimpleDataModelsNormalGeometry": ".simple_data_models_normal_geometry",
    "SimpleDataModelsNormalGeometryType": ".simple_data_models_normal_geometry_type",
    "SimpleDataModelsPointWithExtent": ".simple_data_models_point_with_extent",
    "SimpleDataModelsPointWithExtentType": ".simple_data_models_point_with_extent_type",
    "SimpleDataModelsPolygon": ".simple_data_models_polygon",
    "SimpleDataModelsPolygonType": ".simple_data_models_polygon_type",
    "SimpleDataModelsTextLongType": ".simple_data_models_text_long_type",
    "SimpleDataModelsTextShortType": ".simple_data_models_text_short_type",
    "SimpleDataModelsUomDistance": ".simple_data_models_uom_distance",
    "TimePeriod": ".time_period",
    "UasZoneVersion": ".uas_zone_version",
    "UasZoneVersionMessageItem": ".uas_zone_version_message_item",
    "UasZoneVersionNameItem": ".uas_zone_version_name_item",
    "UasZoneVersionOtherReasonInfoItem": ".uas_zone_version_other_reason_info_item",
    "UasZoneVersionReasonItem": ".uas_zone_version_reason_item",
    "UasZoneVersionRegulationExemption": ".uas_zone_version_regulation_exemption",
    "UasZoneVersionType": ".uas_zone_version_type",
    "UasZoneVersionVariant": ".uas_zone_version_variant",
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
    "Authority",
    "AuthorityContactNameItem",
    "AuthorityNameItem",
    "AuthorityPurpose",
    "AuthorityServiceItem",
    "BoundingBox",
    "DatasetMetadata",
    "DatasetMetadataDescription",
    "DatasetMetadataProvider",
    "DatasetMetadataTechnicalLimitation",
    "Feature",
    "FeatureCollection",
    "FeatureCollectionType",
    "FeatureType",
    "GeoJsonCoordinates",
    "OauthScope",
    "SimpleDataModels",
    "SimpleDataModelsCodeAuthorityRole",
    "SimpleDataModelsCodeDaylightEventType",
    "SimpleDataModelsCodeGeometrySubType",
    "SimpleDataModelsCodeVerticalReferenceType",
    "SimpleDataModelsCodeWeekDayType",
    "SimpleDataModelsCodeYesNoType",
    "SimpleDataModelsCodeZoneReasonTypeItem",
    "SimpleDataModelsCodeZoneType",
    "SimpleDataModelsCodeZoneVariantType",
    "SimpleDataModelsGeoJsonGeometryType",
    "SimpleDataModelsGeoJsonGeometryTypeFive",
    "SimpleDataModelsGeoJsonGeometryTypeFiveType",
    "SimpleDataModelsGeoJsonGeometryTypeFour",
    "SimpleDataModelsGeoJsonGeometryTypeFourType",
    "SimpleDataModelsGeoJsonGeometryTypeOne",
    "SimpleDataModelsGeoJsonGeometryTypeOneType",
    "SimpleDataModelsGeoJsonGeometryTypeThree",
    "SimpleDataModelsGeoJsonGeometryTypeThreeType",
    "SimpleDataModelsGeoJsonGeometryTypeTwo",
    "SimpleDataModelsGeoJsonGeometryTypeTwoType",
    "SimpleDataModelsGeoJsonGeometryTypeZero",
    "SimpleDataModelsGeoJsonGeometryTypeZeroType",
    "SimpleDataModelsGeometryCollection",
    "SimpleDataModelsGeometryCollectionGeometriesItem",
    "SimpleDataModelsGeometryCollectionGeometriesItemType",
    "SimpleDataModelsGeometryCollectionType",
    "SimpleDataModelsLineString",
    "SimpleDataModelsLineStringType",
    "SimpleDataModelsMultiLineString",
    "SimpleDataModelsMultiLineStringType",
    "SimpleDataModelsMultiPoint",
    "SimpleDataModelsMultiPointType",
    "SimpleDataModelsMultiPolygon",
    "SimpleDataModelsMultiPolygonType",
    "SimpleDataModelsNormalGeometry",
    "SimpleDataModelsNormalGeometryType",
    "SimpleDataModelsPointWithExtent",
    "SimpleDataModelsPointWithExtentType",
    "SimpleDataModelsPolygon",
    "SimpleDataModelsPolygonType",
    "SimpleDataModelsTextLongType",
    "SimpleDataModelsTextShortType",
    "SimpleDataModelsUomDistance",
    "TimePeriod",
    "UasZoneVersion",
    "UasZoneVersionMessageItem",
    "UasZoneVersionNameItem",
    "UasZoneVersionOtherReasonInfoItem",
    "UasZoneVersionReasonItem",
    "UasZoneVersionRegulationExemption",
    "UasZoneVersionType",
    "UasZoneVersionVariant",
]
