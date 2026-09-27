

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ValidationErrorResponse(UniversalBaseModel):
    """
    Field-level validation error envelope; emitted by writeValidationError.
    `error` carries a localized summary; `fields` maps field name to
    localized per-field message keyed by validator/v10 tag.
    """

    error: str
    fields: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
