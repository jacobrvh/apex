The build hook can be used to install required libraries using pip. You need to install these libraries at function level so that they become part of the zip files.

The requirements are mentioned in the requirements.txt and the build hook is used to install the dependencies before the build

```
"hooks":{
    "build": "docker run -v $(pwd):/tmp python-build pip install -r /tmp/requirements.txt -t /tmp"
  }
```

[Docker](https://www.docker.com/) must be installed since it is used to build the dependencies against the [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami), which is used for lambdas. The docker image is not the exact same as the AMI currently being used for lambdas, however it is close enough for most cases.

The docker image must be built first so from the python3 directory run: docker build -t python-build functions/platformdependency/

[Numpy](http://www.numpy.org) is pretty large so it can take a while to build, deploy and execute. You may want to remove the build command and manually execute it when appropriate during development.
