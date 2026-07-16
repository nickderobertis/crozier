

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_active_or_historic_currency_and_amount5 import ObActiveOrHistoricCurrencyAndAmount5
from .ob_external_statement_benefit_type1code import ObExternalStatementBenefitType1Code


class ObStatement2StatementBenefitItem(UniversalBaseModel):
    """
    Set of elements used to provide details of a benefit or reward amount for the statement resource.
    """

    amount: typing_extensions.Annotated[ObActiveOrHistoricCurrencyAndAmount5, FieldMetadata(alias="Amount")]
    type: typing_extensions.Annotated[ObExternalStatementBenefitType1Code, FieldMetadata(alias="Type")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
