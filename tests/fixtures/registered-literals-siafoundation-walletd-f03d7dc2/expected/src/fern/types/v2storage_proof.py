

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chain_index_element import ChainIndexElement
from .hash256 import Hash256


class V2StorageProof(UniversalBaseModel):
    proof_index: typing_extensions.Annotated[
        ChainIndexElement, FieldMetadata(alias="proofIndex"), pydantic.Field(alias="proofIndex")
    ]
    leaf: str = pydantic.Field()
    """
    Hex-encoded 64 byte leaf.
    """

    proof: typing.List[Hash256]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
