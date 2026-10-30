

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GeneralAuth(UniversalBaseModel):
    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Any other general authentication data to save
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
