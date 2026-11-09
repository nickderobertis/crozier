

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PolicyBlock(UniversalBaseModel):
    id: str
    block_type: typing_extensions.Annotated[str, FieldMetadata(alias="blockType"), pydantic.Field(alias="blockType")]
    is_active: typing_extensions.Annotated[bool, FieldMetadata(alias="isActive"), pydantic.Field(alias="isActive")]
    ui_meta_data: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="uiMetaData"), pydantic.Field(alias="uiMetaData")
    ]
    blocks: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
