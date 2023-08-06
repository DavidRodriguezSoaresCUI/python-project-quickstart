# Changelog for Python Project Quickstart
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- Sections should be one of: Added, Changed, Fixed, Removed -->

## 2023-08-06

### Added

- Automatically adds Pypy license classifier when possible or warns that chosen license doesn't hava a corresponding Pypy classifier
- Adds info message when chosen license isn't OSI approved
- Ability to make created package PEP-561 compliant through `py.typed` file

## 2023-08-05

### Added

- Ask user for target minimum Python runtime version (defaults to `3.10`). _Previous behavior was to set minimum version to `3.7` without asking._
 > Version `3.10` was chosen since it's the last mature version at the time of writing and is scheduled to be supported until October 2026
- Licence generation using `lice`

### Removed

- Classifiers in `pyproject.toml` for obvious reasons