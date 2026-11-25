

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LockCrew_Lockkeeper(UniversalBaseModel):
    """
    A typed, required tag under an anyOf without a mapping.
    """

    role: typing.Literal["lockkeeper"] = "lockkeeper"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LockCrew_Volunteer(UniversalBaseModel):
    """
    A typed, required tag under an anyOf without a mapping.
    """

    role: typing.Literal["volunteer"] = "volunteer"
    hours: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LockCrew = typing_extensions.Annotated[
    typing.Union[LockCrew_Lockkeeper, LockCrew_Volunteer], pydantic.Field(discriminator="role")
]
