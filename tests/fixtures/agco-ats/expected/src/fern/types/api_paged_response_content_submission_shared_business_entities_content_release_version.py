

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_paged_response_metadata import ApiPagedResponseMetadata
from .content_submission_shared_business_entities_content_release_version import (
    ContentSubmissionSharedBusinessEntitiesContentReleaseVersion,
)


class ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion(UniversalBaseModel):
    """
    A response containing a page of results and metadata concerning the results
    """

    entities: typing_extensions.Annotated[
        typing.Optional[typing.List[ContentSubmissionSharedBusinessEntitiesContentReleaseVersion]],
        FieldMetadata(alias="Entities"),
        pydantic.Field(alias="Entities", description="The set of entities that make up this page."),
    ] = None
    """
    The set of entities that make up this page.
    """

    metadata: typing_extensions.Annotated[
        typing.Optional[ApiPagedResponseMetadata],
        FieldMetadata(alias="Metadata"),
        pydantic.Field(alias="Metadata", description="Metadata about this paged response"),
    ] = None
    """
    Metadata about this paged response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
