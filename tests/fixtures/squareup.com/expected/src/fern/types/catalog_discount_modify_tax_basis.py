

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogDiscountModifyTaxBasis(enum.StrEnum):
    """ """

    MODIFY_TAX_BASIS = "MODIFY_TAX_BASIS"
    DO_NOT_MODIFY_TAX_BASIS = "DO_NOT_MODIFY_TAX_BASIS"

    def visit(
        self, modify_tax_basis: typing.Callable[[], T_Result], do_not_modify_tax_basis: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CatalogDiscountModifyTaxBasis.MODIFY_TAX_BASIS:
            return modify_tax_basis()
        if self is CatalogDiscountModifyTaxBasis.DO_NOT_MODIFY_TAX_BASIS:
            return do_not_modify_tax_basis()
