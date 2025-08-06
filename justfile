#!/usr/bin/env just --justfile

uv := require('uv')

@_default:
    just --list

# run all checks, tests, and type checks
[group('contribute')]
all: check test typing

# run all pre-commit hooks, including Ruff
[group('contribute')]
check: (test 'style')

# generate coverage report
[group('contribute')]
coverage:
    uv run pytest --cov=advent_of_code_ocr --cov-report=xml

# build documentation with Sphinx
[group('contribute')]
docs: (test 'docs')

# format code with Ruff
[group('contribute')]
format:
    uv run ruff format

# set up pre-commit hooks
[group('contribute')]
install-hooks:
    uv run pre-commit install

# lint and auto-fix code with Ruff
[group('contribute')]
lint:
    uv run ruff check --fix

# run both linting and formatting with Ruff
[group('contribute')]
ruff: lint format

# run tests (across all Python versions by default, runs in CI)
[group('contribute')]
test env='':
    #!/usr/bin/env bash
    if [[ '{{env}}' == '' ]]; then
        uv run tox
    else
        uv run tox -e {{env}}
    fi

# run type checking with mypy (runs in CI)
[group('contribute')]
typing: (test 'typing')

# bump the version number
[group('maintain')]
bump type:
    uv version --bump {{type}}

# upgrade GitHub Actions, pre-commit hooks, and uv.lock
[group('maintain')]
upgrade:
    uv run tox -m update
