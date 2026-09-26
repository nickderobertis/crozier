

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AcceptQuoteData(UniversalBaseModel):
    deposit_payment_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="depositPaymentUrl"), pydantic.Field(alias="depositPaymentUrl")
    ] = None
    id: float
    version_number: typing_extensions.Annotated[
        float, FieldMetadata(alias="versionNumber"), pydantic.Field(alias="versionNumber")
    ]
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    guid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
