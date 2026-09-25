

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdMedicationHistoryCreateConsentRequest(UniversalBaseModel):
    expiry_date: typing_extensions.Annotated[str, FieldMetadata(alias="ExpiryDate"), pydantic.Field(alias="ExpiryDate")]
    memo: typing_extensions.Annotated[str, FieldMetadata(alias="Memo"), pydantic.Field(alias="Memo")]
    consent: typing_extensions.Annotated[str, FieldMetadata(alias="Consent"), pydantic.Field(alias="Consent")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
