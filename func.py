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