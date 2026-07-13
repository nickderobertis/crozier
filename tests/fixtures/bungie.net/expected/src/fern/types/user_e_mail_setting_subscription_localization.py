

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserEMailSettingSubscriptionLocalization(UniversalBaseModel):
    """
    Localized text relevant to a given EMail setting in a given localization. Extra settings specifically for subscriptions.
    """

    description: typing.Optional[str] = None
    known_user_action_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="knownUserActionText")
    ] = None
    registered_user_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="registeredUserDescription")
    ] = None
    title: typing.Optional[str] = None
    unknown_user_action_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unknownUserActionText")
    ] = None
    unknown_user_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unknownUserDescription")
    ] = None
    unregistered_user_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unregisteredUserDescription")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
