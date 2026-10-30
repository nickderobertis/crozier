

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FulfillmentSimulationResponseItemsItemOfferingsItem(UniversalBaseModel):
    """
    Services that may be offered for this SKU. example are the assembly of a piece of furniture or warranty. In case these information are sent, the following fields are mandatory. If you don’t want to send it, use an empty array.
    """

    id: str = pydantic.Field()
    """
    Service ID.
    """

    name: str = pydantic.Field()
    """
    Service name.
    """

    price: int = pydantic.Field()
    """
    Service price. The last two digits are the cents.
    """

    type: str = pydantic.Field()
    """
    Type of the service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
