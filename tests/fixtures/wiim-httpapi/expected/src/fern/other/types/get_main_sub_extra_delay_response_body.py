

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetMainSubExtraDelayResponseBody(UniversalBaseModel):
    error_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorType"), pydantic.Field(alias="errorType")
    ] = None
    main_sub_extra_delay: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mainSubExtraDelay"), pydantic.Field(alias="mainSubExtraDelay")
    ] = None
    main_delay: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mainDelay"), pydantic.Field(alias="mainDelay")
    ] = None
    sub_delay: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="subDelay"), pydantic.Field(alias="subDelay")
    ] = None
    error_describe: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorDescribe"), pydantic.Field(alias="errorDescribe")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
