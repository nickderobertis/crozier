

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConsistencyProof(UniversalBaseModel):
    hashes: typing.List[str]
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
