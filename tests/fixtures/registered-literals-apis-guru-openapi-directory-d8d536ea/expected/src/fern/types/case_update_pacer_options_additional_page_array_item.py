

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_update_pacer_options_additional_page_array_item_page import CaseUpdatePacerOptionsAdditionalPageArrayItemPage


class CaseUpdatePacerOptionsAdditionalPageArrayItem(UniversalBaseModel):
    fetch_if_older_than_days: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="fetchIfOlderThanDays"),
        pydantic.Field(
            alias="fetchIfOlderThanDays",
            description="You can limit how often this page information is fetched to reduce your PACER fees.\n\nMin days is 0 and Max days is 100.\n\nExample:\n1.  Specifying a value of 0 ensures that this page is fetched from PACER for this case update irrespective of when the page was last fetched.\n2.  Specifying a value of 30 ensures that this page is fetched from PACER for this case update only if the last fetch was older than 30 days.",
        ),
    ] = None
    """
    You can limit how often this page information is fetched to reduce your PACER fees.
    
    Min days is 0 and Max days is 100.
    
    Example:
    1.  Specifying a value of 0 ensures that this page is fetched from PACER for this case update irrespective of when the page was last fetched.
    2.  Specifying a value of 30 ensures that this page is fetched from PACER for this case update only if the last fetch was older than 30 days.
    """

    page: typing.Optional[CaseUpdatePacerOptionsAdditionalPageArrayItemPage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
