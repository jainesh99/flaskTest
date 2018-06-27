pipeline {
  agent any
  stages {
    stage('Build') {
      agent {
        docker {
          image 'python:3-alpine'
        }

      }
      steps {
        sh 'python -m py_compile mainRun.py testpyauto.py'
      }
    }
    stage('Create Installer') {
      agent {
        docker {
          image 'cdrx/pyinstaller-linux:latest'
        }

      }
      steps {
        sh 'pyinstaller --onefile mainRun.py'
      }
    }
    stage('Delivery') {
      steps {
        cifsPublisher(publishers: [[configName: 'test', transfers: [[cleanRemote: true, excludes: '', flatten: false, makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[,]+', remoteDirectory: '$JOB_NAME', remoteDirectorySDF: false, removePrefix: 'dist', sourceFiles: 'dist/**/**']], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true]])
      }
    }
    stage('Execute') {
      steps {
        node(label: 'test') {
          bat(script: 'cd ..', returnStatus: true, returnStdout: true)
          powershell(script: 'main', returnStatus: true, returnStdout: true)
        }

      }
    }
  }
}