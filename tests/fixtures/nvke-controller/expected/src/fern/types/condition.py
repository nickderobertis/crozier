

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition_status import ConditionStatus


class Condition(UniversalBaseModel):
    """
    A status, when it last changed, and a message.
    """

    status: ConditionStatus = pydantic.Field()
    """
    Condition status.
    """

    last_transition_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastTransitionTime"),
        pydantic.Field(alias="lastTransitionTime", description="When the status last changed."),
    ]
    """
    When the status last changed.
    """

    message: str = pydantic.Field()
    """
    Human-readable detail. May be empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
