

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_google_tag_response_google_tag_ids_item import ListGoogleTagResponseGoogleTagIdsItem


class ListGoogleTagResponse(UniversalBaseModel):
    """
    A list of Google Tags configured for a site.
    """

    google_tag_ids: typing_extensions.Annotated[
        typing.List[ListGoogleTagResponseGoogleTagIdsItem],
        FieldMetadata(alias="googleTagIds"),
        pydantic.Field(alias="googleTagIds", description="List of Google Tags configured for a site, sorted by order."),
    ]
    """
    List of Google Tags configured for a site, sorted by order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
