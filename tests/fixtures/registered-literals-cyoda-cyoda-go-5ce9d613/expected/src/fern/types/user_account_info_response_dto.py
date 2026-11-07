

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_account_info_dto import UserAccountInfoDto


class UserAccountInfoResponseDto(UniversalBaseModel):
    user_account_info: typing_extensions.Annotated[
        UserAccountInfoDto, FieldMetadata(alias="userAccountInfo"), pydantic.Field(alias="userAccountInfo")
    ]
    feature_toggles: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, bool]],
        FieldMetadata(alias="featureToggles"),
        pydantic.Field(alias="featureToggles", description="A map of feature toggles with their values"),
    ] = None
    """
    A map of feature toggles with their values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
