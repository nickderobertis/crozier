

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentModelsContentPreview(UniversalBaseModel):
    item_in_set: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="itemInSet")] = None
    name: typing.Optional[str] = None
    path: typing.Optional[str] = None
    set_nesting: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="setNesting")] = None
    set_tag: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="setTag")] = None
    use_set_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="useSetId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
