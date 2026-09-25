

LinkifierUrlTemplate = str
"""
The [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html)
compliant URL template used for the link.
If you used named groups in `pattern`, you can insert their
content here with `{name_of_group}`.

**Changes**: New in Zulip 7.0 (feature level 176). This replaced
the `url_format_string` parameter, which was a format string in which
named groups' content could be inserted with `%(name_of_group)s`.
"""
