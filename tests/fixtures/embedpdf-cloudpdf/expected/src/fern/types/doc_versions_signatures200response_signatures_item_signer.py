

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocVersionsSignatures200ResponseSignaturesItemSigner(UniversalBaseModel):
    name: typing.Optional[str] = None
    reason: typing.Optional[str] = None
    location: typing.Optional[str] = None
    contact_info: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contactInfo"), pydantic.Field(alias="contactInfo")
    ] = None
    claimed_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="claimedTime"), pydantic.Field(alias="claimedTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
