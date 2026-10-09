

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Notice_DoorLocked(UniversalBaseModel):
    kind: typing.Literal["door.locked"] = "door.locked"
    door: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Notice_DoorUnlocked(UniversalBaseModel):
    kind: typing.Literal["door.unlocked"] = "door.unlocked"
    door: str
    keyholder: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Notice = typing_extensions.Annotated[
    typing.Union[Notice_DoorLocked, Notice_DoorUnlocked], pydantic.Field(discriminator="kind")
]
