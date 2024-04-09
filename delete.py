# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class delete:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret
        )
        config.endpoint = 'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(instance_id: str) -> None:
        client = delete.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        delete_instance_request = ecs_20140526_models.DeleteInstanceRequest(
            instance_id=instance_id,  # Corrected variable name
            force=True
        )
        runtime = util_models.RuntimeOptions()
        try:
            client.delete_instance_with_options(delete_instance_request, runtime)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))

    @staticmethod
    async def main_async(instance_id: str) -> None:
        client = delete.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        delete_instance_request = ecs_20140526_models.DeleteInstanceRequest(
            instance_id=instance_id,  # Corrected variable name
            force=True
        )
        runtime = util_models.RuntimeOptions()
        try:
            await client.delete_instance_with_options_async(delete_instance_request, runtime)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        delete.main(sys.argv[1])
    else:
        print("Please provide an instance ID.")
