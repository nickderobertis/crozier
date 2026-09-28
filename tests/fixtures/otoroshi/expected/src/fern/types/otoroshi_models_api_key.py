

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_api_key_valid_until import OtoroshiModelsApiKeyValidUntil
from .otoroshi_models_entity_identifier import OtoroshiModelsEntityIdentifier


class OtoroshiModelsApiKey(UniversalBaseModel):
    """
    An otoroshi apikey that can allow you to access some services
    """

    daily_quota: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="dailyQuota"),
        pydantic.Field(alias="dailyQuota", description="Authorized number of calls per day"),
    ] = None
    """
    Authorized number of calls per day
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Bunch of metadata for the key
    """

    throttling_quota: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="throttlingQuota"),
        pydantic.Field(alias="throttlingQuota", description="Authorized number of calls per window"),
    ] = None
    """
    Authorized number of calls per window
    """

    constrained_services_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="constrainedServicesOnly"),
        pydantic.Field(
            alias="constrainedServicesOnly",
            description="This apikey can only be used on services that constrained their apikey routing",
        ),
    ] = None
    """
    This apikey can only be used on services that constrained their apikey routing
    """

    allow_client_id_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowClientIdOnly"),
        pydantic.Field(alias="allowClientIdOnly", description="This apikey can be used juste with the client_id value"),
    ] = None
    """
    This apikey can be used juste with the client_id value
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    restrictions: typing.Optional[typing.Any] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Apikey tags
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the key is enabled. If disabled, resources won't be available to calls using this key
    """

    read_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="readOnly"),
        pydantic.Field(alias="readOnly", description="The apikey only allow access for GET, HEAD and OPTIONS verbs"),
    ] = None
    """
    The apikey only allow access for GET, HEAD and OPTIONS verbs
    """

    client_secret: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientSecret"),
        pydantic.Field(
            alias="clientSecret",
            description="The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything",
        ),
    ] = None
    """
    The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything
    """

    valid_until: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsApiKeyValidUntil],
        FieldMetadata(alias="validUntil"),
        pydantic.Field(alias="validUntil", description="Date until when the apikey is valid"),
    ] = None
    """
    Date until when the apikey is valid
    """

    client_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientName"),
        pydantic.Field(alias="clientName", description="The name of the api key, for humans ;-)"),
    ] = None
    """
    The name of the api key, for humans ;-)
    """

    monthly_quota: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyQuota"),
        pydantic.Field(alias="monthlyQuota", description="Authorized number of calls per month"),
    ] = None
    """
    Authorized number of calls per month
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of this apikey
    """

    rotation: typing.Optional[typing.Any] = None
    authorized_entities: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiModelsEntityIdentifier]],
        FieldMetadata(alias="authorizedEntities"),
        pydantic.Field(
            alias="authorizedEntities",
            description="The group/service ids (prefixed by group_ or service_ on which the key is authorized",
        ),
    ] = None
    """
    The group/service ids (prefixed by group_ or service_ on which the key is authorized
    """

    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientId"),
        pydantic.Field(
            alias="clientId",
            description="The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything",
        ),
    ] = None
    """
    The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
