

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObAddressTypeCode(str, enum.Enum):
    """
    Identifies the nature of the postal address.
    """

    BUSINESS = "Business"
    CORRESPONDENCE = "Correspondence"
    DELIVERY_TO = "DeliveryTo"
    MAIL_TO = "MailTo"
    PO_BOX = "POBox"
    POSTAL = "Postal"
    RESIDENTIAL = "Residential"
    STATEMENT = "Statement"

    def visit(
        self,
        business: typing.Callable[[], T_Result],
        correspondence: typing.Callable[[], T_Result],
        delivery_to: typing.Callable[[], T_Result],
        mail_to: typing.Callable[[], T_Result],
        po_box: typing.Callable[[], T_Result],
        postal: typing.Callable[[], T_Result],
        residential: typing.Callable[[], T_Result],
        statement: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObAddressTypeCode.BUSINESS:
            return business()
        if self is ObAddressTypeCode.CORRESPONDENCE:
            return correspondence()
        if self is ObAddressTypeCode.DELIVERY_TO:
            return delivery_to()
        if self is ObAddressTypeCode.MAIL_TO:
            return mail_to()
        if self is ObAddressTypeCode.PO_BOX:
            return po_box()
        if self is ObAddressTypeCode.POSTAL:
            return postal()
        if self is ObAddressTypeCode.RESIDENTIAL:
            return residential()
        if self is ObAddressTypeCode.STATEMENT:
            return statement()
