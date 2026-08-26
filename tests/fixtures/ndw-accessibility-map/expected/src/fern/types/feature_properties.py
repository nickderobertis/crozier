

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .accessible import Accessible
from .delay_in_milli_seconds_because_of_restrictions import DelayInMilliSecondsBecauseOfRestrictions
from .direction import Direction
from .functional_road_class import FunctionalRoadClass
from .road_section_id import RoadSectionId


class FeatureProperties_RoadSectionSegment(UniversalBaseModel):
    type: typing.Literal["roadSectionSegment"] = "roadSectionSegment"
    road_section_id: typing_extensions.Annotated[
        typing.Optional[RoadSectionId], FieldMetadata(alias="roadSectionId"), pydantic.Field(alias="roadSectionId")
    ] = None
    functional_road_class: typing_extensions.Annotated[
        typing.Optional[FunctionalRoadClass],
        FieldMetadata(alias="functionalRoadClass"),
        pydantic.Field(alias="functionalRoadClass"),
    ] = None
    delay_in_milli_seconds_because_of_restrictions: typing_extensions.Annotated[
        typing.Optional[DelayInMilliSecondsBecauseOfRestrictions],
        FieldMetadata(alias="delayInMilliSecondsBecauseOfRestrictions"),
        pydantic.Field(alias="delayInMilliSecondsBecauseOfRestrictions"),
    ] = None
    accessible: typing.Optional[Accessible] = None
    direction: Direction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FeatureProperties_Destination(UniversalBaseModel):
    type: typing.Literal["destination"] = "destination"
    road_section_id: typing_extensions.Annotated[
        typing.Optional[RoadSectionId], FieldMetadata(alias="roadSectionId"), pydantic.Field(alias="roadSectionId")
    ] = None
    accessible: typing.Optional[Accessible] = None
    reasons: typing.Optional[typing.List[typing.List["Reason"]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FeatureProperties_Unknown(UniversalBaseModel):
    value: "FeatureProperties"
    type: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


FeatureProperties = typing_extensions.Annotated[
    typing.Union[FeatureProperties_RoadSectionSegment, FeatureProperties_Destination, FeatureProperties_Unknown],
    pydantic.Field(discriminator="type"),
]
from .reason import Reason

update_forward_refs(FeatureProperties_Destination, Reason=Reason)
update_forward_refs(FeatureProperties_Unknown, FeatureProperties=FeatureProperties)
