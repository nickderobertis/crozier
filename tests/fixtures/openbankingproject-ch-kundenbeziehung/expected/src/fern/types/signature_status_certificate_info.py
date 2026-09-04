

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SignatureStatusCertificateInfo(UniversalBaseModel):
    """
    Zertifikatsinformationen
    """

    issuer: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    valid_from: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="validFrom"), pydantic.Field(alias="validFrom")
    ] = None
    valid_to: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="validTo"), pydantic.Field(alias="validTo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
