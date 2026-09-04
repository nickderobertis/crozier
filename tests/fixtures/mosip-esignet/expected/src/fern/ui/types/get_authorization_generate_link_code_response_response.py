

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetAuthorizationGenerateLinkCodeResponseResponse(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="TransactionId same the one passed in the request."),
    ] = None
    """
    TransactionId same the one passed in the request.
    """

    link_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="linkCode"),
        pydantic.Field(alias="linkCode", description="Unique random string mapped to this transactionId."),
    ] = None
    """
    Unique random string mapped to this transactionId.
    """

    expire_date_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expireDateTime"),
        pydantic.Field(
            alias="expireDateTime",
            description="Expire date time (ISO format) for the generated linkCode. After this date time linkCode in this request is not valid.",
        ),
    ] = None
    """
    Expire date time (ISO format) for the generated linkCode. After this date time linkCode in this request is not valid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
