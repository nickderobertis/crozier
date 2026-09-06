

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dealer_db_models_voucher_history_type import DealerDbModelsVoucherHistoryType


class DealerDbModelsVoucherHistory(UniversalBaseModel):
    changed_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="ChangedDate"), pydantic.Field(alias="ChangedDate")
    ] = None
    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CreatedDate"),
        pydantic.Field(alias="CreatedDate", description="Read-Only. The date the voucher was created."),
    ] = None
    """
    Read-Only. The date the voucher was created.
    """

    dealer_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DealerCode"),
        pydantic.Field(
            alias="DealerCode",
            description="The dealer code the voucher is assigned to.  Required for commercial vouchers.",
        ),
    ] = None
    """
    The dealer code the voucher is assigned to.  Required for commercial vouchers.
    """

    deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Deleted"),
        pydantic.Field(alias="Deleted", description="Read-Only. True if voucher has been deleted."),
    ] = None
    """
    Read-Only. True if voucher has been deleted.
    """

    email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Email"),
        pydantic.Field(alias="Email", description="The email address. Required for Internal Vouchers"),
    ] = None
    """
    The email address. Required for Internal Vouchers
    """

    expiration_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="ExpirationDate"),
        pydantic.Field(
            alias="ExpirationDate", description="The expiration date of the voucher. Required for Temporary Vouchers."
        ),
    ] = None
    """
    The expiration date of the voucher. Required for Temporary Vouchers.
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The id of the voucher history item"),
    ] = None
    """
    The id of the voucher history item
    """

    license_to: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LicenseTo"),
        pydantic.Field(alias="LicenseTo", description="Required for Internal Vouchers"),
    ] = None
    """
    Required for Internal Vouchers
    """

    modified_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ModifiedBy"),
        pydantic.Field(
            alias="ModifiedBy", description="Read-Only. The user that made the last modification to the voucher."
        ),
    ] = None
    """
    Read-Only. The user that made the last modification to the voucher.
    """

    order_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrderNumber"),
        pydantic.Field(
            alias="OrderNumber",
            description="The order number of a commercial license. Required for Commercial Vouchers. Not supported for other Vouchers.",
        ),
    ] = None
    """
    The order number of a commercial license. Required for Commercial Vouchers. Not supported for other Vouchers.
    """

    punched: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Punched"),
        pydantic.Field(
            alias="Punched",
            description="True if voucher has aleady been used.  False if the voucher has not been used.",
        ),
    ] = None
    """
    True if voucher has aleady been used.  False if the voucher has not been used.
    """

    punched_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="PunchedDate"),
        pydantic.Field(alias="PunchedDate", description="Read-Only. The date the voucher was punched."),
    ] = None
    """
    Read-Only. The date the voucher was punched.
    """

    purpose: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Purpose"),
        pydantic.Field(alias="Purpose", description="Required for Internal Vouchers"),
    ] = None
    """
    Required for Internal Vouchers
    """

    type: typing_extensions.Annotated[
        typing.Optional[DealerDbModelsVoucherHistoryType],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The type of voucher."),
    ] = None
    """
    The type of voucher.
    """

    voucher_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="VoucherCode"),
        pydantic.Field(alias="VoucherCode", description="The voucher code."),
    ] = None
    """
    The voucher code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
