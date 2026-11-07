

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .validation_issue_value import ValidationIssueValue


class ValidationIssue(UniversalBaseModel):
    path: str
    value: ValidationIssueValue
    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional information about the error. Context dependant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
