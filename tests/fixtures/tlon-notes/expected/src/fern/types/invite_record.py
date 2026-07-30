

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InviteRecord(UniversalBaseModel):
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    sent_at: typing_extensions.Annotated[
        int, FieldMetadata(alias="sentAt"), pydantic.Field(alias="sentAt", description="Unix seconds")
    ]
    """
    Unix seconds
    """

    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
