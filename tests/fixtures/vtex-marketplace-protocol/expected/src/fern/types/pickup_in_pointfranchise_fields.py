

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pickup_in_pointfranchise_fields_fields import PickupInPointfranchiseFieldsFields


class PickupInPointfranchiseFields(UniversalBaseModel):
    """
    Structure with important fields for the connector. This structure is only returned if the response is successful. Includes the following fields:

    `mainOrderId`: String with the order's ID inside the main seller account in VTEX.

    `franchiseOrderId`: - String with the order's ID inside the franchise seller account in VTEX. Only returned if the order was integrated using the [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) feature, that is:

    - `allowFranchises` field set to `true` when integrating the order

    - `SLA` chosen for the order is from a franchise account.
    """

    fields: typing.Optional[PickupInPointfranchiseFieldsFields] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
