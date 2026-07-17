

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_user_info_card import UserUserInfoCard


class ApplicationsApplicationDeveloper(UniversalBaseModel):
    api_eula_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="apiEulaVersion"), pydantic.Field(alias="apiEulaVersion")
    ] = None
    role: typing.Optional[int] = None
    user: typing.Optional[UserUserInfoCard] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
