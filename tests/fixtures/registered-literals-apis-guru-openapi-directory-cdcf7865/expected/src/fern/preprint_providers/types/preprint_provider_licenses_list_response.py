

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preprint_provider_licenses_list_response_attributes import PreprintProviderLicensesListResponseAttributes
from .preprint_provider_licenses_list_response_links import PreprintProviderLicensesListResponseLinks


class PreprintProviderLicensesListResponse(UniversalBaseModel):
    attributes: typing.Optional[PreprintProviderLicensesListResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the license.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the license.
    """

    links: typing.Optional[PreprintProviderLicensesListResponseLinks] = pydantic.Field(default=None)
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
