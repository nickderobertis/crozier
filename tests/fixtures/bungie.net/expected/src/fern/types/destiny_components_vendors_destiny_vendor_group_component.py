

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_components_vendors_destiny_vendor_group import DestinyComponentsVendorsDestinyVendorGroup


class DestinyComponentsVendorsDestinyVendorGroupComponent(UniversalBaseModel):
    """
    This component returns references to all of the Vendors in the response, grouped by categorizations that Bungie has deemed to be interesting, in the order in which both the groups and the vendors within that group should be rendered.
    """

    groups: typing.Optional[typing.List[DestinyComponentsVendorsDestinyVendorGroup]] = pydantic.Field(default=None)
    """
    The ordered list of groups being returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
