

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field import Field
from .single_conditional_payload_comparison import SingleConditionalPayloadComparison
from .single_conditional_payload_value import SingleConditionalPayloadValue


class SingleConditionalPayload(UniversalBaseModel):
    """
    Single condition comparing one field to a value.
    """

    field: Field
    comparison: SingleConditionalPayloadComparison = pydantic.Field()
    """
    Comparison operator for the condition.
    """

    value: typing.Optional[SingleConditionalPayloadValue] = pydantic.Field(default=None)
    """
    Comparison value or field reference. Nullable for empty checks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
