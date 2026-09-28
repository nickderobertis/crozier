

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_elastic_analytics_config_index import OtoroshiModelsElasticAnalyticsConfigIndex
from .otoroshi_models_elastic_analytics_config_password import OtoroshiModelsElasticAnalyticsConfigPassword
from .otoroshi_models_elastic_analytics_config_type import OtoroshiModelsElasticAnalyticsConfigType
from .otoroshi_models_elastic_analytics_config_user import OtoroshiModelsElasticAnalyticsConfigUser
from .otoroshi_models_elastic_analytics_config_version import OtoroshiModelsElasticAnalyticsConfigVersion


class OtoroshiModelsElasticAnalyticsConfig(UniversalBaseModel):
    """
    Settings for connection to an elastic cluster
    """

    type: typing.Optional[OtoroshiModelsElasticAnalyticsConfigType] = pydantic.Field(default=None)
    """
    Object type
    """

    send_workers: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sendWorkers"), pydantic.Field(alias="sendWorkers", description="???")
    ] = None
    """
    ???
    """

    apply_template: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="applyTemplate"),
        pydantic.Field(alias="applyTemplate", description="Enable template creation/update"),
    ] = None
    """
    Enable template creation/update
    """

    uris: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    mtls_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="mtlsConfig"), pydantic.Field(alias="mtlsConfig")
    ] = None
    version: typing.Optional[OtoroshiModelsElasticAnalyticsConfigVersion] = pydantic.Field(default=None)
    """
    Version of Elasticsearch
    """

    max_bulk_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxBulkSize"), pydantic.Field(alias="maxBulkSize", description="???")
    ] = None
    """
    ???
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Additionnal headers in the http request
    """

    index_settings: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="indexSettings"), pydantic.Field(alias="indexSettings")
    ] = None
    user: typing.Optional[OtoroshiModelsElasticAnalyticsConfigUser] = pydantic.Field(default=None)
    """
    Elasticsearch user
    """

    index: typing.Optional[OtoroshiModelsElasticAnalyticsConfigIndex] = pydantic.Field(default=None)
    """
    Index name
    """

    password: typing.Optional[OtoroshiModelsElasticAnalyticsConfigPassword] = pydantic.Field(default=None)
    """
    Elastic password
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
