

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .claim_detail import ClaimDetail
from .verified_claim_detail import VerifiedClaimDetail


class ClaimUserinfo(UniversalBaseModel):
    name: typing.Optional[ClaimDetail] = None
    given_name: typing.Optional[ClaimDetail] = None
    email: typing.Optional[ClaimDetail] = None
    gender: typing.Optional[ClaimDetail] = None
    birthdate: typing.Optional[ClaimDetail] = None
    phone_number: typing.Optional[ClaimDetail] = None
    profile_photo: typing.Optional[ClaimDetail] = None
    address: typing.Optional[ClaimDetail] = None
    locale: typing.Optional[ClaimDetail] = None
    individual_id: typing.Optional[ClaimDetail] = None
    verified_claims: typing.Optional[typing.List[VerifiedClaimDetail]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
