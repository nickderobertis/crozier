

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FileRevisionMetadataV1Links(UniversalBaseModel):
    self_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="The URL of this resource on this API"),
    ]
    """
    The URL of this resource on this API
    """

    html: str = pydantic.Field()
    """
    The URL of this resource on Val Town
    """

    module: str = pydantic.Field()
    """
    The URL of this resource's source code as a module
    """

    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    This resource's web endpoint, where it serves a website or API
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    This resource's email address for receiving emails (for email-type vals)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
