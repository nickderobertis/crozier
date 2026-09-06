

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.feedback_experiment_item import FeedbackExperimentItem
from ...types.insert_experiment_event import InsertExperimentEvent


class CrossObjectInsertRequestExperimentValue(UniversalBaseModel):
    events: typing.Optional[typing.List[InsertExperimentEvent]] = pydantic.Field(default=None)
    """
    A list of experiment events to insert
    """

    feedback: typing.Optional[typing.List[FeedbackExperimentItem]] = pydantic.Field(default=None)
    """
    A list of experiment feedback items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
