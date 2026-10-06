

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cause_exception import CauseException
from .query_execution_message_level import QueryExecutionMessageLevel
from .query_execution_message_properties import QueryExecutionMessageProperties


class QueryExecutionMessage(UniversalBaseModel):
    """
    A message object that informs or warns about a query execution issue.
    """

    message: str = pydantic.Field()
    """
    A human readable message.
    """

    level: QueryExecutionMessageLevel
    timestamp: dt.datetime
    action: str = pydantic.Field()
    """
    The request action that caused this message.
    """

    category: str = pydantic.Field()
    """
    The subsystem that issued this message.
    """

    properties: typing.Optional[QueryExecutionMessageProperties] = None
    exception: typing.Optional[CauseException] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
