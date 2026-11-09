

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identity_verification_template_id import IdentityVerificationTemplateId
from .identity_verification_template_version import IdentityVerificationTemplateVersion


class IdentityVerificationTemplateReference(UniversalBaseModel):
    """
    The resource ID and version number of the template configuring the behavior of a given identity verification.
    """

    id: IdentityVerificationTemplateId
    version: IdentityVerificationTemplateVersion

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
