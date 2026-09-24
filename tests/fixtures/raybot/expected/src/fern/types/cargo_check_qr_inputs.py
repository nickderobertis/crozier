

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CargoCheckQrInputs(UniversalBaseModel):
    qr_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="qrCode"), pydantic.Field(alias="qrCode", description="The QR code to check")
    ]
    """
    The QR code to check
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
