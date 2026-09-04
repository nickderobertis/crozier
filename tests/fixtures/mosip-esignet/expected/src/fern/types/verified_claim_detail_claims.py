

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .claim_detail import ClaimDetail


class VerifiedClaimDetailClaims(UniversalBaseModel):
    """
    Object that is the container for the Verified Claims about the End-User.
    """

    name: typing.Optional[ClaimDetail] = None
    email: typing.Optional[ClaimDetail] = None
    phone_number: typing.Optional[ClaimDetail] = None
    birth_date: typing_extensions.Annotated[
        typing.Optional[ClaimDetail], FieldMetadata(alias="birthDate"), pydantic.Field(alias="birthDate")
    ] = None
    address: typing.Optional[ClaimDetail] = None
    given_name: typing.Optional[ClaimDetail] = None
    gender: typing.Optional[ClaimDetail] = None
    profile_photo: typing.Optional[ClaimDetail] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
