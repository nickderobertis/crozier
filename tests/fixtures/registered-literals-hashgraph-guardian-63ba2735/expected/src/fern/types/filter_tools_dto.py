

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilterToolsDto(UniversalBaseModel):
    tool_id1: typing_extensions.Annotated[str, FieldMetadata(alias="toolId1"), pydantic.Field(alias="toolId1")]
    tool_id2: typing_extensions.Annotated[str, FieldMetadata(alias="toolId2"), pydantic.Field(alias="toolId2")]
    tool_ids: typing_extensions.Annotated[str, FieldMetadata(alias="toolIds"), pydantic.Field(alias="toolIds")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
