

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class V1HoursUpdateEventTimestampsItem(UniversalBaseModel):
    id: typing.Optional[int] = None
    from_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[str] = None
    entry_ids: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
