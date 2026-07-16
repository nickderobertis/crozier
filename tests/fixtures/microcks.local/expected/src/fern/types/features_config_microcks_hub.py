

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FeaturesConfigMicrocksHub(UniversalBaseModel):
    """
    Microcks Hub feature properties
    """

    allowed_roles: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="allowed-roles")] = None
    enabled: typing.Optional[str] = None
    endpoint: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
