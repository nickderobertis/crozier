

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NormJudgePublicDataNameHistoryArrayItem(UniversalBaseModel):
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    is_visible: typing_extensions.Annotated[bool, FieldMetadata(alias="isVisible"), pydantic.Field(alias="isVisible")]
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    middle_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")
    ] = None
    prefix: typing.Optional[str] = None
    suffix: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
