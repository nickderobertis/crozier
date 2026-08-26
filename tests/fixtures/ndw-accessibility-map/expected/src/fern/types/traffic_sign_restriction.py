

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .traffic_sign_id import TrafficSignId
from .traffic_sign_type import TrafficSignType


class TrafficSignRestriction(UniversalBaseModel):
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
