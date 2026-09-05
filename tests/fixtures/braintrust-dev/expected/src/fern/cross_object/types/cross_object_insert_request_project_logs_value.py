

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.feedback_project_logs_item import FeedbackProjectLogsItem
from ...types.insert_project_logs_event import InsertProjectLogsEvent


class CrossObjectInsertRequestProjectLogsValue(UniversalBaseModel):
    events: typing.Optional[typing.List[InsertProjectLogsEvent]] = pydantic.Field(default=None)
    """
    A list of project logs events to insert
    """

    feedback: typing.Optional[typing.List[FeedbackProjectLogsItem]] = pydantic.Field(default=None)
    """
    A list of project logs feedback items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
