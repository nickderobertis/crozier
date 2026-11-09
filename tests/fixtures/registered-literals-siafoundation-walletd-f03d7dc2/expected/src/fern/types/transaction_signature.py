

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .covered_fields import CoveredFields
from .hash256 import Hash256


class TransactionSignature(UniversalBaseModel):
    parent_id: typing_extensions.Annotated[Hash256, FieldMetadata(alias="parentID"), pydantic.Field(alias="parentID")]
    public_key_index: typing_extensions.Annotated[
        int, FieldMetadata(alias="publicKeyIndex"), pydantic.Field(alias="publicKeyIndex")
    ]
    timelock: typing.Optional[int] = None
    covered_fields: typing_extensions.Annotated[
        CoveredFields, FieldMetadata(alias="coveredFields"), pydantic.Field(alias="coveredFields")
    ]
    signature: str = pydantic.Field()
    """
    Hex-encoded signature.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
