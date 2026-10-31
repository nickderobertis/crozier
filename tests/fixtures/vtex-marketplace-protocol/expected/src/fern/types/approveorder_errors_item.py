

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApproveorderErrorsItem(UniversalBaseModel):
    code: str = pydantic.Field()
    """
    String containing the code returned by the source. Example value: If the source is `Fulfillment`, the code can be FMT005 to indicate that the item(s) in the order are not available.
    """

    description: str = pydantic.Field()
    """
    String containing the error message/description returned by the source.
    """

    source: str = pydantic.Field()
    """
    Includes the following fields pointing out the context of the error: 
    
    `Fulfillment` 
    
    `Checkout` 
    
    `Order Integration`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
