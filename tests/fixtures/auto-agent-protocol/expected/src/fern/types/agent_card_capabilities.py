

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AgentCardCapabilities(UniversalBaseModel):
    """
    A2A capability flags and extensions.
    """

    streaming: typing.Optional[bool] = None
    push_notifications: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="pushNotifications"), pydantic.Field(alias="pushNotifications")
    ] = None
    extensions: typing.List[typing.Any] = pydantic.Field()
    """
    Declared A2A extensions. MUST include the AAP automotive-retail v1.0 entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
