

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_field_value import CustomFieldValue


class CustomField(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    More information about the custom field
    """

    id: str
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the custom field.
    """

    value: typing.Optional[CustomFieldValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
