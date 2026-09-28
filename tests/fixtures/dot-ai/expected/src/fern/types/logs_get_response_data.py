

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LogsGetResponseData(UniversalBaseModel):
    logs: str = pydantic.Field()
    """
    Container log output
    """

    container: str = pydantic.Field()
    """
    Container name
    """

    container_count: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="containerCount"),
        pydantic.Field(alias="containerCount", description="Number of containers in the pod"),
    ]
    """
    Number of containers in the pod
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
