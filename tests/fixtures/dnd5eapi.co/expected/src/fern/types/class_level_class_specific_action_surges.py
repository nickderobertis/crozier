

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClassLevelClassSpecificActionSurges(UniversalBaseModel):
    """
    Fighter Class Specific Features
    """

    action_surges: typing.Optional[float] = None
    extra_attacks: typing.Optional[float] = None
    indomitable_uses: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
