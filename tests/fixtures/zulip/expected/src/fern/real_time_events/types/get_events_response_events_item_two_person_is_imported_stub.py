

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonIsImportedStub(UniversalBaseModel):
    """
    When an imported user logs into the organization for
    the first time.

    **Changes**: New in Zulip 12.0 (feature level 433).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user affected by this change.
    """

    is_imported_stub: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This value is always `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
