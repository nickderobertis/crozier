

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SettingRef(UniversalBaseModel):
    """
    Reference to a setting definition used by this provider.
    """

    group: str = pydantic.Field()
    """
    Setting form group name.
    """

    name: str = pydantic.Field()
    """
    Setting metadata.name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
