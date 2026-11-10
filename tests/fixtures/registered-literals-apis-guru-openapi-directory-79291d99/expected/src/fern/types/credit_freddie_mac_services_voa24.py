

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_service_voa24 import CreditFreddieMacServiceVoa24


class CreditFreddieMacServicesVoa24(UniversalBaseModel):
    """
    A collection of objects that describe requests and responses for services.
    """

    service: typing_extensions.Annotated[
        CreditFreddieMacServiceVoa24, FieldMetadata(alias="SERVICE"), pydantic.Field(alias="SERVICE")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
