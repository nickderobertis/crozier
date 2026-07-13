

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock(UniversalBaseModel):
    """
    Presentation nodes can be restricted by various requirements. This defines the rules of those requirements, and the message(s) to be shown if these requirements aren't met.
    """

    entitlement_unavailable_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="entitlementUnavailableMessage")
    ] = pydantic.Field(default=None)
    """
    If this node is not accessible due to Entitlements (for instance, you don't own the required game expansion), this is the message to show.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
