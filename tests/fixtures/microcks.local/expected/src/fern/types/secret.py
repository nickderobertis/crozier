

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Secret(UniversalBaseModel):
    """
    A Secret allows grouping informations on how to access a restricted resource such as a repsoitory URL. Secrets are typically used by ImpoortJobs.
    """

    ca_cert_pem: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="caCertPem")] = None
    description: str = pydantic.Field()
    """
    Description of this Secret
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of Secret
    """

    name: str = pydantic.Field()
    """
    Unique distinct name of Secret
    """

    password: typing.Optional[str] = None
    token: typing.Optional[str] = None
    token_header: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="tokenHeader")] = None
    username: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
