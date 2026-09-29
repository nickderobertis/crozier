

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_detail_response_status import SessionDetailResponseStatus


class SessionDetailResponse(UniversalBaseModel):
    """
    Session detail — same public shape as the summary today.
    """

    id: str
    title: str
    status: SessionDetailResponseStatus
    checkpoint_version: int
    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
