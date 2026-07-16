

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorInteractionReplyDefinition(UniversalBaseModel):
    """
    When the interaction is replied to, Reward sites will fire and items potentially selected based on whether the given unlock expression is TRUE.
    You can potentially choose one from multiple replies when replying to an interaction: this is how you get either/or rewards from vendors.
    """

    item_rewards_selection: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemRewardsSelection"),
        pydantic.Field(alias="itemRewardsSelection", description="The rewards granted upon responding to the vendor."),
    ] = None
    """
    The rewards granted upon responding to the vendor.
    """

    reply: typing.Optional[str] = pydantic.Field(default=None)
    """
    The localized text for the reply.
    """

    reply_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="replyType"),
        pydantic.Field(alias="replyType", description="An enum indicating the type of reply being made."),
    ] = None
    """
    An enum indicating the type of reply being made.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
