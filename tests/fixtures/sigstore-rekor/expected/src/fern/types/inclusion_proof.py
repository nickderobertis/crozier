

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InclusionProof(UniversalBaseModel):
    checkpoint: str = pydantic.Field()
    """
    The checkpoint (signed tree head) that the inclusion proof is based on
    """

    hashes: typing.List[str] = pydantic.Field()
    """
    A list of hashes required to compute the inclusion proof, sorted in order from leaf to root
    """

    log_index: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="logIndex"),
        pydantic.Field(alias="logIndex", description="The index of the entry in the transparency log"),
    ]
    """
    The index of the entry in the transparency log
    """

    root_hash: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rootHash"),
        pydantic.Field(
            alias="rootHash",
            description="The hash value stored at the root of the merkle tree at the time the proof was generated",
        ),
    ]
    """
    The hash value stored at the root of the merkle tree at the time the proof was generated
    """

    tree_size: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="treeSize"),
        pydantic.Field(
            alias="treeSize", description="The size of the merkle tree at the time the inclusion proof was generated"
        ),
    ]
    """
    The size of the merkle tree at the time the inclusion proof was generated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
