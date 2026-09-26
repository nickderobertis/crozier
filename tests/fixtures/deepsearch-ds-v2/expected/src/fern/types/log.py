

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Log(UniversalBaseModel):
    """
    Log entry to describe an ETL task on a document.
    """

    task: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier of this task. It may be used to identify this task from other tasks of the same agent and type.
    """

    agent: str = pydantic.Field()
    """
    The Docling agent that performed the task, e.g., CCS or CXS.
    """

    type: str = pydantic.Field()
    """
    A task category.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the task or any comments in natural language.
    """

    date: dt.datetime = pydantic.Field()
    """
    A string representation of the task execution datetime in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
