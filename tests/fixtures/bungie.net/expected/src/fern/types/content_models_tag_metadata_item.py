

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentModelsTagMetadataItem(UniversalBaseModel):
    description: typing.Optional[str] = None
    groups: typing.Optional[typing.List[str]] = None
    is_default: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDefault"), pydantic.Field(alias="isDefault")
    ] = None
    name: typing.Optional[str] = None
    tag_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagText"), pydantic.Field(alias="tagText")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
