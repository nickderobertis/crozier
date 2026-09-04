

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetFapiConfigResponseSpecs(UniversalBaseModel):
    security_profile: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="securityProfile"), pydantic.Field(alias="securityProfile")
    ] = None
    message_signing: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="messageSigning"), pydantic.Field(alias="messageSigning")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
