

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NotifierInfo(UniversalBaseModel):
    """
    Notifier metadata used by notification preference UI.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    description of the notifier
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="display name of the notifier"),
    ] = None
    """
    display name of the notifier
    """

    name: str = pydantic.Field()
    """
    notifier <code>metadata.name</code>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
