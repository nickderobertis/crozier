

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.feedback_dataset_item import FeedbackDatasetItem
from ...types.insert_dataset_event import InsertDatasetEvent


class CrossObjectInsertRequestDatasetValue(UniversalBaseModel):
    events: typing.Optional[typing.List[InsertDatasetEvent]] = pydantic.Field(default=None)
    """
    A list of dataset events to insert
    """

    feedback: typing.Optional[typing.List[FeedbackDatasetItem]] = pydantic.Field(default=None)
    """
    A list of dataset feedback items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
