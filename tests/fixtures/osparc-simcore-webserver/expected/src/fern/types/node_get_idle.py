

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_get_idle_service_state import NodeGetIdleServiceState


class NodeGetIdle(UniversalBaseModel):
    service_state: typing_extensions.Annotated[
        NodeGetIdleServiceState, FieldMetadata(alias="serviceState"), pydantic.Field(alias="serviceState")
    ]
    service_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceUuid"), pydantic.Field(alias="serviceUuid")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
