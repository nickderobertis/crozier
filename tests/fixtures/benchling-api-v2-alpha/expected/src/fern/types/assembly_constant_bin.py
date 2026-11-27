

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssemblyConstantBin(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the bin.
    """

    name: str
    residues: str = pydantic.Field()
    """
    Base pairs or amino acid residues for the spacer/constant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
