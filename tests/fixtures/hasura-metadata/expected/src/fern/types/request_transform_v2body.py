

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RequestTransformV2Body_Remove(UniversalBaseModel):
    action: typing.Literal["remove"] = "remove"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RequestTransformV2Body_Transform(UniversalBaseModel):
    action: typing.Literal["transform"] = "transform"
    template: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RequestTransformV2Body_XWwwFormUrlencoded(UniversalBaseModel):
    action: typing.Literal["x_www_form_urlencoded"] = "x_www_form_urlencoded"
    form_template: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RequestTransformV2Body = typing_extensions.Annotated[
    typing.Union[
        RequestTransformV2Body_Remove, RequestTransformV2Body_Transform, RequestTransformV2Body_XWwwFormUrlencoded
    ],
    pydantic.Field(discriminator="action"),
]
