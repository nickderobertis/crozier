

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .template_ref_get import TemplateRefGet


class TemplateGet(UniversalBaseModel):
    ref: TemplateRefGet
    context_schema: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="contextSchema"), pydantic.Field(alias="contextSchema")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
