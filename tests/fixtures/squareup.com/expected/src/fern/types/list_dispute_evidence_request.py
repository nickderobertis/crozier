

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListDisputeEvidenceRequest(UniversalBaseModel):
    """
    Defines the parameters for a `ListDisputeEvidence` request.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this cursor to retrieve the next set of results for the original query.
    For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
