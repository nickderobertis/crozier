



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .asset import Asset
    from .bulk_transaction_method import BulkTransactionMethod
    from .bulk_transaction_model import BulkTransactionModel
    from .collection import Collection
    from .collection_input import CollectionInput
    from .collection_input_summaries_value import CollectionInputSummariesValue
    from .collection_input_type import CollectionInputType
    from .collection_summaries_value import CollectionSummariesValue
    from .collection_type import CollectionType
    from .collections import Collections
    from .conformance import Conformance
    from .extent import Extent
    from .feature import Feature
    from .feature_bbox_item import FeatureBboxItem
    from .feature_collection_model import FeatureCollectionModel
    from .geometry_collection_input import GeometryCollectionInput
    from .geometry_collection_input_geometries_item import (
        GeometryCollectionInputGeometriesItem,
        GeometryCollectionInputGeometriesItem_GeometryCollection,
        GeometryCollectionInputGeometriesItem_LineString,
        GeometryCollectionInputGeometriesItem_MultiLineString,
        GeometryCollectionInputGeometriesItem_MultiPoint,
        GeometryCollectionInputGeometriesItem_MultiPolygon,
        GeometryCollectionInputGeometriesItem_Point,
        GeometryCollectionInputGeometriesItem_Polygon,
    )
    from .geometry_collection_input_type import GeometryCollectionInputType
    from .geometry_collection_output import GeometryCollectionOutput
    from .geometry_collection_output_geometries_item import (
        GeometryCollectionOutputGeometriesItem,
        GeometryCollectionOutputGeometriesItem_GeometryCollection,
        GeometryCollectionOutputGeometriesItem_LineString,
        GeometryCollectionOutputGeometriesItem_MultiLineString,
        GeometryCollectionOutputGeometriesItem_MultiPoint,
        GeometryCollectionOutputGeometriesItem_MultiPolygon,
        GeometryCollectionOutputGeometriesItem_Point,
        GeometryCollectionOutputGeometriesItem_Polygon,
    )
    from .health_check import HealthCheck
    from .health_check_status import HealthCheckStatus
    from .http_validation_error import HttpValidationError
    from .input_model import InputModel
    from .item import Item
    from .item_collection import ItemCollection
    from .item_collection_input import ItemCollectionInput
    from .item_collection_output import ItemCollectionOutput
    from .item_collection_output_type import ItemCollectionOutputType
    from .item_collection_type import ItemCollectionType
    from .item_geometry import (
        ItemGeometry,
        ItemGeometry_GeometryCollection,
        ItemGeometry_LineString,
        ItemGeometry_MultiLineString,
        ItemGeometry_MultiPoint,
        ItemGeometry_MultiPolygon,
        ItemGeometry_Point,
        ItemGeometry_Polygon,
    )
    from .item_input import ItemInput
    from .item_input_geometry import (
        ItemInputGeometry,
        ItemInputGeometry_GeometryCollection,
        ItemInputGeometry_LineString,
        ItemInputGeometry_MultiLineString,
        ItemInputGeometry_MultiPoint,
        ItemInputGeometry_MultiPolygon,
        ItemInputGeometry_Point,
        ItemInputGeometry_Polygon,
    )
    from .item_input_type import ItemInputType
    from .item_properties import ItemProperties
    from .item_type import ItemType
    from .items_link import ItemsLink
    from .items_link_method import ItemsLinkMethod
    from .items_link_rel import ItemsLinkRel
    from .items_link_type import ItemsLinkType
    from .items_model import ItemsModel
    from .items_model_value import ItemsModelValue
    from .landing_page import LandingPage
    from .landing_page_type import LandingPageType
    from .line_string import LineString
    from .line_string_coordinates_item import LineStringCoordinatesItem
    from .line_string_type import LineStringType
    from .link import Link
    from .link_type import LinkType
    from .links import Links
    from .links_input import LinksInput
    from .mime_types import MimeTypes
    from .multi_line_string import MultiLineString
    from .multi_line_string_coordinates_item_item import MultiLineStringCoordinatesItemItem
    from .multi_line_string_type import MultiLineStringType
    from .multi_point import MultiPoint
    from .multi_point_coordinates_item import MultiPointCoordinatesItem
    from .multi_point_type import MultiPointType
    from .multi_polygon import MultiPolygon
    from .multi_polygon_coordinates_item_item_item import MultiPolygonCoordinatesItemItemItem
    from .multi_polygon_type import MultiPolygonType
    from .operator import Operator
    from .pagination_link import PaginationLink
    from .pagination_link_method import PaginationLinkMethod
    from .pagination_link_rel import PaginationLinkRel
    from .pagination_link_type import PaginationLinkType
    from .partial_collection import PartialCollection
    from .partial_item import PartialItem
    from .partial_item_type import PartialItemType
    from .patch_add_replace_test import PatchAddReplaceTest
    from .patch_add_replace_test_op import PatchAddReplaceTestOp
    from .patch_move_copy import PatchMoveCopy
    from .patch_move_copy_op import PatchMoveCopyOp
    from .patch_remove import PatchRemove
    from .patch_remove_op import PatchRemoveOp
    from .point import Point
    from .point_coordinates import PointCoordinates
    from .point_type import PointType
    from .polygon import Polygon
    from .polygon_coordinates_item_item import PolygonCoordinatesItemItem
    from .polygon_type import PolygonType
    from .position2d import Position2D
    from .position3d import Position3D
    from .post_fields_extension import PostFieldsExtension
    from .provider import Provider
    from .range import Range
    from .range_maximum import RangeMaximum
    from .range_minimum import RangeMinimum
    from .search_link import SearchLink
    from .search_link_method import SearchLinkMethod
    from .search_link_rel import SearchLinkRel
    from .search_link_type import SearchLinkType
    from .search_post_request import SearchPostRequest
    from .search_post_request_filter_lang import SearchPostRequestFilterLang
    from .search_post_request_intersects import SearchPostRequestIntersects
    from .sort_directions import SortDirections
    from .sort_extension import SortExtension
    from .sortables_schema import SortablesSchema
    from .spatial_extent import SpatialExtent
    from .stac_pydantic_api_collection_collection import StacPydanticApiCollectionCollection
    from .stac_pydantic_api_collection_collection_summaries_value import (
        StacPydanticApiCollectionCollectionSummariesValue,
    )
    from .stac_pydantic_api_collection_collection_type import StacPydanticApiCollectionCollectionType
    from .stac_pydantic_api_item_item import StacPydanticApiItemItem
    from .stac_pydantic_api_item_item_geometry import (
        StacPydanticApiItemItemGeometry,
        StacPydanticApiItemItemGeometry_GeometryCollection,
        StacPydanticApiItemItemGeometry_LineString,
        StacPydanticApiItemItemGeometry_MultiLineString,
        StacPydanticApiItemItemGeometry_MultiPoint,
        StacPydanticApiItemItemGeometry_MultiPolygon,
        StacPydanticApiItemItemGeometry_Point,
        StacPydanticApiItemItemGeometry_Polygon,
    )
    from .stac_pydantic_api_item_item_type import StacPydanticApiItemItemType
    from .stac_pydantic_api_links_links import StacPydanticApiLinksLinks
    from .stac_pydantic_api_links_links_item import StacPydanticApiLinksLinksItem
    from .stac_pydantic_collection_collection_output import StacPydanticCollectionCollectionOutput
    from .stac_pydantic_collection_collection_output_summaries_value import (
        StacPydanticCollectionCollectionOutputSummariesValue,
    )
    from .stac_pydantic_collection_collection_output_type import StacPydanticCollectionCollectionOutputType
    from .stac_pydantic_item_item_output import StacPydanticItemItemOutput
    from .stac_pydantic_item_item_output_geometry import (
        StacPydanticItemItemOutputGeometry,
        StacPydanticItemItemOutputGeometry_GeometryCollection,
        StacPydanticItemItemOutputGeometry_LineString,
        StacPydanticItemItemOutputGeometry_MultiLineString,
        StacPydanticItemItemOutputGeometry_MultiPoint,
        StacPydanticItemItemOutputGeometry_MultiPolygon,
        StacPydanticItemItemOutputGeometry_Point,
        StacPydanticItemItemOutputGeometry_Polygon,
    )
    from .stac_pydantic_item_item_output_type import StacPydanticItemItemOutputType
    from .stac_pydantic_links_links import StacPydanticLinksLinks
    from .time_interval import TimeInterval
    from .transaction_error_model import TransactionErrorModel
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "Asset": ".asset",
    "BulkTransactionMethod": ".bulk_transaction_method",
    "BulkTransactionModel": ".bulk_transaction_model",
    "Collection": ".collection",
    "CollectionInput": ".collection_input",
    "CollectionInputSummariesValue": ".collection_input_summaries_value",
    "CollectionInputType": ".collection_input_type",
    "CollectionSummariesValue": ".collection_summaries_value",
    "CollectionType": ".collection_type",
    "Collections": ".collections",
    "Conformance": ".conformance",
    "Extent": ".extent",
    "Feature": ".feature",
    "FeatureBboxItem": ".feature_bbox_item",
    "FeatureCollectionModel": ".feature_collection_model",
    "GeometryCollectionInput": ".geometry_collection_input",
    "GeometryCollectionInputGeometriesItem": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputGeometriesItem_GeometryCollection": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputGeometriesItem_LineString": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputGeometriesItem_MultiLineString": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputGeometriesItem_MultiPoint": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputGeometriesItem_MultiPolygon": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputGeometriesItem_Point": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputGeometriesItem_Polygon": ".geometry_collection_input_geometries_item",
    "GeometryCollectionInputType": ".geometry_collection_input_type",
    "GeometryCollectionOutput": ".geometry_collection_output",
    "GeometryCollectionOutputGeometriesItem": ".geometry_collection_output_geometries_item",
    "GeometryCollectionOutputGeometriesItem_GeometryCollection": ".geometry_collection_output_geometries_item",
    "GeometryCollectionOutputGeometriesItem_LineString": ".geometry_collection_output_geometries_item",
    "GeometryCollectionOutputGeometriesItem_MultiLineString": ".geometry_collection_output_geometries_item",
    "GeometryCollectionOutputGeometriesItem_MultiPoint": ".geometry_collection_output_geometries_item",
    "GeometryCollectionOutputGeometriesItem_MultiPolygon": ".geometry_collection_output_geometries_item",
    "GeometryCollectionOutputGeometriesItem_Point": ".geometry_collection_output_geometries_item",
    "GeometryCollectionOutputGeometriesItem_Polygon": ".geometry_collection_output_geometries_item",
    "HealthCheck": ".health_check",
    "HealthCheckStatus": ".health_check_status",
    "HttpValidationError": ".http_validation_error",
    "InputModel": ".input_model",
    "Item": ".item",
    "ItemCollection": ".item_collection",
    "ItemCollectionInput": ".item_collection_input",
    "ItemCollectionOutput": ".item_collection_output",
    "ItemCollectionOutputType": ".item_collection_output_type",
    "ItemCollectionType": ".item_collection_type",
    "ItemGeometry": ".item_geometry",
    "ItemGeometry_GeometryCollection": ".item_geometry",
    "ItemGeometry_LineString": ".item_geometry",
    "ItemGeometry_MultiLineString": ".item_geometry",
    "ItemGeometry_MultiPoint": ".item_geometry",
    "ItemGeometry_MultiPolygon": ".item_geometry",
    "ItemGeometry_Point": ".item_geometry",
    "ItemGeometry_Polygon": ".item_geometry",
    "ItemInput": ".item_input",
    "ItemInputGeometry": ".item_input_geometry",
    "ItemInputGeometry_GeometryCollection": ".item_input_geometry",
    "ItemInputGeometry_LineString": ".item_input_geometry",
    "ItemInputGeometry_MultiLineString": ".item_input_geometry",
    "ItemInputGeometry_MultiPoint": ".item_input_geometry",
    "ItemInputGeometry_MultiPolygon": ".item_input_geometry",
    "ItemInputGeometry_Point": ".item_input_geometry",
    "ItemInputGeometry_Polygon": ".item_input_geometry",
    "ItemInputType": ".item_input_type",
    "ItemProperties": ".item_properties",
    "ItemType": ".item_type",
    "ItemsLink": ".items_link",
    "ItemsLinkMethod": ".items_link_method",
    "ItemsLinkRel": ".items_link_rel",
    "ItemsLinkType": ".items_link_type",
    "ItemsModel": ".items_model",
    "ItemsModelValue": ".items_model_value",
    "LandingPage": ".landing_page",
    "LandingPageType": ".landing_page_type",
    "LineString": ".line_string",
    "LineStringCoordinatesItem": ".line_string_coordinates_item",
    "LineStringType": ".line_string_type",
    "Link": ".link",
    "LinkType": ".link_type",
    "Links": ".links",
    "LinksInput": ".links_input",
    "MimeTypes": ".mime_types",
    "MultiLineString": ".multi_line_string",
    "MultiLineStringCoordinatesItemItem": ".multi_line_string_coordinates_item_item",
    "MultiLineStringType": ".multi_line_string_type",
    "MultiPoint": ".multi_point",
    "MultiPointCoordinatesItem": ".multi_point_coordinates_item",
    "MultiPointType": ".multi_point_type",
    "MultiPolygon": ".multi_polygon",
    "MultiPolygonCoordinatesItemItemItem": ".multi_polygon_coordinates_item_item_item",
    "MultiPolygonType": ".multi_polygon_type",
    "Operator": ".operator",
    "PaginationLink": ".pagination_link",
    "PaginationLinkMethod": ".pagination_link_method",
    "PaginationLinkRel": ".pagination_link_rel",
    "PaginationLinkType": ".pagination_link_type",
    "PartialCollection": ".partial_collection",
    "PartialItem": ".partial_item",
    "PartialItemType": ".partial_item_type",
    "PatchAddReplaceTest": ".patch_add_replace_test",
    "PatchAddReplaceTestOp": ".patch_add_replace_test_op",
    "PatchMoveCopy": ".patch_move_copy",
    "PatchMoveCopyOp": ".patch_move_copy_op",
    "PatchRemove": ".patch_remove",
    "PatchRemoveOp": ".patch_remove_op",
    "Point": ".point",
    "PointCoordinates": ".point_coordinates",
    "PointType": ".point_type",
    "Polygon": ".polygon",
    "PolygonCoordinatesItemItem": ".polygon_coordinates_item_item",
    "PolygonType": ".polygon_type",
    "Position2D": ".position2d",
    "Position3D": ".position3d",
    "PostFieldsExtension": ".post_fields_extension",
    "Provider": ".provider",
    "Range": ".range",
    "RangeMaximum": ".range_maximum",
    "RangeMinimum": ".range_minimum",
    "SearchLink": ".search_link",
    "SearchLinkMethod": ".search_link_method",
    "SearchLinkRel": ".search_link_rel",
    "SearchLinkType": ".search_link_type",
    "SearchPostRequest": ".search_post_request",
    "SearchPostRequestFilterLang": ".search_post_request_filter_lang",
    "SearchPostRequestIntersects": ".search_post_request_intersects",
    "SortDirections": ".sort_directions",
    "SortExtension": ".sort_extension",
    "SortablesSchema": ".sortables_schema",
    "SpatialExtent": ".spatial_extent",
    "StacPydanticApiCollectionCollection": ".stac_pydantic_api_collection_collection",
    "StacPydanticApiCollectionCollectionSummariesValue": ".stac_pydantic_api_collection_collection_summaries_value",
    "StacPydanticApiCollectionCollectionType": ".stac_pydantic_api_collection_collection_type",
    "StacPydanticApiItemItem": ".stac_pydantic_api_item_item",
    "StacPydanticApiItemItemGeometry": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemGeometry_GeometryCollection": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemGeometry_LineString": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemGeometry_MultiLineString": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemGeometry_MultiPoint": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemGeometry_MultiPolygon": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemGeometry_Point": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemGeometry_Polygon": ".stac_pydantic_api_item_item_geometry",
    "StacPydanticApiItemItemType": ".stac_pydantic_api_item_item_type",
    "StacPydanticApiLinksLinks": ".stac_pydantic_api_links_links",
    "StacPydanticApiLinksLinksItem": ".stac_pydantic_api_links_links_item",
    "StacPydanticCollectionCollectionOutput": ".stac_pydantic_collection_collection_output",
    "StacPydanticCollectionCollectionOutputSummariesValue": ".stac_pydantic_collection_collection_output_summaries_value",
    "StacPydanticCollectionCollectionOutputType": ".stac_pydantic_collection_collection_output_type",
    "StacPydanticItemItemOutput": ".stac_pydantic_item_item_output",
    "StacPydanticItemItemOutputGeometry": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputGeometry_GeometryCollection": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputGeometry_LineString": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputGeometry_MultiLineString": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputGeometry_MultiPoint": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputGeometry_MultiPolygon": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputGeometry_Point": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputGeometry_Polygon": ".stac_pydantic_item_item_output_geometry",
    "StacPydanticItemItemOutputType": ".stac_pydantic_item_item_output_type",
    "StacPydanticLinksLinks": ".stac_pydantic_links_links",
    "TimeInterval": ".time_interval",
    "TransactionErrorModel": ".transaction_error_model",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "Asset",
    "BulkTransactionMethod",
    "BulkTransactionModel",
    "Collection",
    "CollectionInput",
    "CollectionInputSummariesValue",
    "CollectionInputType",
    "CollectionSummariesValue",
    "CollectionType",
    "Collections",
    "Conformance",
    "Extent",
    "Feature",
    "FeatureBboxItem",
    "FeatureCollectionModel",
    "GeometryCollectionInput",
    "GeometryCollectionInputGeometriesItem",
    "GeometryCollectionInputGeometriesItem_GeometryCollection",
    "GeometryCollectionInputGeometriesItem_LineString",
    "GeometryCollectionInputGeometriesItem_MultiLineString",
    "GeometryCollectionInputGeometriesItem_MultiPoint",
    "GeometryCollectionInputGeometriesItem_MultiPolygon",
    "GeometryCollectionInputGeometriesItem_Point",
    "GeometryCollectionInputGeometriesItem_Polygon",
    "GeometryCollectionInputType",
    "GeometryCollectionOutput",
    "GeometryCollectionOutputGeometriesItem",
    "GeometryCollectionOutputGeometriesItem_GeometryCollection",
    "GeometryCollectionOutputGeometriesItem_LineString",
    "GeometryCollectionOutputGeometriesItem_MultiLineString",
    "GeometryCollectionOutputGeometriesItem_MultiPoint",
    "GeometryCollectionOutputGeometriesItem_MultiPolygon",
    "GeometryCollectionOutputGeometriesItem_Point",
    "GeometryCollectionOutputGeometriesItem_Polygon",
    "HealthCheck",
    "HealthCheckStatus",
    "HttpValidationError",
    "InputModel",
    "Item",
    "ItemCollection",
    "ItemCollectionInput",
    "ItemCollectionOutput",
    "ItemCollectionOutputType",
    "ItemCollectionType",
    "ItemGeometry",
    "ItemGeometry_GeometryCollection",
    "ItemGeometry_LineString",
    "ItemGeometry_MultiLineString",
    "ItemGeometry_MultiPoint",
    "ItemGeometry_MultiPolygon",
    "ItemGeometry_Point",
    "ItemGeometry_Polygon",
    "ItemInput",
    "ItemInputGeometry",
    "ItemInputGeometry_GeometryCollection",
    "ItemInputGeometry_LineString",
    "ItemInputGeometry_MultiLineString",
    "ItemInputGeometry_MultiPoint",
    "ItemInputGeometry_MultiPolygon",
    "ItemInputGeometry_Point",
    "ItemInputGeometry_Polygon",
    "ItemInputType",
    "ItemProperties",
    "ItemType",
    "ItemsLink",
    "ItemsLinkMethod",
    "ItemsLinkRel",
    "ItemsLinkType",
    "ItemsModel",
    "ItemsModelValue",
    "LandingPage",
    "LandingPageType",
    "LineString",
    "LineStringCoordinatesItem",
    "LineStringType",
    "Link",
    "LinkType",
    "Links",
    "LinksInput",
    "MimeTypes",
    "MultiLineString",
    "MultiLineStringCoordinatesItemItem",
    "MultiLineStringType",
    "MultiPoint",
    "MultiPointCoordinatesItem",
    "MultiPointType",
    "MultiPolygon",
    "MultiPolygonCoordinatesItemItemItem",
    "MultiPolygonType",
    "Operator",
    "PaginationLink",
    "PaginationLinkMethod",
    "PaginationLinkRel",
    "PaginationLinkType",
    "PartialCollection",
    "PartialItem",
    "PartialItemType",
    "PatchAddReplaceTest",
    "PatchAddReplaceTestOp",
    "PatchMoveCopy",
    "PatchMoveCopyOp",
    "PatchRemove",
    "PatchRemoveOp",
    "Point",
    "PointCoordinates",
    "PointType",
    "Polygon",
    "PolygonCoordinatesItemItem",
    "PolygonType",
    "Position2D",
    "Position3D",
    "PostFieldsExtension",
    "Provider",
    "Range",
    "RangeMaximum",
    "RangeMinimum",
    "SearchLink",
    "SearchLinkMethod",
    "SearchLinkRel",
    "SearchLinkType",
    "SearchPostRequest",
    "SearchPostRequestFilterLang",
    "SearchPostRequestIntersects",
    "SortDirections",
    "SortExtension",
    "SortablesSchema",
    "SpatialExtent",
    "StacPydanticApiCollectionCollection",
    "StacPydanticApiCollectionCollectionSummariesValue",
    "StacPydanticApiCollectionCollectionType",
    "StacPydanticApiItemItem",
    "StacPydanticApiItemItemGeometry",
    "StacPydanticApiItemItemGeometry_GeometryCollection",
    "StacPydanticApiItemItemGeometry_LineString",
    "StacPydanticApiItemItemGeometry_MultiLineString",
    "StacPydanticApiItemItemGeometry_MultiPoint",
    "StacPydanticApiItemItemGeometry_MultiPolygon",
    "StacPydanticApiItemItemGeometry_Point",
    "StacPydanticApiItemItemGeometry_Polygon",
    "StacPydanticApiItemItemType",
    "StacPydanticApiLinksLinks",
    "StacPydanticApiLinksLinksItem",
    "StacPydanticCollectionCollectionOutput",
    "StacPydanticCollectionCollectionOutputSummariesValue",
    "StacPydanticCollectionCollectionOutputType",
    "StacPydanticItemItemOutput",
    "StacPydanticItemItemOutputGeometry",
    "StacPydanticItemItemOutputGeometry_GeometryCollection",
    "StacPydanticItemItemOutputGeometry_LineString",
    "StacPydanticItemItemOutputGeometry_MultiLineString",
    "StacPydanticItemItemOutputGeometry_MultiPoint",
    "StacPydanticItemItemOutputGeometry_MultiPolygon",
    "StacPydanticItemItemOutputGeometry_Point",
    "StacPydanticItemItemOutputGeometry_Polygon",
    "StacPydanticItemItemOutputType",
    "StacPydanticLinksLinks",
    "TimeInterval",
    "TransactionErrorModel",
    "ValidationError",
    "ValidationErrorLocItem",
]
