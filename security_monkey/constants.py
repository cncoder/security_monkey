#     Copyright 2014 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
"""
.. module: security_monkey.constants
    :platform: Unix

.. version:: $$VERSION$$
.. moduleauthor:: Patrick Kelley <pkelley@netflix.com> @monkeysecurity

"""

# SM will not alert on exceptions that occur while attempting to retrieve data
# from these regions.  In our case, we do not have permissions to these regions.cn-north-1
TROUBLE_REGIONS = ['us-east-1', 'us-east-2','us-west-1','us-west-2','ca-central-1','eu-west-1','eu-central-1','eu-west-2','ap-northeast-1','ap-northeast-2','ap-southeast-1','ap-southeast-2','ap-south-1','sa-east-1','us-gov-west-1']