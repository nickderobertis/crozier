

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conditional_action_payload import ConditionalActionPayload
from .conditional_action_type import ConditionalActionType


class ConditionalAction(UniversalBaseModel):
    """
    Conditional action wrapper.
    """

    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    type: ConditionalActionType = pydantic.Field()
    """
    Action type; determines which payload fields are relevant.
    """

    payload: typing.Optional[ConditionalActionPayload] = pydantic.Field(default=None)
    """
    Action details executed when conditions match.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
