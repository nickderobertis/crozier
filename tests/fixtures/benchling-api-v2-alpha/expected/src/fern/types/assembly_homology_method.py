

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assembly_homology_method_parameters import AssemblyHomologyMethodParameters


class AssemblyHomologyMethod(UniversalBaseModel):
    parameters: AssemblyHomologyMethodParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
