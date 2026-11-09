

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PacerSearchReceipt(UniversalBaseModel):
    billable_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="billablePages"),
        pydantic.Field(alias="billablePages", description="No of pages that was billed for the given PACER search."),
    ]
    """
    No of pages that was billed for the given PACER search.
    """

    client_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientCode"),
        pydantic.Field(alias="clientCode", description="client code added if any was set."),
    ] = None
    """
    client code added if any was set.
    """

    cso_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="csoId"),
        pydantic.Field(alias="csoId", description="PACER Account ID."),
    ] = None
    """
    PACER Account ID.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the search made.
    """

    firm_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firmId"), pydantic.Field(alias="firmId", description="Firm ID.")
    ] = None
    """
    Firm ID.
    """

    login_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="loginId"),
        pydantic.Field(alias="loginId", description="ID which is used for PACER login."),
    ]
    """
    ID which is used for PACER login.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    report_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="reportId"),
        pydantic.Field(alias="reportId", description="Report ID for the search made."),
    ] = None
    """
    Report ID for the search made.
    """

    search: typing.Optional[str] = pydantic.Field(default=None)
    """
    Details of the search made for this request.
    """

    search_fee: typing_extensions.Annotated[
        str, FieldMetadata(alias="searchFee"), pydantic.Field(alias="searchFee", description="PACER Search Fee.")
    ]
    """
    PACER Search Fee.
    """

    transaction_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="transactionDate"),
        pydantic.Field(
            alias="transactionDate", description="Date when the transaction was made at the pacer court site."
        ),
    ]
    """
    Date when the transaction was made at the pacer court site.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
