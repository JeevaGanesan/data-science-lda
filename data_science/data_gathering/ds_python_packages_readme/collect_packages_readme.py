#!/usr/bin/env python3
#
# Copyright(C) 2020 Francesco Murdaca
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Create dataset using SrcOpsMetrics."""

import logging

from pathlib import Path

import data_science

_LOGGER = logging.getLogger(
    "data_science_lda.data_gathering.ds_python_packages_readme.collect_packages_readme"
)

ADJUSTED_GITHUB_REPO = {"nni": ["microsoft", "nni"], "spacy": ["explosion", "spaCy"]}

# TODO: Add function to collect readme for each package using srcopsmetrics package
def _collect_readme_per_python_package() -> None:
    """Collect README for each Github project repo."""
    _LOGGER.warning(
        "No implementation currently.."
        "See: https://github.com/AICoE/SrcOpsMetrics/issues/91"
    )


def aggregate_dataset() -> None:
    """Collect and aggregate all README in one json file."""
    _collect_readme_per_python_package()

    current_path = Path.cwd()
    repo_path = current_path.joinpath("data_science")

    complete_file_path = repo_path.joinpath(
        "data_gathering",
        "ds_python_packages_readme",
        "data_science_github_repo_complete.json",
    )
    data_science_github_repo_complete = data_science.utils._retrieve_file(
        file_path=complete_file_path, file_type="json"
    )
    dataset = {}
    for package, data in data_science_github_repo_complete.items():
        dataset[package] = {}
        if data:
            _LOGGER.debug(f"Retrieving README for {data['github_repo']}...")
            project = data["github_repo"][0]
            repo = data["github_repo"][1]
            current_path = Path.cwd()
            try:
                file_path = repo_path.joinpath(
                    "data_gathering",
                    "ds_python_packages_readme",
                    f"bot_knowledge/{project}/{repo}/content_file.json",
                )
                package_readme = data_science.utils._retrieve_file(
                    file_path=file_path, file_type="json"
                )
                dataset[package]["file_name"] = "/".join(
                    data["github_repo"]
                    + [package_readme["results"]["content_files"]["name"]]
                )
                dataset[package]["raw_text"] = package_readme["results"][
                    "content_files"
                ]["content"]

            except Exception as e:

                try:
                    project = ADJUSTED_GITHUB_REPO[package][0]
                    repo = ADJUSTED_GITHUB_REPO[package][1]
                    file_path = repo_path.joinpath(
                        "data_gathering",
                        "ds_python_packages_readme",
                        f"bot_knowledge/{project}/{repo}/content_file.json",
                    )

                    package_readme = data_science.utils._retrieve_file(
                        file_path=file_path, file_type="json"
                    )
                    dataset[package]["file_name"] = "/".join(
                        ADJUSTED_GITHUB_REPO[package]
                        + [package_readme["results"]["content_files"]["name"]]
                    )
                    dataset[package]["raw_text"] = package_readme["results"][
                        "content_files"
                    ]["content"]

                except Exception as e:
                    _LOGGER.warning("README file cannot be collected.")
                    dataset[package]["raw_text"] = ""
                    pass

        else:
            dataset[package]["file_name"] = ""
            dataset[package]["raw_text"] = ""

    dataset_path = repo_path.joinpath(
        "datasets", "hundreds_data_science_packages_initial_dataset.json"
    )
    data_science.utils._store_file(
        file_path=dataset_path, file_type="json", collected_data=dataset
    )
