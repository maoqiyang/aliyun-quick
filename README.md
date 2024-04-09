# aliyun-quick
基于阿里云api的二次开发。  
增加阿里云每次创建 删除的效率。使用阿里云api跳过输入短信验证码，以及一键创建云主机。
## 前端内容

```powershell
<!DOCTYPE html>
<html lang="ch">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">

    <title>我的 云计算 应用</title>
    <style>
        body {
            background: url('/static/background.jpg') no-repeat center center fixed;
            background-size: cover;
        }

        .container-fluid {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            padding: 40px;

        }

        .card {
            width: 100%;
        }

        .card-img-top {
            height: 100px;
            /* 设置图片高度，确保卡片大小一致 */
            object-fit: cover;
            /* 保持图片比例 */
        }
    </style>
</head>

<body>
    <script src="/static/js/jquery-3.6.0.min.js"></script>
    <!-- 引入jQuery库，版本3.6.0，用于简化JavaScript操作 -->
    <script src="/static/js/popper.min.js"></script>
    <!-- 引入Popper.js，通常用于Bootstrap的提示框（如下拉菜单、提示信息等）的定位 -->
    <script src="/static/js/bootstrap.min.js"></script>
    <!-- 引入Bootstrap的JavaScript库，用于使Bootstrap的各种组件（模态框、折叠菜单等）可交互 -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">CloudComputingApp</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">首页 <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">功能</a>
                </li>
            </ul>
        </div>
    </nav>
    <!-- 来自bootstrap 官网的navbar -->

    <div class="container-fluid">
        <h1>欢迎来到我的 cloudcomputing 应用</h1>
        <div class="row">
            <!-- 第一个服务的卡片 -->
            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务1">
                    <div class="card-body">
                        <h5 class="card-title">创建虚拟机</h5>
                        <p class="card-text">快速部署云主机。</p>
                        <button id="create-vm-button" class="btn btn-success">创建虚拟机</button>
                        <div id="instance-id-display"></div> <!-- 在这里显示实例ID -->

                        <script>
                            $(document).ready(function () {
                                $("#create-vm-button").click(function (event) {
                                    event.preventDefault(); // 防止表单默认提交行为
                                    var $button = $(this); // 获取当前按钮
                                    // 禁用按钮，防止重复点击
                                    $button.prop('disabled', true);
                                    $.ajax({
                                        url: '/create_vm',
                                        type: 'POST',
                                        success: function (response) {
                                            // 操作成功后的处理，将实例ID显示在页面上
                                            if (response.success) {
                                                // 立即显示创建成功的消息
                                                $("#instance-id-display").html("创建虚拟机成功！实例ID: <strong>" + response.instance_id + "</strong>");
                                                // 设置延时2秒后显示正在启动的消息
                                                setTimeout(function () {
                                                    $("#instance-id-display").html("<strong>" + response.instance_id + " 正在启动" + "</strong>");
                                                }, 2000);
                                            } else {
                                                $("#instance-id-display").text("创建虚拟机失败！");
                                            }
                                        },
                                        error: function () {
                                            // 错误处理
                                            $("#instance-id-display").text("创建虚拟机失败！");
                                        },
                                        complete: function () {
                                            // 设置延时5秒后重新启用按钮，并清除消息
                                            setTimeout(function () {
                                                $button.prop('disabled', false);
                                            }, 5000); // 保证用户有足够的时间看到正在启动的消息
                                        }
                                    });
                                });
                            });
                        </script>
                    </div>
                </div>
            </div>
 <!-- javaScript（具体地，使用jQuery库）- 用于添加动态行为，比如处理按钮点击事件，
 向服务器发送异步请求（AJAX），并根据服务器响应更新页面内容。前端通过AJAX向服务器发送POST请求。直接可以在页面进行显示 -->

            <!-- 第二个服务的卡片 -->
            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">删除云服务</h5>
                        <p class="card-text">通过uuid来删除。</p>
                        <!-- 按钮触发模态框 -->
                        <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#deleteVmModal">
                            删除虚拟机
                        </button>
                        <!-- 模态框 -->
                        <div class="modal fade" id="deleteVmModal" tabindex="-1" aria-labelledby="deleteVmModalLabel"
                            aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="deleteVmModalLabel">删除虚拟机</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                            <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div class="modal-body">
                                        <form id="delete-vm-form">
                                            <div class="form-group">
                                                <label for="vm-uuid">虚拟机UUID</label>
                                                <input type="text" class="form-control" id="vm-uuid" name="vm_uuid"
                                                    required>
                                            </div>
                                            <button type="submit" class="btn btn-danger">确认删除</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <script>
                            $(document).ready(function () {
                                // 处理表单提交
                                $("#delete-vm-form").submit(function (event) {
                                    event.preventDefault(); // 阻止表单默认提交行为
                                    var vmUuid = $("#vm-uuid").val(); // 获取输入的UUID
                                    // AJAX请求删除虚拟机
                                    $.ajax({
                                        url: '/delete_vm',
                                        type: 'POST',
                                        data: { vm_uuid: vmUuid },
                                        success: function (response) {
                                            // 关闭模态框
                                            $('#deleteVmModal').modal('hide');
                                            // 显示删除成功的消息，这里简单使用alert
                                            alert(response.message);
                                        },
                                        error: function () {
                                            alert("删除操作失败！");
                                        }
                                    });
                                });
                            });
                        </script>
                    </div>
                </div>
            </div>
            <!-- Bootstrap的模态组件：用于创建模态框，这是Bootstrap组件库中的一个交互式组件，
            它可以在用户的浏览器中弹出一个覆盖层（overlay），显示附加信息或表单，而不需要跳转到另一个页面或重新加载页面。 -->

            <!-- 添加更多服务的卡片... -->
            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">显示所有云</h5>
                        <p class="card-text">列出所有云详情</p>
                        <!-- 假设这是你的主页模板 index.html -->
                        <a href="/show_vms" class="btn btn-primary">显示所有虚拟机</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">危险操作</h5>
                        <p class="card-text">删除所有上海的云主机</p>
                        <a href="/delete_all_vms" class="btn btn-danger">删除所有！</a>  <!-- 简单响应 -->
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">暂停所有云主机</h5>
                        <p class="card-text">暂停以省钱，节省模式</p>
                        <a href="/stop_all_vms" class="btn btn-primary">暂停所有</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">开启所有云主机</h5>
                        <p class="card-text">开始运行</p>
                        <a href="/start_all_vms" class="btn btn-primary">start cloudserver</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">开启US服务器</h5>
                        <p class="card-text">启动</p>
                        <a href="/start_US" class="btn btn-primary">free is good</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">暂停US云主机</h5>
                        <p class="card-text">暂停以省钱</p>
                        <a href="/stop_US" class="btn btn-primary">stop cloudserver</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">查看美国云主机详情</h5>
                        <p class="card-text">列出云主机内容</p>
                        <a href="/show_us_vms" class="btn btn-primary">点我查看</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card">
                    <img src="/static/test.png" class="card-img-top" alt="服务2">
                    <div class="card-body">
                        <h5 class="card-title">github</h5>
                        <p class="card-text">跳转至github</p>
                        <a href="https://github.com/maoqiyang" class="btn btn-primary">了解更多</a>
                    </div>
                </div>
            </div>
            <!-- 请根据需要复制以上卡片代码，并修改其中的图片、标题、文本和链接 -->
        </div>

        <footer class="text-center mt-4 py-2" style="background-color: rgba(0, 0, 0, 0.05);">
            联系我: <a href="mailto:your_email@example.com">27410949@qq.com</a>
        </footer>
    </div>
</body>
</html>
                        
```


## 后端代码
### 后端命令行交换主文件 aliyun_main.py
```powershell
import time
import func

def main():
    sto = "none"
    while True:
        print("请选择操作：1.创建虚拟机 2.删除虚拟机 3.显示所有云主机属性 4.删除所有虚拟机 5.停止所有虚拟机 6.开启所有虚拟机  "
              "7.开启美国服务器 8.停止美国服务器 9.显示美国ip地址 10.退出")

        choice = input("输入选项：").strip()
        if choice == "1":
            info=func.create_vm().to_map()
            instance_id = info['body']['InstanceIdSets']['InstanceIdSet'][0]
            print(f"实例 ID: {instance_id}")
            sto=instance_id

        elif choice == "2":
            user_input = input(f"请输入实例 ID(直接回车使用默认值 {sto}): ").strip()
            # 检查用户是否有输入
            if user_input == "":
                # 用户直接回车，使用默认值
                instance_id = sto
            else:
                # 用户有输入，使用用户的输入
                instance_id = user_input
            # 调用 func.main，并传入 instance_id
                print(f"正在删除{instance_id}")
            time.sleep(5)
            func.delete_vm(instance_id)
            if sto != "none":
                print("well done!")

        elif choice == "3":
            func.shallfuc()

        elif choice == "4":
            func.delete_all()

        elif choice == "5":
            func.stop_vm()
        elif choice == "6":
            func.start_vm()
        elif choice == "7":
            func.us_start()
        elif choice == "8":
            func.us_stop()
        elif choice == "9":
            func.us_show()
        elif choice == "10":
            print("退出程序。")
            break
        else:
            print("无效的选项，请重新输入。")
if __name__ == "__main__":
    main()

```

### 实现各种功能的func文件 func.py
```powershell
import sys
from create import create
from delete import delete
from showall import shall
from stop import sp
from start import st
from us_start import us_st
from us_stop import us_sp
from us_show import Sample
def create_vm():
    info = create.main(sys.argv[1:])
    return info

def delete_vm(instance_id):
    delete.main(instance_id)

def delete_all():
    info=shall.main(sys.argv[1:]).to_map()
    instances = info['body']['Instances']['Instance']
    # 遍历每个实例，提取重要信息
    for instance in instances:
        instance_id = instance['InstanceId']
        print(instance_id)
        delete_vm(instance_id)

def shallfuc():
    info=shall.main(sys.argv[1:]).to_map()
# 假设 info 是之前调用 describe_instances_with_options 方法得到的响应字典
    instances = info['body']['Instances']['Instance']
# 遍历每个实例，提取重要信息
    for instance in instances:
        instance_id = instance['InstanceId']
        instance_name = instance['InstanceName']
        cpu = instance['Cpu']
        memory = instance['Memory']
        public_ip_addresses = instance['PublicIpAddress']['IpAddress']
        status = instance['Status']  # 获取运行状态
    # 打印提取的信息
        print(f"实例 ID: {instance_id}")
        print(f"实例名称: {instance_name}")
        print(f"CPU 核数: {cpu}")
        print(f"内存大小: {memory} MB")
        print(f"公网 IP 地址: {public_ip_addresses}")
        print(f"运行状态: {status}")
        print("-" * 60)
    return instances

def stop_vm():
    info = shall.main(sys.argv[1:]).to_map()
    instances = info['body']['Instances']['Instance']
    # 遍历每个实例，提取重要信息
    for instance in instances:
        instance_id = instance['InstanceId']
        print(f"尝试停止实例: {instance_id}")
        sp.stop_instance(instance_id)  # 停止实例
        print("停止虚拟机")

def start_vm():
    info = shall.main(sys.argv[1:]).to_map()
    instances = info['body']['Instances']['Instance']
    # 遍历每个实例，提取重要信息
    for instance in instances:
        instance_id = instance['InstanceId']
        print(f"尝试开启实例: {instance_id}")
        st.start_instance(instance_id)  # 停止实例
    print("开启虚拟机")

def us_start():
    us_st.main(sys.argv[1:])

def us_stop():
    us_sp.main(sys.argv[1:])

def us_show():
    return Sample.main(sys.argv[1:])
```

### 创建云主机 create.py
**修改此文件可以更改云主机规格，这里设置了一个return info作为返回值**
```powershell
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


class create:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = f'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = create.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd_entry',
            size='40'
        )
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-shanghai',
            instance_type='ecs.e-c1m2.large',
            security_group_id='sg-uf68ogvsofz1u0vdu4tf',
            v_switch_id='vsw-uf6qdbgxrcv1ee0kihxsv',
            image_id='centos_7_6_x64_20G_alibase_20211130.vhd',
            internet_max_bandwidth_in=200,
            internet_max_bandwidth_out=5,
            password='123456',
            internet_charge_type='PayByTraffic',
            key_pair_name='uesrtest',
            spot_strategy='SpotAsPriceGo',
            system_disk=system_disk,
            #amount = 2
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值

            info=client.run_instances_with_options(run_instances_request, runtime)
            return info
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = create.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd_entry',
            size='40'
        )
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-shanghai',
            instance_type='ecs.e-c1m2.large',
            security_group_id='sg-uf68ogvsofz1u0vdu4tf',
            v_switch_id='vsw-uf6qdbgxrcv1ee0kihxsv',
            image_id='centos_7_6_x64_20G_alibase_20211130.vhd',
            internet_max_bandwidth_in=200,
            internet_max_bandwidth_out=5,
            password='123456',
            internet_charge_type='PayByTraffic',
            key_pair_name='uesrtest',
            spot_strategy='SpotAsPriceGo',
            system_disk=system_disk,
            #amount = 2   增加数量
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.run_instances_with_options_async(run_instances_request, runtime)
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    create.main(sys.argv[1:])
```

### 删除云主机 delete.py
**原有基础上更改代码，使代码接受一个instanceid并做判断**
```powershell
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

```

### 显示所有云主机 showall.py
**修改源代码使函数拥有return返回值**
```powershell
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


class shall:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = f'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = shall.create_client()
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='cn-shanghai'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            show=client.describe_instances_with_options(describe_instances_request, runtime)
            return show

        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = shall.create_client()
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='cn-shanghai'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.describe_instances_with_options_async(describe_instances_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    shall.main(sys.argv[1:])

```

### 开启所有虚拟机 start.py
**同样也是改为接受instaceid 在showall之后循环使用达成开启所有虚拟机**
```powershell
# -*- coding: utf-8 -*-
import os
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class st:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        """
        config = open_api_models.Config(
            access_key_id=os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID'),
            access_key_secret=os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
        )
        config.endpoint = 'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def start_instance(instance_id: str) -> None:
        client = st.create_client()
        start_instance_request = ecs_20140526_models.StartInstanceRequest(
            instance_id=instance_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = client.start_instance_with_options(start_instance_request, runtime)
            print(response)
        except Exception as error:
            print(f"Error message: {error.message}")
            if error.data:
                print(f"Recommend: {error.data.get('Recommend')}")

    @staticmethod
    async def start_instance_async(instance_id: str) -> None:
        client = st.create_client()
        start_instance_request = ecs_20140526_models.StartInstanceRequest(
            instance_id=instance_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = await client.start_instance_with_options_async(start_instance_request, runtime)
            print(response)
        except Exception as error:
            print(f"Error message: {error.message}")
            if error.data:
                print(f"Recommend: {error.data.get('Recommend')}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        st.start_instance(sys.argv[1])
    else:
        print("Please provide an instance ID.")

```

### 关闭所有虚拟机 stop.py
```powershell
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

class sp:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        """
        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        config.endpoint = 'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def stop_instance(instance_id: str) -> None:
        client = sp.create_client()
        stop_instance_request = ecs_20140526_models.StopInstanceRequest(
            instance_id=instance_id,
            stopped_mode='StopCharging'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 尝试停止实例并打印返回的 API 响应
            response = client.stop_instance_with_options(stop_instance_request, runtime)
            print(response)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))

    @staticmethod
    async def stop_instance_async(instance_id: str) -> None:
        client = sp.create_client()
        stop_instance_request = ecs_20140526_models.StopInstanceRequest(
            instance_id=instance_id,
            stopped_mode = 'StopCharging'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 异步停止实例并打印返回的 API 响应
            response = await client.stop_instance_with_options_async(stop_instance_request, runtime)
            print(response)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sp.stop_instance(sys.argv[1])
    else:
        print("Please provide an instance ID.")

```

### 美国节点单独操作
```powershell
这个节点有相关v2ray的配置，所以stop停止很省钱，如果删除重新配置就很麻烦，不想写脚本
所以单独为它配置三个操作方法
```

#### us_show.py
```powershell
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


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = f'ecs.us-east-1.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='us-east-1'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            show=client.describe_instances_with_options(describe_instances_request, runtime).to_map()
            instances = show['body']['Instances']['Instance']
            # 遍历每个实例，提取公网 IP 地址
            for instance in instances:
                public_ip_addresses = instance['PublicIpAddress']['IpAddress']
                status = instance['Status']  # 获取运行状态
                str=status+"  "+public_ip_addresses[0]
                print(str)
                return  str

        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='us-east-1'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.describe_instances_with_options_async(describe_instances_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])

```

#### us_start.py
```powershell
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


class us_st:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = f'ecs.us-east-1.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = us_st.create_client()
        start_instance_request = ecs_20140526_models.StartInstanceRequest(
            instance_id='i-0xii36hq2moemykzrn97'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.start_instance_with_options(start_instance_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = us_st.create_client()
        start_instance_request = ecs_20140526_models.StartInstanceRequest(
            instance_id='i-0xii36hq2moemykzrn97'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.start_instance_with_options_async(start_instance_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    us_st.main(sys.argv[1:])

```

#### us_stop.py
```powershell
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


class us_sp:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = f'ecs.us-east-1.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = us_sp.create_client()
        stop_instance_request = ecs_20140526_models.StopInstanceRequest(
            instance_id='i-0xii36hq2moemykzrn97',
            stopped_mode='StopCharging'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            print(client.stop_instance_with_options(stop_instance_request, runtime))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = us_sp.create_client()
        stop_instance_request = ecs_20140526_models.StopInstanceRequest(
            instance_id='i-0xii36hq2moemykzrn97',
            stopped_mode='StopCharging'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.stop_instance_with_options_async(stop_instance_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    us_sp.main(sys.argv[1:])

```

![image](https://github.com/maoqiyang/aliyun-quick/assets/114151655/84a032c9-97b1-4fb2-8167-861d7357fb81)
## 使用 flask + bootstrap + python
**对接前后端，设置相应按钮来调用函数**
```powershell
from flask import Flask, request, redirect, url_for,render_template,make_response,jsonify
import time
import func
import  random
app = Flask(__name__)


@app.route('/create_vm', methods=['POST'])
def create_vm():
    info = func.create_vm().to_map()
    instance_id = info['body']['InstanceIdSets']['InstanceIdSet'][0]
    print(f"实例 ID: {instance_id}")
    return jsonify(success=True, instance_id=instance_id)

@app.route('/')
def hello_world():
    return render_template('hello.html', name='Flask')


@app.route('/delete_vm', methods=['POST'])
def delete_vm():
    vm_uuid = request.form['vm_uuid']
    # 根据vm_uuid来删除虚拟机，这里省略具体实现
    func.delete_vm(vm_uuid)
    # 假设删除成功
    return jsonify(message=f"虚拟机 {vm_uuid} 删除成功。")

@app.route('/show_vms', methods=['GET'])
def show_vms():
    # 模拟数据
    info=func.shallfuc()
    print(info)
    return render_template('vms.html', vms=info)


@app.route('/delete_all_vms', methods=['GET'])
def delete_all_vms():
    # 模拟数据
    info=func.delete_all()
    print(info)
    return render_template('hello.html', name='Flask')


@app.route('/stop_all_vms', methods=['GET'])
def stop_all_vms():
    # 模拟数据
    info=func.stop_vm()
    print(info)
    return render_template('hello.html', name='Flask')

@app.route('/start_all_vms', methods=['GET'])
def start_all_vms():
    # 模拟数据
    info=func.start_vm()
    print(info)
    return render_template('hello.html', name='Flask')

@app.route('/start_US', methods=['GET'])
def start_US():
    # 模拟数据
    info=func.us_start()
    print(info)
    return render_template('hello.html', name='Flask')

@app.route('/stop_US', methods=['GET'])
def stop_US():
    # 模拟数据
    info=func.us_stop()
    print(info)
    return render_template('hello.html', name='Flask')

@app.route('/show_us_vms', methods=['GET'])
def show_us_vms():
    # 模拟数据
    info=func.us_show()
    print(info)
    return render_template('usvms.html', vms=info)

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=5000, debug=True))

```


![image](https://github.com/maoqiyang/aliyun-quick/assets/114151655/6920c24a-d4d6-44b8-a215-2062af6d016c)


## 进行docker打包 使程序在树莓派上运行
![image](https://github.com/maoqiyang/aliyun-quick/assets/114151655/2d4887d1-153c-4168-82c4-55d3bfd2bf48)


```powershell
# 使用官方 Python 运行时作为父镜像
FROM python:3.8-slim
# 设置工作目录
# 将当前目录内容复制到位于 /app 中的容器中
COPY aliyun-project /root/aliyun-project
WORKDIR /root/aliyun-project
# 安装 requirements.txt 中指定的任何所需包
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 使端口 80 可供此容器外的环境使用
EXPOSE 5000
ENV ALIBABA_CLOUD_ACCESS_KEY_ID=xxxxxxx123
ENV ALIBABA_CLOUD_ACCESS_KEY_SECRET=xxxxxxx123
# 在容器启动时运行 app.py
CMD ["python3.8", "app.py"]
```

```powershell
root@raspberrypi:~/aliyun-project# cat requirements.txt 
alibabacloud_ecs20140526==4.0.3
flask
```
构建并启动docker
```powershell
root@raspberrypi:~# docker build -t aliyun .
root@raspberrypi:~# docker run --network host -d  aliyun  
a2533311c34a53e1af8e9d764010176349fe635fe5990cc8683212cb74553fe1
root@raspberrypi:~# docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS     NAMES
a2533311c34a   aliyun               "python3.8 app.py"       6 seconds ago   Up 5 seconds 
```
![image](https://github.com/maoqiyang/aliyun-quick/assets/114151655/94b43426-bafc-4618-88bb-332b747378b9)

## 公网访问
配置 域名和公网服务器 映射  
配置ssl
```powershell
curl https://get.acme.sh | sh
ln -s /root/.acme.sh/acme.sh /usr/local/bin/acme.sh
## 可以选择切换ca机构 acme.sh --set-default-ca --server letsencrypt
yum -y install socat
acme.sh --issue -d 域名信息 --standalone -k ec-256
acme.sh --installcert -d 域名信息 --ecc --key-file  /usr/local/server.key --fullchain-file /usr/local/server.crt

[root@iZuf65w653nremm3zw9ne1Z ~]# tree aliyun-project/
aliyun-project/
├── aliyun_main.py
├── app.py
├── create.py
├── delete.py
├── func.py
├── requirements.txt
├── showall.py
├── start.py
├── static
│   ├── background.jpg
│   ├── css
│   │   └── bootstrap.min.css
│   ├── favicon.ico
│   ├── js
│   │   ├── bootstrap.min.js
│   │   ├── jquery-3.6.0.min.js
│   │   └── popper.min.js
│   └── test.png
├── stop.py
├── templates
│   ├── hello.html
│   ├── usvms.html
│   └── vms.html
├── us_show.py
├── us_start.py
└── us_stop.py

[root@iZuf65w653nremm3zw9ne1Z aliyun-project]# tail -n3 app.py
if __name__ == '__main__':
    app.run(app.run(debug=True))
修改app.py 只允许127.0.0.1来进行访问

编写dockerfile
[root@iZuf65w653nremm3zw9ne1Z ~]# cat Dockerfile
#使用官方 Python 运行时作为父镜像
FROM python:3.6
# 设置工作目录
# 将当前目录内容复制到位于 /app 中的容器中
COPY aliyun-project /root/aliyun-project
WORKDIR /root/aliyun-project
# 安装 requirements.txt 中指定的任何所需包
RUN pip install  alibabacloud_ecs20140526 -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install   flask -i https://mirrors.aliyun.com/pypi/simple/
# 使端口 80 可供此容器外的环境使用
EXPOSE 5000
ENV ALIBABA_CLOUD_ACCESS_KEY_ID=123xxxxxxxxxx
ENV ALIBABA_CLOUD_ACCESS_KEY_SECRET=123xxxxxxxxxx
# 在容器启动时运行 app.py
CMD ["python3.6", "app.py"]


构建镜像
[root@iZuf65w653nremm3zw9ne1Z ~]# docker build -t aliyun .
[root@iZuf65w653nremm3zw9ne1Z ~]# docker run -d --network host aliyun
41af2214f24dc11ffec6fe59fb2d4b1a6d8befc5b6586661caf616a1e1d2f551
[root@iZuf65w653nremm3zw9ne1Z ~]# docker ps
CONTAINER ID        IMAGE               COMMAND              CREATED             STATUS              PORTS
 NAMES
41af2214f24d        aliyun              "python3.6 app.py"   2 seconds ago       Up 1 second
 determined_almeida
[root@iZuf65w653nremm3zw9ne1Z ~]#
```
**配置nginx反代,ssl,密码认证**
```
server {
 listen 443 ssl;
 listen [::]:443 ssl;
 server_name xxx.xxx.xxx; #你的域名
 ssl_certificate /usr/local/server.crt;
 ssl_certificate_key /usr/local/server.key;
 ssl_session_timeout 1d;
 ssl_session_cache shared:MozSSL:10m;
 ssl_session_tickets off;
 ssl_protocols TLSv1.2 TLSv1.3;
 ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCMSHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSACHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSAAES256-GCM-SHA384;
 ssl_prefer_server_ciphers off;
 location / {
    auth_basic "login password";
    auth_basic_user_file /opt/nginx/user_file;
    proxy_pass http://127.0.0.1:5000;
    proxy_ssl_server_name on;
    proxy_redirect off;
    sub_filter_once off;
    sub_filter "127.0.0.1:5000" $server_name;
    proxy_set_header Host "127.0.0.1:5000";
    proxy_set_header Referer $http_referer;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header User-Agent $http_user_agent;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header Accept-Encoding "";
    proxy_set_header Accept-Language "zh-CN";
 }
}

server {
 listen 80;
 server_name xxx.xxx.xxx; #你的域名
 rewrite ^(.*)$ https://${server_name}$1 permanent;
}
```







