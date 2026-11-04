

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LicensesReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the license.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the license.
    """

    required_fields: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fields required for this license (provided to help front-end validators). Maps to properties on the NodeLicense model.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full text of the license.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
