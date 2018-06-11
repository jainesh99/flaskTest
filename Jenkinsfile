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
    stage('Copy Artifacts') {
      steps {
        copyArtifacts(projectName: 'flaskTest', target: 'testNode')
      }
    }
  }
}