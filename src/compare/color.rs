//! Whether `crozier compare` colours its human output, and the colours it uses.
//!
//! The rule, decided once in [`color_enabled`]:
//!
//! 1. `NO_COLOR` set to a non-empty value turns colour off, whatever else is set;
//! 2. otherwise `CLICOLOR_FORCE` set to a non-empty value other than `0` turns it
//!    on;
//! 3. otherwise colour is on only when stderr is a terminal.
//!
//! Only the human output on stderr is ever coloured; the JSON report and the
//! `--diff-dir` files never are.

use super::report::Status;

const GREEN: &str = "\u{1b}[32m";
const RED: &str = "\u{1b}[31m";
const YELLOW: &str = "\u{1b}[33m";
const RESET: &str = "\u{1b}[0m";

/// Decide whether to colour the human output from the environment (read
/// through `get`) and whether stderr is a terminal.
pub fn color_enabled(get: impl Fn(&str) -> Option<String>, stderr_is_terminal: bool) -> bool {
    let set = |name: &str| get(name).filter(|value| !value.is_empty());
    if set("NO_COLOR").is_some() {
        return false;
    }
    if set("CLICOLOR_FORCE").is_some_and(|value| value != "0") {
        return true;
    }
    stderr_is_terminal
}

/// Paints text in a status's colour, or leaves it plain when colour is off.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Painter {
    enabled: bool,
}

impl Painter {
    /// A painter that colours only when `enabled`.
    #[must_use]
    pub fn new(enabled: bool) -> Self {
        Painter { enabled }
    }

    /// `text` in `status`'s colour: matched green, mismatched red,
    /// could-not-check yellow.
    #[must_use]
    pub fn status(self, status: Status, text: &str) -> String {
        let color = match status {
            Status::Matched => GREEN,
            Status::Mismatched => RED,
            Status::CouldNotCheck => YELLOW,
        };
        self.paint(color, text)
    }

    /// `text` in the colour of exit status `code`: 0 green, 3 red, anything else
    /// (4) yellow.
    #[must_use]
    pub fn exit(self, code: u8, text: &str) -> String {
        let color = match code {
            0 => GREEN,
            3 => RED,
            _ => YELLOW,
        };
        self.paint(color, text)
    }

    fn paint(self, color: &str, text: &str) -> String {
        if self.enabled {
            format!("{color}{text}{RESET}")
        } else {
            text.to_string()
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn env<'a>(pairs: &'a [(&'a str, &'a str)]) -> impl Fn(&str) -> Option<String> + 'a {
        move |name| {
            pairs
                .iter()
                .find(|(k, _)| *k == name)
                .map(|(_, v)| (*v).to_string())
        }
    }

    #[test]
    fn no_color_wins_over_everything() {
        assert!(!color_enabled(env(&[("NO_COLOR", "1")]), true));
        assert!(!color_enabled(
            env(&[("NO_COLOR", "1"), ("CLICOLOR_FORCE", "1")]),
            true
        ));
    }

    #[test]
    fn an_empty_no_color_does_not_count() {
        assert!(color_enabled(env(&[("NO_COLOR", "")]), true));
        assert!(color_enabled(
            env(&[("NO_COLOR", ""), ("CLICOLOR_FORCE", "1")]),
            false
        ));
    }

    #[test]
    fn clicolor_force_turns_colour_on_unless_empty_or_zero() {
        assert!(color_enabled(env(&[("CLICOLOR_FORCE", "1")]), false));
        assert!(color_enabled(env(&[("CLICOLOR_FORCE", "yes")]), false));
        assert!(!color_enabled(env(&[("CLICOLOR_FORCE", "0")]), false));
        assert!(!color_enabled(env(&[("CLICOLOR_FORCE", "")]), false));
    }

    #[test]
    fn otherwise_colour_follows_the_terminal() {
        assert!(color_enabled(env(&[]), true));
        assert!(!color_enabled(env(&[]), false));
        // A `0` force falls through to the terminal check rather than forcing off.
        assert!(color_enabled(env(&[("CLICOLOR_FORCE", "0")]), true));
    }

    #[test]
    fn painter_colours_each_status_and_exit_code() {
        let on = Painter::new(true);
        assert_eq!(on.status(Status::Matched, "m"), "\u{1b}[32mm\u{1b}[0m");
        assert_eq!(on.status(Status::Mismatched, "m"), "\u{1b}[31mm\u{1b}[0m");
        assert_eq!(
            on.status(Status::CouldNotCheck, "m"),
            "\u{1b}[33mm\u{1b}[0m"
        );
        assert_eq!(on.exit(0, "r"), "\u{1b}[32mr\u{1b}[0m");
        assert_eq!(on.exit(3, "r"), "\u{1b}[31mr\u{1b}[0m");
        assert_eq!(on.exit(4, "r"), "\u{1b}[33mr\u{1b}[0m");
        let off = Painter::new(false);
        assert_eq!(off.status(Status::Mismatched, "m"), "m");
        assert_eq!(off.exit(3, "r"), "r");
    }
}
