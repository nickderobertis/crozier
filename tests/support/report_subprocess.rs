//! The output of a report subprocess a test needs to have succeeded.

use std::process::Output;

/// The report's standard output, once its process exited successfully.
///
/// # Panics
///
/// When the process failed, with its exit status and its standard error beside
/// its standard output: a reporter that dies before printing (a panic, a signal)
/// writes nothing to standard output, and a message carrying only that output
/// would be empty, hiding the one thing needed to diagnose it.
pub fn successful_report(output: Output) -> String {
    if !output.status.success() {
        panic!(
            "the report subprocess failed ({}).\n--- its standard error ---\n{}\n--- its standard output ---\n{}",
            output.status,
            String::from_utf8_lossy(&output.stderr),
            String::from_utf8_lossy(&output.stdout),
        );
    }
    String::from_utf8(output.stdout).expect("the report's standard output is UTF-8")
}
