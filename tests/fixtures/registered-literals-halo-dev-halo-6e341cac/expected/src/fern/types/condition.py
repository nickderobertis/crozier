

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition_status import ConditionStatus


class Condition(UniversalBaseModel):
    """
    EqualsAndHashCode 排除了lastTransitionTime否则失败时，lastTransitionTime 会被更新 导致 equals 为 false，一直被加入队列.
    """

    last_transition_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastTransitionTime"),
        pydantic.Field(
            alias="lastTransitionTime", description="Last time the condition transitioned from one status to another."
        ),
    ]
    """
    Last time the condition transitioned from one status to another.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable message indicating details about last transition. This may be an empty string.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique, one-word, CamelCase reason for the condition's last transition.
    """

    status: ConditionStatus = pydantic.Field()
    """
    Status is the status of the condition. Can be True, False, Unknown.
    """

    type: str = pydantic.Field()
    """
    type of condition in CamelCase or in foo.example.com/CamelCase. example: Ready, Initialized. maxLength: 316.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
