

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PulsarDataExporterConfig(UniversalBaseModel):
    """
    The configuration for kafka access
    """

    namespace: str = pydantic.Field()
    """
    Namespace
    """

    tenant: str = pydantic.Field()
    """
    Tenant
    """

    topic: str = pydantic.Field()
    """
    Topic
    """

    uri: typing.List[str] = pydantic.Field()
    """
    URI of the pulsar server
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
