

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .evidence_check_detail_time import EvidenceCheckDetailTime


class EvidenceCheckDetail(UniversalBaseModel):
    """
    Object representing the checks done in relation to the evidence.

    The eKYC and Identity Assurance Working Group maintains a wiki page
    """

    check_method: str = pydantic.Field()
    """
    String representing the check done, this includes processes such as checking the authenticity of the document, or verifying the user's biometric against an identity document.
    """

    organization: typing.Optional[str] = pydantic.Field(default=None)
    """
    String denoting the legal entity that performed the check. This SHOULD be included if the OP did not perform the check itself.
    """

    txn: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier referring to the identity verification transaction.
    """

    time: typing.Optional[EvidenceCheckDetailTime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
