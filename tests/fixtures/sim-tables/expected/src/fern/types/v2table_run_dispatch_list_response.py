

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_run_dispatch import V2TableRunDispatch


class V2TableRunDispatchListResponse(UniversalBaseModel):
    """
    The table's active run dispatches.
    """

    data: typing.List[V2TableRunDispatch] = pydantic.Field()
    """
    Items in the current page.
    """

    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(
            alias="nextCursor",
            description="Always `null` — this list has no `cursor` or `limit` param and returns its whole bounded set in one page. Present so the list can gain pages later without a shape change.",
        ),
    ] = None
    """
    Always `null` — this list has no `cursor` or `limit` param and returns its whole bounded set in one page. Present so the list can gain pages later without a shape change.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
