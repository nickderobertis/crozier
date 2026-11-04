

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBodyErrorCode(UniversalBaseModel):
    instance: str = pydantic.Field()
    """
    Unique identifier of this error occurrence.
    """

    error_code: str = pydantic.Field()
    """
    Platform code for the error.
    """

    error_message: str = pydantic.Field()
    """
    Short description of the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
