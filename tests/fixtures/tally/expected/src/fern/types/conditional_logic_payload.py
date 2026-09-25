

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .conditional_action import ConditionalAction
from .conditional_logic_payload_logical_operator import ConditionalLogicPayloadLogicalOperator


class ConditionalLogicPayload(UniversalBaseModel):
    """
    Payload for CONDITIONAL_LOGIC block type. Used for form logic and branching.
    """

    conditionals: typing.List["Conditional"] = pydantic.Field()
    """
    Conditions that must be satisfied before actions run.
    """

    actions: typing.List[ConditionalAction] = pydantic.Field()
    """
    Actions executed when conditions are satisfied.
    """

    logical_operator: typing_extensions.Annotated[
        ConditionalLogicPayloadLogicalOperator,
        FieldMetadata(alias="logicalOperator"),
        pydantic.Field(alias="logicalOperator", description="How to combine top-level conditions (AND/OR)."),
    ]
    """
    How to combine top-level conditions (AND/OR).
    """

    update_uuid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updateUuid"),
        pydantic.Field(alias="updateUuid", description="UUID of the logic block being updated; null when creating."),
    ] = None
    """
    UUID of the logic block being updated; null when creating.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conditional import Conditional
from .group_conditional import GroupConditional
from .group_conditional_payload import GroupConditionalPayload

update_forward_refs(
    ConditionalLogicPayload,
    Conditional=Conditional,
    GroupConditional=GroupConditional,
    GroupConditionalPayload=GroupConditionalPayload,
)
