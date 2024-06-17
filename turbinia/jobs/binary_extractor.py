# -*- coding: utf-8 -*-
# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Job to execute binary_extractor task."""

from turbinia.evidence import Directory
from turbinia.evidence import GoogleCloudDisk
from turbinia.evidence import GoogleCloudDiskRawEmbedded
from turbinia.evidence import RawDisk
from turbinia.evidence import EwfDisk
from turbinia.evidence import BinaryExtraction
from turbinia.jobs import interface
from turbinia.jobs import manager
from turbinia.workers.binary_extractor import BinaryExtractorTask


class BinaryExtractorJob(interface.TurbiniaJob):
  """Run image_export on evidence to extract binaries."""

  # The types of evidence that this Job will process.
  evidence_input = [
      Directory, GoogleCloudDisk, GoogleCloudDiskRawEmbedded, RawDisk, EwfDisk
  ]
  evidence_output = [BinaryExtraction]

  NAME = 'BinaryExtractorJob'

  def create_tasks(self, evidence):
    """Create task.

    Args:
      evidence: List of evidence objects to process

    Returns:
        A list of tasks to schedule.
    """
    tasks = [BinaryExtractorTask() for _ in evidence]
    return tasks


manager.JobsManager.RegisterJob(BinaryExtractorJob)
