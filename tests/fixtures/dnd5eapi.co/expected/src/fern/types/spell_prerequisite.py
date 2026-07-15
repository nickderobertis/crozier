

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference


class SpellPrerequisite(ApiReference):
    """
    `SpellPrerequisite`
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of prerequisite.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
