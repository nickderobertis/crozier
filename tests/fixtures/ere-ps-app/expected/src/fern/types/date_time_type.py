

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .date import Date
from .i_base_extension_object_object import IBaseExtensionObjectObject
from .temporal_precision_enum import TemporalPrecisionEnum
from .time_zone import TimeZone


class DateTimeType(UniversalBaseModel):
    format_comments_pre: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPre"),
        pydantic.Field(alias="formatCommentsPre"),
    ] = None
    format_comments_post: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPost"),
        pydantic.Field(alias="formatCommentsPost"),
    ] = None
    extension: typing.Optional[typing.List[IBaseExtensionObjectObject]] = None
    user_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="userData"), pydantic.Field(alias="userData")
    ] = None
    boolean_primitive: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="booleanPrimitive"), pydantic.Field(alias="booleanPrimitive")
    ] = None
    metadata_based: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="metadataBased"), pydantic.Field(alias="metadataBased")
    ] = None
    resource: typing.Optional[bool] = None
    xhtml: typing.Optional["XhtmlNode"] = None
    id: typing.Optional["StringType"] = None
    disallow_extensions: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="disallowExtensions"), pydantic.Field(alias="disallowExtensions")
    ] = None
    id_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="idElement"), pydantic.Field(alias="idElement")
    ] = None
    extension_first_rep: typing_extensions.Annotated[
        typing.Optional["Extension"],
        FieldMetadata(alias="extensionFirstRep"),
        pydantic.Field(alias="extensionFirstRep"),
    ] = None
    id_base: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idBase"), pydantic.Field(alias="idBase")
    ] = None
    value_as_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="valueAsString"), pydantic.Field(alias="valueAsString")
    ] = None
    my_coerced_value: typing_extensions.Annotated[
        typing.Optional[Date], FieldMetadata(alias="myCoercedValue"), pydantic.Field(alias="myCoercedValue")
    ] = None
    my_string_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="myStringValue"), pydantic.Field(alias="myStringValue")
    ] = None
    value: typing.Optional[Date] = None
    empty: typing.Optional[bool] = None
    primitive: typing.Optional[bool] = None
    my_fractional_seconds: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="myFractionalSeconds"), pydantic.Field(alias="myFractionalSeconds")
    ] = None
    my_precision: typing_extensions.Annotated[
        typing.Optional[TemporalPrecisionEnum], FieldMetadata(alias="myPrecision"), pydantic.Field(alias="myPrecision")
    ] = None
    my_time_zone: typing_extensions.Annotated[
        typing.Optional[TimeZone], FieldMetadata(alias="myTimeZone"), pydantic.Field(alias="myTimeZone")
    ] = None
    my_time_zone_zulu: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="myTimeZoneZulu"), pydantic.Field(alias="myTimeZoneZulu")
    ] = None
    day: typing.Optional[int] = None
    hour: typing.Optional[int] = None
    millis: typing.Optional[int] = None
    minute: typing.Optional[int] = None
    month: typing.Optional[int] = None
    seconds_milli: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="secondsMilli"), pydantic.Field(alias="secondsMilli")
    ] = None
    nanos: typing.Optional[int] = None
    precision: typing.Optional[TemporalPrecisionEnum] = None
    second: typing.Optional[int] = None
    time_zone: typing_extensions.Annotated[
        typing.Optional[TimeZone], FieldMetadata(alias="timeZone"), pydantic.Field(alias="timeZone")
    ] = None
    value_as_calendar: typing_extensions.Annotated[
        typing.Optional["GregorianCalendar"],
        FieldMetadata(alias="valueAsCalendar"),
        pydantic.Field(alias="valueAsCalendar"),
    ] = None
    year: typing.Optional[int] = None
    time_zone_zulu: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="timeZoneZulu"), pydantic.Field(alias="timeZoneZulu")
    ] = None
    today: typing.Optional[bool] = None
    value_as_v3string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="valueAsV3String"), pydantic.Field(alias="valueAsV3String")
    ] = None
    high_edge: typing_extensions.Annotated[
        typing.Optional["BaseDateTimeType"], FieldMetadata(alias="highEdge"), pydantic.Field(alias="highEdge")
    ] = None
    default_precision_for_datatype: typing_extensions.Annotated[
        typing.Optional[TemporalPrecisionEnum],
        FieldMetadata(alias="defaultPrecisionForDatatype"),
        pydantic.Field(alias="defaultPrecisionForDatatype"),
    ] = None
    tz_sign: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="tzSign"), pydantic.Field(alias="tzSign")
    ] = None
    tz_hour: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="tzHour"), pydantic.Field(alias="tzHour")
    ] = None
    tz_min: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="tzMin"), pydantic.Field(alias="tzMin")
    ] = None
    as_v3: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="asV3"), pydantic.Field(alias="asV3")
    ] = None
    date_time: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="dateTime"), pydantic.Field(alias="dateTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .xhtml_node import XhtmlNode
from .xhtml_node_list import XhtmlNodeList
from .extension import Extension
from .string_type import StringType
from .type import Type
from .uri_type import UriType
from .gregorian_calendar import GregorianCalendar
from .base_date_time_type import BaseDateTimeType

update_forward_refs(
    DateTimeType,
    BaseDateTimeType=BaseDateTimeType,
    Extension=Extension,
    GregorianCalendar=GregorianCalendar,
    StringType=StringType,
    Type=Type,
    UriType=UriType,
    XhtmlNode=XhtmlNode,
    XhtmlNodeList=XhtmlNodeList,
)
