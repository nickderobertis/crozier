

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResourcesKindsGetResponseDataKindsItem(UniversalBaseModel):
    kind: str = pydantic.Field()
    """
    Resource kind (e.g., "Pod", "Deployment")
    """

    api_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="apiVersion"),
        pydantic.Field(alias="apiVersion", description='API version (e.g., "v1", "apps/v1")'),
    ]
    """
    API version (e.g., "v1", "apps/v1")
    """

    count: float = pydantic.Field()
    """
    Number of resources of this kind
    """

    api_group: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiGroup"),
        pydantic.Field(alias="apiGroup", description='API group (e.g., "apps", "networking.k8s.io")'),
    ] = None
    """
    API group (e.g., "apps", "networking.k8s.io")
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
