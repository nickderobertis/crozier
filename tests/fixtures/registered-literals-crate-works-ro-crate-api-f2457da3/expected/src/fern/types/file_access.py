

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FileAccess(UniversalBaseModel):
    """
    Access information for this file, including content permissions and enrolment details.
    """

    content: bool = pydantic.Field()
    """
    Whether content is accessible to the current user.
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
