

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .untag_resource_request_tag_keys import UntagResourceRequestTagKeys


class UntagResourceRequest(UniversalBaseModel):
    """
    The request to remove tags from a CloudFront resource.
    """

    tag_keys: typing_extensions.Annotated[
        UntagResourceRequestTagKeys,
        FieldMetadata(alias="TagKeys"),
        pydantic.Field(
            alias="TagKeys", description=" A complex type that contains zero or more <code>Tag</code> key elements."
        ),
    ]
    """
     A complex type that contains zero or more <code>Tag</code> key elements.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
