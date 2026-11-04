

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .license_list_response_item_attributes import LicenseListResponseItemAttributes
from .license_list_response_item_links import LicenseListResponseItemLinks


class LicenseListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[LicenseListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the license.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the license.
    """

    links: typing.Optional[LicenseListResponseItemLinks] = pydantic.Field(default=None)
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
