

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dashboard import Dashboard


class ListDashboardsResponse(UniversalBaseModel):
    """
    The ListDashboards request.
    """

    dashboards: typing.Optional[typing.List[Dashboard]] = pydantic.Field(default=None)
    """
    The list of requested dashboards.
    """

    next_page_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageToken"),
        pydantic.Field(
            alias="nextPageToken",
            description="If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method.",
        ),
    ] = None
    """
    If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
