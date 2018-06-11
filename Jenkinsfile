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
        sh 'python -m py_compile main.py testpyauto.py'
      }
    }
  }
}