For Docker and Kubernetes setup
1. Create a repository in Github named as deployingtodockerhub
2. Go to Docker Hub and create a new repository
3. In deployingtodockerhub folder update the JenkinsFile - in the stage Build Image - give your dockerhub repository
3. In Push Image stage of the JenkinsFile give some id - the same id needs to be passed in Jenkins for storing dockerhub credentials
4. Push deployingtodockerhub to Github
5. Create a repository in Github named as deployingtokubernetes
6. In deployingtokubernetes folder update the deplyment.yaml file - in spec part update the image repository url
7. In deployingtokubernetes folder update the JenkinsFile - in 'Update GIT' stage give your github username and useremail, update the id (same id needs to be passed in Jenkins for saving credentials), update dockerhub url
8. Push deployingtokubernetes to Github
9. Got to Jenkins and Create a New Jenkins Job - select pipeline and give GIThub url for deployingtodockerhub repository
10. Create one more job and name the job same as given in DockerFile of deployingtodockerhub folder (Look at Trigger Manifest stage) and give GIThub url for deployingtokubernetes repository 
11. Click on Build Now and run the pipeline

For Argo CD setup
1. Create a kubernetescluster
2. Install ArgoCD
3. Go to ArgoCD and create new app - give github url here and select sync properties as automatically
4. Now using command line (kubectl get svc) get the load balancer url and  this will contain the deployed flask application

To Automate the Jenkins job using Github:
1. Go to deployingtodockerhub repository in Github and add Jenkins url in Webhooks
2. Go to Jenkins Job - select Configure and then select Github hook trigger for git scm polling and save




 