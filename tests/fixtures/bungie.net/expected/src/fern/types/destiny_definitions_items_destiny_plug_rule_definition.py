

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsItemsDestinyPlugRuleDefinition(UniversalBaseModel):
    """
    Dictates a rule around whether the plug is enabled or insertable.
    In practice, the live Destiny data will refer to these entries by index. You can then look up that index in the appropriate property (enabledRules or insertionRules) to get the localized string for the failure message if it failed.
    """

    failure_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="failureMessage"),
        pydantic.Field(alias="failureMessage", description="The localized string to show if this rule fails."),
    ] = None
    """
    The localized string to show if this rule fails.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
