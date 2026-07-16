

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem(
    UniversalBaseModel
):
    """
    Other fee type code which is not available in the standard code set
    """

    code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Code")] = pydantic.Field(default=None)
    """
    The four letter Mnemonic used within an XML file to identify a code
    """

    description: typing_extensions.Annotated[str, FieldMetadata(alias="Description")] = pydantic.Field()
    """
    Description to describe the purpose of the code
    """

    name: typing_extensions.Annotated[str, FieldMetadata(alias="Name")] = pydantic.Field()
    """
    Long name associated with the code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
