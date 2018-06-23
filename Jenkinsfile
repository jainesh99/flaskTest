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
    stage('Artifact Storage') {
      steps {
        archiveArtifacts 'dist/main'
      }
    }
    stage('Delivery') {
      parallel {
        stage('Delivery') {
          steps {
              cifsPublisher(publishers: [[configName: 'test', transfers: [[cleanRemote: false, excludes: '', flatten: false, makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '', remoteDirectory: '$JOB_NAME/$BUILD_NUMBER', remoteDirectorySDF: false, removePrefix: 'dist/', sourceFiles: 'dist/']], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true]])
          }
        }
        stage('Echo') {
          steps {
            sh 'pwd'
          }
        }
      }
    }
  }
}