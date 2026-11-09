

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RoCrateAccess(UniversalBaseModel):
    """
    Access information for this RO-Crate. `metadata` governs this resource; `content` governs the deposited metadata document and file retrieval.
    """

    metadata: bool = pydantic.Field()
    """
    Whether this RO-Crate resource is accessible to the current user.
    """

    content: bool = pydantic.Field()
    """
    Whether the deposited metadata document is accessible to the current user.
    """

    metadata_authorization_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="metadataAuthorizationUrl"),
        pydantic.Field(
            alias="metadataAuthorizationUrl",
            description="URL for enrolment or authorisation process if metadata access is restricted.",
        ),
    ] = None
    """
    URL for enrolment or authorisation process if metadata access is restricted.
    """

    content_authorization_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contentAuthorizationUrl"),
        pydantic.Field(
            alias="contentAuthorizationUrl",
            description="URL for enrolment or authorisation process if content access is restricted.",
        ),
    ] = None
    """
    URL for enrolment or authorisation process if content access is restricted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
