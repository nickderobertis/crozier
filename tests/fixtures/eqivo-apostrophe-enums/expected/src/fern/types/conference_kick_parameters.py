

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConferenceKickParameters(UniversalBaseModel):
    conference_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ConferenceName"),
        pydantic.Field(alias="ConferenceName", description="Name of the conference in question"),
    ]
    """
    Name of the conference in question
    """

    member_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="MemberID"),
        pydantic.Field(
            alias="MemberID",
            description="List of comma separated member IDs to be affected; `all` shorthand is available too.",
        ),
    ]
    """
    List of comma separated member IDs to be affected; `all` shorthand is available too.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
