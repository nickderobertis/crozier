

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostA2ARequestParamsMessageMessagePartsItem_Text(UniversalBaseModel):
    kind: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostA2ARequestParamsMessageMessagePartsItem_Data(UniversalBaseModel):
    kind: typing.Literal["data"] = "data"
    data: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostA2ARequestParamsMessageMessagePartsItem = typing_extensions.Annotated[
    typing.Union[PostA2ARequestParamsMessageMessagePartsItem_Text, PostA2ARequestParamsMessageMessagePartsItem_Data],
    pydantic.Field(discriminator="kind"),
]
