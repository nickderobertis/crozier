

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .test_source_parameters import TestSourceParameters


class WithParameters(UniversalBaseModel):
    source_parameters: typing_extensions.Annotated[
        TestSourceParameters, FieldMetadata(alias="sourceParameters"), pydantic.Field(alias="sourceParameters")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
