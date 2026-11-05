

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConferenceListParameters(UniversalBaseModel):
    call_uuid_filter: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CallUUIDFilter"),
        pydantic.Field(
            alias="CallUUIDFilter",
            description="Restricts listed calls to the provided values (comma separated call UUID list)",
        ),
    ] = None
    """
    Restricts listed calls to the provided values (comma separated call UUID list)
    """

    deaf_filter: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="DeafFilter"),
        pydantic.Field(alias="DeafFilter", description="Restricts listed members to deaf ones"),
    ] = None
    """
    Restricts listed members to deaf ones
    """

    member_filter: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MemberFilter"),
        pydantic.Field(
            alias="MemberFilter",
            description="Restricts listed members to the provided values (comma separated member ID list)",
        ),
    ] = None
    """
    Restricts listed members to the provided values (comma separated member ID list)
    """

    muted_filter: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="MutedFilter"),
        pydantic.Field(alias="MutedFilter", description="Restricts listed members to muted ones"),
    ] = None
    """
    Restricts listed members to muted ones
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
