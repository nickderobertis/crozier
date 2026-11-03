

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Side_Herb(UniversalBaseModel):
    """
    A side dish of one kind or another.
    """

    kind: typing.Literal["herb"] = "herb"
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Side_Grain(UniversalBaseModel):
    """
    A side dish of one kind or another.
    """

    kind: typing.Literal["grain"] = "grain"
    cups: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Side = typing_extensions.Annotated[typing.Union[Side_Herb, Side_Grain], pydantic.Field(discriminator="kind")]
