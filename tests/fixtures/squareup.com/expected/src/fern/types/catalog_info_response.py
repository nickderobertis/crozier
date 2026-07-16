

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_info_response_limits import CatalogInfoResponseLimits
from .error import Error
from .standard_unit_description_group import StandardUnitDescriptionGroup


class CatalogInfoResponse(UniversalBaseModel):
    """ """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    limits: typing.Optional[CatalogInfoResponseLimits] = None
    standard_unit_description_group: typing.Optional[StandardUnitDescriptionGroup] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
