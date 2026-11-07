

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hash256 import Hash256


class ElementAccumulator(UniversalBaseModel):
    """
    Accumulator used to track Merkle proofs for chain elements.
    """

    num_leaves: typing_extensions.Annotated[int, FieldMetadata(alias="numLeaves"), pydantic.Field(alias="numLeaves")]
    trees: typing.List[Hash256] = pydantic.Field()
    """
    Roots of the accumulator trees currently populated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
