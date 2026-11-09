

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .unlock_key import UnlockKey


class UnlockConditions(UniversalBaseModel):
    timelock: int
    public_keys: typing_extensions.Annotated[
        typing.List[UnlockKey], FieldMetadata(alias="publicKeys"), pydantic.Field(alias="publicKeys")
    ]
    signatures_required: typing_extensions.Annotated[
        int, FieldMetadata(alias="signaturesRequired"), pydantic.Field(alias="signaturesRequired")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
