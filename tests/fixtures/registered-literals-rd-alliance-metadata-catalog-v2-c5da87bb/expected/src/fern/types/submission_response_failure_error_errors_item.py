

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubmissionResponseFailureErrorErrorsItem(UniversalBaseModel):
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Nature of validation error.
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Object key where the error occurred, in JSONPath dot notation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
