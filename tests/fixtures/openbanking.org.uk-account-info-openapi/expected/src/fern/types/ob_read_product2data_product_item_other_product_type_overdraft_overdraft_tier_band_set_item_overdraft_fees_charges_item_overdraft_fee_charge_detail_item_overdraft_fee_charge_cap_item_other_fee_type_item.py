

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .description3 import Description3
from .name4 import Name4
from .ob_code_mnemonic import ObCodeMnemonic


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem(
    UniversalBaseModel
):
    """
    Other fee type code which is not available in the standard code set
    """

    code: typing_extensions.Annotated[typing.Optional[ObCodeMnemonic], FieldMetadata(alias="Code")] = None
    description: typing_extensions.Annotated[Description3, FieldMetadata(alias="Description")]
    name: typing_extensions.Annotated[Name4, FieldMetadata(alias="Name")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
