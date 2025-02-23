#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Enums for DAG serialization."""
from __future__ import annotations

from enum import Enum, unique


# Fields of an encoded object in serialization.
@unique
class Encoding(str, Enum):
    """Enum of encoding constants."""

    TYPE = "__type"
    VAR = "__var"


# Supported types for encoding. primitives and list are not encoded.
@unique
class DagAttributeTypes(str, Enum):
    """Enum of supported attribute types of DAG."""

    DAG = "dag"
    OP = "operator"
    DATETIME = "datetime"
    TIMEDELTA = "timedelta"
    TIMEZONE = "timezone"
    RELATIVEDELTA = "relativedelta"
    DICT = "dict"
    SET = "set"
    TUPLE = "tuple"
    POD = "k8s.V1Pod"
    TASK_GROUP = "taskgroup"
    EDGE_INFO = "edgeinfo"
    PARAM = "param"
    XCOM_REF = "xcomref"
    DATASET = "dataset"
    SIMPLE_TASK_INSTANCE = "simple_task_instance"
    BASE_JOB = "Job"
    TASK_INSTANCE = "task_instance"
    DAG_RUN = "dag_run"
    DATA_SET = "data_set"
    CONNECTION = "connection"
    ARG_NOT_SET = "arg_not_set"
