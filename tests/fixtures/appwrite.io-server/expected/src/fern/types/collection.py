

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rule import Rule


class Collection(UniversalBaseModel):
    """
    Collection
    """

    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id")] = pydantic.Field()
    """
    Collection ID.
    """

    permissions: typing_extensions.Annotated[
        typing.Dict[str, typing.Optional[typing.Any]], FieldMetadata(alias="$permissions")
    ] = pydantic.Field()
    """
    Collection permissions.
    """

    date_created: typing_extensions.Annotated[int, FieldMetadata(alias="dateCreated")] = pydantic.Field()
    """
    Collection creation date in Unix timestamp.
    """

    date_updated: typing_extensions.Annotated[int, FieldMetadata(alias="dateUpdated")] = pydantic.Field()
    """
    Collection creation date in Unix timestamp.
    """

    name: str = pydantic.Field()
    """
    Collection name.
    """

    rules: typing.List[Rule] = pydantic.Field()
    """
    Collection rules.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
