

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assembly_concatenation_method_parameters import AssemblyConcatenationMethodParameters


class AssemblyConcatenationMethod(UniversalBaseModel):
    parameters: AssemblyConcatenationMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
