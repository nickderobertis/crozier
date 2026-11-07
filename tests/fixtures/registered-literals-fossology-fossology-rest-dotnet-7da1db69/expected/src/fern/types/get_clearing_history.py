

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_clearing_history_scope import GetClearingHistoryScope
from .get_clearing_history_type import GetClearingHistoryType


class GetClearingHistory(UniversalBaseModel):
    date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date of the clearing history
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Username of the user who created the decision.
    """

    scope: typing.Optional[GetClearingHistoryScope] = pydantic.Field(default=None)
    """
    Scope of the clearing
    """

    type: typing.Optional[GetClearingHistoryType] = pydantic.Field(default=None)
    """
    Type of the clearing
    """

    added_licenses: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="addedLicenses"),
        pydantic.Field(alias="addedLicenses", description="List of license shortnames added to the decision"),
    ] = None
    """
    List of license shortnames added to the decision
    """

    removed_licenses: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="removedLicenses"),
        pydantic.Field(alias="removedLicenses", description="List of license shortnames removed from the decision"),
    ] = None
    """
    List of license shortnames removed from the decision
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
