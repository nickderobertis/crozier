

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .accessible import Accessible
from .road_section_id import RoadSectionId


class DestinationFeatureProperties(UniversalBaseModel):
    road_section_id: typing_extensions.Annotated[
        typing.Optional[RoadSectionId], FieldMetadata(alias="roadSectionId"), pydantic.Field(alias="roadSectionId")
    ] = None
    accessible: typing.Optional[Accessible] = None
    reasons: typing.Optional[typing.List[typing.List["Reason"]]] = pydantic.Field(default=None)
    """
    Group of combined reasons why the destination is inaccessible. Each group contains a list of unique reasons. why the destination is inaccessible. Resolving one of these groups would mean the destination is accessible.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .reason import Reason

update_forward_refs(DestinationFeatureProperties, Reason=Reason)
