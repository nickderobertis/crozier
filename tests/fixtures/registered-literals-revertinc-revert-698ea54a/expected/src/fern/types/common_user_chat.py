

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonUserChat(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Id of user according to connected communication app
    """

    name: str = pydantic.Field()
    """
    The name of user in communication app
    """

    created_timestamp: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="createdTimestamp"), pydantic.Field(alias="createdTimestamp")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
