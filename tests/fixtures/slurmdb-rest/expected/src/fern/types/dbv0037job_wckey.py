

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobWckey(UniversalBaseModel):
    """
    Job assigned wckey details
    """

    wckey: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job assigned wckey
    """

    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    wckey flags
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
