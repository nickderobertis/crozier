

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResourcesSearchGetResponseDataResourcesItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Resource name
    """

    namespace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Namespace (for namespaced resources)
    """

    kind: str = pydantic.Field()
    """
    Resource kind
    """

    api_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion", description="API version")
    ]
    """
    API version
    """

    api_group: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiGroup"), pydantic.Field(alias="apiGroup", description="API group")
    ] = None
    """
    API group
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Resource labels
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Creation timestamp"),
    ] = None
    """
    Creation timestamp
    """

    score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Search relevance score (for search results)
    """

    status: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Live status from Kubernetes API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
