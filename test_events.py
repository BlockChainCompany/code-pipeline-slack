TEST_EVENTS = [
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED"
    },
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:11:41Z",
    "id": "ae75c080-2f81-dd60-e6cc-76ec00489305",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED",
      "stage": "Source"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:11:42Z",
    "id": "c3800d8b-1551-6671-1c6b-8ca0c45df928",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "state": "STARTED",
      "version": 1,
      "action": "SourceAction",
      "type": {
        "owner": "ThirdParty",
        "category": "Source",
        "version": "1",
        "provider": "GitHub"
      },
      "stage": "Source"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:11:44Z",
    "id": "0a96add4-c565-174d-5553-19aea4e7f90b",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "state": "SUCCEEDED",
      "version": 1,
      "action": "SourceAction",
      "type": {
        "owner": "ThirdParty",
        "category": "Source",
        "version": "1",
        "provider": "GitHub"
      },
      "stage": "Source"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:12:17Z",
    "id": "6a5718f4-0a53-0bdb-1648-56b67093d219",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "version": 1,
      "state": "SUCCEEDED",
      "stage": "Source"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:12:17Z",
    "id": "733d49c2-6473-22f9-5170-5c82117938b8",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:12:23 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "SUBMITTED",
      "completed-phase-context": "[]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "phase-type": "PROVISIONING",
            "start-time": "May 20, 2018 4:12:23 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 20, 2018 4:12:23 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:12:23Z",
    "id": "96edf410-fbb3-aad7-0b7b-eb142b31ba6f",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "state": "STARTED",
      "version": 1,
      "action": "CodeBuildAction",
      "type": {
        "owner": "AWS",
        "category": "Build",
        "version": "1",
        "provider": "CodeBuild"
      },
      "stage": "Build"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:12:21Z",
    "id": "9db0bff9-a39b-c347-68a6-f01212f07b33",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "project-name": "buildfish-web-ng-dev",
      "current-phase": "SUBMITTED",
      "current-phase-context": "[]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "build-status": "IN_PROGRESS",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip"
      }
    },
    "detail-type": "CodeBuild Build State Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:12:23Z",
    "id": "3bb9e84a-34df-4817-61e8-1bcfbf955df1",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED",
      "stage": "Build"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:12:19Z",
    "id": "5f686b80-7fe6-7ad3-a232-425b66f941bf",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:12:23 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "PROVISIONING",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "DOWNLOAD_SOURCE",
            "start-time": "May 20, 2018 4:12:41 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 17,
      "completed-phase-end": "May 20, 2018 4:12:41 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:12:23Z",
    "id": "266e73c9-84b0-8a64-791c-5897e8490c52",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:12:41 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "DOWNLOAD_SOURCE",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "INSTALL",
            "start-time": "May 20, 2018 4:13:00 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 19,
      "completed-phase-end": "May 20, 2018 4:13:00 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:12:41Z",
    "id": "9156e335-aa01-c3d1-7f81-cb6a1b93da8b",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:13:00 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "INSTALL",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "PRE_BUILD",
            "start-time": "May 20, 2018 4:13:00 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 20, 2018 4:13:00 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:13:00Z",
    "id": "9af58f74-2c13-2cff-cae4-bfc524e70ed8",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:13:00 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "PRE_BUILD",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:13 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 12,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "BUILD",
            "start-time": "May 20, 2018 4:13:13 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 12,
      "completed-phase-end": "May 20, 2018 4:13:13 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:13:00Z",
    "id": "46ad609c-ee4f-e2c4-e25f-92244a943ab6",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:13:13 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "BUILD",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:13 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 12,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:14:30 AM",
            "start-time": "May 20, 2018 4:13:13 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "BUILD",
            "duration-in-seconds": 77,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "POST_BUILD",
            "start-time": "May 20, 2018 4:14:30 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 77,
      "completed-phase-end": "May 20, 2018 4:14:30 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:13:13Z",
    "id": "b0d7b001-3877-7879-3432-536b7d5b815c",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:15:14 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "UPLOAD_ARTIFACTS",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "md5sum": "7427e8a8fb2f45e155117763c4b58830",
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ",
          "sha256sum": "eb3fd320161abfe2343144c8ac23021b5f7c310efec18ccc7de4e4e4c9ae0414"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:13 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 12,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:14:30 AM",
            "start-time": "May 20, 2018 4:13:13 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "BUILD",
            "duration-in-seconds": 77,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:14 AM",
            "start-time": "May 20, 2018 4:14:30 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 44,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:15 AM",
            "start-time": "May 20, 2018 4:15:14 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "FINALIZING",
            "start-time": "May 20, 2018 4:15:15 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 20, 2018 4:15:15 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:15:14Z",
    "id": "8a2ad335-3639-827d-ac46-fceb9275a783",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:14:30 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "POST_BUILD",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:13 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 12,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:14:30 AM",
            "start-time": "May 20, 2018 4:13:13 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "BUILD",
            "duration-in-seconds": 77,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:14 AM",
            "start-time": "May 20, 2018 4:14:30 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 44,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "UPLOAD_ARTIFACTS",
            "start-time": "May 20, 2018 4:15:14 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 44,
      "completed-phase-end": "May 20, 2018 4:15:14 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:14:30Z",
    "id": "912f8de9-a54d-20cd-f5c2-91b16ab52108",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 20, 2018 4:15:15 AM",
      "project-name": "buildfish-web-ng-dev",
      "completed-phase": "FINALIZING",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "md5sum": "7427e8a8fb2f45e155117763c4b58830",
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ",
          "sha256sum": "eb3fd320161abfe2343144c8ac23021b5f7c310efec18ccc7de4e4e4c9ae0414"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:13 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 12,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:14:30 AM",
            "start-time": "May 20, 2018 4:13:13 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "BUILD",
            "duration-in-seconds": 77,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:14 AM",
            "start-time": "May 20, 2018 4:14:30 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 44,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:15 AM",
            "start-time": "May 20, 2018 4:15:14 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:17 AM",
            "start-time": "May 20, 2018 4:15:15 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "FINALIZING",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "COMPLETED",
            "start-time": "May 20, 2018 4:15:17 AM"
          }
        ]
      },
      "completed-phase-duration-seconds": 2,
      "completed-phase-end": "May 20, 2018 4:15:17 AM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:15:15Z",
    "id": "8e064d5e-ce6c-895c-2de9-e3c3828125db",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "project-name": "buildfish-web-ng-dev",
      "current-phase": "COMPLETED",
      "current-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281",
      "build-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": True,
        "build-start-time": "May 20, 2018 4:12:23 AM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-web-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-web-ng-dev;stream=9c03e399-6019-4f94-bdda-7cde94fe6f19",
          "stream-name": "9c03e399-6019-4f94-bdda-7cde94fe6f19"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-web-ng-code-pipeline-dev",
        "artifact": {
          "md5sum": "7427e8a8fb2f45e155117763c4b58830",
          "location": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/D1Ai2AQ",
          "sha256sum": "eb3fd320161abfe2343144c8ac23021b5f7c310efec18ccc7de4e4e4c9ae0414"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/nodejs:6.3.1",
          "type": "LINUX_CONTAINER",
          "environment-variables": [
            {
              "type": "PLAINTEXT",
              "name": "S3_DEPLOY_BUCKET",
              "value": "app-dev.buildfish.co"
            },
            {
              "type": "PLAINTEXT",
              "name": "CLOUDFRONT_DISTRIBUTION_ID",
              "value": "E348NP8S478145"
            }
          ],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-web-ng-code-pipeline-repository-dev/buildfish-web-ng-cod/buildfish-/R7LpCOx.zip",
        "phases": [
          {
            "end-time": "May 20, 2018 4:12:23 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 20, 2018 4:12:41 AM",
            "start-time": "May 20, 2018 4:12:23 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 17,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:12:41 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:00 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:13:13 AM",
            "start-time": "May 20, 2018 4:13:00 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 12,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:14:30 AM",
            "start-time": "May 20, 2018 4:13:13 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "BUILD",
            "duration-in-seconds": 77,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:14 AM",
            "start-time": "May 20, 2018 4:14:30 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 44,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:15 AM",
            "start-time": "May 20, 2018 4:15:14 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 20, 2018 4:15:17 AM",
            "start-time": "May 20, 2018 4:15:15 AM",
            "phase-status": "SUCCEEDED",
            "phase-type": "FINALIZING",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "COMPLETED",
            "start-time": "May 20, 2018 4:15:17 AM"
          }
        ]
      }
    },
    "detail-type": "CodeBuild Build State Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-20T04:15:31Z",
    "id": "f964c333-f1fd-4a5b-71fc-88a61909f9e4",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-web-ng-dev:8d2c7ba5-902c-43f1-b1f2-377922a66281"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "version": 1,
      "state": "SUCCEEDED",
      "stage": "Build"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:16:33Z",
    "id": "5028a236-e0ee-0400-975b-3825b1518c66",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "version": 1,
      "state": "SUCCEEDED"
    },
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:16:35Z",
    "id": "e9f66ea0-6367-7bdf-c9b9-840f9633d999",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "c776b515-1810-465f-a0ab-3a30a1d4341b",
      "pipeline": "buildfish-web-ng-code-pipeline-dev",
      "state": "SUCCEEDED",
      "version": 1,
      "action": "CodeBuildAction",
      "type": {
        "owner": "AWS",
        "category": "Build",
        "version": "1",
        "provider": "CodeBuild"
      },
      "stage": "Build"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-20T04:16:33Z",
    "id": "23204ac3-9431-1c10-4574-c70d5589f3a3",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-web-ng-code-pipeline-dev"
    ]
  }
]

TEST_ERROR_EVENTS = [
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED"
    },
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:51:35Z",
    "id": "01627013-339d-9e88-ae93-9a2ff339b34e",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED",
      "stage": "Source"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:51:37Z",
    "id": "e8af225b-e48f-6461-53ab-9227abfc4bf6",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "60d8a325-6304-484e-8044-55c22f82ace6",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED"
    },
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:51:38Z",
    "id": "9d73d67b-5147-13e2-7ffa-cef83a3ebfaa",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "state": "STARTED",
      "version": 1,
      "action": "SourceAction",
      "type": {
        "owner": "ThirdParty",
        "category": "Source",
        "version": "1",
        "provider": "GitHub"
      },
      "stage": "Source"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:51:39Z",
    "id": "87c08733-af39-6dff-aba8-4433fefeb588",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "state": "SUCCEEDED",
      "version": 1,
      "action": "SourceAction",
      "type": {
        "owner": "ThirdParty",
        "category": "Source",
        "version": "1",
        "provider": "GitHub"
      },
      "stage": "Source"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:10Z",
    "id": "de7e40f6-a18c-1406-bddc-7be6fecce5b1",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "state": "STARTED",
      "version": 1,
      "action": "CodeBuildAction",
      "type": {
        "owner": "AWS",
        "category": "Build",
        "version": "1",
        "provider": "CodeBuild"
      },
      "stage": "Build"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:15Z",
    "id": "c963077b-e285-955a-702e-6db23767f7ad",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED",
      "stage": "Build"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:13Z",
    "id": "340de96c-826f-10f0-4449-462c817b1719",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "SUCCEEDED",
      "stage": "Source"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:11Z",
    "id": "774ab96d-fd2e-e066-1403-fdeddfa6b10d",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "project-name": "buildfish-repo-server-ng-dev",
      "current-phase": "SUBMITTED",
      "current-phase-context": "[]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "build-status": "IN_PROGRESS",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip"
      }
    },
    "detail-type": "CodeBuild Build State Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:52:17Z",
    "id": "e46688c4-cd3e-f156-162f-0c2251bfa9d3",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:52:17 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "SUBMITTED",
      "completed-phase-context": "[]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "phase-type": "PROVISIONING",
            "start-time": "May 22, 2018 5:52:18 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:52:18 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:52:17Z",
    "id": "ded8339d-4d80-a7d0-ec19-55e0ad79d625",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "60d8a325-6304-484e-8044-55c22f82ace6",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED",
      "stage": "Source"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:20Z",
    "id": "b5ccc976-bc0c-5d59-5ba4-c0cfc43c18cd",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "60d8a325-6304-484e-8044-55c22f82ace6",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "state": "STARTED",
      "version": 1,
      "action": "SourceAction",
      "type": {
        "owner": "ThirdParty",
        "category": "Source",
        "version": "1",
        "provider": "GitHub"
      },
      "stage": "Source"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:23Z",
    "id": "4c1b58d7-ece7-3ce9-bbfb-3d48c31f7cbc",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:52:18 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "PROVISIONING",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "DOWNLOAD_SOURCE",
            "start-time": "May 22, 2018 5:52:38 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 19,
      "completed-phase-end": "May 22, 2018 5:52:38 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:52:18Z",
    "id": "6b30413b-ce38-8280-3461-b6f1cae26178",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:52:38 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "DOWNLOAD_SOURCE",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "INSTALL",
            "start-time": "May 22, 2018 5:52:45 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 7,
      "completed-phase-end": "May 22, 2018 5:52:45 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:52:38Z",
    "id": "5465a19c-3f83-7784-33e0-d5b753b10582",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:52:45 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "PRE_BUILD",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "BUILD",
            "start-time": "May 22, 2018 5:52:45 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:52:45 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:52:45Z",
    "id": "3d5a397e-f15e-c8e3-6c91-643a2e4cb206",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:52:45 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "INSTALL",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "PRE_BUILD",
            "start-time": "May 22, 2018 5:52:45 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:52:45 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:52:45Z",
    "id": "a9985532-6ce5-18a8-b014-705c1ce208c9",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "60d8a325-6304-484e-8044-55c22f82ace6",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "SUCCEEDED",
      "stage": "Source"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:56Z",
    "id": "94ad8334-02e9-8e9d-8478-fae4303c46e2",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "60d8a325-6304-484e-8044-55c22f82ace6",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "state": "SUCCEEDED",
      "version": 1,
      "action": "SourceAction",
      "type": {
        "owner": "ThirdParty",
        "category": "Source",
        "version": "1",
        "provider": "GitHub"
      },
      "stage": "Source"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:52:54Z",
    "id": "8f311352-259b-0164-18b7-c1a85be99ca5",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:53:21 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "UPLOAD_ARTIFACTS",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 36,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "FINALIZING",
            "start-time": "May 22, 2018 5:53:21 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:53:21 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:53:21Z",
    "id": "e42c81e8-25a2-229f-53b9-7c67a42e32bf",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:53:21 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "POST_BUILD",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 36,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "UPLOAD_ARTIFACTS",
            "start-time": "May 22, 2018 5:53:21 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:53:21 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:53:21Z",
    "id": "50b380f9-2c7b-734c-f1f8-05d91a7fdd94",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:52:45 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "BUILD",
      "completed-phase-context": "[COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "FAILED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 36,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "phase-type": "POST_BUILD",
            "start-time": "May 22, 2018 5:53:21 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 36,
      "completed-phase-end": "May 22, 2018 5:53:21 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:52:45Z",
    "id": "c577aacf-ffde-e876-3c18-96566bec40e5",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:53:21 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "FINALIZING",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 36,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:23 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "FINALIZING",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "COMPLETED",
            "start-time": "May 22, 2018 5:53:23 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 2,
      "completed-phase-end": "May 22, 2018 5:53:23 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:53:21Z",
    "id": "efbc2460-bc0e-5196-8bab-b5bbd868d7cd",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "project-name": "buildfish-repo-server-ng-dev",
      "current-phase": "COMPLETED",
      "current-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e",
      "build-status": "FAILED",
      "additional-information": {
        "build-complete": True,
        "build-start-time": "May 22, 2018 5:52:17 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=1e81d092-63ae-4811-933b-02214d605c6e",
          "stream-name": "1e81d092-63ae-4811-933b-02214d605c6e"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/WTANUFS"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/CGQPD3p.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:52:18 PM",
            "start-time": "May 22, 2018 5:52:17 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:52:38 PM",
            "start-time": "May 22, 2018 5:52:18 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 19,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:38 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 7,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:52:45 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:52:45 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 36,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:21 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:53:23 PM",
            "start-time": "May 22, 2018 5:53:21 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "FINALIZING",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "COMPLETED",
            "start-time": "May 22, 2018 5:53:23 PM"
          }
        ]
      }
    },
    "detail-type": "CodeBuild Build State Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:53:36Z",
    "id": "257b32ae-8f71-a7fb-f3f9-2540e725b79f",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:1e81d092-63ae-4811-933b-02214d605c6e"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "FAILED",
      "stage": "Build"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:54:22Z",
    "id": "23b2ad90-c402-7b8a-bcb2-99458a1eaab4",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "state": "FAILED",
      "version": 1,
      "action": "CodeBuildAction",
      "type": {
        "owner": "AWS",
        "category": "Build",
        "version": "1",
        "provider": "CodeBuild"
      },
      "stage": "Build"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:54:21Z",
    "id": "f3dc1c7c-b606-efda-b1bc-6eab6ab72463",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "a68bd8b4-e5cb-4174-a2f4-8b28652d5352",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "FAILED"
    },
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:54:22Z",
    "id": "8fce8526-5f0d-3836-6c29-4e26cf788557",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:54:45 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "SUBMITTED",
      "completed-phase-context": "[]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "phase-type": "PROVISIONING",
            "start-time": "May 22, 2018 5:54:45 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:54:45 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:54:45Z",
    "id": "f475c009-5cc4-63d5-34ef-c55f7896ce3a",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "project-name": "buildfish-repo-server-ng-dev",
      "current-phase": "SUBMITTED",
      "current-phase-context": "[]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "build-status": "IN_PROGRESS",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip"
      }
    },
    "detail-type": "CodeBuild Build State Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:54:45Z",
    "id": "816b652b-43b7-edde-3795-cbeb91b11602",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "60d8a325-6304-484e-8044-55c22f82ace6",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "version": 1,
      "state": "STARTED",
      "stage": "Build"
    },
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:54:41Z",
    "id": "de410a7c-4c92-5885-ec14-17cb23cc5c0a",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "execution-id": "60d8a325-6304-484e-8044-55c22f82ace6",
      "pipeline": "buildfish-repo-server-ng-code-pipeline-dev",
      "state": "STARTED",
      "version": 1,
      "action": "CodeBuildAction",
      "type": {
        "owner": "AWS",
        "category": "Build",
        "version": "1",
        "provider": "CodeBuild"
      },
      "stage": "Build"
    },
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "version": "0",
    "time": "2018-05-22T17:54:43Z",
    "id": "ced423a0-e520-b487-2815-acddd0d66fa3",
    "resources": [
      "arn:aws:codepipeline:us-west-2:164943972409:buildfish-repo-server-ng-code-pipeline-dev"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:54:56 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "INSTALL",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:53 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "PRE_BUILD",
            "start-time": "May 22, 2018 5:54:56 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:54:56 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:54:56Z",
    "id": "b6cf9822-f19d-eb99-6c81-5d85ea44677f",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:54:53 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "DOWNLOAD_SOURCE",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:53 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "INSTALL",
            "start-time": "May 22, 2018 5:54:56 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 2,
      "completed-phase-end": "May 22, 2018 5:54:56 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:54:53Z",
    "id": "eafef193-3081-7d77-7a9b-848678dc6d36",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:54:45 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "PROVISIONING",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "DOWNLOAD_SOURCE",
            "start-time": "May 22, 2018 5:54:53 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 8,
      "completed-phase-end": "May 22, 2018 5:54:53 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:54:45Z",
    "id": "75fed851-1262-0111-bec1-621c424b538c",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:54:56 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "PRE_BUILD",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:53 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "BUILD",
            "start-time": "May 22, 2018 5:54:56 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:54:56 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:54:56Z",
    "id": "dc3ef5cb-dbb2-04df-4763-f56017c34d7a",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:55:25 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "UPLOAD_ARTIFACTS",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:53 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 29,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:55:25 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:55:25 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "FINALIZING",
            "start-time": "May 22, 2018 5:55:25 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:55:25 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:55:25Z",
    "id": "72c1c322-dc7b-66fc-4921-b8608d9347e5",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:55:25 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "POST_BUILD",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:53 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 29,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:55:25 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "UPLOAD_ARTIFACTS",
            "start-time": "May 22, 2018 5:55:25 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 0,
      "completed-phase-end": "May 22, 2018 5:55:25 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:55:25Z",
    "id": "6652b713-4ecc-b916-2436-d1f5e6c3cb0b",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:55:25 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "FINALIZING",
      "completed-phase-context": "[: ]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "SUCCEEDED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:53 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 29,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:55:25 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "POST_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:55:25 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "UPLOAD_ARTIFACTS",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:28 PM",
            "start-time": "May 22, 2018 5:55:25 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "FINALIZING",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "phase-type": "COMPLETED",
            "start-time": "May 22, 2018 5:55:28 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 2,
      "completed-phase-end": "May 22, 2018 5:55:28 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:55:25Z",
    "id": "d302b115-ea5c-2bda-301c-7c6005895fcf",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  },
  {
    "account": "164943972409",
    "region": "us-west-2",
    "detail": {
      "completed-phase-start": "May 22, 2018 5:54:56 PM",
      "project-name": "buildfish-repo-server-ng-dev",
      "completed-phase": "BUILD",
      "completed-phase-context": "[COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1]",
      "version": "1",
      "build-id": "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0",
      "completed-phase-status": "FAILED",
      "additional-information": {
        "build-complete": False,
        "build-start-time": "May 22, 2018 5:54:45 PM",
        "logs": {
          "group-name": "/aws/codebuild/buildfish-repo-server-ng-dev",
          "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/buildfish-repo-server-ng-dev;stream=2d03c62f-4541-4318-9817-fbed96b0efc0",
          "stream-name": "2d03c62f-4541-4318-9817-fbed96b0efc0"
        },
        "source": {
          "type": "CODEPIPELINE"
        },
        "initiator": "codepipeline/buildfish-repo-server-ng-code-pipeline-dev",
        "artifact": {
          "location": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/bsanMeJ"
        },
        "environment": {
          "compute-type": "BUILD_GENERAL1_SMALL",
          "image": "aws/codebuild/java:openjdk-8",
          "type": "LINUX_CONTAINER",
          "environment-variables": [],
          "privileged-mode": False
        },
        "timeout-in-minutes": 60,
        "source-version": "arn:aws:s3:::buildfish-repo-server-ng-code-pipeline-repository-dev/buildfish-repo-serve/buildfish-/UsoAfgl.zip",
        "phases": [
          {
            "end-time": "May 22, 2018 5:54:45 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "SUBMITTED",
            "duration-in-seconds": 0,
            "phase-context": []
          },
          {
            "end-time": "May 22, 2018 5:54:53 PM",
            "start-time": "May 22, 2018 5:54:45 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PROVISIONING",
            "duration-in-seconds": 8,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:53 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "DOWNLOAD_SOURCE",
            "duration-in-seconds": 2,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "INSTALL",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:54:56 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "SUCCEEDED",
            "phase-type": "PRE_BUILD",
            "duration-in-seconds": 0,
            "phase-context": [
              ": "
            ]
          },
          {
            "end-time": "May 22, 2018 5:55:25 PM",
            "start-time": "May 22, 2018 5:54:56 PM",
            "phase-status": "FAILED",
            "phase-type": "BUILD",
            "duration-in-seconds": 29,
            "phase-context": [
              "COMMAND_EXECUTION_ERROR: Error while executing command: mvn package. Reason: exit status 1"
            ]
          },
          {
            "phase-type": "POST_BUILD",
            "start-time": "May 22, 2018 5:55:25 PM"
          }
        ]
      },
      "completed-phase-duration-seconds": 29,
      "completed-phase-end": "May 22, 2018 5:55:25 PM"
    },
    "detail-type": "CodeBuild Build Phase Change",
    "source": "aws.codebuild",
    "version": "0",
    "time": "2018-05-22T17:54:56Z",
    "id": "faa41b4d-2807-bc30-dab3-86582cd68021",
    "resources": [
      "arn:aws:codebuild:us-west-2:164943972409:build/buildfish-repo-server-ng-dev:2d03c62f-4541-4318-9817-fbed96b0efc0"
    ]
  }
]
