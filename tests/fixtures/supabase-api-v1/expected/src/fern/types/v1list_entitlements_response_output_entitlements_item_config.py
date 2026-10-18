

import typing

from .v1list_entitlements_response_output_entitlements_item_config_enabled import (
    V1ListEntitlementsResponseOutputEntitlementsItemConfigEnabled,
)
from .v1list_entitlements_response_output_entitlements_item_config_unit import (
    V1ListEntitlementsResponseOutputEntitlementsItemConfigUnit,
)
from .v1list_entitlements_response_output_entitlements_item_config_zero import (
    V1ListEntitlementsResponseOutputEntitlementsItemConfigZero,
)

V1ListEntitlementsResponseOutputEntitlementsItemConfig = typing.Union[
    V1ListEntitlementsResponseOutputEntitlementsItemConfigZero,
    V1ListEntitlementsResponseOutputEntitlementsItemConfigUnit,
    V1ListEntitlementsResponseOutputEntitlementsItemConfigEnabled,
]
