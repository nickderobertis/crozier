

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_target_ip_address import OtoroshiModelsTargetIpAddress
from .otoroshi_models_target_protocol import OtoroshiModelsTargetProtocol


class OtoroshiModelsTarget(UniversalBaseModel):
    """
    ???
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    weight: typing.Optional[int] = pydantic.Field(default=None)
    """
    ???
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    protocol: typing.Optional[OtoroshiModelsTargetProtocol] = pydantic.Field(default=None)
    """
    ???
    """

    predicate: typing.Optional[typing.Any] = None
    ip_address: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsTargetIpAddress],
        FieldMetadata(alias="ipAddress"),
        pydantic.Field(alias="ipAddress", description="???"),
    ] = None
    """
    ???
    """

    mtls_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="mtlsConfig"), pydantic.Field(alias="mtlsConfig")
    ] = None
    scheme: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
