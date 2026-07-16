

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dispute_evidence import DisputeEvidence
from .error import Error


class ListDisputeEvidenceResponse(UniversalBaseModel):
    """
    Defines the fields in a `ListDisputeEvidence` response.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request.
    If unset, this is the final response. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    evidence: typing.Optional[typing.List[DisputeEvidence]] = pydantic.Field(default=None)
    """
    The list of evidence previously uploaded to the specified dispute.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
