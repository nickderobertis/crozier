

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feedback_dataset_item_source import FeedbackDatasetItemSource


class FeedbackDatasetItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The id of the dataset event to log feedback for. This is the row `id` returned by `POST /v1/dataset/{dataset_id}/insert`
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional comment string to log about the dataset event
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A dictionary with additional data about the feedback. If you have a `user_id`, you can log it here and access it in the Braintrust UI. Note, this metadata does not correspond to the main event itself, but rather the audit log attached to the event.
    """

    source: typing.Optional[FeedbackDatasetItemSource] = pydantic.Field(default=None)
    """
    The source of the feedback. Must be one of "external" (default), "app", or "api"
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tags to log
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
