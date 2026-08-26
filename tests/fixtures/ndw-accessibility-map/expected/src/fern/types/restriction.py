

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .road_section_id import RoadSectionId
from .traffic_sign_id import TrafficSignId
from .traffic_sign_type import TrafficSignType


class Restriction_RoadSection(UniversalBaseModel):
    """
    Describes a restriction.
    """

    type: typing.Literal["roadSection"] = "roadSection"
    road_section_id: typing_extensions.Annotated[
        typing.Optional[RoadSectionId], FieldMetadata(alias="roadSectionId"), pydantic.Field(alias="roadSectionId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Restriction_TrafficSign(UniversalBaseModel):
    """
    Describes a restriction.
    """

    type: typing.Literal["trafficSign"] = "trafficSign"
    traffic_sign_id: typing_extensions.Annotated[
        TrafficSignId, FieldMetadata(alias="trafficSignId"), pydantic.Field(alias="trafficSignId")
    ]
    traffic_sign_type: typing_extensions.Annotated[
        TrafficSignType, FieldMetadata(alias="trafficSignType"), pydantic.Field(alias="trafficSignType")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Restriction = typing_extensions.Annotated[
    typing.Union[Restriction_RoadSection, Restriction_TrafficSign], pydantic.Field(discriminator="type")
]
