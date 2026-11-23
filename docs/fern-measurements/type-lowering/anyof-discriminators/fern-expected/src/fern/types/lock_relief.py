

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LockRelief_Volunteer(UniversalBaseModel):
    """
    One referenced member under a mapped discriminator.
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


LockRelief = LockRelief_Volunteer
