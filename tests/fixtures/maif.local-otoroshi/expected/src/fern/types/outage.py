

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Outage(UniversalBaseModel):
    """
    An outage by the Snow Monkey on a service
    """

    descriptor_id: typing_extensions.Annotated[str, FieldMetadata(alias="descriptorId")] = pydantic.Field()
    """
    The service impacted by outage
    """

    descriptor_name: typing_extensions.Annotated[str, FieldMetadata(alias="descriptorName")] = pydantic.Field()
    """
    The name of service impacted by outage
    """

    duration: int = pydantic.Field()
    """
    The duration of the outage
    """

    until: str = pydantic.Field()
    """
    The end of the outage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
