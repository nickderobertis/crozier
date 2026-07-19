

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InactiveShardLogInfo(UniversalBaseModel):
    root_hash: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rootHash"),
        pydantic.Field(alias="rootHash", description="The current hash value stored at the root of the merkle tree"),
    ]
    """
    The current hash value stored at the root of the merkle tree
    """

    signed_tree_head: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="signedTreeHead"),
        pydantic.Field(alias="signedTreeHead", description="The current signed tree head"),
    ]
    """
    The current signed tree head
    """

    tree_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="treeID"), pydantic.Field(alias="treeID", description="The current treeID")
    ]
    """
    The current treeID
    """

    tree_size: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="treeSize"),
        pydantic.Field(alias="treeSize", description="The current number of nodes in the merkle tree"),
    ]
    """
    The current number of nodes in the merkle tree
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
