

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RequestInquiryReference(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the request inquiry (batch).
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of request inquiry. Can be RequestInquiry or RequestInquiryBatch.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
