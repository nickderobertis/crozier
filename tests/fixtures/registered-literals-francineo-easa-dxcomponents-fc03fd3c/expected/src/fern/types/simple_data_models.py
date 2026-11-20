

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
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
from .simple_data_models_geometry_collection import SimpleDataModelsGeometryCollection
from .simple_data_models_line_string import SimpleDataModelsLineString
from .simple_data_models_multi_line_string import SimpleDataModelsMultiLineString
from .simple_data_models_multi_point import SimpleDataModelsMultiPoint
from .simple_data_models_multi_polygon import SimpleDataModelsMultiPolygon
from .simple_data_models_normal_geometry import SimpleDataModelsNormalGeometry
from .simple_data_models_point_with_extent import SimpleDataModelsPointWithExtent
from .simple_data_models_polygon import SimpleDataModelsPolygon
from .simple_data_models_text_long_type import SimpleDataModelsTextLongType
from .simple_data_models_text_short_type import SimpleDataModelsTextShortType
from .simple_data_models_uom_distance import SimpleDataModelsUomDistance


class SimpleDataModels(UniversalBaseModel):
    """
    ED-318 specific data models as defined in chapter 4.2.5
    """

    code_authority_role: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeAuthorityRole],
        FieldMetadata(alias="CodeAuthorityRole"),
        pydantic.Field(
            alias="CodeAuthorityRole",
            description="Roles that an authority has in relation with the UAS zone, represented by\na string with an enumerated list of values.",
        ),
    ] = None
    """
    Roles that an authority has in relation with the UAS zone, represented by
    a string with an enumerated list of values.
    """

    code_daylight_event_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeDaylightEventType],
        FieldMetadata(alias="CodeDaylightEventType"),
        pydantic.Field(
            alias="CodeDaylightEventType",
            description="A time identified in relation with an astronomical event, such as sunrise/sunset,\nrepresented by a string with an enumerated list of values.",
        ),
    ] = None
    """
    A time identified in relation with an astronomical event, such as sunrise/sunset,
    represented by a string with an enumerated list of values.
    """

    uom_distance: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsUomDistance],
        FieldMetadata(alias="UomDistance"),
        pydantic.Field(
            alias="UomDistance",
            description="The unit of measurement in which the upper and lower values are expressed.\nIf this member is not specified, the units should be assumed to be metres.",
        ),
    ] = None
    """
    The unit of measurement in which the upper and lower values are expressed.
    If this member is not specified, the units should be assumed to be metres.
    """

    code_zone_identifier_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CodeZoneIdentifierType"),
        pydantic.Field(
            alias="CodeZoneIdentifierType",
            description="A string of maximum 7 characters that uniquely identifies the area\nwithin a geographical scope.",
        ),
    ] = None
    """
    A string of maximum 7 characters that uniquely identifies the area
    within a geographical scope.
    """

    code_country_iso_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CodeCountryISOType"),
        pydantic.Field(
            alias="CodeCountryISOType",
            description="A 3 letter identifier of a country or territory using the ISO 3166-1 alpha-3 standard.",
        ),
    ] = None
    """
    A 3 letter identifier of a country or territory using the ISO 3166-1 alpha-3 standard.
    """

    code_zone_variant_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeZoneVariantType],
        FieldMetadata(alias="CodeZoneVariantType"),
        pydantic.Field(alias="CodeZoneVariantType"),
    ] = None
    code_zone_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeZoneType],
        FieldMetadata(alias="CodeZoneType"),
        pydantic.Field(alias="CodeZoneType"),
    ] = None
    condition_expression_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ConditionExpressionType"),
        pydantic.Field(
            alias="ConditionExpressionType",
            description="Coded expression that provides information about what is\nauthorised / forbidden in a zone that has conditional access.",
        ),
    ] = None
    """
    Coded expression that provides information about what is
    authorised / forbidden in a zone that has conditional access.
    """

    code_zone_reason_type: typing_extensions.Annotated[
        typing.Optional[typing.List[SimpleDataModelsCodeZoneReasonTypeItem]],
        FieldMetadata(alias="CodeZoneReasonType"),
        pydantic.Field(
            alias="CodeZoneReasonType",
            description="An indication of a reason that justifies the existence of an UAS Zone,\nrepresented as a string with a list of enumerated values.",
        ),
    ] = None
    """
    An indication of a reason that justifies the existence of an UAS Zone,
    represented as a string with a list of enumerated values.
    """

    text_short_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsTextShortType],
        FieldMetadata(alias="TextShortType"),
        pydantic.Field(
            alias="TextShortType",
            description="A free text with a maximum length of 200 characters, optionally accompanied\nby an indication of the language in which the text is written.",
        ),
    ] = None
    """
    A free text with a maximum length of 200 characters, optionally accompanied
    by an indication of the language in which the text is written.
    """

    text_long_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsTextLongType],
        FieldMetadata(alias="TextLongType"),
        pydantic.Field(
            alias="TextLongType",
            description="A free text with a maximum length of 1000 characters, optionally accompanied\nby an indication of the language in which the text is written.",
        ),
    ] = None
    """
    A free text with a maximum length of 1000 characters, optionally accompanied
    by an indication of the language in which the text is written.
    """

    code_week_day_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeWeekDayType],
        FieldMetadata(alias="CodeWeekDayType"),
        pydantic.Field(
            alias="CodeWeekDayType",
            description="Indicates a day of the week, represented as a string with a list of enumerated values.",
        ),
    ] = None
    """
    Indicates a day of the week, represented as a string with a list of enumerated values.
    """

    date_time_type: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="DateTimeType"),
        pydantic.Field(alias="DateTimeType", description="RFC3339 Datetime"),
    ] = None
    """
    RFC3339 Datetime
    """

    time_interval: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TimeInterval"),
        pydantic.Field(
            alias="TimeInterval",
            description="A period of time represented as a string formatted according to the ISO 8601\nrules for time intervals, in the format PnnDTnnHnnM, where:\n- P is a mandatory character that indicates that the value is a time interval\n- nnD is an optional block that indicates the number of days comprised in the interval\n- T is a mandatory character that indicates the start of the time block\n- nnH is an optional block that indicates the number of hours comprised in the interval\n- nnM is an optional block that indicates the number of minutes comprised in the interval",
        ),
    ] = None
    """
    A period of time represented as a string formatted according to the ISO 8601
    rules for time intervals, in the format PnnDTnnHnnM, where:
    - P is a mandatory character that indicates that the value is a time interval
    - nnD is an optional block that indicates the number of days comprised in the interval
    - T is a mandatory character that indicates the start of the time block
    - nnH is an optional block that indicates the number of hours comprised in the interval
    - nnM is an optional block that indicates the number of minutes comprised in the interval
    """

    time_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TimeType"),
        pydantic.Field(
            alias="TimeType",
            description="A time instant, represented by a string in the form hh:mmS where the date and\ntime format shall follow the ISO 8601 standard, with 'S' indicating the time zone",
        ),
    ] = None
    """
    A time instant, represented by a string in the form hh:mmS where the date and
    time format shall follow the ISO 8601 standard, with 'S' indicating the time zone
    """

    code_yes_no_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeYesNoType],
        FieldMetadata(alias="CodeYesNoType"),
        pydantic.Field(
            alias="CodeYesNoType",
            description="A choice between a positive (yes) or a negative (no) applicability,\nrepresented as a string with a list of enumerated values.",
        ),
    ] = None
    """
    A choice between a positive (yes) or a negative (no) applicability,
    represented as a string with a list of enumerated values.
    """

    urn_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="URNType"),
        pydantic.Field(
            alias="URNType",
            description="String of characters that complies with the Uniform Resource Name (URN) scheme as specified in the RFC 2141",
        ),
    ] = None
    """
    String of characters that complies with the Uniform Resource Name (URN) scheme as specified in the RFC 2141
    """

    code_geometry_sub_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeGeometrySubType],
        FieldMetadata(alias="CodeGeometrySubType"),
        pydantic.Field(
            alias="CodeGeometrySubType",
            description="A string indicating what type of geometry sub-type is being provided. Currently supports only circle.",
        ),
    ] = None
    """
    A string indicating what type of geometry sub-type is being provided. Currently supports only circle.
    """

    code_vertical_reference_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsCodeVerticalReferenceType],
        FieldMetadata(alias="CodeVerticalReferenceType"),
        pydantic.Field(
            alias="CodeVerticalReferenceType",
            description="A code indicating a vertical reference system. Allowed values:\nAGL = Above ground level (or above water surface, as applicable)\nAMSL = Above Mean Sea Level\nWGS84 = Above the surface of the WGS-84 ellipsoid (Ellipsoidal height)",
        ),
    ] = None
    """
    A code indicating a vertical reference system. Allowed values:
    AGL = Above ground level (or above water surface, as applicable)
    AMSL = Above Mean Sea Level
    WGS84 = Above the surface of the WGS-84 ellipsoid (Ellipsoidal height)
    """

    geo_json_geometry_type: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsGeoJsonGeometryType],
        FieldMetadata(alias="GeoJSONGeometryType"),
        pydantic.Field(alias="GeoJSONGeometryType", description="Type of geometry being used to describe the feature."),
    ] = None
    """
    Type of geometry being used to describe the feature.
    """

    normal_geometry: typing.Optional[SimpleDataModelsNormalGeometry] = pydantic.Field(default=None)
    """
    Individual geometry entry not in a collection.
    """

    point_with_extent: typing.Optional[SimpleDataModelsPointWithExtent] = pydantic.Field(default=None)
    """
    GeoJSON Point with LayeredGeoJSON extent validation.
    """

    line_string: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsLineString],
        FieldMetadata(alias="LineString"),
        pydantic.Field(alias="LineString"),
    ] = None
    polygon: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsPolygon], FieldMetadata(alias="Polygon"), pydantic.Field(alias="Polygon")
    ] = None
    multi_point: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsMultiPoint],
        FieldMetadata(alias="MultiPoint"),
        pydantic.Field(alias="MultiPoint"),
    ] = None
    multi_line_string: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsMultiLineString],
        FieldMetadata(alias="MultiLineString"),
        pydantic.Field(alias="MultiLineString"),
    ] = None
    multi_polygon: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsMultiPolygon],
        FieldMetadata(alias="MultiPolygon"),
        pydantic.Field(alias="MultiPolygon"),
    ] = None
    geometry_collection: typing_extensions.Annotated[
        typing.Optional[SimpleDataModelsGeometryCollection],
        FieldMetadata(alias="GeometryCollection"),
        pydantic.Field(alias="GeometryCollection"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
