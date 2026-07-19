

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_ran_node_id import GlobalRanNodeId
from .tai import Tai


class NgRanTargetId(UniversalBaseModel):
    ran_node_id: typing_extensions.Annotated[
        GlobalRanNodeId, FieldMetadata(alias="ranNodeId"), pydantic.Field(alias="ranNodeId")
    ]
    tai: Tai

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
