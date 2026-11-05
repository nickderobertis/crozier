

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HangupCallParameters(UniversalBaseModel):
    call_uuid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(
            alias="CallUUID",
            description="Unique identifier of the call (when established); this parameter is mutually exclusive with RequestUUID",
        ),
    ] = None
    """
    Unique identifier of the call (when established); this parameter is mutually exclusive with RequestUUID
    """

    request_uuid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RequestUUID"),
        pydantic.Field(
            alias="RequestUUID",
            description="Unique identifier of the API request (when the call is not established yet); this parameter is mutually exclusive with CallUUID",
        ),
    ] = None
    """
    Unique identifier of the API request (when the call is not established yet); this parameter is mutually exclusive with CallUUID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
