

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reasoning_message_source import ReasoningMessageSource


class ReasoningMessage(UniversalBaseModel):
    """
    Representation of an agent's internal reasoning.

    Args:
        id (str): The ID of the message
        date (datetime): The date the message was created in ISO format
        name (Optional[str]): The name of the sender of the message
        source (Literal["reasoner_model", "non_reasoner_model"]): Whether the reasoning
            content was generated natively by a reasoner model or derived via prompting
        reasoning (str): The internal reasoning of the agent
        signature (Optional[str]): The model-generated signature of the reasoning step
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
    source: typing.Optional[ReasoningMessageSource] = None
    reasoning: str
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
