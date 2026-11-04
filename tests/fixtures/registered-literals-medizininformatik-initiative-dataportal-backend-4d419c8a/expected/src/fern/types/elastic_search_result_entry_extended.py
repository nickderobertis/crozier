

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry
from .term_code import TermCode


class ElasticSearchResultEntryExtended(UniversalBaseModel):
    display: typing.Optional[DisplayEntry] = None
    id: typing.Optional[str] = None
    availability: typing.Optional[int] = pydantic.Field(default=None)
    """
    Not sure if we want this as numeric value, percentage or just boolean?
    """

    context: typing.Optional[TermCode] = None
    term_codes: typing_extensions.Annotated[
        typing.Optional[typing.List[TermCode]], FieldMetadata(alias="termCodes"), pydantic.Field(alias="termCodes")
    ] = None
    terminology: typing.Optional[str] = None
    kds_module: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kdsModule"), pydantic.Field(alias="kdsModule")
    ] = None
    selectable: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
