

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BillingPosition(UniversalBaseModel):
    amount: int
    count: float
    description: str
    service: str
    single_price: typing_extensions.Annotated[
        float, FieldMetadata(alias="singlePrice"), pydantic.Field(alias="singlePrice")
    ]
    sum: float
    unit: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
