

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBody(UniversalBaseModel):
    error: typing.Optional[str] = None
    expected_checksum: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present when checksum validation fails
    """

    actual_checksum: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present when checksum validation fails
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
