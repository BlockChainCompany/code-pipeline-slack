# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import boto3
import time

from test_events import TEST_EVENTS, TEST_ERROR_EVENTS
from build_info import BuildInfo, CodeBuildInfo
from slack_helper import post_build_msg, find_message_for_build
from message_builder import MessageBuilder

import re
import sys

client = boto3.client('codepipeline')

def parse(event):
  if event['source'] == 'aws.codebuild':
    ini = event['detail']['additional-information']['initiator']
    m = re.match('codepipeline/(.+)', ini)
    if m:
      pipeline = m.group(1)
      r = client.get_pipeline_state(name=pipeline)

  buildInfo = BuildInfo.fromEvent(event)
  return buildInfo

def findRevisionInfo(info):
  r = client.get_pipeline_execution(
    pipelineName=info.pipeline,
    pipelineExecutionId=info.executionId
  )['pipelineExecution']

  revs = r.get('artifactRevisions',[])
  if len(revs) > 0:
      return revs[0]
  return None


def pipelineFromBuild(codeBuildInfo):
  r = client.get_pipeline_state(name=codeBuildInfo.pipeline)

  for s in r['stageStates']:
    for a in s['actionStates']:
      executionId = a.get('latestExecution', {}).get('externalExecutionId')
      if executionId and codeBuildInfo.buildId.endswith(executionId):
        pe = s['latestExecution']['pipelineExecutionId']
        return (s['stageName'], pe, a)

  return (None, None, None)


def processCodePipeline(event):
  buildInfo = BuildInfo.fromEvent(event)
  existing_msg = find_message_for_build(buildInfo)
  builder = MessageBuilder(buildInfo, existing_msg)
  builder.updatePipelineEvent(event)

  if builder.needsRevisionInfo():
    revision = findRevisionInfo(buildInfo)
    builder.attachRevisionInfo(revision)

  post_build_msg(builder)

def processCodeBuild(event):
  cbi = CodeBuildInfo.fromEvent(event)
  (stage, pid, actionStates) = pipelineFromBuild(cbi)

  if not pid:
    return

  buildInfo = BuildInfo(pid, cbi.pipeline)

  existing_msg = find_message_for_build(buildInfo)
  builder = MessageBuilder(buildInfo, existing_msg)

  if 'phases' in event['detail']['additional-information']:
    phases = event['detail']['additional-information']['phases']
    builder.updateBuildStageInfo(stage, phases, actionStates)
  
  logs = event['detail'].get('additional-information', {}).get('logs')
  if logs:
    builder.attachLogs(event['detail']['additional-information']['logs'])
    
  post_build_msg(builder)


def process(event):
  if event['source'] == "aws.codepipeline":
    processCodePipeline(event)
  if event['source'] == "aws.codebuild":
    processCodeBuild(event)

# https://www.christopherrung.com/2017/05/04/slack-build-notifications/
def run(event, context):
  print(json.dumps(event, indent=2, default=str))
  m = process(event)

if __name__ == "__main__":
    max_events = len(TEST_ERROR_EVENTS)
    print(len(sys.argv))
    if len(sys.argv) > 1:
        max_events = int(sys.argv[1])
    for i in xrange(0, max_events):
      print(i)
      event = TEST_ERROR_EVENTS[i]
      run(event, {})
      time.sleep(1)
