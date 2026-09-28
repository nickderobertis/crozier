

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .status_ok_response_status import StatusOkResponseStatus


class StatusOkResponse(UniversalBaseModel):
    """
    `{status:"ok"}` envelope used by reviewReply and refreshReviews.
    Enum-pinned variant of `StatusOKResponse`.
    """

    status: StatusOkResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
