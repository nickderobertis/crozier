

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClientRegistrationResponseSwissStandardsSupport(UniversalBaseModel):
    qr_code: typing.Optional[bool] = None
    iso20022: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="iso_20022"), pydantic.Field(alias="iso_20022")
    ] = None
    finma_compliant: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
