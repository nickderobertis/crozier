

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037UserDefault(UniversalBaseModel):
    """
    Default settings
    """

    account: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default account name
    """

    wckey: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default wckey
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
