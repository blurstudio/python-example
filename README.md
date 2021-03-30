# Python Example

This is a template project to jump-start the creation of additional project repositories, managed by Blur Studio, on GitHub. Below is a walk-through of various characteristics of the project.

## Package Configuration

### `setup.py`

- Enables the `setuptools` extension `setuptools_scm`. This extension replaces the need to statically define a package's version and instead derives the version from SCM metadata (such as the latest git tag).
- Permit package installation in editable mode. (i.e. `pip install -e .`)

_You should not need to modify the contents `setup.py`._

> _Originally `setup.py` was the primary manor by which to define a package's metadata. It has mostly been replaced by `setup.cfg`._

### `setup.cfg`

- Defines static package metadata such as package description, author, and PyPI classifiers.
- Lists package requirements (`install_requires`).
- Lists auxiliary package requirements (`extras_require`). These can be installed by appending the extras group name (or "all" for all groups) in square-brackets upon install (ex: `pip install -e .[lint]`).
- Configures `flake8`.

_Be sure to update the various properties so they pertain to your project._

### `pyproject.toml`

- Defines build system characteristics, more specifically those pertaining to `setuptools_scm` which provides automatic versioning based off git repo state.
- Configures `pytest`.

_The only property that will need updating is the `write_to` destination for the `version.txt`-file._

> _While it would be ideal to fully migrate to `pyproject.toml` there are still several aspects of configuration that have not yet fully migrated to support the finalized [PEP 621] standard._

### `requirements.txt` & `requirements-dev.txt`

- Defines a list of packages required in order to install and run the project's package.
- The `-dev` requirements file lists packages useful during development (ex: `pytest`, `flake8`).

_Keep these up to date with any packages required by the project._

## Coding Style & Formatting

### flake8

Analyses for a number of common errors and syntactical violations. Configuration is provided by a section in `setup.cfg`.

### black

Conforms code to a set of opinionated formatting standards.

## Pre-commit Hooks

To install: `pip install pre-commit`

Then run: `pre-commit install`

## GitHub Action Workflows

### Static Analysis

Runs against every push, regardless of branch. Checks the codebase for common errors and syntactical violations with `flake8` and that the code is formatted according to `black`.

### Release

Runs when a new release is created.

## Community Documents

### `CODE_OF_CONDUCT.md`

Describes a set of standards contributors and maintainers alike are intended to follow when interacting with and contributing to projects maintained by Blur Studio.

### `CONTRIBUTING.md`

A kick-start document standardizing the manor by which other developers can contribute to projects maintained by Blur Studio.

### `BUG_REPORT.md`, `FEATURE_REQUEST.md`, & `PULL_REQUEST_TEMPLATE.md`

Templates for reporting issues (bugs or feature requests) and submitting pull requests. Each provide a scaffolding for reporters and contributors to follow, ensuring each request has the appropriate information upon first submission.

[PEP 621]: https://www.python.org/dev/peps/pep-0621/
