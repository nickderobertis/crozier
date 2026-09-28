

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccountCategoriesUpdatedWebhookData(UniversalBaseModel):
    modified_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="modifiedDate"),
        pydantic.Field(
            alias="modifiedDate", description="The date on which this account categories were last modified in Codat."
        ),
    ] = None
    """
    The date on which this account categories were last modified in Codat.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
