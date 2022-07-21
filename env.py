from dependencies.env_dependencies import *

engine = create_engine("mysql+pymysql://root:leticia123@/lpweb?charset=utf8mb4", echo=True)
Base = declarative_base()
#Para fazer consultar tem que criar uma sessao
Session = sessionmaker(bind=engine)
session = Session()
print("^CHEGOU AQUI")