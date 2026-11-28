

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WeavePlanThreadsItem_Warp(UniversalBaseModel):
    thread_type: typing_extensions.Annotated[
        typing.Literal["WARP"], FieldMetadata(alias="threadType"), pydantic.Field(alias="threadType")
    ] = "WARP"
    colour: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WeavePlanThreadsItem_Weft(UniversalBaseModel):
    thread_type: typing_extensions.Annotated[
        typing.Literal["WEFT"], FieldMetadata(alias="threadType"), pydantic.Field(alias="threadType")
    ] = "WEFT"
    count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


WeavePlanThreadsItem = typing_extensions.Annotated[
    typing.Union[WeavePlanThreadsItem_Warp, WeavePlanThreadsItem_Weft], pydantic.Field(discriminator="thread_type")
]
