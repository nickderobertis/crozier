

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EnvVar(UniversalBaseModel):
    key: typing.Optional[str] = None
    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional free-form text for annotating the environment variable.
    """

    precedence: typing.Optional[int] = None
    used: typing.Optional[bool] = None
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
