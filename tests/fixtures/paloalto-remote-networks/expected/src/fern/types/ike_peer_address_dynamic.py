

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IkePeerAddressDynamic(UniversalBaseModel):
    dynamic: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    enable dynamic option please set the value of this field to {'': ''}
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
