

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel import Channel
from .template_name import TemplateName


class TemplateRef(UniversalBaseModel):
    channel: Channel
    template_name: typing_extensions.Annotated[
        TemplateName, FieldMetadata(alias="templateName"), pydantic.Field(alias="templateName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
