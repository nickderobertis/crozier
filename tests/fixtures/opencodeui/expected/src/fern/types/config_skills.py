

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigSkills(UniversalBaseModel):
    """
    Additional skill folder paths
    """

    paths: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Additional paths to skill folders
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
