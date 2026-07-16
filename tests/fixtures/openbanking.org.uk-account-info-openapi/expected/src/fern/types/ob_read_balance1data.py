

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_balance1data_balance_item import ObReadBalance1DataBalanceItem


class ObReadBalance1Data(UniversalBaseModel):
    balance: typing_extensions.Annotated[
        typing.List[ObReadBalance1DataBalanceItem], FieldMetadata(alias="Balance"), pydantic.Field(alias="Balance")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
