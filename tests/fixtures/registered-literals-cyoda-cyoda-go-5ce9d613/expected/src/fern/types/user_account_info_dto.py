

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .legal_entity_info_dto import LegalEntityInfoDto
from .subscription_dto import SubscriptionDto
from .user_role_dto import UserRoleDto


class UserAccountInfoDto(UniversalBaseModel):
    user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId", description="Unique identifier for the user")
    ]
    """
    Unique identifier for the user
    """

    user_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="userName"), pydantic.Field(alias="userName", description="The name of the user")
    ]
    """
    The name of the user
    """

    legal_entity: typing_extensions.Annotated[
        LegalEntityInfoDto, FieldMetadata(alias="legalEntity"), pydantic.Field(alias="legalEntity")
    ]
    roles: typing.List[UserRoleDto]
    current_subscription: typing_extensions.Annotated[
        typing.Optional[SubscriptionDto],
        FieldMetadata(alias="currentSubscription"),
        pydantic.Field(alias="currentSubscription"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
