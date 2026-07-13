

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityUnlockStringDefinition(UniversalBaseModel):
    """
    Represents a status string that could be conditionally displayed about an activity. Note that externally, you can only see the strings themselves. Internally we combine this information with server state to determine which strings should be shown.
    """

    display_string: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="displayString")] = (
        pydantic.Field(default=None)
    )
    """
    The string to be displayed if the conditions are met.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
