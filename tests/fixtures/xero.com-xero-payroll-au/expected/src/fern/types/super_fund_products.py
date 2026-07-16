

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .super_fund_product import SuperFundProduct


class SuperFundProducts(UniversalBaseModel):
    super_fund_products: typing_extensions.Annotated[
        typing.Optional[typing.List[SuperFundProduct]],
        FieldMetadata(alias="SuperFundProducts"),
        pydantic.Field(alias="SuperFundProducts"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
