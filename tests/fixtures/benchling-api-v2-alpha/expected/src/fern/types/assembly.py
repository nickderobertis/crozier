

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .assembly_shared import AssemblyShared
from .finalized_assembly import FinalizedAssembly


class Assembly(AssemblyShared, FinalizedAssembly):
    """
    Bulk assembly object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
