

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .monetary_account_bank import MonetaryAccountBank
from .monetary_account_external import MonetaryAccountExternal
from .monetary_account_investment import MonetaryAccountInvestment
from .monetary_account_joint import MonetaryAccountJoint
from .monetary_account_light import MonetaryAccountLight
from .monetary_account_savings import MonetaryAccountSavings


class MonetaryAccountRead(UniversalBaseModel):
    monetary_account_bank: typing_extensions.Annotated[
        typing.Optional[MonetaryAccountBank], FieldMetadata(alias="MonetaryAccountBank")
    ] = pydantic.Field(default=None)
    """
    
    """

    monetary_account_external: typing_extensions.Annotated[
        typing.Optional[MonetaryAccountExternal], FieldMetadata(alias="MonetaryAccountExternal")
    ] = pydantic.Field(default=None)
    """
    
    """

    monetary_account_investment: typing_extensions.Annotated[
        typing.Optional[MonetaryAccountInvestment], FieldMetadata(alias="MonetaryAccountInvestment")
    ] = pydantic.Field(default=None)
    """
    
    """

    monetary_account_joint: typing_extensions.Annotated[
        typing.Optional[MonetaryAccountJoint], FieldMetadata(alias="MonetaryAccountJoint")
    ] = pydantic.Field(default=None)
    """
    
    """

    monetary_account_light: typing_extensions.Annotated[
        typing.Optional[MonetaryAccountLight], FieldMetadata(alias="MonetaryAccountLight")
    ] = pydantic.Field(default=None)
    """
    
    """

    monetary_account_savings: typing_extensions.Annotated[
        typing.Optional[MonetaryAccountSavings], FieldMetadata(alias="MonetaryAccountSavings")
    ] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
