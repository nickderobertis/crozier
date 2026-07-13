

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorItem(UniversalBaseModel):
    error_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error description in English.
    """

    error_description_translated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error description translated to the user's language.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
