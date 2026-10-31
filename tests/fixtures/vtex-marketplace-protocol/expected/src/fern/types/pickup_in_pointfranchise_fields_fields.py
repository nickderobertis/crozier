

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PickupInPointfranchiseFieldsFields(UniversalBaseModel):
    franchise_order_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="franchiseOrderId"),
        pydantic.Field(
            alias="franchiseOrderId",
            description="String with the order's ID inside the franchise seller account in VTEX. Only returned if the order was integrated using the [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) feature, that is: \n\n- `allowFranchises` field set to `true` when integrating the order \r\n- SLA chosen for the order is from a franchise account",
        ),
    ] = None
    """
    String with the order's ID inside the franchise seller account in VTEX. Only returned if the order was integrated using the [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) feature, that is: 
    
    - `allowFranchises` field set to `true` when integrating the order 
    - SLA chosen for the order is from a franchise account
    """

    main_order_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="mainOrderId"),
        pydantic.Field(
            alias="mainOrderId", description="String with the order’s ID inside the main seller account in VTEX."
        ),
    ]
    """
    String with the order’s ID inside the main seller account in VTEX.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
