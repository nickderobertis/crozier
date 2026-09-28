

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverBreakpointMatcherResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique id assigned to this matcher
    """

    phases: typing.Optional[typing.List[str]] = None
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientId"),
        pydantic.Field(alias="clientId", description="echoed back from the request"),
    ] = None
    """
    echoed back from the request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
