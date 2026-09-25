

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class GroupConditional(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    payload: "GroupConditionalPayload" = pydantic.Field()
    """
    Group of conditions combined with AND/OR.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conditional import Conditional
from .group_conditional_payload import GroupConditionalPayload

update_forward_refs(GroupConditional, Conditional=Conditional, GroupConditionalPayload=GroupConditionalPayload)
