

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .parameter_dto_ref_clazz import ParameterDtoRefClazz


class ParameterDto(UniversalBaseModel):
    name: str
    ref_clazz: typing_extensions.Annotated[
        ParameterDtoRefClazz, FieldMetadata(alias="refClazz"), pydantic.Field(alias="refClazz")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ParameterDto)
