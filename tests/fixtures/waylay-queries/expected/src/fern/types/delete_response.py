

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delete_response_embeddings_value import DeleteResponseEmbeddingsValue
from .delete_response_links_value import DeleteResponseLinksValue
from .message import Message


class DeleteResponse(UniversalBaseModel):
    """
    Confirmation of a delete request.
    """

    messages: typing.Optional[typing.List[Message]] = None
    links: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DeleteResponseLinksValue]],
        FieldMetadata(alias="_links"),
        pydantic.Field(alias="_links", description="HAL links, indexed by link relation."),
    ] = None
    """
    HAL links, indexed by link relation.
    """

    embeddings: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DeleteResponseEmbeddingsValue]],
        FieldMetadata(alias="_embeddings"),
        pydantic.Field(alias="_embeddings", description="Hal embeddings, indexed by relation."),
    ] = None
    """
    Hal embeddings, indexed by relation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
