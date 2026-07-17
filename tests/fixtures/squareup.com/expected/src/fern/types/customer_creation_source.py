

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerCreationSource(enum.StrEnum):
    """
    Indicates the method used to create the customer profile.
    """

    OTHER = "OTHER"
    APPOINTMENTS = "APPOINTMENTS"
    COUPON = "COUPON"
    DELETION_RECOVERY = "DELETION_RECOVERY"
    DIRECTORY = "DIRECTORY"
    EGIFTING = "EGIFTING"
    EMAIL_COLLECTION = "EMAIL_COLLECTION"
    FEEDBACK = "FEEDBACK"
    IMPORT = "IMPORT"
    INVOICES = "INVOICES"
    LOYALTY = "LOYALTY"
    MARKETING = "MARKETING"
    MERGE = "MERGE"
    ONLINE_STORE = "ONLINE_STORE"
    INSTANT_PROFILE = "INSTANT_PROFILE"
    TERMINAL = "TERMINAL"
    THIRD_PARTY = "THIRD_PARTY"
    THIRD_PARTY_IMPORT = "THIRD_PARTY_IMPORT"
    UNMERGE_RECOVERY = "UNMERGE_RECOVERY"

    def visit(
        self,
        other: typing.Callable[[], T_Result],
        appointments: typing.Callable[[], T_Result],
        coupon: typing.Callable[[], T_Result],
        deletion_recovery: typing.Callable[[], T_Result],
        directory: typing.Callable[[], T_Result],
        egifting: typing.Callable[[], T_Result],
        email_collection: typing.Callable[[], T_Result],
        feedback: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
        invoices: typing.Callable[[], T_Result],
        loyalty: typing.Callable[[], T_Result],
        marketing: typing.Callable[[], T_Result],
        merge: typing.Callable[[], T_Result],
        online_store: typing.Callable[[], T_Result],
        instant_profile: typing.Callable[[], T_Result],
        terminal: typing.Callable[[], T_Result],
        third_party: typing.Callable[[], T_Result],
        third_party_import: typing.Callable[[], T_Result],
        unmerge_recovery: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomerCreationSource.OTHER:
            return other()
        if self is CustomerCreationSource.APPOINTMENTS:
            return appointments()
        if self is CustomerCreationSource.COUPON:
            return coupon()
        if self is CustomerCreationSource.DELETION_RECOVERY:
            return deletion_recovery()
        if self is CustomerCreationSource.DIRECTORY:
            return directory()
        if self is CustomerCreationSource.EGIFTING:
            return egifting()
        if self is CustomerCreationSource.EMAIL_COLLECTION:
            return email_collection()
        if self is CustomerCreationSource.FEEDBACK:
            return feedback()
        if self is CustomerCreationSource.IMPORT:
            return import_()
        if self is CustomerCreationSource.INVOICES:
            return invoices()
        if self is CustomerCreationSource.LOYALTY:
            return loyalty()
        if self is CustomerCreationSource.MARKETING:
            return marketing()
        if self is CustomerCreationSource.MERGE:
            return merge()
        if self is CustomerCreationSource.ONLINE_STORE:
            return online_store()
        if self is CustomerCreationSource.INSTANT_PROFILE:
            return instant_profile()
        if self is CustomerCreationSource.TERMINAL:
            return terminal()
        if self is CustomerCreationSource.THIRD_PARTY:
            return third_party()
        if self is CustomerCreationSource.THIRD_PARTY_IMPORT:
            return third_party_import()
        if self is CustomerCreationSource.UNMERGE_RECOVERY:
            return unmerge_recovery()
