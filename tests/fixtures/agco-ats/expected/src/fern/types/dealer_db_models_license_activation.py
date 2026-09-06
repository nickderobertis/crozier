

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DealerDbModelsLicenseActivation(UniversalBaseModel):
    key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Key"),
        pydantic.Field(
            alias="Key",
            description="The license key in base64 format.  This is only provided when the LicenseData is a new license.",
        ),
    ] = None
    """
    The license key in base64 format.  This is only provided when the LicenseData is a new license.
    """

    license_data: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LicenseData"),
        pydantic.Field(alias="LicenseData", description="The license data in base64 format."),
    ] = None
    """
    The license data in base64 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
