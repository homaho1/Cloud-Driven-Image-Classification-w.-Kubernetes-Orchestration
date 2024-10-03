from kubernetes import client, config
from flask import Flask,request
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()
app = Flask(__name__)
# app.run(debug = True)

@app.route('/config', methods=['GET'])
def get_config():
    print("get_config")
    pods = []
    response = v1.list_pod_for_all_namespaces(watch=False)
    for i in response.items:
        pod = {}
        pod["node"] = i.spec.node_name
        pod["ip"] = i.status.pod_ip
        pod["namespace"] = i.metadata.namespace
        pod["name"] = i.metadata.name
        pod["status"] = i.status.phase
        pods.append(pod)

    output = {"pods": pods}
    output = json.dumps(output)

    return output

@app.route('/img-classification/free',methods=['POST'])
def post_free():
    # use create_namespaced_job, which is a method of BatchV1Api
    print("post_free")
    batch_v1 = client.BatchV1Api()
    with open("free-service.yaml") as f:
        dep = yaml.safe_load(f)
        res = batch_v1.create_namespaced_job(body=dep, namespace="free-service")
        print(res)
    return "success", 200


@app.route('/img-classification/premium', methods=['POST'])
def post_premium():
    # use create_namespaced_job
    print("post_premium")
    batch_v1 = client.BatchV1Api()
    with open("premium-service.yaml") as f:
        dep = yaml.safe_load(f)
        res = batch_v1.create_namespaced_job(body=dep, namespace="default")
        print(res)

    return "success", 200

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
