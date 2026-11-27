

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assembly_construct import AssemblyConstruct
from .assembly_fragment_shared import AssemblyFragmentShared
from .finalized_assembly_bins_item import FinalizedAssemblyBinsItem
from .finalized_assembly_method import FinalizedAssemblyMethod


class FinalizedAssembly(UniversalBaseModel):
    bins: typing.Optional[typing.List[FinalizedAssemblyBinsItem]] = None
    constructs: typing.Optional[typing.List[AssemblyConstruct]] = None
    fragments: typing.Optional[typing.List[AssemblyFragmentShared]] = None
    method: typing.Optional[FinalizedAssemblyMethod] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
