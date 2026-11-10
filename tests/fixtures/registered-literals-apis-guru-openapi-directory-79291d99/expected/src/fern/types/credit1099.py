

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit1099filer import Credit1099Filer
from .credit1099payer import Credit1099Payer
from .credit1099recipient import Credit1099Recipient
from .credit_document_metadata import CreditDocumentMetadata
from .form1099type import Form1099Type


class Credit1099(UniversalBaseModel):
    """
    An object representing an end user's 1099 tax form
    """

    april_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for April.
    """

    august_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for August.
    """

    card_not_present_transaction: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount in card not present transactions.
    """

    crop_insurance_proceeds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of crop insurance proceeds.
    """

    december_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for December.
    """

    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier of the document referenced by the document metadata.
    """

    document_metadata: typing.Optional[CreditDocumentMetadata] = None
    excess_golden_parachute_payments: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of golden parachute payments made by payer.
    """

    february_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for February.
    """

    federal_income_tax_withheld: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of federal income tax withheld from payer.
    """

    filer: typing.Optional[Credit1099Filer] = None
    fishing_boat_proceeds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of fishing boat proceeds from payer.
    """

    form1099type: typing_extensions.Annotated[
        typing.Optional[Form1099Type], FieldMetadata(alias="form_1099_type"), pydantic.Field(alias="form_1099_type")
    ] = None
    gross_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Gross amount reported.
    """

    gross_proceeds_paid_to_an_attorney: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of gross proceeds paid to an attorney by payer.
    """

    january_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for January.
    """

    july_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for July.
    """

    june_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for June.
    """

    march_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for March.
    """

    may_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for May.
    """

    medical_and_healthcare_payments: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of medical and healthcare payments from payer.
    """

    merchant_category_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Merchant category of filer.
    """

    nonemployee_compensation: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of nonemployee compensation from payer.
    """

    november_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for November.
    """

    number_of_payment_transactions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Number of payment transactions made.
    """

    october_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for October.
    """

    other_income: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount in other income by payer.
    """

    payer: typing.Optional[Credit1099Payer] = None
    payer_made_direct_sales_of5000or_more_of_consumer_products_to_buyer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer"),
        pydantic.Field(
            alias="payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer",
            description="Whether or not payer made direct sales over $5000 of consumer products.",
        ),
    ] = None
    """
    Whether or not payer made direct sales over $5000 of consumer products.
    """

    payer_state_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary state ID.
    """

    payer_state_number_lower: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secondary state ID.
    """

    primary_state: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary state of business.
    """

    primary_state_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary state ID.
    """

    primary_state_income_tax: typing.Optional[float] = pydantic.Field(default=None)
    """
    State income tax reported for primary state.
    """

    pse_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the PSE (Payment Settlement Entity).
    """

    pse_telephone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity).
    """

    recipient: typing.Optional[Credit1099Recipient] = None
    rents: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount in rent by payer.
    """

    royalties: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount in royalties by payer.
    """

    secondary_state: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secondary state of business.
    """

    secondary_state_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secondary state ID.
    """

    secondary_state_income_tax: typing.Optional[float] = pydantic.Field(default=None)
    """
    State income tax reported for secondary state.
    """

    section409a_deferrals: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="section_409a_deferrals"),
        pydantic.Field(alias="section_409a_deferrals", description="Amount of 409A deferrals earned by payer."),
    ] = None
    """
    Amount of 409A deferrals earned by payer.
    """

    section409a_income: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="section_409a_income"),
        pydantic.Field(alias="section_409a_income", description="Amount of 409A income earned by payer."),
    ] = None
    """
    Amount of 409A income earned by payer.
    """

    september_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount reported for September.
    """

    state_income: typing.Optional[float] = pydantic.Field(default=None)
    """
    State income reported for primary state.
    """

    state_income_lower: typing.Optional[float] = pydantic.Field(default=None)
    """
    State income reported for secondary state.
    """

    state_tax_withheld: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of state tax withheld of payer for primary state.
    """

    state_tax_withheld_lower: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of state tax withheld of payer for secondary state.
    """

    substitute_payments_in_lieu_of_dividends_or_interest: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of substitute payments made by payer.
    """

    tax_year: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tax year of the tax form.
    """

    transactions_reported: typing.Optional[str] = pydantic.Field(default=None)
    """
    One of the values will be provided Payment card Third party network
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
