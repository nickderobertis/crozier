

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiModelsApiError(UniversalBaseModel):
    developer_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DeveloperMessage"), pydantic.Field(alias="DeveloperMessage")
    ] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ErrorCode"), pydantic.Field(alias="ErrorCode")
    ] = None
    more_info: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="MoreInfo"), pydantic.Field(alias="MoreInfo")
    ] = None
    user_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="UserMessage"), pydantic.Field(alias="UserMessage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
