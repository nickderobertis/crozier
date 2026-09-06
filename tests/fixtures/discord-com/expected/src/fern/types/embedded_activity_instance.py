

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedded_activity_instance_location import EmbeddedActivityInstanceLocation
from .snowflake_type import SnowflakeType


class EmbeddedActivityInstance(UniversalBaseModel):
    application_id: SnowflakeType
    instance_id: str
    launch_id: str
    location: typing.Optional[EmbeddedActivityInstanceLocation] = None
    users: typing.List[SnowflakeType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
