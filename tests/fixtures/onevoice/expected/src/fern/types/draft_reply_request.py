

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .draft_reply_example import DraftReplyExample


class DraftReplyRequest(UniversalBaseModel):
    business_id: typing_extensions.Annotated[str, FieldMetadata(alias="businessId"), pydantic.Field(alias="businessId")]
    business_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="businessName"), pydantic.Field(alias="businessName")
    ] = None
    business_category: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="businessCategory"), pydantic.Field(alias="businessCategory")
    ] = None
    business_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="businessDescription"), pydantic.Field(alias="businessDescription")
    ] = None
    platform: str
    review_text: typing_extensions.Annotated[str, FieldMetadata(alias="reviewText"), pydantic.Field(alias="reviewText")]
    rating: int
    author_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="authorName"), pydantic.Field(alias="authorName")
    ] = None
    examples: typing.Optional[typing.List[DraftReplyExample]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
