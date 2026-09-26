

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .prompts_sources_post_response_data_status import PromptsSourcesPostResponseDataStatus


class PromptsSourcesPostResponseData(UniversalBaseModel):
    source: str = pydantic.Field()
    """
    Credential-scrubbed identifier the cached source is keyed by
    """

    content_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contentHash"),
        pydantic.Field(alias="contentHash", description="Echoed content hash, if provided"),
    ] = None
    """
    Echoed content hash, if provided
    """

    file_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="fileCount"), pydantic.Field(alias="fileCount", description="Number of files cached")
    ]
    """
    Number of files cached
    """

    status: PromptsSourcesPostResponseDataStatus = pydantic.Field()
    """
    Ingestion status: "ingested" (decoded and cached) or "unchanged" (content-hash dedup short-circuit)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
