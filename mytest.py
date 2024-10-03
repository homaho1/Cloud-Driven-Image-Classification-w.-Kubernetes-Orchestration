from kubernetes import client, config
from flask import Flask,request
from os import path
import yaml, random, string, json
import sys
import json

config.load_kube_config()
v1 = client.CoreV1Api()

with open("free-service.yaml") as f:
    dep = yaml.safe_load(f)
    print(dep)
    res = v1.create_namespaced_job(body=dep, namespace="free-service")
    print(res)