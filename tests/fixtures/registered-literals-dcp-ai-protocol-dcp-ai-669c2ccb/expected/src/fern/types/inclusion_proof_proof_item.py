

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inclusion_proof_proof_item_direction import InclusionProofProofItemDirection


class InclusionProofProofItem(UniversalBaseModel):
    hash: typing.Optional[str] = None
    direction: typing.Optional[InclusionProofProofItemDirection] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
