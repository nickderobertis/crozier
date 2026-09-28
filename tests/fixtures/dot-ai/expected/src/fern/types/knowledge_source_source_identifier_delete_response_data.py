

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class KnowledgeSourceSourceIdentifierDeleteResponseData(UniversalBaseModel):
    source_identifier: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourceIdentifier"),
        pydantic.Field(alias="sourceIdentifier", description="The source identifier that was deleted"),
    ]
    """
    The source identifier that was deleted
    """

    chunks_deleted: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="chunksDeleted"),
        pydantic.Field(alias="chunksDeleted", description="Number of chunks deleted"),
    ]
    """
    Number of chunks deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
