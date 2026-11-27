

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assembly_fragment_shared_orientation import AssemblyFragmentSharedOrientation
from .assembly_polymer_reference import AssemblyPolymerReference


class AssemblyFragmentShared(UniversalBaseModel):
    end: float = pydantic.Field()
    """
    End position of the fragment in the provided input.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the fragment.
    """

    orientation: AssemblyFragmentSharedOrientation
    polymer: AssemblyPolymerReference
    start: float = pydantic.Field()
    """
    Start position of the fragment in the provided input.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
