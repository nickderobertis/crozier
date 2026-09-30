

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .enum_type_definition import EnumTypeDefinition
from .input_object_type_definition import InputObjectTypeDefinition
from .object_type_definition import ObjectTypeDefinition
from .scalar_type_definition import ScalarTypeDefinition


class CustomTypes(UniversalBaseModel):
    enums: typing.Optional[typing.List[EnumTypeDefinition]] = None
    input_objects: typing.Optional[typing.List[InputObjectTypeDefinition]] = None
    objects: typing.Optional[typing.List[ObjectTypeDefinition]] = None
    scalars: typing.Optional[typing.List[ScalarTypeDefinition]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
