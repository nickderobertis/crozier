

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkedInvoiceItem(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    User defined item code
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the linked item. A reference to the [invoice item](https://developers.apideck.com/apis/accounting/reference#tag/Invoice-Items) that was used to create this line item
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    User defined item name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
