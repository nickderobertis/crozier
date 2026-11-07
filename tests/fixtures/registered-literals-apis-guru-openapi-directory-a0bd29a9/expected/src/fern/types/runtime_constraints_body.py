

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .privacy_enum import PrivacyEnum


class RuntimeConstraintsBody(UniversalBaseModel):
    allowed_port_privacy_settings: typing_extensions.Annotated[
        typing.Optional[typing.List[PrivacyEnum]],
        FieldMetadata(alias="allowedPortPrivacySettings"),
        pydantic.Field(alias="allowedPortPrivacySettings"),
    ] = None
    image_allow_list: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="imageAllowList"), pydantic.Field(alias="imageAllowList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
