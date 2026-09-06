

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorization_codes_shared_models_authorization_code_user import (
    AuthorizationCodesSharedModelsAuthorizationCodeUser,
)
from .authorization_codes_shared_models_category import AuthorizationCodesSharedModelsCategory


class AuthorizationCodesSharedModelsCategoryUserReport(UniversalBaseModel):
    categories: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorizationCodesSharedModelsCategory]],
        FieldMetadata(alias="Categories"),
        pydantic.Field(alias="Categories"),
    ] = None
    user: typing_extensions.Annotated[
        typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeUser],
        FieldMetadata(alias="User"),
        pydantic.Field(alias="User"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
