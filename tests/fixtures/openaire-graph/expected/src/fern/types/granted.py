

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Granted(UniversalBaseModel):
    currency: typing.Optional[str] = None
    total_cost: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="totalCost"), pydantic.Field(alias="totalCost")
    ] = None
    funded_amount: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="fundedAmount"), pydantic.Field(alias="fundedAmount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
