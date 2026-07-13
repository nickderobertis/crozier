

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsSocketsDestinyInsertPlugActionDefinition(UniversalBaseModel):
    """
    Data related to what happens while a plug is being inserted, mostly for UI purposes.
    """

    action_execute_seconds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="actionExecuteSeconds")
    ] = pydantic.Field(default=None)
    """
    How long it takes for the Plugging of the item to be completed once it is initiated, if you care.
    """

    action_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="actionType")] = pydantic.Field(
        default=None
    )
    """
    The type of action being performed when you act on this Socket Type. The most common value is "insert plug", but there are others as well (for instance, a "Masterwork" socket may allow for Re-initialization, and an Infusion socket allows for items to be consumed to upgrade the item)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
