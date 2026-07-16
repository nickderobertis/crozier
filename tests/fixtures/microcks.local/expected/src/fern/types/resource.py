

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resource_type import ResourceType


class Resource(UniversalBaseModel):
    """
    Resource represents a Service or API artifacts such as specification, contract
    """

    content: str = pydantic.Field()
    """
    String content of this resource
    """

    id: str = pydantic.Field()
    """
    Uniquer identifier of this Service or API Resource
    """

    name: str = pydantic.Field()
    """
    Unique name/business identifier for this Service or API resource
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Relatvie path of this resource regarding main resource
    """

    service_id: typing_extensions.Annotated[str, FieldMetadata(alias="serviceId")] = pydantic.Field()
    """
    Unique identifier of the Servoce or API this resource is attached to
    """

    source_artifact: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="sourceArtifact")] = (
        pydantic.Field(default=None)
    )
    """
    Short name of the artifact this resource was extracted from
    """

    type: ResourceType = pydantic.Field()
    """
    Type of this Service or API resource
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
