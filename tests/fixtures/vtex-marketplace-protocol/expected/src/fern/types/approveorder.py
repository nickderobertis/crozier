

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .approveorder_errors_item import ApproveorderErrorsItem
from .approveorder_fields import ApproveorderFields


class Approveorder(UniversalBaseModel):
    account_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountName"),
        pydantic.Field(alias="accountName", description="String that indicates which account made the request."),
    ] = None
    """
    String that indicates which account made the request.
    """

    code: str = pydantic.Field()
    """
    String with a internal Channel Order API code that classifies the response. The possible values returned in this field are described in the Response Codes section of this API Reference.
    """

    errors: typing.Optional[typing.List[ApproveorderErrorsItem]] = pydantic.Field(default=None)
    """
    List with errors related to the response, if there is any.
    """

    fields: typing.Optional[ApproveorderFields] = pydantic.Field(default=None)
    """
    Structure with important fields for the connector. This structure is only returned if the response is successful. Includes the following fields: 
    
    `mainOrderId`: String with the order's ID inside the main seller account in VTEX. 
    
    `franchiseOrderId`: - String with the order's ID inside the franchise seller account in VTEX. Only returned if the order was integrated using the [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) feature, that is: 
    
    - `allowFranchises` field set to `true` when integrating the order 
    
    - `SLA` chosen for the order is from a franchise account.
    """

    flow: str = pydantic.Field()
    """
    String containing the name of the flow responsible for the response. This field can contain the following values: 
    
    `PlaceOrder`: when integrating new orders. 
    
    `ApproveOrder`: when approving existing orders. 
    
    `Unknown`: when we’re not able to identify the flow.
    """

    marketplace_order_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="marketplaceOrderId"),
        pydantic.Field(
            alias="marketplaceOrderId", description="String that indicates the order's ID in the marketplace."
        ),
    ] = None
    """
    String that indicates the order's ID in the marketplace.
    """

    message: str = pydantic.Field()
    """
    String with a message explaining the code returned in the response.
    """

    operation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="operationId"),
        pydantic.Field(
            alias="operationId",
            description="String GUID that identifies the operation in our service. This field can be used to help us analyze unexpected errors or behaviors.",
        ),
    ] = None
    """
    String GUID that identifies the operation in our service. This field can be used to help us analyze unexpected errors or behaviors.
    """

    success: bool = pydantic.Field()
    """
    Boolean that indicates if the response is successful or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
