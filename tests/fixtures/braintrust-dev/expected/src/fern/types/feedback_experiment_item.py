

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feedback_experiment_item_source import FeedbackExperimentItemSource


class FeedbackExperimentItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The id of the experiment event to log feedback for. This is the row `id` returned by `POST /v1/experiment/{experiment_id}/insert`
    """

    scores: typing.Optional[typing.Dict[str, typing.Optional[float]]] = pydantic.Field(default=None)
    """
    A dictionary of numeric values (between 0 and 1) to log. These scores will be merged into the existing scores for the experiment event
    """

    expected: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd compare to `output` to determine if your `output` value is correct or not
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional comment string to log about the experiment event
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A dictionary with additional data about the feedback. If you have a `user_id`, you can log it here and access it in the Braintrust UI. Note, this metadata does not correspond to the main event itself, but rather the audit log attached to the event.
    """

    source: typing.Optional[FeedbackExperimentItemSource] = pydantic.Field(default=None)
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
