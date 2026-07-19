

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreMemoryBlockSchema(UniversalBaseModel):
    created_at: str
    description: typing.Optional[str] = None
    is_template: bool
    label: str
    limit: int
    metadata: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="metadata_"),
        pydantic.Field(alias="metadata_"),
    ] = None
    template_name: typing.Optional[str] = None
    updated_at: str
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
