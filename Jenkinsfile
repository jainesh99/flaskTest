pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'python -m py_compile main.py testpyauto.py'
      }
    }
    stage('Create Installer') {
      steps {
        sh 'pyinstaller --onefile main.py'
      }
    }
    stage('Delivery') {
      steps {
        cifsPublisher(publishers: [[configName: 'test', transfers: [[cleanRemote: true, excludes: '', flatten: false, makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[,]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: 'dist', sourceFiles: 'dist/**/**']], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true]])
      }
    }
    stage('Execute') {
      steps {
        node(label: 'test') {
          bat(script: 'main', returnStatus: true, returnStdout: true)
          powershell(script: 'chrome', returnStatus: true, returnStdout: true)
        }

      }
    }
  }
}