

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .single_conditional_payload import SingleConditionalPayload


class Conditional_Single(UniversalBaseModel):
    """
    Union of single and group conditionals.
    """

    type: typing.Literal["SINGLE"] = "SINGLE"
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    payload: SingleConditionalPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Conditional_Group(UniversalBaseModel):
    """
    Union of single and group conditionals.
    """

    type: typing.Literal["GROUP"] = "GROUP"
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    payload: "GroupConditionalPayload"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Conditional = typing_extensions.Annotated[
    typing.Union[Conditional_Single, Conditional_Group], pydantic.Field(discriminator="type")
]
from .group_conditional_payload import GroupConditionalPayload

update_forward_refs(Conditional_Group, Conditional=Conditional, GroupConditionalPayload=GroupConditionalPayload)
