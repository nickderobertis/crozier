

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.team import Team


class ListJoinedTeamsResponse(UniversalBaseModel):
    odata_context: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.context"), pydantic.Field(alias="@odata.context")
    ] = None
    value: typing.Optional[typing.List[Team]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
