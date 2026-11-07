

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry
from .term_code import TermCode


class CriteriaProfileData(UniversalBaseModel):
    id: typing.Optional[str] = None
    display: typing.Optional[DisplayEntry] = None
    context: typing.Optional[TermCode] = None
    term_codes: typing_extensions.Annotated[
        typing.Optional[typing.List[TermCode]], FieldMetadata(alias="termCodes"), pydantic.Field(alias="termCodes")
    ] = None
    ui_profile_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uiProfileId"), pydantic.Field(alias="uiProfileId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
