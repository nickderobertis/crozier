

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatchlistScreeningDocumentType(enum.StrEnum):
    """
    The kind of official document represented by this object.

    `birth_certificate` - A certificate of birth

    `drivers_license` - A license to operate a motor vehicle

    `immigration_number` - Immigration or residence documents

    `military_id` - Identification issued by a military group

    `other` - Any document not covered by other categories

    `passport` - An official passport issue by a government

    `personal_identification` - Any generic personal identification that is not covered by other categories

    `ration_card` - Identification that entitles the holder to rations

    `ssn` - United States Social Security Number

    `student_id` - Identification issued by an educational institution

    `tax_id` - Identification issued for the purpose of collecting taxes

    `travel_document` - Visas, entry permits, refugee documents, etc.

    `voter_id` - Identification issued for the purpose of voting
    """

    BIRTH_CERTIFICATE = "birth_certificate"
    DRIVERS_LICENSE = "drivers_license"
    IMMIGRATION_NUMBER = "immigration_number"
    MILITARY_ID = "military_id"
    OTHER = "other"
    PASSPORT = "passport"
    PERSONAL_IDENTIFICATION = "personal_identification"
    RATION_CARD = "ration_card"
    SSN = "ssn"
    STUDENT_ID = "student_id"
    TAX_ID = "tax_id"
    TRAVEL_DOCUMENT = "travel_document"
    VOTER_ID = "voter_id"

    def visit(
        self,
        birth_certificate: typing.Callable[[], T_Result],
        drivers_license: typing.Callable[[], T_Result],
        immigration_number: typing.Callable[[], T_Result],
        military_id: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        passport: typing.Callable[[], T_Result],
        personal_identification: typing.Callable[[], T_Result],
        ration_card: typing.Callable[[], T_Result],
        ssn: typing.Callable[[], T_Result],
        student_id: typing.Callable[[], T_Result],
        tax_id: typing.Callable[[], T_Result],
        travel_document: typing.Callable[[], T_Result],
        voter_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WatchlistScreeningDocumentType.BIRTH_CERTIFICATE:
            return birth_certificate()
        if self is WatchlistScreeningDocumentType.DRIVERS_LICENSE:
            return drivers_license()
        if self is WatchlistScreeningDocumentType.IMMIGRATION_NUMBER:
            return immigration_number()
        if self is WatchlistScreeningDocumentType.MILITARY_ID:
            return military_id()
        if self is WatchlistScreeningDocumentType.OTHER:
            return other()
        if self is WatchlistScreeningDocumentType.PASSPORT:
            return passport()
        if self is WatchlistScreeningDocumentType.PERSONAL_IDENTIFICATION:
            return personal_identification()
        if self is WatchlistScreeningDocumentType.RATION_CARD:
            return ration_card()
        if self is WatchlistScreeningDocumentType.SSN:
            return ssn()
        if self is WatchlistScreeningDocumentType.STUDENT_ID:
            return student_id()
        if self is WatchlistScreeningDocumentType.TAX_ID:
            return tax_id()
        if self is WatchlistScreeningDocumentType.TRAVEL_DOCUMENT:
            return travel_document()
        if self is WatchlistScreeningDocumentType.VOTER_ID:
            return voter_id()
