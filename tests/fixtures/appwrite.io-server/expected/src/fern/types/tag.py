

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Tag(UniversalBaseModel):
    """
    Tag
    """

    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="Tag ID.")]
    """
    Tag ID.
    """

    command: str = pydantic.Field()
    """
    The entrypoint command in use to execute the tag code.
    """

    date_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="dateCreated"),
        pydantic.Field(alias="dateCreated", description="The tag creation date in Unix timestamp."),
    ]
    """
    The tag creation date in Unix timestamp.
    """

    function_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="functionId"), pydantic.Field(alias="functionId", description="Function ID.")
    ]
    """
    Function ID.
    """

    size: str = pydantic.Field()
    """
    The code size in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
