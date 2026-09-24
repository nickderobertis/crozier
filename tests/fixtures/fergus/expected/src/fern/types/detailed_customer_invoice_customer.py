

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class DetailedCustomerInvoiceCustomer(UniversalBaseModel):
    id: float
    customer_full_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="customerFullName"), pydantic.Field(alias="customerFullName")
    ]
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
