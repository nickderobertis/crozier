

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .creation_date_time import CreationDateTime
from .end_date_time import EndDateTime
from .ob_external_statement_type1code import ObExternalStatementType1Code
from .ob_statement2detail_statement_amount_item import ObStatement2DetailStatementAmountItem
from .ob_statement2detail_statement_benefit_item import ObStatement2DetailStatementBenefitItem
from .ob_statement2detail_statement_date_time_item import ObStatement2DetailStatementDateTimeItem
from .ob_statement2detail_statement_fee_item import ObStatement2DetailStatementFeeItem
from .ob_statement2detail_statement_interest_item import ObStatement2DetailStatementInterestItem
from .ob_statement2detail_statement_rate_item import ObStatement2DetailStatementRateItem
from .ob_statement2detail_statement_value_item import ObStatement2DetailStatementValueItem
from .start_date_time import StartDateTime
from .statement_id import StatementId
from .statement_reference import StatementReference


class ObStatement2Detail(UniversalBaseModel):
    """
    Provides further details on a statement resource.
    """

    account_id: typing_extensions.Annotated[AccountId, FieldMetadata(alias="AccountId")]
    creation_date_time: typing_extensions.Annotated[CreationDateTime, FieldMetadata(alias="CreationDateTime")]
    end_date_time: typing_extensions.Annotated[EndDateTime, FieldMetadata(alias="EndDateTime")]
    start_date_time: typing_extensions.Annotated[StartDateTime, FieldMetadata(alias="StartDateTime")]
    statement_amount: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2DetailStatementAmountItem]], FieldMetadata(alias="StatementAmount")
    ] = None
    statement_benefit: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2DetailStatementBenefitItem]], FieldMetadata(alias="StatementBenefit")
    ] = None
    statement_date_time: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2DetailStatementDateTimeItem]], FieldMetadata(alias="StatementDateTime")
    ] = None
    statement_description: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="StatementDescription")
    ] = None
    statement_fee: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2DetailStatementFeeItem]], FieldMetadata(alias="StatementFee")
    ] = None
    statement_id: typing_extensions.Annotated[typing.Optional[StatementId], FieldMetadata(alias="StatementId")] = None
    statement_interest: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2DetailStatementInterestItem]], FieldMetadata(alias="StatementInterest")
    ] = None
    statement_rate: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2DetailStatementRateItem]], FieldMetadata(alias="StatementRate")
    ] = None
    statement_reference: typing_extensions.Annotated[
        typing.Optional[StatementReference], FieldMetadata(alias="StatementReference")
    ] = None
    statement_value: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2DetailStatementValueItem]], FieldMetadata(alias="StatementValue")
    ] = None
    type: typing_extensions.Annotated[ObExternalStatementType1Code, FieldMetadata(alias="Type")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
