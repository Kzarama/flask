# To do app

This app is created with google cloud sdk, to see the instructions:

Para [Windows](https://cloud.google.com/sdk/docs/quickstart-windows)  
Para [MacOS](https://cloud.google.com/sdk/docs/quickstart-macos)
Para [Linux](https://cloud.google.com/sdk/docs/quickstart-linux)

## Firestore implementation

Click in the navigation menu, in database, firestore and data, select native database and create, start a collection and in the collection id write users, in document id write a name, in field name password in value write password and click in save. create a new collection inside the document created with collection id todos, field name description and value with a task and click in save.

In cmd login with application default

```cmd
gcloud auth application-default login
```

Create variable with the project id

```cmd
export GOOGLE_CLOUD_PROJECT=PROJECT_ID
```

Change the project of gcloud

```cmd
gcolud config set project NAME_PROJECT
```

See the current project of gcloud

```cmd
gcloud config list
```

## Deploy

Deploy of the application in app engine

```cmd
gcloud app deploy app.yaml
```

Create a new version of the application

```cmd
gcloud app deploy app.yaml --version
```
