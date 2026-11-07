

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PersonalAccessTokenSecret(UniversalBaseModel):
    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    The secret
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique and public identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
