pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'python -m py_compile mainRun.py testpyauto.py'
      }
    }
    stage('Create Installer') {
      parallel {
        stage('Create Installer') {
          steps {
            sh 'pyinstaller --onefile mainRun.py'
          }
        }
        stage('Docker') {
          agent {
            docker {
              image 'cdrx/pyinstaller-windows:latest'
            }

          }
          steps {
            echo 'Docker Creatred'
          }
        }
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