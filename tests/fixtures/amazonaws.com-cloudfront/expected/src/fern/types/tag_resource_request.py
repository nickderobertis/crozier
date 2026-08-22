

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tag_resource_request_tags import TagResourceRequestTags


class TagResourceRequest(UniversalBaseModel):
    """
    The request to add tags to a CloudFront resource.
    """

    tags: typing_extensions.Annotated[
        TagResourceRequestTags,
        FieldMetadata(alias="Tags"),
        pydantic.Field(
            alias="Tags", description=" A complex type that contains zero or more <code>Tag</code> elements."
        ),
    ]
    """
     A complex type that contains zero or more <code>Tag</code> elements.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
