

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_contract_id import FileContractId
from .hash256 import Hash256


class StorageProof(UniversalBaseModel):
    parent_id: typing_extensions.Annotated[
        FileContractId, FieldMetadata(alias="parentID"), pydantic.Field(alias="parentID")
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
