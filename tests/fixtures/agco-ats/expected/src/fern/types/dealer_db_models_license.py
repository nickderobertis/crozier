

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dealer_db_models_license_license_activation_type import DealerDbModelsLicenseLicenseActivationType


class DealerDbModelsLicense(UniversalBaseModel):
    active: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Active"),
        pydantic.Field(alias="Active", description="True if license is active."),
    ] = None
    """
    True if license is active.
    """

    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CreatedDate"),
        pydantic.Field(alias="CreatedDate", description="The date the license was created."),
    ] = None
    """
    The date the license was created.
    """

    deactivated_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="DeactivatedDate"),
        pydantic.Field(alias="DeactivatedDate", description="The date the license was deactivated."),
    ] = None
    """
    The date the license was deactivated.
    """

    license_activation_type: typing_extensions.Annotated[
        typing.Optional[DealerDbModelsLicenseLicenseActivationType],
        FieldMetadata(alias="LicenseActivationType"),
        pydantic.Field(alias="LicenseActivationType", description="The type of license (e.g. EDT, EDT Lite)"),
    ] = None
    """
    The type of license (e.g. EDT, EDT Lite)
    """

    license_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LicenseID"),
        pydantic.Field(alias="LicenseID", description="The LicenseID"),
    ] = None
    """
    The LicenseID
    """

    license_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LicenseVersion"),
        pydantic.Field(alias="LicenseVersion", description="The version of the license."),
    ] = None
    """
    The version of the license.
    """

    refresh_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="RefreshDate"),
        pydantic.Field(alias="RefreshDate", description="The date the license was refreshed."),
    ] = None
    """
    The date the license was refreshed.
    """

    system_info: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SystemInfo"),
        pydantic.Field(alias="SystemInfo", description="Information about the system which is licensed."),
    ] = None
    """
    Information about the system which is licensed.
    """

    updated_license_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedLicenseVersion"),
        pydantic.Field(
            alias="UpdatedLicenseVersion",
            description="The updated version of the license.  A value in this field indicates that the update has not been confirmed.",
        ),
    ] = None
    """
    The updated version of the license.  A value in this field indicates that the update has not been confirmed.
    """

    voucher_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="VoucherCode"),
        pydantic.Field(alias="VoucherCode", description="The voucher code that generated the license."),
    ] = None
    """
    The voucher code that generated the license.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
