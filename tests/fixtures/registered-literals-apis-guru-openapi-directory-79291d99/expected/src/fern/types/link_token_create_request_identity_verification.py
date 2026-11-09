

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identity_verification_consent import IdentityVerificationConsent
from .identity_verification_template_id import IdentityVerificationTemplateId


class LinkTokenCreateRequestIdentityVerification(UniversalBaseModel):
    """
    Specifies option for initializing Link for use with the Identity Verification product.
    """

    consent: typing.Optional[IdentityVerificationConsent] = None
    gave_consent: typing.Optional[IdentityVerificationConsent] = None
    template_id: IdentityVerificationTemplateId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
