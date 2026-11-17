

import typing

from .pallet_consignment import PalletConsignment
from .parcel_consignment import ParcelConsignment

Consignment = typing.Union[ParcelConsignment, PalletConsignment]
