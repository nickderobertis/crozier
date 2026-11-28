

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WeavePlanPattern_Plain(UniversalBaseModel):
    """
    The weave's pattern.
    """

    kind: typing.Literal["PLAIN"] = "PLAIN"
    rows: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WeavePlanPattern_Twill(UniversalBaseModel):
    """
    The weave's pattern.
    """

    kind: typing.Literal["TWILL"] = "TWILL"
    angle: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


WeavePlanPattern = typing_extensions.Annotated[
    typing.Union[WeavePlanPattern_Plain, WeavePlanPattern_Twill], pydantic.Field(discriminator="kind")
]
