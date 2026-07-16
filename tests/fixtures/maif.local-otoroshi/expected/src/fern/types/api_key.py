

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiKey(UniversalBaseModel):
    """
    An Otoroshi Api Key. An Api Key is defined for a group of services to allow usage of the same Api Key for multiple services.
    """

    authorized_entities: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="authorizedEntities")] = (
        pydantic.Field()
    )
    """
    The group/service ids (prefixed by group_ or service_ on which the key is authorized
    """

    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId")] = pydantic.Field()
    """
    The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything
    """

    client_name: typing_extensions.Annotated[str, FieldMetadata(alias="clientName")] = pydantic.Field()
    """
    The name of the api key, for humans ;-)
    """

    client_secret: typing_extensions.Annotated[str, FieldMetadata(alias="clientSecret")] = pydantic.Field()
    """
    The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything
    """

    daily_quota: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="dailyQuota")] = pydantic.Field(
        default=None
    )
    """
    Authorized number of calls per day
    """

    enabled: bool = pydantic.Field()
    """
    Whether or not the key is enabled. If disabled, resources won't be available to calls using this key
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Bunch of metadata for the key
    """

    monthly_quota: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="monthlyQuota")] = (
        pydantic.Field(default=None)
    )
    """
    Authorized number of calls per month
    """

    throttling_quota: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="throttlingQuota")] = (
        pydantic.Field(default=None)
    )
    """
    Authorized number of calls per second, measured on 10 seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
