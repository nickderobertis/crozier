

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_fragment_bin_fragment_production_method import AssemblyFragmentBinFragmentProductionMethod


class AssemblyFragmentBin(UniversalBaseModel):
    fragment_production_method: typing_extensions.Annotated[
        typing.Optional[AssemblyFragmentBinFragmentProductionMethod],
        FieldMetadata(alias="fragmentProductionMethod"),
        pydantic.Field(alias="fragmentProductionMethod"),
    ] = None
    id: str = pydantic.Field()
    """
    Unique identifier for the bin.
    """

    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
