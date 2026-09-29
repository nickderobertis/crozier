

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_object_field_definition import InputObjectFieldDefinition


class InputObjectTypeDefinition(UniversalBaseModel):
    description: typing.Optional[str] = None
    fields: typing.List[InputObjectFieldDefinition]
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
