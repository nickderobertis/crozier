

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Action(UniversalBaseModel):
    action_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="actionCode"),
        pydantic.Field(alias="actionCode", description="The code identifying the action that needs to be completed."),
    ]
    """
    The code identifying the action that needs to be completed.
    """

    resolved: bool = pydantic.Field()
    """
    Indicates whether this action has been successfully completed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
