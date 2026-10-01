

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccountsWebhook(UniversalBaseModel):
    company_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="companyId"),
        pydantic.Field(alias="companyId", description="Unique identifier for a company."),
    ] = None
    """
    Unique identifier for a company.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
