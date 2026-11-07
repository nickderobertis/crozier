

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateTemplateResult(UniversalBaseModel):
    properties: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    sas_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sasUrl"), pydantic.Field(alias="sasUrl")
    ] = None
    template_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="templateId"), pydantic.Field(alias="templateId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
