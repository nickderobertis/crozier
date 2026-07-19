

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field_element import FieldElement
from .inclusion_proof_proof_item import InclusionProofProofItem


class InclusionProof(UniversalBaseModel):
    """
    Merkle inclusion proof for an identity in the tree.
    V3 response differs from V2 in that it doesn't include a status field.
    """

    root: FieldElement = pydantic.Field()
    """
    The root of the Merkle tree
    """

    proof: typing.List[InclusionProofProofItem] = pydantic.Field()
    """
    The Merkle proof path
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
