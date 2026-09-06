

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ValidationErrorItem(UniversalBaseModel):
    """
    Validation errors have their own schema to provide context for invalid requests eg. mismatched types and out of bounds values. There may be any number of these per 422 UNPROCESSABLE ENTITY error.
    """

    loc: typing.List[str] = pydantic.Field()
    """
    The location as a [`Vec`] of [`String`]s -- often in the form `["body", "field_name"]`, `["query", "field_name"]`, etc. They may, however, be arbitrarily deep.
    """

    msg: str = pydantic.Field()
    """
    The message accompanying the validation error item.
    """

    type: str = pydantic.Field()
    """
    The type of error, often "type_error" or "value_error", but sometimes with more context like as "value_error.number.not_ge"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
