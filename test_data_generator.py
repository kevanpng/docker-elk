import json
import logging
import os

import requests
from requests.auth import HTTPBasicAuth

from elasticsearch import Elasticsearch

findings_stat_uid = 'c72111ba-6356-4490-bee2-3a604ddcee04'

logger = logging.getLogger('example')
logging.basicConfig()  # Log to stdout
# info
logger.setLevel(logging.INFO)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
logger.info(f'{ROOT_DIR}')

user_pass = ('elastic', 'changeme')
res = requests.get('http://localhost:9200', auth=HTTPBasicAuth(*user_pass))
logger.info(res.content)
es = Elasticsearch(
    ['http://localhost:9200'],
    http_auth=user_pass
)

# https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html

# how to link code repo to webserver? unless they give us their deployment file
# need to generate a json file of some items that can be put into elasticsearch


def generate_code_scan_finding():
    action_uid = '097f97ff-0b61-4f0e-b41e-ba77bab7d651'
    task_uid = '0d762bea-968e-43d7-a50e-5a8439868688'
    created_at = '2019-01-01T01:00:00Z'
    target = 'https://github.com/kevanpng/code-repo1'
    findings_definition_description = 'webserver susceptible to xss'
    finding = {
        'action_uid': action_uid,
        'task_uid': task_uid,
        'created_at': created_at,
        'target': target,
        'findings_definition_description': findings_definition_description,
        'findings_stat_uid': findings_stat_uid
    }
    return finding


def generate_web_scan_finding():
    action_uid = '66d26cdb-aa6f-4f3d-8593-d6d9694ad353'
    task_uid = '4afa0366-641b-4797-b77f-c56ee952147d'
    created_at = '2019-01-03T01:00:00Z'
    target = 'https://webserver1.com'
    findings_definition_description = 'port 443 is exposed'
    finding = {
        'action_uid': action_uid,
        'task_uid': task_uid,
        'created_at': created_at,
        'target': target,
        'findings_definition_description': findings_definition_description,
        'findings_stat_uid': findings_stat_uid
    }
    return finding


def generate_cloud_scan_finding():
    action_uid = '9a833518-2fa3-4809-b913-9e3ec633b854'
    task_uid = 'a9613863-57f7-448b-86e0-168a7b5990d1'
    created_at = '2019-01-02T01:00:00Z'
    target = 'arn:aws:ec2:ap-southeast-1:12345678:WebServer1'
    findings_definition_description = 'port 443 is exposed'
    finding = {
        'action_uid': action_uid,
        'task_uid': task_uid,
        'created_at': created_at,
        'target': target,
        'findings_definition_description': findings_definition_description,
        'findings_stat_uid': findings_stat_uid
    }
    return finding


if __name__ == '__main__':
    web_scan_finding = generate_web_scan_finding()
    code_scan_finding = generate_code_scan_finding()
    cloud_scan_finding = generate_cloud_scan_finding()
    findings = [web_scan_finding, code_scan_finding, cloud_scan_finding]
    # send data to es
    i = 1
    for finding in findings:
        try:
            result = es.index(
                index='findings', ignore=400,
                id=i, body=finding
            )
        except Exception as e:
            logger.info(f'finding is {finding}')
            logger.exception(e)
        logger.info(result)
        i += 1
