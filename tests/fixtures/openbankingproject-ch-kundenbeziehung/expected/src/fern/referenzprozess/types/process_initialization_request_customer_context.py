

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ProcessInitializationRequestCustomerContext(UniversalBaseModel):
    existing_customer: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="existingCustomer"), pydantic.Field(alias="existingCustomer")
    ] = None
    customer_hint: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="customerHint"), pydantic.Field(alias="customerHint")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
