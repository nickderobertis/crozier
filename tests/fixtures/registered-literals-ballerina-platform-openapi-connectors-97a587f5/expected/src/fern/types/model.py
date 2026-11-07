

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .capabilities import Capabilities
from .deprecation import Deprecation
from .life_cycle_status import LifeCycleStatus
from .state import State
from .type_discriminator import TypeDiscriminator


class Model(UniversalBaseModel):
    """
    A model is either a base model or the result of a successful fine tune job.
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

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The base model identity (model-id) if this is a fine tune model; otherwise `null`.
    """

    fine_tune: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fine tune job identity (fine-tune-id) if this is a fine tune model; otherwise `null`.
    """

    capabilities: Capabilities
    lifecycle_status: LifeCycleStatus
    deprecation: Deprecation

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
