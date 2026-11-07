

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LeaderResponseDto(UniversalBaseModel):
    ha_enabled: typing_extensions.Annotated[bool, FieldMetadata(alias="haEnabled"), pydantic.Field(alias="haEnabled")]
    instance_id: typing_extensions.Annotated[str, FieldMetadata(alias="instanceId"), pydantic.Field(alias="instanceId")]
    is_leader: typing_extensions.Annotated[bool, FieldMetadata(alias="isLeader"), pydantic.Field(alias="isLeader")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
