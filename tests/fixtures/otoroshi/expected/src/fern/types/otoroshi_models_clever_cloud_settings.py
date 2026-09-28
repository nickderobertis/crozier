

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsCleverCloudSettings(UniversalBaseModel):
    """
    Settings for connection to the clever-cloud api
    """

    consumer_secret: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="consumerSecret"),
        pydantic.Field(alias="consumerSecret", description="Clever-Cloud oauth consumer secret"),
    ] = None
    """
    Clever-Cloud oauth consumer secret
    """

    consumer_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="consumerKey"),
        pydantic.Field(alias="consumerKey", description="Clever-Cloud oauth consumer key"),
    ] = None
    """
    Clever-Cloud oauth consumer key
    """

    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Clever-Cloud oauth secret
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Clever-Cloud oauth token
    """

    orga_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="orgaId"),
        pydantic.Field(alias="orgaId", description="Clever-Cloud organization id"),
    ] = None
    """
    Clever-Cloud organization id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
