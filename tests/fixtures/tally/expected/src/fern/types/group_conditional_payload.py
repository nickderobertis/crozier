

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .group_conditional_payload_logical_operator import GroupConditionalPayloadLogicalOperator


class GroupConditionalPayload(UniversalBaseModel):
    """
    Group of conditions combined with AND/OR.
    """

    logical_operator: typing_extensions.Annotated[
        GroupConditionalPayloadLogicalOperator,
        FieldMetadata(alias="logicalOperator"),
        pydantic.Field(alias="logicalOperator", description="How to combine child conditions (AND/OR)."),
    ]
    """
    How to combine child conditions (AND/OR).
    """

    conditionals: typing.List["Conditional"] = pydantic.Field()
    """
    Child conditions in this group.
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

update_forward_refs(GroupConditionalPayload, Conditional=Conditional, GroupConditional=GroupConditional)
