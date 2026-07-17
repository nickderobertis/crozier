

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExposedApi(UniversalBaseModel):
    """
    The Open API configuration for your service (if one)
    """

    expose_api: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="exposeApi"),
        pydantic.Field(
            alias="exposeApi",
            description="Whether or not the current service expose an API with an Open API descriptor",
        ),
    ]
    """
    Whether or not the current service expose an API with an Open API descriptor
    """

    open_api_descriptor_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="openApiDescriptorUrl"),
        pydantic.Field(alias="openApiDescriptorUrl", description="The URL of the Open API descriptor"),
    ] = None
    """
    The URL of the Open API descriptor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
