

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_kiosks_destiny_kiosk_item import DestinyComponentsKiosksDestinyKioskItem


class DestinyComponentsKiosksDestinyKiosksComponent(UniversalBaseModel):
    """
    A Kiosk is a Vendor (DestinyVendorDefinition) that sells items based on whether you have already acquired that item before.
    This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the individual character's DestinyCharacterKiosksComponent.
    Note that, because this component returns vendorItemIndexes (that is to say, indexes into the Kiosk Vendor's itemList property), these results are necessarily content version dependent. Make sure that you have the latest version of the content manifest databases before using this data.
    """

    kiosk_items: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.List[DestinyComponentsKiosksDestinyKioskItem]]],
        FieldMetadata(alias="kioskItems"),
    ] = pydantic.Field(default=None)
    """
    A dictionary keyed by the Kiosk Vendor's hash identifier (use it to look up the DestinyVendorDefinition for the relevant kiosk vendor), and whose value is a list of all the items that the user can "see" in the Kiosk, and any other interesting metadata.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
