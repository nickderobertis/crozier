

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .config_option import ConfigOption


class ConfigSection(UniversalBaseModel):
    """
    The section of configuration.
    """

    name: typing.Optional[str] = None
    options: typing.Optional[typing.List[ConfigOption]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
