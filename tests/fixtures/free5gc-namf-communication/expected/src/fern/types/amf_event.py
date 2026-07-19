

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amf_event_area import AmfEventArea
from .amf_event_type import AmfEventType
from .location_filter import LocationFilter
from .subscribed_data_filter import SubscribedDataFilter


class AmfEvent(UniversalBaseModel):
    type: AmfEventType
    immediate_flag: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="immediateFlag"), pydantic.Field(alias="immediateFlag")
    ] = None
    area_list: typing_extensions.Annotated[
        typing.Optional[typing.List[AmfEventArea]], FieldMetadata(alias="areaList"), pydantic.Field(alias="areaList")
    ] = None
    location_filter_list: typing_extensions.Annotated[
        typing.Optional[typing.List[LocationFilter]],
        FieldMetadata(alias="locationFilterList"),
        pydantic.Field(alias="locationFilterList"),
    ] = None
    subscribed_data_filter_list: typing_extensions.Annotated[
        typing.Optional[typing.List[SubscribedDataFilter]],
        FieldMetadata(alias="subscribedDataFilterList"),
        pydantic.Field(alias="subscribedDataFilterList"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
