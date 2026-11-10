

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProofDto(UniversalBaseModel):
    type: str
    created: dt.datetime
    verification_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="verificationMethod"), pydantic.Field(alias="verificationMethod")
    ]
    proof_purpose: typing_extensions.Annotated[
        str, FieldMetadata(alias="proofPurpose"), pydantic.Field(alias="proofPurpose")
    ]
    jws: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
