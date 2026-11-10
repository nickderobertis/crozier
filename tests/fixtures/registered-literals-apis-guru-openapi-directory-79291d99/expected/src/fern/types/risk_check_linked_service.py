

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckLinkedService(enum.StrEnum):
    """
    An enum indicating the type of a linked service.
    """

    APPLE = "apple"
    EBAY = "ebay"
    FACEBOOK = "facebook"
    FLICKR = "flickr"
    FOURSQUARE = "foursquare"
    GITHUB = "github"
    GOOGLE = "google"
    GRAVATAR = "gravatar"
    INSTAGRAM = "instagram"
    LASTFM = "lastfm"
    LINKEDIN = "linkedin"
    MICROSOFT = "microsoft"
    MYSPACE = "myspace"
    PINTEREST = "pinterest"
    SKYPE = "skype"
    SPOTIFY = "spotify"
    TELEGRAM = "telegram"
    TUMBLR = "tumblr"
    TWITTER = "twitter"
    VIBER = "viber"
    VIMEO = "vimeo"
    WEIBO = "weibo"
    WHATSAPP = "whatsapp"
    YAHOO = "yahoo"
    AIRBNB = "airbnb"
    AMAZON = "amazon"
    BOOKING = "booking"
    DISCORD = "discord"
    KAKAO = "kakao"
    OK = "ok"
    QZONE = "qzone"
    LINE = "line"
    SNAPCHAT = "snapchat"
    ZALO = "zalo"

    def visit(
        self,
        apple: typing.Callable[[], T_Result],
        ebay: typing.Callable[[], T_Result],
        facebook: typing.Callable[[], T_Result],
        flickr: typing.Callable[[], T_Result],
        foursquare: typing.Callable[[], T_Result],
        github: typing.Callable[[], T_Result],
        google: typing.Callable[[], T_Result],
        gravatar: typing.Callable[[], T_Result],
        instagram: typing.Callable[[], T_Result],
        lastfm: typing.Callable[[], T_Result],
        linkedin: typing.Callable[[], T_Result],
        microsoft: typing.Callable[[], T_Result],
        myspace: typing.Callable[[], T_Result],
        pinterest: typing.Callable[[], T_Result],
        skype: typing.Callable[[], T_Result],
        spotify: typing.Callable[[], T_Result],
        telegram: typing.Callable[[], T_Result],
        tumblr: typing.Callable[[], T_Result],
        twitter: typing.Callable[[], T_Result],
        viber: typing.Callable[[], T_Result],
        vimeo: typing.Callable[[], T_Result],
        weibo: typing.Callable[[], T_Result],
        whatsapp: typing.Callable[[], T_Result],
        yahoo: typing.Callable[[], T_Result],
        airbnb: typing.Callable[[], T_Result],
        amazon: typing.Callable[[], T_Result],
        booking: typing.Callable[[], T_Result],
        discord: typing.Callable[[], T_Result],
        kakao: typing.Callable[[], T_Result],
        ok: typing.Callable[[], T_Result],
        qzone: typing.Callable[[], T_Result],
        line: typing.Callable[[], T_Result],
        snapchat: typing.Callable[[], T_Result],
        zalo: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskCheckLinkedService.APPLE:
            return apple()
        if self is RiskCheckLinkedService.EBAY:
            return ebay()
        if self is RiskCheckLinkedService.FACEBOOK:
            return facebook()
        if self is RiskCheckLinkedService.FLICKR:
            return flickr()
        if self is RiskCheckLinkedService.FOURSQUARE:
            return foursquare()
        if self is RiskCheckLinkedService.GITHUB:
            return github()
        if self is RiskCheckLinkedService.GOOGLE:
            return google()
        if self is RiskCheckLinkedService.GRAVATAR:
            return gravatar()
        if self is RiskCheckLinkedService.INSTAGRAM:
            return instagram()
        if self is RiskCheckLinkedService.LASTFM:
            return lastfm()
        if self is RiskCheckLinkedService.LINKEDIN:
            return linkedin()
        if self is RiskCheckLinkedService.MICROSOFT:
            return microsoft()
        if self is RiskCheckLinkedService.MYSPACE:
            return myspace()
        if self is RiskCheckLinkedService.PINTEREST:
            return pinterest()
        if self is RiskCheckLinkedService.SKYPE:
            return skype()
        if self is RiskCheckLinkedService.SPOTIFY:
            return spotify()
        if self is RiskCheckLinkedService.TELEGRAM:
            return telegram()
        if self is RiskCheckLinkedService.TUMBLR:
            return tumblr()
        if self is RiskCheckLinkedService.TWITTER:
            return twitter()
        if self is RiskCheckLinkedService.VIBER:
            return viber()
        if self is RiskCheckLinkedService.VIMEO:
            return vimeo()
        if self is RiskCheckLinkedService.WEIBO:
            return weibo()
        if self is RiskCheckLinkedService.WHATSAPP:
            return whatsapp()
        if self is RiskCheckLinkedService.YAHOO:
            return yahoo()
        if self is RiskCheckLinkedService.AIRBNB:
            return airbnb()
        if self is RiskCheckLinkedService.AMAZON:
            return amazon()
        if self is RiskCheckLinkedService.BOOKING:
            return booking()
        if self is RiskCheckLinkedService.DISCORD:
            return discord()
        if self is RiskCheckLinkedService.KAKAO:
            return kakao()
        if self is RiskCheckLinkedService.OK:
            return ok()
        if self is RiskCheckLinkedService.QZONE:
            return qzone()
        if self is RiskCheckLinkedService.LINE:
            return line()
        if self is RiskCheckLinkedService.SNAPCHAT:
            return snapchat()
        if self is RiskCheckLinkedService.ZALO:
            return zalo()
