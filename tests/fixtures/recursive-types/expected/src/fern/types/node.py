

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Node_And(UniversalBaseModel):
    kind: typing.Literal["and"] = "and"
    children: typing.List["Node"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Node_Leaf(UniversalBaseModel):
    kind: typing.Literal["leaf"] = "leaf"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Node = typing_extensions.Annotated[typing.Union[Node_And, Node_Leaf], pydantic.Field(discriminator="kind")]
update_forward_refs(Node_And)
