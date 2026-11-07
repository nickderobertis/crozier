

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .event import Event
from .file import File
from .hyper_parameters import HyperParameters
from .state import State
from .type_discriminator import TypeDiscriminator


class FineTune(UniversalBaseModel):
    """
    Fine tuning is a job to tailor a model to specific training data.
    """

    object: typing.Optional[TypeDiscriminator] = None
    status: typing.Optional[State] = None
    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    A timestamp when this job or item was created (in unix epochs).
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    A timestamp when this job or item was modified last (in unix epochs).
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identity of this item.
    """

    model: str = pydantic.Field()
    """
    The identifier (model-id) of the base model used for the fine-tune.
    """

    fine_tuned_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier (model-id) of the resulting fine tuned model. This property is only populated for successfully completed fine-tune runs.
    Use this identifier to create a deployment for inferencing.
    """

    training_files: typing.List[File] = pydantic.Field()
    """
    The file identities (file-id) that are used for training the fine tuned model.
    """

    validation_files: typing.Optional[typing.List[File]] = pydantic.Field(default=None)
    """
    The file identities (file-id) that are used to evaluate the fine tuned model during training.
    """

    result_files: typing.Optional[typing.List[File]] = pydantic.Field(default=None)
    """
    The result file identities (file-id) containing training and evaluation metrics in csv format.
    The file is only available for successfully completed fine-tune runs.
    """

    events: typing.Optional[typing.List[Event]] = pydantic.Field(default=None)
    """
    The events that show the progress of the fine-tune run including queued, running and completed.
    """

    organisation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The organisation id of this fine tune job. Unused on Azure OpenAI; compatibility for OpenAI only.
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user id of this fine tune job. Unused on Azure OpenAI; compatibility for OpenAI only.
    """

    hyperparams: typing.Optional[HyperParameters] = None
    suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    The suffix used to identify the fine-tuned model.
    """

    error: typing.Optional["Error"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .error import Error

update_forward_refs(FineTune, Error=Error)
