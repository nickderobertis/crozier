

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_session_error import CreditSessionError
from .credit_session_results import CreditSessionResults


class CreditSession(UniversalBaseModel):
    """
    Metadata and results for a Link session
    """

    errors: typing.Optional[typing.List[CreditSessionError]] = pydantic.Field(default=None)
    """
    The set of errors that occurred during the Link session.
    """

    link_session_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier associated with the Link session. This identifier matches the `link_session_id` returned in the onSuccess/onExit callbacks.
    """

    results: typing.Optional[CreditSessionResults] = None
    session_start_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the Link session started
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
