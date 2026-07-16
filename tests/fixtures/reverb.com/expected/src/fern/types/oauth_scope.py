

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OauthScope(str, enum.Enum):
    PUBLIC = "public"
    """
    
    """

    READ_FEEDBACK = "read_feedback"
    """
    *Originally missing*
    """

    READ_LISTINGS = "read_listings"
    """
    *Originally missing*
    """

    READ_LISTS = "read_lists"
    """
    *Originally missing*
    """

    READ_MESSAGES = "read_messages"
    """
    *Originally missing*
    """

    READ_OFFERS = "read_offers"
    """
    *Originally missing*
    """

    READ_ORDERS = "read_orders"
    """
    *Originally missing*
    """

    READ_PAYOUTS = "read_payouts"
    """
    *Originally missing*
    """

    READ_PROFILE = "read_profile"
    """
    *Originally missing*
    """

    WRITE_FEEDBACK = "write_feedback"
    """
    *Originally missing*
    """

    WRITE_LISTINGS = "write_listings"
    """
    *Originally missing*
    """

    WRITE_LISTINGS_FOR_OTHERS = "write_listings_for_others"
    """
    *Originally missing*
    """

    WRITE_LISTS = "write_lists"
    """
    *Originally missing*
    """

    WRITE_MESSAGES = "write_messages"
    """
    *Originally missing*
    """

    WRITE_OFFERS = "write_offers"
    """
    *Originally missing*
    """

    WRITE_ORDERS = "write_orders"
    """
    *Originally missing*
    """

    WRITE_PROFILE = "write_profile"
    """
    *Originally missing*
    """

    WRITE_REVIEWS = "write_reviews"
    """
    *Originally missing*
    """

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        read_feedback: typing.Callable[[], T_Result],
        read_listings: typing.Callable[[], T_Result],
        read_lists: typing.Callable[[], T_Result],
        read_messages: typing.Callable[[], T_Result],
        read_offers: typing.Callable[[], T_Result],
        read_orders: typing.Callable[[], T_Result],
        read_payouts: typing.Callable[[], T_Result],
        read_profile: typing.Callable[[], T_Result],
        write_feedback: typing.Callable[[], T_Result],
        write_listings: typing.Callable[[], T_Result],
        write_listings_for_others: typing.Callable[[], T_Result],
        write_lists: typing.Callable[[], T_Result],
        write_messages: typing.Callable[[], T_Result],
        write_offers: typing.Callable[[], T_Result],
        write_orders: typing.Callable[[], T_Result],
        write_profile: typing.Callable[[], T_Result],
        write_reviews: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.PUBLIC:
            return public()
        if self is OauthScope.READ_FEEDBACK:
            return read_feedback()
        if self is OauthScope.READ_LISTINGS:
            return read_listings()
        if self is OauthScope.READ_LISTS:
            return read_lists()
        if self is OauthScope.READ_MESSAGES:
            return read_messages()
        if self is OauthScope.READ_OFFERS:
            return read_offers()
        if self is OauthScope.READ_ORDERS:
            return read_orders()
        if self is OauthScope.READ_PAYOUTS:
            return read_payouts()
        if self is OauthScope.READ_PROFILE:
            return read_profile()
        if self is OauthScope.WRITE_FEEDBACK:
            return write_feedback()
        if self is OauthScope.WRITE_LISTINGS:
            return write_listings()
        if self is OauthScope.WRITE_LISTINGS_FOR_OTHERS:
            return write_listings_for_others()
        if self is OauthScope.WRITE_LISTS:
            return write_lists()
        if self is OauthScope.WRITE_MESSAGES:
            return write_messages()
        if self is OauthScope.WRITE_OFFERS:
            return write_offers()
        if self is OauthScope.WRITE_ORDERS:
            return write_orders()
        if self is OauthScope.WRITE_PROFILE:
            return write_profile()
        if self is OauthScope.WRITE_REVIEWS:
            return write_reviews()
