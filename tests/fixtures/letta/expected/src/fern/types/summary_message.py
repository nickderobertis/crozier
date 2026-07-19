

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SummaryMessage(UniversalBaseModel):
    """
    A message representing a summary of the conversation. Sent to the LLM as a user or system message depending on the provider.
    """

    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    summary: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
