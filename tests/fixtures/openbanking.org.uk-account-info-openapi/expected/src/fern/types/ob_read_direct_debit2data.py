

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_direct_debit2data_direct_debit_item import ObReadDirectDebit2DataDirectDebitItem


class ObReadDirectDebit2Data(UniversalBaseModel):
    direct_debit: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadDirectDebit2DataDirectDebitItem]], FieldMetadata(alias="DirectDebit")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
