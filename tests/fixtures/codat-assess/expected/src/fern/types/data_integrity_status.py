

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataIntegrityStatus(UniversalBaseModel):
    amounts: typing.Optional[typing.Any] = None
    connection_ids: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="connectionIds"), pydantic.Field(alias="connectionIds")
    ] = None
    dates: typing.Optional[typing.Any] = None
    status_info: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="statusInfo"), pydantic.Field(alias="statusInfo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
