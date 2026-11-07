

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ListedSnapshotSpec(UniversalBaseModel):
    """
    Display fields for a content snapshot list item.
    """

    modify_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="modifyTime"),
        pydantic.Field(alias="modifyTime", description="Last modification time of the snapshot content."),
    ] = None
    """
    Last modification time of the snapshot content.
    """

    owner: str = pydantic.Field()
    """
    User name of the snapshot owner.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
