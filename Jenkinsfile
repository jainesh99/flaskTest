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
              cifsPublisher(publishers: [[configName: 'test', transfers: [[cleanRemote: false, excludes: '', flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'dist/']], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true]])
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