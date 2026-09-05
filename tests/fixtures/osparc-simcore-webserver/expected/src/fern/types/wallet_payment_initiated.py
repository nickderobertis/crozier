

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WalletPaymentInitiated(UniversalBaseModel):
    payment_id: typing_extensions.Annotated[str, FieldMetadata(alias="paymentId"), pydantic.Field(alias="paymentId")]
    payment_form_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="paymentFormUrl"),
        pydantic.Field(
            alias="paymentFormUrl",
            description="Link to external site that holds the payment submission form.None if no prompt step is required (e.g. pre-selected credit card)",
        ),
    ] = None
    """
    Link to external site that holds the payment submission form.None if no prompt step is required (e.g. pre-selected credit card)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
