

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class S3Coordinates(UniversalBaseModel):
    host: str
    port: int
    ssl: bool
    verify_ssl: typing_extensions.Annotated[bool, FieldMetadata(alias="verifySSL"), pydantic.Field(alias="verifySSL")]
    access_key: typing_extensions.Annotated[str, FieldMetadata(alias="access-key"), pydantic.Field(alias="access-key")]
    secret_key: typing_extensions.Annotated[str, FieldMetadata(alias="secret-key"), pydantic.Field(alias="secret-key")]
    bucket: str
    key_prefix: typing.Optional[str] = None
    location: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
