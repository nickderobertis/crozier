

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_session import CreditSession
from .request_id import RequestId


class CreditSessionsGetResponse(UniversalBaseModel):
    """
    CreditSessionsGetResponse defines the response schema for `/credit/sessions/get`
    """

    request_id: RequestId
    sessions: typing.Optional[typing.List[CreditSession]] = pydantic.Field(default=None)
    """
    A list of Link sessions for the user. Sessions will be sorted in reverse chronological order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
