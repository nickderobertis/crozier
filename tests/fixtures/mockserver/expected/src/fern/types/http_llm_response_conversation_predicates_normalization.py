

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpLlmResponseConversationPredicatesNormalization(UniversalBaseModel):
    collapse_whitespace: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="collapseWhitespace"), pydantic.Field(alias="collapseWhitespace")
    ] = None
    lowercase: typing.Optional[bool] = None
    sort_json_keys: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="sortJsonKeys"), pydantic.Field(alias="sortJsonKeys")
    ] = None
    drop_built_in_volatile_fields: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="dropBuiltInVolatileFields"),
        pydantic.Field(alias="dropBuiltInVolatileFields"),
    ] = None
    drop_volatile_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="dropVolatileFields"),
        pydantic.Field(alias="dropVolatileFields"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
