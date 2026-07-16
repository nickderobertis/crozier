

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dispute_evidence_file import DisputeEvidenceFile


class DisputeEvidence(UniversalBaseModel):
    """ """

    dispute_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the dispute the evidence is associated with.
    """

    evidence_file: typing.Optional[DisputeEvidenceFile] = None
    evidence_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the evidence.
    """

    evidence_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Raw text
    """

    evidence_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the evidence.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the evidence.
    """

    uploaded_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the next action is due, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
