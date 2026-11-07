

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Kek(UniversalBaseModel):
    name: typing.Optional[str] = None
    kms_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kmsType"), pydantic.Field(alias="kmsType")
    ] = None
    kms_key_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kmsKeyId"), pydantic.Field(alias="kmsKeyId")
    ] = None
    kms_props: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="kmsProps"), pydantic.Field(alias="kmsProps")
    ] = None
    doc: typing.Optional[str] = None
    shared: typing.Optional[bool] = None
    ts: typing.Optional[int] = None
    deleted: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
