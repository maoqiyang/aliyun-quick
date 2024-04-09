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
    app.run(app.run(debug=True))
