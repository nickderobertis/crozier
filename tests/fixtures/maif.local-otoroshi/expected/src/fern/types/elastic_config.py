

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ElasticConfig(UniversalBaseModel):
    """
    The configuration for elastic access
    """

    cluster_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clusterUri"),
        pydantic.Field(alias="clusterUri", description="URL of the elastic cluster"),
    ]
    """
    URL of the elastic cluster
    """

    headers: typing.Dict[str, str] = pydantic.Field()
    """
    Additionnal http headers
    """

    index: str = pydantic.Field()
    """
    Index for events. Default is otoroshi-events
    """

    password: str = pydantic.Field()
    """
    Optional password
    """

    type: str = pydantic.Field()
    """
    Type of events. Default is event
    """

    user: str = pydantic.Field()
    """
    Optional user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
