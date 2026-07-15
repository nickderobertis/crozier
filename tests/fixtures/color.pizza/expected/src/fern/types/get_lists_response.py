

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_lists_response_list_descriptions import GetListsResponseListDescriptions


class GetListsResponse(UniversalBaseModel):
    list_descriptions: typing_extensions.Annotated[
        typing.Optional[GetListsResponseListDescriptions], FieldMetadata(alias="listDescriptions")
    ] = None
    local_available_color_name_lists: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="localAvailableColorNameLists")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
