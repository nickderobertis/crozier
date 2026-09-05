

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerMetadata(UniversalBaseModel):
    """
    Resource metadata for identification
    """

    name: str = pydantic.Field()
    """
    Resource name identifier
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Custom key-value pairs for tagging and filtering
    """

    namespace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Kubernetes namespace where resources were created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
