

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ServiceChaosRequest(UniversalBaseModel):
    """
    service-scoped HTTP chaos registration, removal or clear instruction
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    downstream host the chaos profile applies to (mutually exclusive with clear)
    """

    chaos: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    HTTP chaos profile (fault types, probabilities, error status, etc.); omit (or set remove:true) to remove the host's profile
    """

    remove: typing.Optional[bool] = pydantic.Field(default=None)
    """
    when true, removes the named host's chaos profile
    """

    clear: typing.Optional[bool] = pydantic.Field(default=None)
    """
    when true, clears all service-scoped chaos (mutually exclusive with host)
    """

    ttl_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ttlMillis"),
        pydantic.Field(
            alias="ttlMillis",
            description="optional time-to-live in milliseconds after which the registration auto-reverts",
        ),
    ] = None
    """
    optional time-to-live in milliseconds after which the registration auto-reverts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
