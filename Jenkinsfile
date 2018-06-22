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
            node(label: 'test') {
              cifsPublisher(publishers: [[configName: 'test', transfers: [[cleanRemote: false, excludes: '', flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '$JOB_NAME/dist/main']], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true]])
            }

          }
        }
        stage('Echo') {
          steps {
            echo '${env.JOB_NAME}'
          }
        }
      }
    }
  }
}