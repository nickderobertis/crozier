

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workspace import Workspace


class ListWorkspacesResponse(UniversalBaseModel):
    items: typing.List[Workspace]
    page: float = pydantic.Field()
    """
    Current page number
    """

    limit: float = pydantic.Field()
    """
    Number of items per page
    """

    total: float = pydantic.Field()
    """
    Total number of items
    """

    has_more: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasMore"),
        pydantic.Field(alias="hasMore", description="Whether there are more pages available"),
    ]
    """
    Whether there are more pages available
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
