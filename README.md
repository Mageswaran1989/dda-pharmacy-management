# dda-pharmacy-management
BITS Pilanai MTech Software Systems Semester 1 - Database Design and Application


## Conda Environment

```bash
conda create --name dda python=3.8
source activate dda

brew install postgresql # for mac
sudo apt-get install libpq-dev python-dev # for ubuntu

# for reference  
  brew services start postgresql # to start postgresql on Mac natively
  brew services stop postgresql # to stop postgresql 

pip install -r requiremetns.txt

```


## How to run?

### Postgresql DB Server Setup
```
cd docker
docker-compose up # to see logs
docker-compose up -d # to run in the background
```

If you are already running a instance and wanted to have clean restart:
```
cd docker
docker-compose down
docker volume rm docker_db
```

Once everything works, you should see following log on the terminal:
`db_1  | 2022-07-27 12:06:04.713 UTC [1] LOG:  database system is ready to accept connections`

Use any DBclinet to connect to the Postgresql Server, wit following credentials:
```
username: postgres
password: postgres
database: postgres
```

### Streamlit
```bash
export PYTHONPATH=$(pwd):$PYTHONPATH 

python pms/hash_password.py --password admin

streamlit run pms/Home.py
```

## References

**Streamlit**
- https://docs.streamlit.io/library/api-reference
- https://docs.streamlit.io/knowledge-base/tutorials/databases/postgresql
- https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031
- https://www.youtube.com/watch?v=JoFGrSRj4X4
  - https://github.com/Sven-Bo/streamlit-sales-dashboard-with-userauthentication/blob/master/app.py
- https://www.youtube.com/watch?v=hEPoto5xp3k
- https://medium.com/codex/create-a-multi-page-app-with-the-new-streamlit-option-menu-component-3e3edaf7e7ad

**Postgresql**
- https://levelup.gitconnected.com/creating-and-filling-a-postgres-db-with-docker-compose-e1607f6f882f
- https://geshan.com.np/blog/2021/12/docker-postgres/

**Error**
- https://stackoverflow.com/questions/11618898/pg-config-executable-not-found