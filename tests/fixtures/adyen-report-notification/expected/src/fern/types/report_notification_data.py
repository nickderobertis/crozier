

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resource_reference import ResourceReference


class ReportNotificationData(UniversalBaseModel):
    account_holder: typing_extensions.Annotated[
        typing.Optional[ResourceReference],
        FieldMetadata(alias="accountHolder"),
        pydantic.Field(alias="accountHolder", description="The account holder related to the report."),
    ] = None
    """
    The account holder related to the report.
    """

    balance_account: typing_extensions.Annotated[
        typing.Optional[ResourceReference],
        FieldMetadata(alias="balanceAccount"),
        pydantic.Field(alias="balanceAccount", description="The balance account related to the report."),
    ] = None
    """
    The balance account related to the report.
    """

    balance_platform: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="balancePlatform"),
        pydantic.Field(alias="balancePlatform", description="The unique identifier of the balance platform."),
    ] = None
    """
    The unique identifier of the balance platform.
    """

    creation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationDate"),
        pydantic.Field(
            alias="creationDate",
            description="The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.",
        ),
    ] = None
    """
    The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.
    """

    download_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="downloadUrl"),
        pydantic.Field(
            alias="downloadUrl",
            description="The URL at which you can download the report. To download, you must authenticate your GET request with your [API credentials](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/overview).",
        ),
    ]
    """
    The URL at which you can download the report. To download, you must authenticate your GET request with your [API credentials](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/overview).
    """

    file_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="The filename of the report."),
    ]
    """
    The filename of the report.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the resource.
    """

    report_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="reportType"),
        pydantic.Field(
            alias="reportType",
            description="The type of report. Possible values:\n\n- `balanceplatform_accounting_interactive_report`\n- `balanceplatform_accounting_report`\n- `balanceplatform_balance_report`\n- `balanceplatform_fee_report`\n- `balanceplatform_payment_instrument_report`\n- `balanceplatform_payout_report`\n- `balanceplatform_statement_report`",
        ),
    ]
    """
    The type of report. Possible values:
    
    - `balanceplatform_accounting_interactive_report`
    - `balanceplatform_accounting_report`
    - `balanceplatform_balance_report`
    - `balanceplatform_fee_report`
    - `balanceplatform_payment_instrument_report`
    - `balanceplatform_payout_report`
    - `balanceplatform_statement_report`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
