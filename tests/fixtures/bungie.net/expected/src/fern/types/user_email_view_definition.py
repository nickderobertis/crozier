

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_email_view_definition_setting import UserEmailViewDefinitionSetting


class UserEmailViewDefinition(UniversalBaseModel):
    """
    Represents a data-driven view for Email settings. Web/Mobile UI can use this data to show new EMail settings consistently without further manual work.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier for this view.
    """

    view_settings: typing_extensions.Annotated[
        typing.Optional[typing.List[UserEmailViewDefinitionSetting]],
        FieldMetadata(alias="viewSettings"),
        pydantic.Field(alias="viewSettings", description="The ordered list of settings to show in this view."),
    ] = None
    """
    The ordered list of settings to show in this view.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
