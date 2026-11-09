

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_info_fossology import ApiInfoFossology
from .api_info_license import ApiInfoLicense


class ApiInfo(UniversalBaseModel):
    """
    Info about the API
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the API service
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional information
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current API version as per documentation
    """

    security: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Security methods allowed
    """

    contact: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contact email from API docs
    """

    license: typing.Optional[ApiInfoLicense] = pydantic.Field(default=None)
    """
    Licensing of API
    """

    fossology: typing.Optional[ApiInfoFossology] = pydantic.Field(default=None)
    """
    Information about FOSSology server. Values can be null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
