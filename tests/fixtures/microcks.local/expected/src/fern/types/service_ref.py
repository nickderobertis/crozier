

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ServiceRef(UniversalBaseModel):
    """
    Lightweight reference of an existing Service
    """

    name: str = pydantic.Field()
    """
    The Service name
    """

    service_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceId"),
        pydantic.Field(alias="serviceId", description="Unique reference of a Service"),
    ]
    """
    Unique reference of a Service
    """

    version: str = pydantic.Field()
    """
    The Service version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
