

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Team(UniversalBaseModel):
    """
    Team
    """

    id: typing_extensions.Annotated[
        str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="Team ID.")
    ]
    """
    Team ID.
    """

    date_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="dateCreated"),
        pydantic.Field(alias="dateCreated", description="Team creation date in Unix timestamp."),
    ]
    """
    Team creation date in Unix timestamp.
    """

    name: str = pydantic.Field()
    """
    Team name.
    """

    sum: int = pydantic.Field()
    """
    Total sum of team members.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
