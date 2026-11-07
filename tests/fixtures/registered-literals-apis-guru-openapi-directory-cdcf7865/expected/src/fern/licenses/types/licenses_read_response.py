

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .licenses_read_response_attributes import LicensesReadResponseAttributes
from .licenses_read_response_links import LicensesReadResponseLinks


class LicensesReadResponse(UniversalBaseModel):
    attributes: typing.Optional[LicensesReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the license.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the license.
    """

    links: typing.Optional[LicensesReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the license.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the license (`license`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
